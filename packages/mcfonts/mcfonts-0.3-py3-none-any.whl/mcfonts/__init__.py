#!/usr/bin/env python3
# coding=utf-8
# SPDX-License-Identifier: MIT
"""
**mcfonts** is a versatile, fast, and extensible package for working with Minecraft fonts.

mcfonts works with any valid font JSON and can export every kind of texture and sizing,
no matter the format.

| For more information, see `<https://gitlab.com/whoatemybutter/mcfonts/>`_.
| Read the documentation online at `<https://mcfonts.rtfd.io>`_.

----

| Licensed under MIT license, see https://choosealicense.com/licenses/mit/ for details.
| Formatted with Black, see https://github.com/psf/black.
"""
import io
import json
import logging
import sys
import typing
import warnings

import fontTools.ttLib.ttFont
import lxml.etree
import PIL.Image
import tinyunicodeblock
import mcfonts.colors
import mcfonts.compacting
import mcfonts.exceptions
import mcfonts.constants
import mcfonts.exporting
import mcfonts.providers
import mcfonts.utils
import mcfonts.utils.bitmap
import mcfonts.utils.rangestring

__author__ = "WhoAteMyButter"
__version__ = (0, 3, 0)
__license__ = "MIT"


if sys.version_info < (3, 10, 0):
    raise EnvironmentError(f"minimum Python version is 3.10.0, you are running " f"{sys.version.split(' ', 1)[0]}")

# Decompression bombs will error, as they should
warnings.simplefilter("error", PIL.Image.DecompressionBombWarning)


class Logger(logging.getLoggerClass()):
    """Basic logger class."""

    def __init__(self, name: str) -> None:
        logging.Logger.__init__(self, name=name)

    def debug(self, msg: str, *args, **kwargs):
        """Debug messages; non-severe and not needed for normal usage."""
        if mcfonts.colors.USE_COLORS:
            return super().debug(
                f"{mcfonts.colors.MAGENTA_FORE}🔧\ufe0f DEBUG: {msg}{mcfonts.colors.RESET_FORE}",
                *args,
                **kwargs,
            )
        return super().debug(f"🔧\ufe0f DEBUG: {msg}", *args, **kwargs)

    def info(self, msg: str, *args, **kwargs):
        """Info messages; messages tthat are notes about program's execution."""
        return super().info(f"🛈\ufe0f INFO: {msg}", *args, **kwargs)

    def warning(self, msg: str, *args, **kwargs):
        """Warning messages; recoverable errors that should be fixed."""
        if mcfonts.colors.USE_COLORS:
            return super().warning(
                f"{mcfonts.colors.YELLOW_FORE}\u26a0\ufe0f WARN: {msg}" f"{mcfonts.colors.RESET_FORE}",
                *args,
                **kwargs,
            )
        return super().warning(f"\u26a0\ufe0f WARN: {msg}", *args, **kwargs)

    def error(self, msg: str, *args, **kwargs):
        """Error messages; irrecoverable errors that must be fixed."""
        if mcfonts.colors.USE_COLORS:
            return super().error(
                f"{mcfonts.colors.RED_FORE}\u2757\ufe0f ERROR: {msg}" f"{mcfonts.colors.RESET_FORE}",
                *args,
                **kwargs,
            )
        return super().error(f"\u2757\ufe0f ERROR: {msg}", *args, **kwargs)

    def critical(self, msg: str, *args, **kwargs):
        """Critical messages; irrecoverable errors that prevent the program from continuing."""
        if mcfonts.colors.USE_COLORS:
            return super().critical(
                f"{mcfonts.colors.WHITE_BACK}{mcfonts.colors.RED_FORE}\u2602\ufe0f CRITICAL: "
                f"{msg}{mcfonts.colors.RESET_ALL}",
                *args,
                **kwargs,
            )
        return super().critical(f"\u2602\ufe0f CRITICAL: {msg}", *args, **kwargs)


logging.setLoggerClass(Logger)
logger = logging.getLogger(__name__)
"""The default logger used across all subprograms."""
logger.setLevel(logging.DEBUG)


class MinecraftFont:
    """
    The MinecraftFont class.
    Requires the providers of a provider file, and the associated resources mapping.

    You should never instantiate this class directly.
    Use :mod:`mcfonts.importing`.

    If you need to add, modify, or remove providers,  do it through :attr:`self.providers`.
    It's a list of Provider classes, each containing relevant fields and methods.

    Be sure to run :meth:`mcfonts.MinecraftFont.validate` after making any changes;
    it will not be done automatically.

    .. warning::
        | If more than one :class:`mcfonts.providers.OptionsProvider` is present in
        | `provider_list`, only the **last** one will be used.

    :param provider_list:
        A list of providers, all of which are instances of :data:`mcfonts.AnyProvider`.
    :param is_monochrome:
        Whether font resources are loaded with RGBA or not.
        Default is True.
    """

    def __init__(
        self,
        provider_list: list[mcfonts.providers.AnyProvider],
        is_monochrome: bool = True,
    ):
        self.providers: list[mcfonts.providers.AnyVanillaProvider] = []
        self.options: mcfonts.providers.OptionsProvider | None = None
        for provider in provider_list:
            if isinstance(provider, mcfonts.providers.OptionsProvider):
                self.options = provider
            else:
                self.providers.append(provider)
        self.glyph_cache: dict[str, dict[str, PIL.Image.Image] | dict[str, int]] = {
            "bitmap": {},
            "space": {},
        }
        for provider in self.providers:
            if isinstance(provider, mcfonts.providers.BitmapProvider):
                self.glyph_cache["bitmap"].update(provider.glyphs)
            elif isinstance(provider, mcfonts.providers.SpaceProvider):
                self.glyph_cache["space"].update(provider.contents["advances"])
        self.is_monochrome: bool = is_monochrome

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.providers + [self.options]}, {self.is_monochrome})"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}()"

    def __hash__(self) -> int:
        return hash((self.providers, self.glyph_cache, self.is_monochrome, self.options))

    def __add__(self, other: "MinecraftFont"):
        # Make a copy of it
        first = MinecraftFont(self.providers, self.is_monochrome)
        # iadd
        first += other
        return first

    def __iadd__(self, other: "MinecraftFont"):
        self.providers += other.providers
        self.glyph_cache |= other.glyph_cache
        if other.is_monochrome is False:
            self.is_monochrome = False
        self.validate()
        return self

    def __len__(self):
        return self.count_coverage()

    def export(
        self,
        font_name: str,
        select_chars: set[str] | None = None,
        select_policy: typing.Literal["include", "exclude"] = "include",
        options_handling: typing.Literal["include", "ignore", "include_exclusive", "ignore_exclusive"] = "include",
        exclude_providers: list[mcfonts.providers.AnyProvider] | None = None,
        include_credits: bool = True,
    ) -> fontTools.ttLib.TTFont:
        """
        Export the Minecraft font into an OpenType font with Type 2 Charstring outlines.

        The font is crafted through a TTX file (font XML), and characters are added in tables and
        given simple name mappings: ``("u0954", "u1fae4", "u2605")``.

        For some fields, the font's name will be "Minecraft <font name>".

        Font must not contain over 65,535 characters, or else any additional characters
        will not be added, and the font will be saved prematurely.

        :param font_name:
            The name of the resulting font, not what its filename is.
            This will be passed to :func:`mcfonts.utils.sanitize_font_name`.
        :param select_chars:
            A set of characters that will be either included or excluded from the exported font.
            To use a rangestring with this, use :func:`mcfonts.utils.rangestring.rangestring_to_characters`.

            For how to control this selection's effect, see `select_policy`.
            If this is an empty set, it will be ignored, regardless of what `select_policy` is.
        :param select_policy:
            How to handle `select_chars`.

            * "include": Only characters that are in this set will be exported *(default)*.
            * "exclude": Characters that are in this set will not be exported
        :param options_handling:
            How to handle :doc:`options`:

            * If "include", include characters that have options declared.
            * If "ignore", disregard the options for a char, even if declared.
            * If "include_exclusive", only include characters that have options declared.
            * If "ignore_exclusive", only include characters that don't have any options declared.
        :param exclude_providers:
            Don't export providers that match these class types.
            By default, this is
            ``[mcfonts.providers.LegacyUnicodeProvider, mcfonts.providers.TTFProvider]``
            to save performance. Set this explicitly to ``[]`` to export all providers.
        :param include_credits:
            To include basic copyright information and credits in the font file.
        """
        if exclude_providers is None:
            exclude_providers = [
                mcfonts.providers.LegacyUnicodeProvider,
                mcfonts.providers.TTFProvider,
            ]
        if select_chars is None:
            select_chars = set()
        font_xml = mcfonts.constants.XML_FONT_TEMPLATE
        duplicates: set[str] = set()
        num_chars = 0
        num_providers = 0
        for provider in self.providers:
            if not provider or provider.__class__ in exclude_providers:
                logger.info(f"Skipping provider {mcfonts.providers.pretty_print_provider(provider)}")
                continue
            logger.info(f"Working on provider {mcfonts.providers.pretty_print_provider(provider)}")
            try:
                if isinstance(
                    provider,
                    (
                        mcfonts.providers.BitmapProvider,
                        mcfonts.providers.LegacyUnicodeProvider,
                    ),
                ):
                    duplicates.update(
                        provider.export(
                            font_xml, duplicates, select_chars, select_policy, self.options, options_handling
                        )
                    )
                elif isinstance(provider, mcfonts.providers.SpaceProvider):
                    # Space has no options
                    duplicates.update(provider.export(font_xml, duplicates, select_chars, select_policy))
                elif isinstance(provider, mcfonts.providers.TTFProvider):
                    print("Cannot do work for TTF files, skipping.")
                else:
                    logger.warning(mcfonts.providers.format_provider_message(provider, "is an unknown type, skipping."))
                    continue
            except mcfonts.exceptions.GlyphLimitError:
                logger.warning("Font has too many characters (over 65,535), truncating and saving immediately.")
                break
            num_providers += 1
        mcfonts.exporting.set_font_name(font_xml, font_name, include_credits)
        logger.info("Compiling...")
        font = fontTools.ttLib.ttFont.TTFont(recalcTimestamp=False, recalcBBoxes=False, sfntVersion="OTTO")
        font.importXML(io.StringIO(lxml.etree.tostring(font_xml, encoding=str)))
        logger.info(f"Exported {num_chars:,} characters from {num_providers:,} provider(s).")
        return font

    def count_coverage(self) -> int:
        """
        Count the number of glyphs this font covers (has a definition for).

        Characters that are encoded in more than 1 UTF-16 codepoint are counted correctly (SMP+).
        Skin tones, presentation modifiers, combining symbols, etc. are separate characters.

        Characters like U+2414F 𤅏 and U+2603 ☃ have the same length.

        :returns: Number of characters supported.
        """
        return len(self.glyph_cache["bitmap"] | self.glyph_cache["space"])

    def get_chars_covered(self) -> typing.Iterator[str]:
        """
        Yield all the characters this font covers (has a definition for).

        Spaces and null bytes are not counted for the "bitmap" provider.
        "Space" providers are counted.
        """
        for character in self.glyph_cache["bitmap"] | self.glyph_cache["space"]:
            yield character

    def write(self, output_file: str, indent: int | str | None = 4) -> None:
        """
        Simply write the font JSON to a file.
        This is not the same as exporting.

        The file is indented by default.
        If a file exists at ``file_location``, it will be overwritten.

        .. warning:: Not to be confused with :func:`export()`.

        :param output_file:
            File path to write to.
        :param indent:
            The indentation level, refer to :func:`json.dump()` for possible values.
        """
        with open(mcfonts.utils.expand_path(output_file), "w", encoding="utf-8") as open_file_location:
            write_providers = [x.contents for x in self.providers]
            if self.options:
                write_providers += self.options.contents
            json.dump({"providers": write_providers}, open_file_location, ensure_ascii=False, indent=indent)

    def count_providers(self) -> dict[str, int]:
        """
        Return a counted summary of the providers this font contains.

        This is future-proof, and will work with any provider as long as it has a "type" key.

        :returns: A summary of font's providers.
        """
        result = {}
        for provider in self.providers:
            if (provider_type := provider.provider_type) not in result:
                result[provider_type] = 1
            else:
                result[provider_type] += 1
        return result

    def count_providers_total(self) -> int:
        """
        Count the number of providers in the font.

        :returns: Number of providers.
        """
        return len(self.count_providers())

    def print_info(self, table_chars: bool = True, summary_only: bool = False) -> None:
        """
        Print basic information about the font.

        :param table_chars:
            Whether to print a 'chars' list as a square table, or as a simple string.
            This only applies to :class:`mcfonts.providers.BitmapProvider`.
        :param summary_only:
            If True, will only print the number of characters and providers.
        """
        if not summary_only:
            for provider in self.providers:
                if isinstance(provider, mcfonts.providers.BitmapProvider):
                    provider.print_info(table_chars)
                else:
                    provider.print_info()
            print("\n")
        print(f"Characters: {self.count_coverage():,}")
        print(f"Providers: {self.count_providers_total():,}")

    def validate(self) -> None:
        """
        Run basic structure checks on the providers of the font JSON.
        """
        if len(self.providers) < 1:
            logger.warning("There are no providers.")
        for provider in self.providers:
            if isinstance(provider, mcfonts.providers.Provider):
                provider.validate()
            else:
                raise mcfonts.exceptions.ProviderError(
                    mcfonts.providers.format_provider_message(provider, "is not a valid provider.")
                )

    def compact(
        self,
        chars_in_row: int = 0,
        cell_size: tuple[int, int] = (0, 0),
        square_cells: bool = True,
        output_file: str | None = None,
    ) -> tuple[list[str], PIL.Image.Image, tuple[int, int]]:
        """
        Take all "bitmap" providers and export every character sheet into a single sheet.
        Characters are scaled according to the largest effective bounding box in all providers.

        This uses :func:`mcfonts.utils.bitmap.compact_providers_single` behind the scenes.

        :param chars_in_row:
            How many characters to fit inside each row of the resulting sheet.
            If this is 0, this will be set to the length of the first string in the
            "charlist" list. If this is negative, this will be set so that the resulting sheet is
            square. By default, this is 0 (auto first string).
        :param cell_size:
            What size to make each glyph cell.
            If this is (0, 0),
            this will be set to the largest dimensions of every glyph in `glyphs`.
            If this is any other tuple of numbers, TODO actually finish this
        :param square_cells:
            If True, each glyph's width will equal its height.
            This is based on whichever number is largest.
            If False, each glyph's width will be unrelated to its height.
        :param output_file: Where to write the sheet to. If this is None, nothing will be
            written.
        :returns: A list of the new characters, and the new file as a :class:`PIL.Image.Image`.
        """
        sheet = mcfonts.compacting.compact_providers(self.providers, chars_in_row, cell_size, square_cells)
        if output_file:
            with open(mcfonts.utils.expand_path(output_file), "wb") as open_output_file:
                sheet[1].save(open_output_file)
        return sheet

    def build_coverage_report(self) -> dict[str, int | dict[str, int]]:
        """
        Build a report of what characters this font contains.

        This includes information like how many characters are in the font,
        and what Unicode blocks are covered.

        :returns: A dictionary of ``{"chars": int, "blocks": {str: int}}``.
        """
        data = {"chars": 0, "blocks": {}}
        for char in self.get_chars_covered():
            data["chars"] += 1
            if (block := tinyunicodeblock.block(char)) in data["blocks"]:
                data["blocks"][block] += 1
            else:
                data["blocks"][block] = 1
        return data

    def get_glyphs_in_rangestring(self, rangestring: str) -> dict[str, PIL.Image.Image | None]:
        """
        Given a `rangestring`,
        return a dictionary of the requested chars to their glyphs.

        :param rangestring:
            A string representing the requested range of chars.
            See :func:`mcfonts.utils.rangestring_to_range` for details.
        :returns: A list of the requested glyphs that match `rangestring`.
        """
        glyphs: dict[str, PIL.Image.Image | None] = {}
        for provider in self.providers:
            if isinstance(provider, mcfonts.providers.BitmapProvider):
                glyphs |= dict(provider.get_glyphs_in_rangestring(rangestring))
        return glyphs

    def get_covering_providers(self, rangestring: str) -> list[mcfonts.providers.AnyProvider]:
        """
        Given a codepoint range,
        return a list of :class:`mcfonts.providers.AnyProvider` that cover these chars.

        :param rangestring:
            A string representing the requested range of chars.
            See :func:`mcfonts.utils.rangestring_to_range` for details.
            Essentially, accepts any of these:

            * 16FF => one codepoint, 5887
            * 2000-22ff => range of chars from 8192 to 8959
            * U+5460..5800 => range of chars from 21600 to 22528
            * U+6000..6001 => range of chars from 24576 to 24577
            * A-Z => range of chars from 65 to 90
            * ☃ => one codepoint, 9731

            Ranges can be split by commas.
        :returns: A list of the providers that cover codeopints defined in `rangestring`.
        """
        result = []
        covers = mcfonts.utils.rangestring.rangestring_to_characters(rangestring)
        for provider in self.providers:
            if not isinstance(provider, mcfonts.providers.SpaceProvider):
                # Ignore padding chars
                covers.difference_update(mcfonts.utils.PADDING_CHARS)
            if provider.chars_covered.intersection(covers):
                result.append(provider)
        return result

    def reload_to_monochrome(self):
        """
        Replace the resources used in the providers with a grayscale version.
        If the resource is already grayscale, this will have no effect.

        This modifies the resource of this provider in place, and **cannot be undone**.
        """
        for provider in self.providers:
            if isinstance(provider, mcfonts.providers.BitmapProvider):
                provider.reload_to_monochrome()
        self.is_monochrome = True

    def compare(self, other: "MinecraftFont"):
        """
        Given `other`, a second instance of :class:`~mcfonts.MinecraftFont`,
        compare the two, using `self` as a baseline.

        The information compared is:

        * Character count
        * Blocks covered
        * Providers included

        :param other: A second instance of :class:`mcfonts.MinecraftFont` to compare to.
        :returns: Nothing, this function prints its results.
        """
        report_this = self.build_coverage_report()
        report_other = other.build_coverage_report()
        if mcfonts.colors.USE_COLORS:
            print(f"{mcfonts.colors.BRIGHT}COUNTS{mcfonts.colors.RESET_ALL}")
        else:
            print("COUNTS")
        print(":: stat: this | other (delta)")
        print(
            f"Characters: {report_this['chars']:,} | {report_other['chars']:,} "
            f"({mcfonts.utils.color_number(report_other['chars'] - report_this['chars'])})"
        )
        len_blocks = (len(report_this["blocks"]), len(report_other["blocks"]))
        print(
            f"Blocks: {len_blocks[0]:,} | {len_blocks[1]:,} ("
            f"{mcfonts.utils.color_number(len_blocks[1] - len_blocks[0])})\n"
        )
        if mcfonts.colors.USE_COLORS:
            print(f"{mcfonts.colors.BRIGHT}BLOCKS{mcfonts.colors.RESET_ALL}")
        else:
            print("BLOCKS")
        print(":: block: this | other (delta)")
        for block_name in (report_this["blocks"] | report_other["blocks"]).keys():
            block_info: tuple[int, int] = tinyunicodeblock.BLOCKS_BYNAME.get(block_name, (0, 0))
            block_this = report_this["blocks"].get(block_name) or 0
            block_other = report_other["blocks"].get(block_name) or 0
            print(f"{chr(block_info[0] + 14)} ", end="")
            if mcfonts.colors.USE_COLORS:
                print(f"{mcfonts.colors.BRIGHT}{block_name}{mcfonts.colors.RESET_ALL}")
            else:
                print(block_name)
            print(
                f"\t{block_this:,}/{block_info[1]:,} | {block_other:,}/{block_info[1]:,} "
                f"({mcfonts.utils.color_number(block_other - block_this)})"
            )
        if mcfonts.colors.USE_COLORS:
            print(f"\n{mcfonts.colors.BRIGHT}PROVIDERS{mcfonts.colors.RESET_ALL}")
        else:
            print("\nPROVIDERS")
        print(":: type: this | other (delta)")
        providers_this = {"bitmap": 0, "space": 0, "ttf": 0, "legacy_unicode": 0}
        providers_other = providers_this.copy()
        for provider in self.providers:
            providers_this[provider.provider_type] += 1
        for provider in other.providers:
            providers_other[provider.provider_type] += 1
        for provider_type in ("bitmap", "space", "ttf", "legacy_unicode"):
            amount_this = providers_this[provider_type]
            amount_other = providers_other[provider_type]
            print(
                f"\t{provider_type}: "
                f"{amount_this} | {amount_other} "
                f"({mcfonts.utils.color_number(amount_other-amount_this)})"
            )
        print("\n")

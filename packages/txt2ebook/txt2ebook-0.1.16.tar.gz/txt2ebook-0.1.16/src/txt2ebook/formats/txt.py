# Copyright (C) 2021,2022 Kian-Meng Ang
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Convert and back source text file into text as well."""

import argparse
import logging
import shutil
from datetime import datetime as dt
from pathlib import Path

from txt2ebook.models import Book

logger = logging.getLogger(__name__)


class TxtWriter:
    """Module for writing ebook in txt format."""

    def __init__(self, book: Book, opts: argparse.Namespace) -> None:
        """Create a TxtWriter module.

        Args:
            book(Book): The book model which contains metadata and table of
            contents of volumes and chapters.
            opts(argparse.Namespace): The configs from the command-line.

        Returns:
            None
        """
        self.book = book
        self.filename = opts.input_file.name
        self.overwrite = opts.overwrite
        self.overwrite_backup = opts.overwrite_backup

    def write(self) -> None:
        """Optionally backup and overwrite the txt file.

        If the input content came from stdin, we'll skip backup and overwrite
        source text file.
        """
        if self.filename == "<stdin>":
            logger.info("Skip backup source text file as content from stdin")
        else:
            if self.overwrite:
                self._overwrite_file()

            if self.overwrite_backup:
                self._backup_file()
                self._overwrite_file()

    def _backup_file(self) -> None:
        txt_filename = Path(self.filename)

        ymd_hms = dt.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = Path(
            txt_filename.resolve().parent.joinpath(
                txt_filename.stem + "_" + ymd_hms + ".bak.txt"
            )
        )
        shutil.copy(txt_filename, backup_filename)
        logger.info("Backup txt file: %s", backup_filename)

    def _overwrite_file(self) -> None:
        txt_filename = Path(self.filename)

        with open(txt_filename, "w", encoding="utf8") as file:
            file.write(self.book.to_txt())
            logger.info("Overwrite txt file: %s", txt_filename.resolve())

#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PhotoSize = Union[raw.types.PhotoCachedSize, raw.types.PhotoPathSize, raw.types.PhotoSize, raw.types.PhotoSizeEmpty, raw.types.PhotoSizeProgressive, raw.types.PhotoStrippedSize]


# noinspection PyRedeclaration
class PhotoSize:  # type: ignore
    """This base type has 6 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`PhotoCachedSize <pyrogram.raw.types.PhotoCachedSize>`
            - :obj:`PhotoPathSize <pyrogram.raw.types.PhotoPathSize>`
            - :obj:`PhotoSize <pyrogram.raw.types.PhotoSize>`
            - :obj:`PhotoSizeEmpty <pyrogram.raw.types.PhotoSizeEmpty>`
            - :obj:`PhotoSizeProgressive <pyrogram.raw.types.PhotoSizeProgressive>`
            - :obj:`PhotoStrippedSize <pyrogram.raw.types.PhotoStrippedSize>`
    """

    QUALNAME = "pyrogram.raw.base.PhotoSize"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/photo-size")

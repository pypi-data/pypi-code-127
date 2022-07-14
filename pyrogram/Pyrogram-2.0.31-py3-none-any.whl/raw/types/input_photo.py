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

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class InputPhoto(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputPhoto`.

    Details:
        - Layer: ``143``
        - ID: ``3BB3B94A``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        file_reference: ``bytes``
    """

    __slots__: List[str] = ["id", "access_hash", "file_reference"]

    ID = 0x3bb3b94a
    QUALNAME = "types.InputPhoto"

    def __init__(self, *, id: int, access_hash: int, file_reference: bytes) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.file_reference = file_reference  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPhoto":
        # No flags
        
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        file_reference = Bytes.read(b)
        
        return InputPhoto(id=id, access_hash=access_hash, file_reference=file_reference)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Bytes(self.file_reference))
        
        return b.getvalue()

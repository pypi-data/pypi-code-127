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


class StartHistoryImport(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``143``
        - ID: ``B43DF344``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        import_id: ``int`` ``64-bit``

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "import_id"]

    ID = 0xb43df344
    QUALNAME = "functions.messages.StartHistoryImport"

    def __init__(self, *, peer: "raw.base.InputPeer", import_id: int) -> None:
        self.peer = peer  # InputPeer
        self.import_id = import_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StartHistoryImport":
        # No flags
        
        peer = TLObject.read(b)
        
        import_id = Long.read(b)
        
        return StartHistoryImport(peer=peer, import_id=import_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Long(self.import_id))
        
        return b.getvalue()

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


class UpdateShortSentMessage(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Updates`.

    Details:
        - Layer: ``143``
        - ID: ``9015E101``

    Parameters:
        id: ``int`` ``32-bit``
        pts: ``int`` ``32-bit``
        pts_count: ``int`` ``32-bit``
        date: ``int`` ``32-bit``
        out (optional): ``bool``
        media (optional): :obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`
        entities (optional): List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`
        ttl_period (optional): ``int`` ``32-bit``

    See Also:
        This object can be returned by 77 methods:

        .. hlist::
            :columns: 2

            - :obj:`account.GetNotifyExceptions <pyrogram.raw.functions.account.GetNotifyExceptions>`
            - :obj:`contacts.DeleteContacts <pyrogram.raw.functions.contacts.DeleteContacts>`
            - :obj:`contacts.AddContact <pyrogram.raw.functions.contacts.AddContact>`
            - :obj:`contacts.AcceptContact <pyrogram.raw.functions.contacts.AcceptContact>`
            - :obj:`contacts.GetLocated <pyrogram.raw.functions.contacts.GetLocated>`
            - :obj:`contacts.BlockFromReplies <pyrogram.raw.functions.contacts.BlockFromReplies>`
            - :obj:`messages.SendMessage <pyrogram.raw.functions.messages.SendMessage>`
            - :obj:`messages.SendMedia <pyrogram.raw.functions.messages.SendMedia>`
            - :obj:`messages.ForwardMessages <pyrogram.raw.functions.messages.ForwardMessages>`
            - :obj:`messages.EditChatTitle <pyrogram.raw.functions.messages.EditChatTitle>`
            - :obj:`messages.EditChatPhoto <pyrogram.raw.functions.messages.EditChatPhoto>`
            - :obj:`messages.AddChatUser <pyrogram.raw.functions.messages.AddChatUser>`
            - :obj:`messages.DeleteChatUser <pyrogram.raw.functions.messages.DeleteChatUser>`
            - :obj:`messages.CreateChat <pyrogram.raw.functions.messages.CreateChat>`
            - :obj:`messages.ImportChatInvite <pyrogram.raw.functions.messages.ImportChatInvite>`
            - :obj:`messages.StartBot <pyrogram.raw.functions.messages.StartBot>`
            - :obj:`messages.MigrateChat <pyrogram.raw.functions.messages.MigrateChat>`
            - :obj:`messages.SendInlineBotResult <pyrogram.raw.functions.messages.SendInlineBotResult>`
            - :obj:`messages.EditMessage <pyrogram.raw.functions.messages.EditMessage>`
            - :obj:`messages.GetAllDrafts <pyrogram.raw.functions.messages.GetAllDrafts>`
            - :obj:`messages.SetGameScore <pyrogram.raw.functions.messages.SetGameScore>`
            - :obj:`messages.SendScreenshotNotification <pyrogram.raw.functions.messages.SendScreenshotNotification>`
            - :obj:`messages.SendMultiMedia <pyrogram.raw.functions.messages.SendMultiMedia>`
            - :obj:`messages.UpdatePinnedMessage <pyrogram.raw.functions.messages.UpdatePinnedMessage>`
            - :obj:`messages.SendVote <pyrogram.raw.functions.messages.SendVote>`
            - :obj:`messages.GetPollResults <pyrogram.raw.functions.messages.GetPollResults>`
            - :obj:`messages.EditChatDefaultBannedRights <pyrogram.raw.functions.messages.EditChatDefaultBannedRights>`
            - :obj:`messages.SendScheduledMessages <pyrogram.raw.functions.messages.SendScheduledMessages>`
            - :obj:`messages.DeleteScheduledMessages <pyrogram.raw.functions.messages.DeleteScheduledMessages>`
            - :obj:`messages.SetHistoryTTL <pyrogram.raw.functions.messages.SetHistoryTTL>`
            - :obj:`messages.SetChatTheme <pyrogram.raw.functions.messages.SetChatTheme>`
            - :obj:`messages.HideChatJoinRequest <pyrogram.raw.functions.messages.HideChatJoinRequest>`
            - :obj:`messages.HideAllChatJoinRequests <pyrogram.raw.functions.messages.HideAllChatJoinRequests>`
            - :obj:`messages.ToggleNoForwards <pyrogram.raw.functions.messages.ToggleNoForwards>`
            - :obj:`messages.SendReaction <pyrogram.raw.functions.messages.SendReaction>`
            - :obj:`messages.GetMessagesReactions <pyrogram.raw.functions.messages.GetMessagesReactions>`
            - :obj:`messages.SetChatAvailableReactions <pyrogram.raw.functions.messages.SetChatAvailableReactions>`
            - :obj:`messages.SendWebViewData <pyrogram.raw.functions.messages.SendWebViewData>`
            - :obj:`help.GetAppChangelog <pyrogram.raw.functions.help.GetAppChangelog>`
            - :obj:`channels.CreateChannel <pyrogram.raw.functions.channels.CreateChannel>`
            - :obj:`channels.EditAdmin <pyrogram.raw.functions.channels.EditAdmin>`
            - :obj:`channels.EditTitle <pyrogram.raw.functions.channels.EditTitle>`
            - :obj:`channels.EditPhoto <pyrogram.raw.functions.channels.EditPhoto>`
            - :obj:`channels.JoinChannel <pyrogram.raw.functions.channels.JoinChannel>`
            - :obj:`channels.LeaveChannel <pyrogram.raw.functions.channels.LeaveChannel>`
            - :obj:`channels.InviteToChannel <pyrogram.raw.functions.channels.InviteToChannel>`
            - :obj:`channels.DeleteChannel <pyrogram.raw.functions.channels.DeleteChannel>`
            - :obj:`channels.ToggleSignatures <pyrogram.raw.functions.channels.ToggleSignatures>`
            - :obj:`channels.EditBanned <pyrogram.raw.functions.channels.EditBanned>`
            - :obj:`channels.DeleteHistory <pyrogram.raw.functions.channels.DeleteHistory>`
            - :obj:`channels.TogglePreHistoryHidden <pyrogram.raw.functions.channels.TogglePreHistoryHidden>`
            - :obj:`channels.EditCreator <pyrogram.raw.functions.channels.EditCreator>`
            - :obj:`channels.ToggleSlowMode <pyrogram.raw.functions.channels.ToggleSlowMode>`
            - :obj:`channels.ConvertToGigagroup <pyrogram.raw.functions.channels.ConvertToGigagroup>`
            - :obj:`channels.ToggleJoinToSend <pyrogram.raw.functions.channels.ToggleJoinToSend>`
            - :obj:`channels.ToggleJoinRequest <pyrogram.raw.functions.channels.ToggleJoinRequest>`
            - :obj:`payments.AssignAppStoreTransaction <pyrogram.raw.functions.payments.AssignAppStoreTransaction>`
            - :obj:`payments.AssignPlayMarketTransaction <pyrogram.raw.functions.payments.AssignPlayMarketTransaction>`
            - :obj:`payments.RestorePlayMarketReceipt <pyrogram.raw.functions.payments.RestorePlayMarketReceipt>`
            - :obj:`payments.RequestRecurringPayment <pyrogram.raw.functions.payments.RequestRecurringPayment>`
            - :obj:`phone.DiscardCall <pyrogram.raw.functions.phone.DiscardCall>`
            - :obj:`phone.SetCallRating <pyrogram.raw.functions.phone.SetCallRating>`
            - :obj:`phone.CreateGroupCall <pyrogram.raw.functions.phone.CreateGroupCall>`
            - :obj:`phone.JoinGroupCall <pyrogram.raw.functions.phone.JoinGroupCall>`
            - :obj:`phone.LeaveGroupCall <pyrogram.raw.functions.phone.LeaveGroupCall>`
            - :obj:`phone.InviteToGroupCall <pyrogram.raw.functions.phone.InviteToGroupCall>`
            - :obj:`phone.DiscardGroupCall <pyrogram.raw.functions.phone.DiscardGroupCall>`
            - :obj:`phone.ToggleGroupCallSettings <pyrogram.raw.functions.phone.ToggleGroupCallSettings>`
            - :obj:`phone.ToggleGroupCallRecord <pyrogram.raw.functions.phone.ToggleGroupCallRecord>`
            - :obj:`phone.EditGroupCallParticipant <pyrogram.raw.functions.phone.EditGroupCallParticipant>`
            - :obj:`phone.EditGroupCallTitle <pyrogram.raw.functions.phone.EditGroupCallTitle>`
            - :obj:`phone.ToggleGroupCallStartSubscription <pyrogram.raw.functions.phone.ToggleGroupCallStartSubscription>`
            - :obj:`phone.StartScheduledGroupCall <pyrogram.raw.functions.phone.StartScheduledGroupCall>`
            - :obj:`phone.JoinGroupCallPresentation <pyrogram.raw.functions.phone.JoinGroupCallPresentation>`
            - :obj:`phone.LeaveGroupCallPresentation <pyrogram.raw.functions.phone.LeaveGroupCallPresentation>`
            - :obj:`folders.EditPeerFolders <pyrogram.raw.functions.folders.EditPeerFolders>`
            - :obj:`folders.DeleteFolder <pyrogram.raw.functions.folders.DeleteFolder>`
    """

    __slots__: List[str] = ["id", "pts", "pts_count", "date", "out", "media", "entities", "ttl_period"]

    ID = 0x9015e101
    QUALNAME = "types.UpdateShortSentMessage"

    def __init__(self, *, id: int, pts: int, pts_count: int, date: int, out: Optional[bool] = None, media: "raw.base.MessageMedia" = None, entities: Optional[List["raw.base.MessageEntity"]] = None, ttl_period: Optional[int] = None) -> None:
        self.id = id  # int
        self.pts = pts  # int
        self.pts_count = pts_count  # int
        self.date = date  # int
        self.out = out  # flags.1?true
        self.media = media  # flags.9?MessageMedia
        self.entities = entities  # flags.7?Vector<MessageEntity>
        self.ttl_period = ttl_period  # flags.25?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateShortSentMessage":
        
        flags = Int.read(b)
        
        out = True if flags & (1 << 1) else False
        id = Int.read(b)
        
        pts = Int.read(b)
        
        pts_count = Int.read(b)
        
        date = Int.read(b)
        
        media = TLObject.read(b) if flags & (1 << 9) else None
        
        entities = TLObject.read(b) if flags & (1 << 7) else []
        
        ttl_period = Int.read(b) if flags & (1 << 25) else None
        return UpdateShortSentMessage(id=id, pts=pts, pts_count=pts_count, date=date, out=out, media=media, entities=entities, ttl_period=ttl_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.out else 0
        flags |= (1 << 9) if self.media is not None else 0
        flags |= (1 << 7) if self.entities else 0
        flags |= (1 << 25) if self.ttl_period is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(Int(self.pts))
        
        b.write(Int(self.pts_count))
        
        b.write(Int(self.date))
        
        if self.media is not None:
            b.write(self.media.write())
        
        if self.entities:
            b.write(Vector(self.entities))
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        return b.getvalue()

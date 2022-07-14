from typing import Optional

from ...interface import verb_required_block
from ...interpreter import Context


class RequireBlock(verb_required_block(True, parameter=True)):
    """
    The require block will attempt to convert the given parameter into a channel
    role or member, using name or ID. If the user running the tag is not in the
    targeted channel or doesn't have the targeted role, the tag will stop processing
    and it will send the response if one is given. Multiple role or channel
    requirements can be given, and should be split by a ",".

    **Usage:** ``{require(<role, channel, member>):[response]}``

    **Aliases:** ``whitelist``

    **Payload:** ``response``

    **Parameter:** ``role, channel, member``

    **Examples:**

    .. tagscript::

        {require(Moderator)}
        {require(#general, #bot-cmds):This tag can only be run in #general and #bot-cmds.}
        {require(757425366209134764, 668713062186090506, 737961895356792882):You aren't allowed to use this tag.}
    """

    ACCEPTED_NAMES = ("require", "whitelist")

    def process(self, ctx: Context) -> Optional[str]:
        """
        Process the requirements
        """
        actions = ctx.response.actions.get("requires")
        if actions:
            return None
        ctx.response.actions["requires"] = {
            "items": [i.strip() for i in ctx.verb.parameter.split(",")],
            "response": ctx.verb.payload,
        }
        return ""


class BlacklistBlock(verb_required_block(True, parameter=True)):
    """
    The blacklist block will attempt to convert the given parameter into a channel
    or role, using name or ID. If the user running the tag is in the targeted
    channel or has the targeted role, the tag will stop processing and
    it will send the response if one is given. Multiple role or channel
    requirements can be given, and should be split by a ",".

    **Usage:** ``{blacklist(<role,channel>):[response]}``

    **Payload:** ``response``

    **Parameter:** ``role, channel``

    **Examples:**

    .. tagscript::
        {blacklist(Muted)}
        {blacklist(#support):This tag is not allowed in #support.}
        {blacklist(Tag Blacklist, 668713062186090506):You are blacklisted from using tags.}
    """

    ACCEPTED_NAMES = ("blacklist",)

    def process(self, ctx: Context) -> Optional[str]:
        """
        Process the blacklists
        """
        actions = ctx.response.actions.get("blacklist")
        if actions:
            return None
        ctx.response.actions["blacklist"] = {
            "items": [i.strip() for i in ctx.verb.parameter.split(",")],
            "response": ctx.verb.payload,
        }
        return ""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional
import datetime

from .asset import Asset
from .user import User

if TYPE_CHECKING:
    from .server import Server
    from .state import State
    from .types import File
    from .types import Member as MemberPayload

__all__ = ("Member",)

def flattern_user(member: Member, user: User):
    for attr in user.__flattern_attributes__:
        setattr(member, attr, getattr(user, attr))

class Member(User):
    """Represents a member of a server, subclasses :class:`User`

    Attributes
    -----------
    nickname: Optional[:class:`str`]
        The nickname of the member if any
    roles: list[:class:`Role`]
        The roles of the member, ordered by the role's rank in decending order
    server: :class:`Server`
        The server the member belongs to
    guild_avatar: Optional[:class:`Asset`]
        The member's guild avatar if any
    """
    __slots__ = ("state", "nickname", "roles", "server", "guild_avatar", "joined_at", "timeout")

    def __init__(self, data: MemberPayload, server: Server, state: State):
        user = state.get_user(data["_id"]["user"])

        # due to not having a user payload and only a user object we have to manually add all the attributes instead of calling User.__init__
        flattern_user(self, user)
        user._members.add(self)

        self.state = state

        if avatar := data.get("avatar"):
            self.guild_avatar = Asset(avatar, state)
        else:
            self.guild_avatar = None

        roles = [server.get_role(role_id) for role_id in data.get("roles", [])]
        self.roles = sorted(roles, key=lambda role: role.rank, reverse=True)

        self.server = server
        self.nickname = data.get("nickname")
        joined_at = data["joined_at"]

        if isinstance(joined_at, int):
            self.joined_at = datetime.datetime.fromtimestamp(joined_at / 1000)
        else:
            self.joined_at = datetime.datetime.strptime(joined_at, "%Y-%m-%dT%H:%M:%S.%f%z")
        self.timeout = None

        if timeout := data.get("timeout"):
            self.timeout = datetime.datetime.strptime(timeout, "%Y-%m-%dT%H:%M:%S.%f%z")

    @property
    def avatar(self) -> Optional[Asset]:
        """Optional[:class:`Asset`] The avatar the member is displaying, this includes guild avatars and masqueraded avatar"""
        return self.masquerade_avatar or self.guild_avatar or self.original_avatar

    @property
    def mention(self) -> str:
        """:class:`str`: Returns a string that allows you to mention the given member."""
        return f"<@{self.id}>"

    def _update(self, *, nickname: Optional[str] = None, avatar: Optional[File] = None, roles: Optional[list[str]] = None):
        if nickname:
            self.nickname = nickname

        if avatar:
            self.guild_avatar = Asset(avatar, self.state)

        if roles is not None:
            member_roles = [self.server.get_role(role_id) for role_id in roles]
            self.roles = sorted(member_roles, key=lambda role: role.rank, reverse=True)

    async def kick(self):
        """Kicks the member from the server"""
        await self.state.http.kick_member(self.server.id, self.id)

    async def ban(self, *, reason: Optional[str] = None):
        """Bans the member from the server

        Parameters
        -----------
        reason: Optional[:class:`str`]
            The reason for the ban
        """
        await self.state.http.ban_member(self.server.id, self.id, reason)

    async def unban(self):
        """Unbans the member from the server"""
        await self.state.http.unban_member(self.server.id, self.id)

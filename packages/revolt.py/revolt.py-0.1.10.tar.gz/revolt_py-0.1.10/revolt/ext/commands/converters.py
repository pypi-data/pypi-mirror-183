from __future__ import annotations

import re
from typing import Annotated, TypeVar, TYPE_CHECKING

from revolt import Category, Channel, Member, User, utils

from .context import Context
from .errors import (BadBoolArgument, CategoryConverterError,
                     ChannelConverterError, MemberConverterError, ServerOnly,
                     UserConverterError)

if TYPE_CHECKING:
    from .client import CommandsClient

__all__ = ("bool_converter", "category_converter", "channel_converter", "user_converter", "member_converter", "IntConverter", "BoolConverter", "CategoryConverter", "UserConverter", "MemberConverter", "ChannelConverter")

channel_regex = re.compile("<#([A-z0-9]{26})>")
user_regex = re.compile("<@([A-z0-9]{26})>")

ClientT = TypeVar("ClientT", bound="CommandsClient")

def bool_converter(arg: str, _):
    lowered = arg.lower()
    if lowered in  ["yes", "true", "ye", "y", "1", "on", "enable"]:
        return True
    elif lowered in ('no', 'n', 'false', 'f', '0', 'disable', 'off'):
        return False
    else:
        raise BadBoolArgument(lowered)

def category_converter(arg: str, context: Context[ClientT]) -> Category:
    if not (server := context.server):
        raise ServerOnly

    try:
        return server.get_category(arg)
    except KeyError:
        try:
            return utils.get(server.categories, name=arg)
        except LookupError:
            raise CategoryConverterError(arg)

def channel_converter(arg: str, context: Context[ClientT]) -> Channel:
    if not (server := context.server):
        raise ServerOnly

    if (match := channel_regex.match(arg)):
        arg = match.group(1)

    try:
        return server.get_channel(arg)
    except KeyError:
        try:
            return utils.get(server.channels, name=arg)
        except LookupError:
            raise ChannelConverterError(arg)

def user_converter(arg: str, context: Context[ClientT]) -> User:
    if (match := user_regex.match(arg)):
        arg = match.group(1)

    try:
        return context.client.get_user(arg)
    except KeyError:
        try:
            return utils.get(context.client.users, name=arg)
        except LookupError:
            raise UserConverterError(arg)

def member_converter(arg: str, context: Context[ClientT]) -> Member:
    if not (server := context.server):
        raise ServerOnly

    if (match := user_regex.match(arg)):
        arg = match.group(1)

    try:
        return server.get_member(arg)
    except KeyError:
        try:
            return utils.get(server.members, name=arg)
        except LookupError:
            raise MemberConverterError(arg)

def int_converter(arg: str, context: Context[ClientT]) -> int:
    return int(arg)

IntConverter = Annotated[int, int_converter]
BoolConverter = Annotated[bool, bool_converter]
CategoryConverter = Annotated[Category, category_converter]
UserConverter = Annotated[User, user_converter]
MemberConverter = Annotated[Member, member_converter]
ChannelConverter = Annotated[Channel, channel_converter]

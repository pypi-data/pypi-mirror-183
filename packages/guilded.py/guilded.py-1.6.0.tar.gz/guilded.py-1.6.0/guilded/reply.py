"""
MIT License

Copyright (c) 2020-present shay (shayypy)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

------------------------------------------------------------------------------

This project includes code from https://github.com/Rapptz/discord.py, which is
available under the MIT license:

The MIT License (MIT)

Copyright (c) 2015-present Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from .abc import Reply

if TYPE_CHECKING:
    from .channel import ForumTopic
    from .emote import Emote


__all__ = (
    'ForumTopicReply',
)


class ForumTopicReply(Reply):
    """Represents a reply to a :class:`ForumTopic`.

    .. container:: operations

        .. describe:: x == y

            Checks if two replies are equal.

        .. describe:: x != y

            Checks if two replies are not equal.

        .. describe:: hash(x)

            Returns the reply's hash.

    .. versionadded:: 1.5

    Attributes
    -----------
    id: :class:`int`
        The reply's ID.
    content: :class:`str`
        The reply's content.
    parent: :class:`.ForumTopic`
        The topic that the reply is a child of.
    parent_id: :class:`int`
        The ID of the parent topic.
    created_at: :class:`datetime.datetime`
        When the reply was created.
    updated_at: Optional[:class:`datetime.datetime`]
        When the reply was last updated.
    """

    if TYPE_CHECKING:
        parent: ForumTopic
        parent_id: int

    async def edit(
        self,
        *,
        content: str,
    ) -> ForumTopicReply:
        """|coro|

        Edit this reply.

        Parameters
        -----------
        content: :class:`str`
            The content of the reply.

        Returns
        --------
        :class:`ForumTopicReply`
            The updated reply.

        Raises
        -------
        NotFound
            This reply does not exist.
        Forbidden
            You do not have permission to update this reply.
        HTTPException
            Failed to update this reply.
        """

        payload = {
            'content': content,
        }

        data = await self._state.update_forum_topic_comment(self.parent.channel_id, self.parent_id, self.id, payload=payload)
        return ForumTopicReply(state=self._state, data=data['forumTopicComment'], parent=self.parent)

    async def add_reaction(self, emote: Emote, /) -> None:
        """|coro|

        Add a reaction to this reply.

        .. versionadded:: 1.6

        Parameters
        -----------
        emote: :class:`.Emote`
            The emote to add.
        """
        emote_id: int = getattr(emote, 'id', emote)
        await self._state.add_forum_topic_comment_reaction_emote(self.channel.id, self.parent_id, self.id, emote_id)

    async def remove_self_reaction(self, emote: Emote, /) -> None:
        """|coro|

        Remove one of your reactions from this reply.

        .. versionadded:: 1.6

        Parameters
        -----------
        emote: :class:`.Emote`
            The emote to remove.
        """
        emote_id: int = getattr(emote, 'id', emote)
        await self._state.remove_forum_topic_comment_reaction_emote(self.channel.id, self.parent_id, self.id, emote_id)

    async def delete(self) -> None:
        """|coro|

        Delete this reply.

        Raises
        -------
        NotFound
            This reply does not exist.
        Forbidden
            You do not have permission to delete this reply.
        HTTPException
            Failed to delete this reply.
        """

        await self._state.delete_forum_topic_comment(self.parent.channel_id, self.parent_id, self.id)

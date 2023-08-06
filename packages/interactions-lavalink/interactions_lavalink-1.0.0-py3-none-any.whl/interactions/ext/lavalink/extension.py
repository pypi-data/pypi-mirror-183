from typing import Union

from lavalink import Client as LavalinkClient
from lavalink import Event as BaseLavalinkEvent

from interactions import Channel, Client, Guild, OpCodeType, Snowflake

from .player import Player

__all__ = ("Lavalink", "setup")


class Lavalink:
    def __init__(self, bot: Client):
        self._bot: Client = bot
        self.client: LavalinkClient = None

        if bot.me is not None:
            self.__init_lavalink()

        self._bot._websocket._dispatch.register(self.__raw_socket_create, "raw_socket_create")

    def add_node(
        self,
        host: str,
        port: int,
        password: str,
        region: str,
        resume_key: str = None,
        resume_timeout: int = 60,
        name: str = None,
        reconnect_attempts: int = 3,
        filters: bool = True,
        ssl: bool = False,
    ):
        if self.client is None:
            self.__init_lavalink()

        return self.client.add_node(
            host=host,
            port=port,
            password=password,
            region=region,
            resume_key=resume_key,
            resume_timeout=resume_timeout,
            name=name,
            reconnect_attempts=reconnect_attempts,
            filters=filters,
            ssl=ssl,
        )

    def __init_lavalink(self):
        self.client = LavalinkClient(int(self._bot.me.id), player=Player)
        self.client.add_event_hook(self.__lavalink_event)

    def get_player(self, guild_id: Union[Guild, Snowflake, str, int]) -> Player:
        """
        :param Union[Guild, Snowflake, str, int] guild_id: The ID of the guild
        :return: Founded player
        :rtype: Player
        """
        _guild_id = int(guild_id.id if isinstance(guild_id, Guild) else guild_id)

        player: Player = self.client.player_manager.get(_guild_id)

        return player

    def create_player(self, guild_id: Union[Guild, Snowflake, str, int]) -> Player:
        """
        :param Union[Guild, Snowflake, str, int] guild_id: The ID of the guild
        :return: Created player
        :rtype: Player
        """
        _guild_id = int(guild_id.id if isinstance(guild_id, Guild) else guild_id)

        player = self.client.player_manager.create(_guild_id)
        player._bot = self._bot

        return player

    async def connect(
        self,
        guild_id: Union[Guild, Snowflake, str, int],
        channel_id: Union[Channel, Snowflake, str, int],
        self_deaf: bool = False,
        self_mute: bool = False,
    ) -> Player:
        """
        Connects to voice channel and creates player.

        :param Union[Snowflake, int, str] guild_id: The guild id to connect.
        :param Union[Snowflake, int, str] channel_id: The channel id to connect.
        :param bool self_deaf: Whether bot is self deafened
        :param bool self_mute: Whether bot is self muted
        :return: Created guild player.
        :rtype: Player
        """
        _guild_id = int(guild_id.id if isinstance(guild_id, Guild) else guild_id)
        _channel_id = int(channel_id.id if isinstance(channel_id, Channel) else channel_id)
        await self.__update_voice_state(_guild_id, _channel_id, self_deaf, self_mute)

        player = self.get_player(_guild_id)
        if player is None:
            player = self.create_player(_guild_id)
        return player

    async def disconnect(self, guild_id: Union[Guild, Snowflake, str, int]):
        """
        :param Union[Snowflake, int, str] guild_id: The guild id to disconnect from.
        """
        _guild_id = int(guild_id.id if isinstance(guild_id, Guild) else guild_id)

        await self.__update_voice_state(_guild_id)
        await self.client.player_manager.destroy(_guild_id)

    async def __lavalink_event(self, event: BaseLavalinkEvent):
        event_name: str = self._get_event_name(event.__class__.__name__)

        self._bot._websocket._dispatch.dispatch(event_name, event)

    @staticmethod
    def _get_event_name(event_name: str) -> str:
        _event_name = event_name.removesuffix("Event")
        for char in _event_name:
            if char.isupper():
                _event_name = _event_name.replace(char, f"_{char.lower()}", 1)
        return f"on{_event_name}"

    async def __raw_socket_create(self, name: str, data: dict):
        if name not in {"VOICE_STATE_UPDATE", "VOICE_SERVER_UPDATE"}:
            return

        _data: dict = {"t": name, "d": data}
        await self.client.voice_update_handler(_data)

    async def __update_voice_state(
        self,
        guild_id: int,
        channel_id: int = None,
        self_deaf: bool = None,
        self_mute: bool = None,
    ):
        """
        Sends VOICE_STATE packet to websocket.

        :param int guild_id: The guild id.
        :param int channel_id: The channel id.
        :param bool self_deaf: Whether bot is self deafened
        :param bool self_mute: Whether bot is self muted
        """
        payload = {
            "op": OpCodeType.VOICE_STATE,
            "d": {
                "guild_id": str(guild_id),
                "channel_id": str(channel_id) if channel_id is not None else None,
            },
        }

        if self_deaf is not None:
            payload["d"]["self_deaf"] = self_deaf
        if self_mute is not None:
            payload["d"]["self_mute"] = self_mute

        await self._bot._websocket._send_packet(payload)


def setup(bot: Client):
    return Lavalink(bot)

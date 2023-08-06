from discord.ext.commands import Cog, Bot, AutoShardedBot
from .client import SBLApiClient
from typing import Union

class SBLCog(
  Cog
):
  """Cog handler class for :class:`~sblpy.client.SBLApiClient`

  Parameters
  -----------
  bot: Union[:class:`~discord.ext.commands.Bot`, :class:`~discord.ext.commands.AutoShardedBot`]
    Your dpy Bot
  auth: :class:`~str`
    Your auth token of SBL Api
  """
  def __init__(
    self,
    bot: Union[
      Bot,
      AutoShardedBot
    ],
    auth: str
  ):
    """Constructor"""
    self.bot = bot
    if not hasattr(
      self.bot,
      "SBLClient"
    ):
      SBLApiClient(
        self.bot,
        auth
      )

  @Cog.listener()
  async def on_guild_join(
    self,
    guild
  ):
    """Posts server count when bot joins a guild"""
    if self.bot.SBLClient.postBotStats():
      self.bot.SBLClient.log("Posted stats on guild join")

  @Cog.listener()
  async def on_guild_remove(
    self,
    guild
  ):
    """Posts server count when bot leaves a guild"""
    if self.bot.SBLClient.postBotStats():
      self.bot.SBLClient.log("Posted stats on guild leave")

  @Cog.listener()
  async def on_ready(
    self
  ):
    """Posts server count when bot is ready to serve"""
    if self.bot.SBLClient.postBotStats():
      self.bot.SBLClient.log("Posted stats on ready")


  @classmethod
  def setup(
    cls,
    bot: Union[
      Bot,
      AutoShardedBot
    ],
    auth: str = ""
  ):
    """Main method, this will add cog to bot

    Parameters
    -----------
    bot: Union[:class:`~discord.ext.commands.Bot`, :class:`~discord.ext.commands.AutoShardedBot`]
      Your dpy Bot
    auth: :class:`~str`
      Your auth token of SBL Api

    Examples
    ----------
    
    .. code-block:: python3

        from sblpy import SBLCog


        # if you are using discord.py 2.0.0+, then
        await SBLCog.setup(bot,"SBL_AUTH_TOKEN")
        # else
        SBLCog.setup(bot, "SBL_AUTH_TOKEN")
    """
    self = cls(
      bot,
      auth
    )
    return self.bot.add_cog(
      self
    )

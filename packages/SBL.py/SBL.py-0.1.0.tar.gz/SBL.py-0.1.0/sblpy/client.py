from typing import Union
from discord import Client, AutoShardedClient
from discord.ext.commands import Bot, AutoShardedBot
from .http import Route
from .error import SBLError


class SBLApiClient:
  """SBLApiClient is the client of https://SmartBots.tk api

  Parameters
  ------------
  bot: Union[:class:`~discord.ext.commands.Bot`, :class:`~discord.ext.commands.AutoShardedBot`]
    Your dpy Bot
  auth_token: :class:`~str`
    Bot's auth token of SBL Api
  """
  def __init__(
    self,
    bot: Union[
      Bot,
      AutoShardedBot
    ],
    auth_token: str
  ) -> None:
    """Constructor"""
    self.bot = bot
    self.token = auth_token
    self.bot.SBLClient = self
    self.log = print

  @property
  def logger(self):
    r"""The logger, used by SBLCog

    To set it use ``SblClient.logger = function``
    This should must be callable

    Default: :meth:`print`
    """
    return self.log

  @logger.setter
  def logger(self, func):
    self.log = func

  @property
  def id(
    self
  ) -> int:
    return int(
      self.bot.user.id
    )

  def postBotStats(
    self
  ):
    """Posts Bot's server count"""
    headers = {
      "authorization": str(
        self.token
      ),
      "Content-Type": "application/json"
    }
    payload = {
      "server_count": len(
        self.bot.guilds
      )
    }
    route = Route(
      "POST",
      "/stats/{id}",
      headers = headers,
      json = payload,
      id = self.id
    )
    try:
      resp = route.go().json()
    except:
      self.dispatch(
        "error",
        "SmartBots server is offline",
      )
      return False

    if str(
      resp.get(
        "success"
      )
    ).lower() == "false":
      self.dispatch(
        "error",
        resp.get(
          "error"
        )
      )
      return False

    return resp

  def getBotLikes(
    self
  ):
    """Get likers of bot who liked within 12hrs"""
    headers = {
      "authorization": str(self.token)
    }
    route = Route(
      "GET",
      "/liked/{id}",
      headers = headers,
      id = self.id
    )
    try:
      resp = route.go().json()
    except:
      self.dispatch(
        "error",
        "SmartBots server is offline",
      )
      return False

    if str(
      resp.get(
        "success"
      )
    ).lower() == "false":
      self.dispatch(
        "error",
        resp.get(
          "error"
        )
      )
      return False

    return resp

  def dispatch(self, handler, *args):
    self.bot.dispatch("sbl_"+handler,*args)

  def on_error(self, func):
    """Used to get error, occurred during using SBL

    Examples
    ---------

    .. code-block:: python3

        @bot.SblClient.on_error
        async def on_sbl_error(error):
            print("An error during using SBL:", error)

    """
    func.__name__ = "on_sbl_error"
    return self.bot.event(func)

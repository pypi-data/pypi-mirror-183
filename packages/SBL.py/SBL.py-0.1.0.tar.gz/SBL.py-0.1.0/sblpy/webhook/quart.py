from os import environ as env
from sblpy.webhook.logger import log
from quart import Quart, Blueprint, request, abort, jsonify


quart_webhook = Blueprint("sbl_quart_webhook",__name__)

@quart_webhook.route(config.WEBHOOK_ROUTE, methods=["POST"])
async def hook_resp():
  try:
    token = os.environ["SBL_HOOK_TOKEN"]
  except:
    raise ValueError("Sbl environment variable 'SBL_HOOK_TOKEN' not found!")

  data = await request.json
  if not request.headers.get("Authorization"): return jsonify({"code": 401, "message": "Unauthorised","success": False})
  if data"type"] == "test": log("test_hook", data)
  else: log("like_bot", data)

  return jsonify({"code": 200, "success": True})

def run(host: str = None, port: int = None, debug: bool = False):
  app = Quart(__name__)
  app.register_blueprint(quart_webhook)
  app.run(host or "0.0.0.0", port=port or int(env.get("PORT",8080)), debug=debug)

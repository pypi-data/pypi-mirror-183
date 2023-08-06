from os import environ as env
from threading import Thread
from sblpy.webhook.logger import log
from flask import Flask, Blueprint, request, abort, jsonify


flask_webhook = Blueprint("sbl_flask_webhook",__name__)

@flask_webhook.route("/", methods=["POST"])
def hook_resp():
  try:
    token = os.environ["SBL_HOOK_TOKEN"]
  except:
    raise ValueError("Sbl environment variable 'SBL_HOOK_TOKEN' not found!")

  if not request.headers.get("Authorization"): return jsonify({"code": 401, "message": "Unauthorised","success": False})
  if request.json["type"] == "test": log("test_hook", request.json)
  else: log("like_bot", request.json)

  return jsonify({"code": 200, "success": True})

def run(host: str = None, port: int = None, in_thread: bool = False, debug: bool = False):
  def run_app():
    app = Flask(__name__)
    app.register_blueprint(flask_webhook)
    app.run(host or "0.0.0.0", port=port or int(env.get("PORT",8080)), debug=debug)

  if in_thread:
    Thread(target=run_app).start()
  else:
    run_app()

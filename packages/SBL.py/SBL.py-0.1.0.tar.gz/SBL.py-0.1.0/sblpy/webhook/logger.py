def log(type, data):
  if type is "test":
    print("Recieved a test like for the bot", data["bot"])
  else:
    print("Recieved a like from user", data["user"], "for the bot", data["bot"])

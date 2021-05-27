from flask import Flask
from o import jwt, app
from ha_lib.api.ha_api import ha
# Create Flask App
app.register_blueprint(ha)

# Check for blacklited tokens




if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 5000, debug = True)
    
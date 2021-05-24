from flask import Flask
from o import jwt, app
from gov_lib.api.gov_functions import GovFunc as GF
from gov_lib.api.gov_api import gov
# Create Flask App
app.register_blueprint(gov)

# Check for blacklited tokens

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    print(jti)
    return GF.check_token(jti)


if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 4000, debug = True)
    
from flask import Flask, Blueprint, json, request, redirect, jsonify, render_template, g, url_for, session
from flask.globals import current_app
from gov_lib.models.account_model import AccountModel as AM
from gov_lib.models.account_tokens_revoked_model import UserRevokedTokensModel as URT
from gov_lib.api.gov_functions import GovFunc as GF
from o import db
import datetime
from datetime import date
import uuid

from flask_jwt_extended import (
    create_access_token, 
    get_jwt_identity,
    jwt_required,
    get_jwt
)


gov = Blueprint("site", __name__)

@gov.route("/")
def dbcreation():
    """Gets all people registered
    :return: Returns all people registered
   
    """
    db.create_all() 
    return "Hi"

@gov.route("/register", methods=['POST'])
def register():

    # Read JSON data from post
    data = request.get_json()

    # Break down JSON data
    user_uuid = str(uuid.uuid4())
    first_name = data['first_name']
    last_name = data['last_name']
    email_address = data['email_address']
    drivers_licence = data['drivers_licence']
    password = data['password']
    phone_number = data['phone_number']

    # Create new user
    new_user = AM(uuid = user_uuid,
        first_name = first_name,
        last_name = last_name,
        email_address = email_address,
        drivers_licence = drivers_licence,
        password = password,
        phone_number = phone_number
    )

    try:
        # Submit to DB
        new_user.save_to_db()
        
        # Return in JSON
        return jsonify(uuid = new_user.uuid)
    
    except Exception as e:
                emsg = e
                return jsonify(emsg = emsg)


@gov.route("/login", methods=['POST'])
def login():

    # Read JSON data from post
    data = request.get_json()

    # Break down JSON data
    user_uuid = data['uuid']
    password = data['password']

    # Capture the current user UUID
    current_user = AM.find_by_uuid(user_uuid)

    # Check the password
    if current_user.password == password:
        msg = 'Logged in'

        # Time limit for JTI token
        expires = datetime.timedelta(minutes=30) 

        # Create the JTI access tokens
        access_token = create_access_token(identity = user_uuid, expires_delta = expires, fresh = True)

        # Return a 200 with tokens
        return jsonify(msg = msg, access_token = access_token), 200

    else:
        msg = "Try Again - Wrong Credtials"
        return jsonify(msg = msg), 400



@gov.route("/logout", methods=['POST'])
@jwt_required()
def logout():

    try:
        
        jti = get_jwt()['jti']

        token = URT(jti = jti, date = date.today())
        token.save_to_db()

        return jsonify(msg='User is now logged out'), 200 
            

    except Exception as e:

        return jsonify(msg="A error as occurred, try relogging in", error = str(e)), 500


@gov.route("/check", methods=['POST'])
@jwt_required()
def check():
    return "Hi"


from flask import Flask, Blueprint, json, request, redirect, jsonify, render_template, g, url_for, session
from ha_lib.api.ha_functions import ha_functions as haf
from o import db
from datetime import datetime
import requests, hashlib
from urllib.parse import urlparse

ha = Blueprint("site", __name__)

@ha.route("/")
def home():

    return "hi"

@ha.route("/newpermit", methods = ["POST"])
def permit():

    # capture json
    json = request.json

    # VERY basic json check
    if json == None:
        return jsonify( msg = "do you even json"), 418

    for each in json:
        if each == None:
        
            return jsonify( msg = each +" must have a value"), 418
    
    exact_address = json["exact_address"]
    town = json["town"]
    postcode = json["postcode"]
    appraised_value = json["appraised_value"]
    wanted_value = json["wanted_value"]
    current_owner_id = json["current_owner_id"]

    return haf.newApplication(exact_address, town, postcode, appraised_value, wanted_value, current_owner_id)

@ha.route("/permit_status", methods=["GET"])
def permit_status():

    # capture json
    json = request.json

    # VERY basic json check
    if json == None:
        return jsonify( msg = "do you even json"), 418
    
    for each in json:
        if each == None:
        
            return jsonify( msg = each +" must have a value"), 418

    propertyNumber = json["propertyNumber"]

    return haf.getIndividual(propertyNumber)


@ha.route("/all_permits")
def permit_all():

    return haf.getAll()

@ha.route("/change_owner", methods=["POST"])
def change_owner():

    # capture json
    json = request.json

    # VERY basic json check
    if json == None:
        return jsonify( msg = "do you even json"), 418
    
    for each in json:
        if each == None:
        
            return jsonify( msg = each +" must have a value"), 418

    propertyNumber = json["propertyNumber"]
    new_owner_id = json["new_owner_id"]

    return haf.changeOwner(propertyNumber, new_owner_id)


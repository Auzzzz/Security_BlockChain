import hashlib, requests, urllib
from flask import Flask, Blueprint, json, request, jsonify

from o import auth_api

class ha_functions():

    def newApplication(exact_address, town, postcode, appraised_value, wanted_value, current_owner_id):


        propertyNumber = ha_functions.propertyNumber(exact_address, town, postcode)
        
        application = {
                "propertyNumber": propertyNumber,
                "prop_id":propertyNumber,
                "exact_address":exact_address,
                "town":town,
                "postcode":postcode,
                "appraised_value":appraised_value,
                "wanted_value":wanted_value,
                "current_owner_id":current_owner_id,
                "application_ipfs":"",
                "status":"Open",
                "auth_s_id":"",
                "bank_loan_id":""
            }
        
        q = 'http://%s/api/add' % (auth_api,)
        res = requests.post(q, json= application)

        return jsonify(msg = res.content, propertyNumber=propertyNumber)

    def getIndividual(propertyNumber):
        # Set
        q = 'http://%s/api/query/%s' % (auth_api, propertyNumber)

        # Post/Get
        res = requests.get(q)
        
        # return the content of the reply
        return res.content

    def getAll():
        # Set
        q = 'http://%s/api/query/all' % (auth_api)

        # Post/Get
        res = requests.get(q)
        
        # return the content of the reply
        return res.content

    def changeOwner(propertyNumber, new_owner_id):
        
        json = {
            "prop_index": propertyNumber,
            "owner":new_owner_id
        }

        # Set
        q = 'http://%s/api/changeowner' % (auth_api)

        # Post/Get
        res = requests.put(q, json = json)
        
        # return the content of the reply
        return res.content



    def propertyNumber(exact_Address, town, postcode):

        # Make one string
        string = "EA=" + str(exact_Address) + "T=" + str(town) + "P=" + str(postcode)
        # String to bytes
        string = str.encode(string)

        # Return a sha256 string
        return hashlib.sha256(string).hexdigest()
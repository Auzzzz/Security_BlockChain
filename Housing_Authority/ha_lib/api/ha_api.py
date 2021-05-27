

from flask import Flask, Blueprint, json, request, redirect, jsonify, render_template, g, url_for, session
#from ha_lib.api.ha_functions import ha_bc
from o import db
from datetime import datetime


class ha_bc:
    def __init__(self):
        self.transactions = []
        self.chain = []

        # Create the first block 'genesis block)'
        self.create_block(previous_hash='1')

    # find the last block id
    @property
    def last_block(self):
        return self.chain[-1]

    def create_block(self, previous_hash):

        new_block = {
            'index': len(self.chain) + 1,
            'time': datetime.now(),
            'transactions': self.transactions,
            'check': True,
            'previous_hash': 12,
        }


        self.chain.append(new_block)
        print(self.chain)
        return new_block
        

    def blockchain_valid_check(chain):

        last_block = chain[0]
        index = 1

        while index < len(chain):
            block = chain[index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")
            
            # Rehash to check the hash is correct
            last_block_hash = self.hash(last_block)
            if block['previous_hash'] != last_block_hash:
                return False

            last_block = block
            index += 1

        return True


    def assign_permit(self, ha_staff_id, reciver, permit_id):
        
        # Add permit to a block as a "transaction" between the Authority and the inidivdual

        self.transactions.append({
            'ha_approver': ha_staff_id,
            'reciver': reciver,
            'permit_id': permit_id,
        })
    
        return self.last_block['index'] + 1


## Api ##

ha = Blueprint("site", __name__)

@ha.route("/")
def dbcreation():
    """Gets all people registered
    :return: Returns all people registered
   
    """
    db.create_all() 
    return "Hi"

@ha.route('/permit/new', methods = ['POST'])
def new_permit():

    # get data from post data
    data = request.get_json()

    new_permit = ha_bc()
    new_permit.assign_permit(data['ha_staff_id'], data['reciver'], data['permit_id'])
    print(new_permit)

    return "hi"
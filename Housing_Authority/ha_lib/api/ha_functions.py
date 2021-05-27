

class ha_bc:
    def __init__(self):
        self.transactions = []
        self.chain = []

        # Create the genesis block
        self.new_block(previous_hash='1')

    # find the last block id
    @property
    def last_block(self):
        return self.chain[-1]

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


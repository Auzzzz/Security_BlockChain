# Flask API implimentation for 2021 Sem 1 Security in IT RMIT

## To install, Python3, virtualenv & git must be installed

```bash

pip install virtualenv
virtualenv env
source env/env/bin

to leave a virtualenv 'deactvate' in the command line

```

## Clone repo & install all requirements
the requirements will cover all API's

```bash

git clone https://github.com/Auzzzz/Security_BlockChain.git
cd /Security_BlockChain

pip install -r requirements.txt

```

## Setup Flask
for RMIT - use the predefined IP for the Hyperledger Fabric install
If you have somehow found this you will need to complete the setup for Hyperledger https://github.com/Auzzzz/Hyperledger_Fabric-for-Security-In-Comp--RMIT-


In each file is a o.py, this has the setup for flask
``` bash

# for the Gov server a MYSQL connection is needed
HOST = ""
USER = ""
PASSWORD = ""
DATABASE = ""

# Housing_Authority & Banks
auth_api is the connection to the Hyperledger Fabric API

```


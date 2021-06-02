# Object file to avoid circular imports due to use of blueprints
# To be called at the start of each blueprint file
from flask_sqlalchemy import SQLAlchemy 
from flask_jwt_extended import JWTManager
from flask import Flask

app = Flask(__name__)

# SQLAlchemy Object
db = SQLAlchemy()
# JwtManager object
jwt = JWTManager(app)

auth_api = "178.128.149.221:8080"

# MySQL Server Connection
HOST = "128.199.0.44"
USER = "user"
PASSWORD = "Banana123"
DATABASE = "ha"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{}:{}@{}/{}".format(USER, PASSWORD, HOST, DATABASE)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# App Config
app.config['SECRET_KEY'] = '8sOGgEM1Ie2gFer4wMlYbSahMeuf0cki'
app.config['JWT_SECRET_KEY'] = 'p3kjr2ifh997g8pyi31hlk3948yhrbf2lq24kej4diml2wrfkehivun9'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']

# Init the DB connection
db.init_app(app)
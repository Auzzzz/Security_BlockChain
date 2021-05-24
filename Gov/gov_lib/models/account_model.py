from o import db
from flask import jsonify

class AccountModel(db.Model):
    __tablename__ = "accounts"
    uuid = db.Column(db.VARCHAR(36), primary_key = True)
    first_name = db.Column(db.VARCHAR(50))
    last_name = db.Column(db.VARCHAR(50))
    email_address = db.Column(db.VARCHAR(70))
    drivers_licence = db.Column(db.VARCHAR(12))
    password = db.Column(db.VARCHAR(192))
    phone_number = db.Column(db.VARCHAR(14))

    def __init__(self, uuid, first_name, last_name, email_address, password, phone_number, drivers_licence):
        self.uuid = uuid
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.password = password
        self.phone_number = phone_number
        self.drivers_licence = drivers_licence

    def find_everyone():

        return AccountModel.query.all()

    def find_by_username(username):

        return AccountModel.query.filter_by(username=username).first()


    def find_by_uuid(uuid):

        return AccountModel.query.filter_by(uuid=uuid).first()

    def check_uuid(uuid):
        if AccountModel.query.filter_by(uuid=uuid).first:
            return False

        return True
    
    def save_to_db(self):

        db.session.add(self)
        db.session.commit()
    
    def deleteme(self):

        db.session.delete(self)
        db.session.commit()
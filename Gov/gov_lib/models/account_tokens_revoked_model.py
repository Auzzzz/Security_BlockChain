from o import db

class UserRevokedTokensModel(db.Model):
    __tablename__ = "user_revoked_tokens"
    jti = db.Column(db.String(287), primary_key = True)
    date = db.Column(db.DateTime)

    def __init__(self, jti, date):
            self.jti = jti
            self.date = date
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def check_token(jti):

        return UserRevokedTokensModel.query.filter_by(jti=jti).first()
    
    def deleteme(self):

        db.session.delete(self)
        db.session.commit()

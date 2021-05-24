from gov_lib.models.account_tokens_revoked_model import UserRevokedTokensModel as UR
from gov_lib.models.account_model import AccountModel as AM

class GovFunc():

    def blacklist_token(jti):
            try:
                
                token = UR(jti = jti, date = date.today())
                token.save_to_db()

                return True
            except Exception as e:
                print(e)

                return e

    def unblacklist_token(jti):
            try:
                
                token = UR.check_token(jti)
                token.deleteme()

                return True

            except Exception as e:
                print(e)

                return e

    def check_token(jti):

        return UR.check_token(jti)

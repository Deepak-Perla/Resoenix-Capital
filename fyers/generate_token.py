from fyers_api import accessToken
app_id = open('app_id.txt','r').read()
app_secret = open('app_secret.txt','r').read()
app_session = accessToken.SessionModel(app_id, app_secret)
response = app_session.auth()
print(response)
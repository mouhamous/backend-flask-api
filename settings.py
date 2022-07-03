import datetime
# configuration

class Config():
	DEBUG = True
	SECRET_KEY = 'super-secret'
	JWT_EXPIRATION_DELTA= datetime.timedelta(hours=1)
	#db
	SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False


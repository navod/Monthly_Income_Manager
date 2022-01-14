class Config(object):
	# SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@localhost:3306/income'
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:navod2000@income.ckqyp22eptyw.us-east-2.rds.amazonaws.com:3306/income'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
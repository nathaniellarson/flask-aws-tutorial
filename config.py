# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:iVfLwDvKfPP5rv4FL13E@aws-flask-tutorial.cp7tlp79g8xx.us-east-1.rds.amazonaws.com:3306/aws-flask-tutorial'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:iVfLwDvKfPP5rv4FL13E@quiz.c9zzyfawbdwa.us-east-1.rds.amazonaws.com:3306/chicago_quiz'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://apiot:kud0s2023@terraform-20200820224258521800000001.cjsrvztn6fqk.us-east-1.rds.amazonaws.com:3306/apiot'

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'

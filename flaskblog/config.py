import os

# I hard-coded some of the configurations, Corey Schafer recommends configuring this as environment variables for security reasons.

class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'#os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' #os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'tomtomwrong@gmail.com' #os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = 'Hamburgers123'  #os.environ.get('EMAIL_PASS')

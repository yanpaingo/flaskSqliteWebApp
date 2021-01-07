
class Config:
    SECRET_KEY = 'd3c0863848a88fbb9a3f10467aa59d17'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    DEBUG = True

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587  # 25
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'testingto009@gmail.com'
    MAIL_PASSWORD = 'testingto0987654321'
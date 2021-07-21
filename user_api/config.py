class Config:
        SECRET_KEY="testetesteteste"

class Development(Config):
    FLASK_ENV='development'
    FLASK_DEBUG=1

class Prodution(Config):
    FLASK_ENV='production'
    FLASK_DEBUG=0

class Testing(Config):
    FLASK_ENV='testing'


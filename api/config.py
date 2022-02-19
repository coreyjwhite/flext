class Config:
    # Flask options
    DEBUG = True

    OPENAPI_VERSION = "3.0.2"

    # SQLAlchemy options
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable deprecated feature
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"

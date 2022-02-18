class Config:
    # Flask options
    DEBUG = True

    # SQLAlchemy options
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable deprecated feature
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"

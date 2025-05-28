import os
class Config:
    SECRET_KEY = 'q!#x0w6fvf53)rc%4a5=rg0xw6dv@sg!+72+(cq8p6t*hoe631'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    ENV = 'base'

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
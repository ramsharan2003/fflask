import os

class Config:
    SECRET_KEY = os.environ.get('Thisissecret') 
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgresql://postgres:tonu%402003@localhost:5432/flaskapi') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('thisisjwt') 


#postgresql://flaskapi_bo0o_user:4RUrYB8gm30UU1hOKcqhPIMEwQVcvxE2@dpg-cr6b5u5umphs73bj04s0-a/flaskapi_bo0o
#postgresql://flaskapi_bo0o_user:4RUrYB8gm30UU1hOKcqhPIMEwQVcvxE2@dpg-cr6b5u5umphs73bj04s0-a.singapore-postgres.render.com/flaskapi_bo0o


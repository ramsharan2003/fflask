import os

class Config:
    SECRET_KEY = os.environ.get('Thisissecret') 
    SQLALCHEMY_DATABASE_URI = os.environ.get('psql "postgres://default:x1SfVbRac7vX@ep-solitary-dust-a1cazav3.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('thisisjwt') 


#postgresql://flaskapi_bo0o_user:4RUrYB8gm30UU1hOKcqhPIMEwQVcvxE2@dpg-cr6b5u5umphs73bj04s0-a/flaskapi_bo0o
#postgresql://flaskapi_bo0o_user:4RUrYB8gm30UU1hOKcqhPIMEwQVcvxE2@dpg-cr6b5u5umphs73bj04s0-a.singapore-postgres.render.com/flaskapi_bo0o


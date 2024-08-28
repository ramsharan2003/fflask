import os
from flask import Flask
from config import Config
from models import db, bcrypt
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flaskapi_bo0o_user:4RUrYB8gm30UU1hOKcqhPIMEwQVcvxE2@dpg-cr6b5u5umphs73bj04s0-a.singapore-postgres.render.com/flaskapi_bo0o'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tonu%402003@localhost:5432/flaskapi'
    app.config['JWT_SECRET_KEY']='thisissecret'
    app.config['SECRET_KEY']='secretIshere'
    db.init_app(app)
    bcrypt.init_app(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)

    from routes.user_routes import user_bp
    from routes.contact_routes import contact_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(contact_bp)

    return app

if __name__ == "__main__":
 

  app = create_app()
  port = int(os.environ.get('PORT',5000))
  app.run(port=port)


  
     
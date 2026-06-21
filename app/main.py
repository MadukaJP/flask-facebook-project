import os
from flask import Flask
from flask_migrate import Migrate
from models.models import db
from views.views import create_view
from  admins.admin import admin
from flask_socketio import SocketIO


basedir = os.path.abspath(os.path.dirname(__file__))



def create_app():
    app = Flask(__name__)

    app.config["UPLOAD_EXTENSIONS"] = [".jpg", ".png", ".jpeg"]
    app.config["UPLOAD_PATH"] = "static/images/uploads"
    app.config['SECRET_KEY'] = "weertyuijkopl"

    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False 

    db.init_app(app)
    admin.init_app(app)
    migrate = Migrate(app, db)

    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

    create_view(app)
  

    return app


if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get("PORT", 5000))
    app.socketio.run(app, host='0.0.0.0', port=port, debug=True, allow_unsafe_werkzeug=True)


    



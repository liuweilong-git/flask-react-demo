from flask import Flask, session, g, request
from exts import db, mail
from flask_migrate import Migrate
from blueprints.general_user import bp as g_bp
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(g_bp)
# app.register_blueprint(user_bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!！'


if __name__ == '__main__':
    app.run(debug=True, port=5000)

# backend/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend.models.user import db  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# 导入路由
from backend.routes.dialogue import bp as dialogue_bp
from backend.routes.game import bp as game_bp
from backend.routes.economy import bp as economy_bp

app.register_blueprint(dialogue_bp)
app.register_blueprint(game_bp)
app.register_blueprint(economy_bp)

if __name__ == '__main__':
    app.run(debug=True)
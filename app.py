# app.py
# Stock Simulator
# Main executable for stock trading web app

from flask import Flask, render_template, session
from api import apiBlueprint
from stock import stockBlueprint
from portfolio import Portfolio, serialize


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY='secretkey')
    app.register_blueprint(apiBlueprint)
    app.register_blueprint(stockBlueprint)

    @app.route('/')
    def index():
        if 'portfolio' not in session:
            session['portfolio'] = serialize(Portfolio(500, {}))
        return render_template('index.html')

    return app

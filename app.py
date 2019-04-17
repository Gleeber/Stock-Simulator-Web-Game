# app.py
# Stock Simulator
# Main executable for stock trading web app

from flask import Flask, render_template
from api import apiBlueprint
from stock import stockBlueprint


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
            SECRET_KEY = 'secretkey'
            )
    app.register_blueprint(apiBlueprint)
    app.register_blueprint(stockBlueprint)
    @app.route('/')
    def index():
        return render_template('index.html')
    return app

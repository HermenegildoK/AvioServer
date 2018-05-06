# -*- coding: utf-8 -*-
from flask import Flask
from config import DEBUG
from avioserver.views.controllers import avio_controllers
from avioserver.views.apptest import apptest_controllers

avio_server_app = Flask(__name__)
avio_server_app.config.from_object('config')
avio_server_app.register_blueprint(avio_controllers)

if DEBUG:
    avio_server_app.register_blueprint(apptest_controllers)

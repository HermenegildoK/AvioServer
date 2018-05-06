# -*- coding: utf-8 -*-
from flask import Flask
from avioserver.views.controllers import avio_controllers

avio_server_app = Flask(__name__)
avio_server_app.config.from_object('config')
avio_server_app.register_blueprint(avio_controllers)

# -*- coding: utf-8 -*-
from flask import Blueprint
from avioserver.utils import ok_response, error_response

avio_controllers = Blueprint("controllers", __name__)


@avio_controllers.route('/', methods=["GET"])
def index():
    return ok_response(
        {
            "message": "Hello!"
        }
    )


@avio_controllers.route('/error', methods=["GET"])
def error_index():
    return error_response(
        {
            "message": "Hello!"
        }
    )

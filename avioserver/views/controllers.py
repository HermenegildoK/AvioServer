# -*- coding: utf-8 -*-
from flask import Blueprint, request
from avioserver.utils import ok_response, error_response
from avioserver.hardware_modules.motor_communicator import MotorController

avio_controllers = Blueprint("controllers", __name__)
AvioMotorController = MotorController()


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


@avio_controllers.route('/motors/wings', methods=["POST"])
def control_wings():
    AvioMotorController.set_aerlon(int(request.json["position"]))
    return ok_response(
        {
            "message": "Hello",
            "received_data": request.json
        }
    )


@avio_controllers.route('/motors/tail', methods=["POST"])
def control_tail():
    return ok_response(
        {
            "message": "Hello",
            "received_data": request.json
        }
    )


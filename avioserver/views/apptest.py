# -*- coding: utf-8 -*-
from flask import Blueprint, request
from avioserver.utils import ok_response
from time import sleep

apptest_controllers = Blueprint("apptest", __name__)


@apptest_controllers.route('/test/connections/<int:connection_id>', methods=["GET"])
def connections_get(connection_id):
    print(f'connection {connection_id} started')
    sleep(2)
    print(f'connection {connection_id} done')
    return ok_response(
        {
            "message": f"Hello {connection_id}"
        }
    )


@apptest_controllers.route('/test/connections/<int:connection_id>', methods=["POST"])
def connections_post(connection_id):
    return ok_response(
        {
            "message": f"Hello {connection_id}",
            "received_data": request.json
        }
    )

# -*- coding: utf-8 -*-
from flask import jsonify
from datetime import datetime

OK = 2000
ERROR = 5000


def ok_response(data):
    return jsonify(
        {
            "status": OK,
            "server_time": datetime.utcnow().isoformat(),
            "data": data
        }
    )


def error_response(data):
    return jsonify(
        {
            "status": ERROR,
            "server_time": datetime.utcnow().isoformat(),
            "data": data
        }
    )

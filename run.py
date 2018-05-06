# -*- coding: utf-8 -*-
from avioserver import avio_server_app
from config import HOST, PORT, DEBUG

avio_server_app.run(
    host=HOST,
    port=PORT,
    debug=DEBUG
)

# -*- coding: utf-8 -*-
from avioserver import avio_server_app


if __name__ == "__main__":
    """Used with gunicorn
    example:
        
        gunicorn -w 4 -b 127.0.0.1:8000 wsgi:avio_server_app

    """
    avio_server_app.run()

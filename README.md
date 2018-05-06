AvioServer
==========

Flask app which will control model airplane.

To start working on this app:
- create virtualenv, 
- install requirements from `requirements.tx` with:
    
    ```
    pip install -r requirements.txt
    ```
    
and have fun.

To run app:

    python run.py
    
Example for gunicorn:

    pip install gunicorn

    gunicorn -w 4 -b 127.0.0.1:8000 wsgi:avio_server_app

Imagined by @DrazenHizakowski


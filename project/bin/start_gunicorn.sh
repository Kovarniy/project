#!/bin/bash
surce /home/evgen/code/project/env/bin/activate
exec gunicorn -c "/home/evgen/code/project/project/gunicorn_config.py" project.wsgi

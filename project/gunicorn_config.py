command = '/home/evgen/code/project/env/bin/gunicorn'
pythonpath = '/home/evgen/code/project/project'
bind = '127.0.0.1:8000'
workers = 3
user = 'evgen'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=project.settings'

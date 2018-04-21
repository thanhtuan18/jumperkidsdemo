import mongoengine

# mongodb://<admin>:<admin>@ds111798.mlab.com:11798/jumperkids

host = "ds111798.mlab.com"
port = 11798
db_name = "jumperkids"
user_name = "admin"
password = "admin"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())

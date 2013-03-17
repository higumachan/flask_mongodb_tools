
from flask import g
from functools import wraps

def get_db(collection, id_name=None):
    def _(f):
        @wraps(f)
        def __(*args, **kwargs):
            if id_name:
                id = kwargs[id_name]
            else:
                id = kwargs["id"]
            kwargs[collection] = g.db[collection].find_one({"_id": id})
            return f(*args, **kwargs);
        return __
    return _

if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__);
    app.debug = True;
    app.run();


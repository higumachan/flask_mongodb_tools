
from flask import g
from functools import wraps

def get_db(collection, id_name=None, arg_name=None):
    def _(f):
        @wraps(f)
        def __(*args, **kwargs):
            print args;
            print kwargs
            if id_name:
                id = kwargs[id_name]
            else:
                id = kwargs["id"]
            res = g.db[collection].find_one({"_id": id})
            if arg_name:
                kwargs[arg_name] = res;
            else:
                kwargs[collection] = res;
            
            return f(*args, **kwargs);
        return __
    return _

if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__);
    app.debug = True;
    app.run();


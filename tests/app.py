from flask import *
from logging.handlers import *
from settings import *
import pymongo

import sys
sys.path.append("..")

import db

app = Flask(__name__);

formatter = logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
)
error_log = os.path.join(app.root_path, 'logs/error.log')
error_file_handler = RotatingFileHandler(
    error_log, maxBytes=100000, backupCount=10
)    
error_file_handler.setLevel(logging.ERROR)
error_file_handler.setFormatter(formatter)
app.logger.addHandler(error_file_handler)


@app.before_request
def before_request():
    g.conn = pymongo.Connection(host=DB_HOST);
    g.db = g.conn[DB_NAME];

@app.teardown_request
def teardown_request(exception):
    g.conn.close();

@app.route("/")
def index():
    pass;

@app.route("/user/<int:id>")
@db.get_db("users")
def user(id, users):
    print id;
    print users;
    return users["name"] + " " + str(int(users["age"]))

@app.route("/user2/<int:user_id>")
@db.get_db("users", id_name="user_id")
def user2(user_id, users):
    print id;
    print users;
    return users["name"] + " " + str(int(users["age"]))


@app.route("/user3/<int:user_id>")
@db.get_db("users", id_name="user_id", arg_name="user")
def user3(user_id, user):
    print id;
    print user;
    return user["name"] + " " + str(int(user["age"]))

if __name__ == "__main__":
    app.debug = True;
    app.run(port=5500);


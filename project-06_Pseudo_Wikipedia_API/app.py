#

"""
Flask app that exposes the Wikipedia API.
"""

from sqlite3 import dbapi2 as sqlite3
from flask import Flask
from flask import request

# Create application
app = Flask(__name__)

# Load default config and override
def connect_db():
    """Connects to the database"""
    rv = sqlite3.connect(app.config[''])

@app.route("/search")
def hello_world():

    search_query = request.args.get('search_query')
    return "I am searching for {}".format(search_query)

@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)

if __name__ == "__main__":
    app.run()

import os

from flask import render_template
from flask import Flask

from Query.view import QueryView
from imageDatabase.view import InsertIntoImageDatabseView, GetImagesInDB
from flask_mongoengine import MongoEngine

app = Flask(__name__)
UPLOAD_FOLDER = 'protected/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MONGODB_SETTINGS'] = {
    'db': 'VMM',
    'host': 'mongodb+srv://vmm:cyuDkD1H1Fjbnhpu@vmm.n5s2fbf.mongodb.net/VMM?retryWrites=true&w=majority'
}

app.add_url_rule('/image', view_func=InsertIntoImageDatabseView.as_view('imageUpload'))
app.add_url_rule('/image/list', view_func=GetImagesInDB.as_view('imageList'))
app.add_url_rule('/', view_func=QueryView.as_view('query'))

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
db = MongoEngine(app)


@app.route('/')
def index():
    return render_template('query.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0:5000')

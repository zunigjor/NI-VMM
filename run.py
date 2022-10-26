from flask import render_template
from flask import Flask
from views.images.images import Images


app = Flask(__name__)
app.add_url_rule('/images', view_func=Images.as_view('images'))

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0:5000')

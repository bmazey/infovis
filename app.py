import os
import sys
from flask import Flask, render_template

sys.path.append(os.path.dirname(__name__))
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/bars')
def bars():
    return render_template('aid-bars.html')


@app.route('/map')
def diverging_map():
    return render_template('aid-diverging-map.html')


@app.route('/categories')
def categories():
    return render_template('aid-type-bars.html')


if __name__ == '__main__':
    app.run()

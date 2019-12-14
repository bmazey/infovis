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


@app.route('/assignment')
def assignment():
    return render_template('assignment.html')


@app.route('/project-2-viz-1-donated')
def project_2_viz_1_donated():
    return render_template('project-2-viz-1-donor.html')


@app.route('/project-2-viz-1-received')
def project_2_viz_1_received():
    return render_template('project-2-viz-1-recipients.html')


@app.route('/project-2-viz-2')
def project_2_viz_2():
    return render_template('project-2-viz-2.html')


@app.route('/project-3-viz-1')
def project_3_viz_1():
    return render_template('project-3-viz-1.html')


if __name__ == '__main__':
    app.run()

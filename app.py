from flask import Flask, render_template,send_file
import json
import os

# create flask app
app = Flask(__name__, static_url_path='/alimurtaza/static')

def get_projects():
    file_path = os.path.join('static', 'assets', 'projects.json')
    with open(file_path, 'r') as file:
            projects = json.load(file)
    return projects['projects']


@app.errorhandler(Exception)
def handle_exception(message):
    return render_template('error.html', message="Bad Request"), 400


@app.errorhandler(404)
def err_404(message):
    return render_template('error.html', message='404 Page Not Found'), 404


@app.route('/alimurtaza/')
def main_page():
    return render_template('index.html', title='Ali Murtaza - Homepage')


@app.route('/alimurtaza/home')
def home():
    return render_template('base.html', title='Base')

@app.route('/alimurtaza/about')
def about_page():
    return render_template('about.html', title="About")

@app.route('/alimurtaza/contact', methods=['GET', 'POST'])
def contact_page():
    return render_template('contact.html', title='Contact Page')

@app.route('/alimurtaza/projects')
def projects_page():
    return render_template('projects.html', title="Projects", cards=get_projects())

@app.route('/alimurtaza/resume')
def resume():
    return send_file("static/assets/Ali_murtaza-Resume.pdf", as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
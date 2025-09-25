from flask import Flask, render_template

def create_app():

    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template("home.html")
    
    @app.route('/homepage')
    def homepage():
        return render_template("homepage.html")
    
    return app
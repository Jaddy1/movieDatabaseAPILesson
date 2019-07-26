from app import app
from flask import render_template, request
from app.models import model




@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/movieResult', methods=['GET', 'POST'])
def movieResult():
    
    formData = dict(request.form)
    movie = formData["movie"]
    
    movieName = model.userSearch(movie)
    return render_template("movieResult.html", movie = movie)
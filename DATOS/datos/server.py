from flask import Flask

app = Flask(__name__)

from movies import movies
    
@app.route('/movies')
def my_movies():
    return movies

if __name__ == '__main__':
    app.run(debug=True, port=5000)

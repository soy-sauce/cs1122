from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "this is the root"

@app.route('/tuna')
def tuna():
    return '<h2>tuna is good</h2>'

@app.route('/profile/<username>')
def profile(username):
    return "Hey %s" %username

@app.route('/post/<int:post_id>')
def post(post_id):
    return "Post ID is %s" %post_id

if __name__ == "__main__":
    app.run(debug=True)
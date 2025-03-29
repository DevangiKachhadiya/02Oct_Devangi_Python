from flask import Flask

app = Flask(__name__)  # app initlization

@app.route('/')
def index():
    return "Hello Flask!"

@app.route('/about_us')
def about_us():
    return "Welcome to About Us!"

if __name__ == '__main__':
    app.run(debug=True)
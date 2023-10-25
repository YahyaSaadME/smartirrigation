from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route and associated view function
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/temp')
def temp():
    return 10.34

if __name__ == '__main__':
    # Run the Flask application on a local development server
    app.run()

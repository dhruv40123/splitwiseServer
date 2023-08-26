from flask import Flask
from User import getUser

# Create a Flask web application instance
app = Flask(__name__)

# Define a route and a function to handle it


@app.route('/')
def hello():
    # data = getUser()
    # print(data)
    # return data
    return 'Hello, World! hii'


# Run the Flask app when this script is executed
if __name__ == '__main__':
    app.run(debug=True)

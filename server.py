"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <body>
        <h3>Hi! This is the home page.</h3>
        <a href="/hello">Go to the hello page</a>
      </body>
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
        <style>
        body {
          font-family: sans-serif;
        }
        h1 {
          color:#464646;
        }
        .form-inputs {
          margin:1em;
        }
        </style>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <div class="form-inputs">
            <label for "name">What's your name?</label>
            <input type="text" name="person">
          </div>
          <div class="form-inputs">
            <label for="compliments">Would you like compliment?</label>
            <select name="compliments" id="compliments">
                <option value="nice">Nice</option>
                <option value="kind">Kind</option>
                <option value="thoughtful">Thoughtful</option>
            </select>
            <input type="submit" value="Submit">
          </div>
        </form>

        <form action="/diss">
          <div class="form-inputs">
            <label for "name">What's your name?</label>
            <input type="text" name="person">
          </div>
          <div class="form-inputs">
            <label for="diss">Would you like a diss?</label>
            <select name="diss" id="diss">
                <option value="old">Old</option>
                <option value="mean">Mean</option>
                <option value="cold">Cold</option>
            </select>
            <input type="submit" value="Submit">
          </div>
        </form>
        
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliments")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        <h3>Hi, <span>{}</span>! I think you're <span>{}</span>!</h3>
      </body>
    </html>
    """.format(player, compliment)

@app.route('/diss')
def greet_person_diss():
    """Get user by name."""

    player = request.args.get("person")

    diss = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        <h3>Hi, <span>{}</span>! I think you're <span>{}</span>!</h3>
      </body>
    </html>
    """.format(player, diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")

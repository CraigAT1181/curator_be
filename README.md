# Curator

## Introduction

Thanks for your interest in Curator.

This web application allows users to explore museum exhibits or artworks, and store them for the duration of their session. Each particular object can be clicked on to see further detaild information, and a button click allows them to save the piece in their own collection, or remove it again.

## Important Links

This web application does not currently feature a database where user information can be stored. It simply acts as a proxy for requests made to 3rd-party museum APIs. Therefore, for further information about these APIs, please click the following links:

1. Metropolitan Museum: https://metmuseum.github.io/
2. Cleveland Museum of Art: https://openaccess-api.clevelandart.org/

## Technical Specifications

- Flask
- Flask-Cors
- Flask-Caching
- requests
- python-dotenv

## Running Locally

1. Once you've created a local folder from where you intend to run the app, initialise it as a GIT repo using `git init`. Next,

2. Type `git clone https://github.com/CraigAT1181/curator_be.git` into the terminal.

3. In the terminal, type the command `python3 -m venv curator_venv` to create a virtual environment, then

4. Activate the virtual environment with the command `source curator_venv/bin/activate`.

5. Once in the venv, in the terminal, type the command `python3 -r install requirements.txt`.

6. Generate a secret key in preparation for the next step by typing `python3 generate_token.py` in the terminal. Copy the key.

7. In the root directory, create a `.env` and `.flaskenv` file and input the following:

    `.env`:         SECRET_KEY=Your key from the previous step
    `.flaskenv`:    FLASK_APP=app.py 
                    FLASK_ENV=development
                    FLASK_DEBUG=True

8. Finally, run the server by typing `flask run`. It will now be able to receive requests from the front-end.
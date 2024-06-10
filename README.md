# Curator

## Introduction

Thanks for your interest in Curator.

This web application allows users to explore museum exhibits or artworks, and store them for the duration of their session.

## Important Links

This web application does not currently feature a database where user information can be stored. Rather, it acts as a proxy for requests made to 3rd-party museum APIs. See below for further information about these APIs, along with a link to where the backend is hosted.

1. Hosted API: https://curator-be.onrender.com 
2. Metropolitan Museum: https://metmuseum.github.io/
3. Cleveland Museum of Art: https://openaccess-api.clevelandart.org/ 

## Technical Specifications

(see requirements.txt)

## Running Locally

1. Once you've created a local folder from where you intend to run the app, initialise it as a GIT repo using `git init`. Next,

2. Type `git clone https://github.com/CraigAT1181/curator_be.git` into the terminal.

3. In the terminal, type the command `python3 -m venv curator_venv` to create a virtual environment, then

4. Activate the virtual environment with the command `source curator_venv/bin/activate`.

5. Once in the venv (recognisable by the venv name in the command line), in the terminal, type the command `python3 -r install requirements.txt`.

6. Generate a secret key in preparation for the next step by typing `python3 generate_token.py` in the terminal. Copy the key.

7. In the root directory, create a `.env` and `.flaskenv` file and input the following:

    `.env`:         SECRET_KEY=Your key from the previous step
    `.flaskenv`:    FLASK_APP=app.py 
                    FLASK_ENV=development
                    FLASK_DEBUG=True

8. Finally, run the server by typing `flask run`. It will now be able to receive requests from the front-end.

9. Ensure that, if you're making API requests to this local server, that the baseURL in the api.js file on the front end is amended accordingly. It should be changed to `http://127.0.0.1:5000`, otherwise, it will be set to make requests to the hosted API address provided under "Important Links".
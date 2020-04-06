# home-automation for Signzy recrutation

## Tech stack
* Python + Flask + SQLAlchemy: I used this tech stack because of ease of use, quick development and prototyping
* Flask blueprints for modularization and expansions of the project if new functionalities were needed.

## Assumptions
I didn't know what was the meaning behind "To talk to devices mimic one or more libraries that just logs the action it performed. ". I assumed simple CRUD application will be eficient to showcase REST API development.

## Application
Application requires for a user to register and later sign in so she can add every smart home device in the home. From the webconsole she can simply turn on/off selected device from a list.
User registration was done with multiple users in mind if such application was meant to be expanded.
I implemented only "Sign In" and "Registration", next steps would be a user profile page and changing the password/restarting the password.
Whole application is dockerized.

## Running the application
1. Have docker installed
2. In the root folder of the project run `docker-compose up --build` to build and run the application
3. Application will be available under localhost:5000

# eh-notes-app

This app was designed as a take-home test for a position with Open Energy Solutions. It's a simple app that allows you to save your notes. Web UI is built with Vue 3 and API is built with Python 3.10 and Postgres.

## Running the app

Ensure that you have Docker and Docker Compose installed on your machine.

In the root of this repository: `docker compose up -d --build` will start all services on their default ports

Shortcomings:

- UI isn't part of docker compose build yet. You'll need to start API with docker compose, then follow instructions in UI project to start dev server locally.

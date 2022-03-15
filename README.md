# flask-todo

This is a little flask project I made using jinja templates to show off a little todo app. It supports multiple users, each with their own tasks. I used SQLite for the database, SQLAlchemy for the ORM. I didn't focus very much on the frontend for this application, if you would like my frontend work checkout my [porfolio website](http://benmclean981.github.io/).

The main features of this application that I want to highlight are:

- My code, I think I write very clean simple code.
- The database models and the relationships they have. Admittedly this is a small project, but it shows my understanding of databases.
- Project structure, I think I do a good job at making my project structure understandable. I like patterns and I try to do whatever the framework maintainers recommend.

### Development Environment

It is my personal opinion that all developers on a project should share the same dev environment. As such, I have committed my .vscode and .pylintrc files. I recommend you use VSCode if you want to run this project or make any of your own changes.

### Startup

Ensure you are running python 3.10.1. Any earlier version may work but they are untested. I usually work on the latest stable release if I can for a new project.
`python --version`

First install the dependencies.
`pip install -r requirements.txt`

Next, if you are using VSCode, you may simply run the debug command.

If you are not using VSCode, run the following:
`python todo_debug.py`

### Testing

I threw this together in a hurry (< 2 days), and testing is the area that suffered the most. This is unfortunate because I really think automated tests are as important as the source code, especially with Python due to the fact that it does everything at runtime. What tests I do have can be run with `pytest`.

"""Launcher for prod mode"""

from todo.app import create_app

if __name__ == "__main__":
    app = create_app()
    app.run()

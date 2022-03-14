"""Launcher for debug mode"""
from todo.app import create_app
from todo.config import DevelopmentConfig

if __name__ == "__main__":
    app = create_app(DevelopmentConfig())
    app.run()

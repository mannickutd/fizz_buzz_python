from aiohttp import web
from fizz_buzz_python import create_app


if __name__ == '__main__':
    app = create_app()
    web.run_app(app)

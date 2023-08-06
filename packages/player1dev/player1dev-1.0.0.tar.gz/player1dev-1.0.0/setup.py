from setuptools import setup

setup(
    author_email="postbox@ophuscado.com",
    author="Ophuscado",
    description="Simple framework for building (web) apps with Python and Flet. The client is made to operate locally, but can be deployed to a server. The server is made to operate on a server, but can be deployed locally. What you have to decide is the exposition and scope of both. Giving public access to the `client.py` will have serious security risks.\n\nIt relies on Flet (Flutter) and FastAPI. Flet is a Python library that allows you to build Flutter apps with Python. FastAPI is a Python library that allows you to build web apps with Python.",
    include_package_data=True,
    license="BSD-2-Clause",
    links={
        "Author": "https://ophuscado.com",
        "Source": "https://github.com/Ophuscado/py-player1dev",
        "Tracker": "https://github.com/Ophuscado/py-player1dev/issues",
    },
    name="player1dev",
    py_modules=["player1dev"],
    version="1.0.0",
)

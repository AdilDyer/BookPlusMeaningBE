from setuptools import setup

setup(
    name="app",
    version="0.1",
    py_modules=["app"],  # Replace with your script's name without `.py` extension
    install_requires=[
        # List any external dependencies here, for example:
        # 'requests',
        'nltk',
        'flask',
        'flask-cors',
    ],
)

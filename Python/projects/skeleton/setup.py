try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Education Project',
    'author': 'Brandon Tsao',
    'url': 'None',
    'download_url': 'None',
    'author_email': 'brandonstsao@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Pythonic'],
    'scripts': [],
    'name': 'Pythonic'
}

setup(**config)

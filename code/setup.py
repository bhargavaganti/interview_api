import setuptools

__version__ = '0.1'

config = {
    'name': 'schedule',
    'author': 'Mekan ALLABERDIYEV <mekan.allaberdi@gmail.com>',
    'author_email': 'mekan.allaberdi@gmail.com',
    'version': __version__,
    'install_requires': [
                'flask',
                'sqlalchemy',
                'psycopg2'],
    'tests_require': ['nose'],
    'include_package_data': True,
    'zip_safe': False,
    'scripts': [],
    'entry_points': {
        'console_scripts': [
            'interview=schedule:main',
        ]
    }
}

print('Interview Version: %s' % __version__)

packages = setuptools.find_packages()
config['packages'] = packages
setuptools.setup(**config)

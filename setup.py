from setuptools import setup

setup(
    name="init",
    version='0.1',
    py_modules=['init_bot'],
    install_requires=[
        'Click',
        'pyfiglet',
    ],
    entry_points='''
        [console_scripts]
        init=init_bot:cli
    ''',
)

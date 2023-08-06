from setuptools import setup

setup (
    name='tools_hjh',
    version='2.3.2',
    author='HuaJunhao',
    author_email='huajunhao6@yeah.net',
    include_package_data=True,
    install_requires=[
          'dbutils'
        # , 'pillow'
        , 'pymysql'
        , 'cx_Oracle'
        , 'paramiko'
        # , 'zipfile36'
        # , 'crypto'
        , 'requests'
        # , 'selenium'
    ],
    packages=['tools_hjh']
)

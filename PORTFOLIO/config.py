import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')

class DevelopmentConfig:
    # this turns on debug mode in flask
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/portfolio?charset=utf8'.format(**{
                                'user': os.environ.get('MYSQL_USER', 'root'),
                                'password': os.environ.get('MYSQL_PASSWORD', 'root'),
                                'host': os.environ.get('DB_HOST', 'localhost:8889'),
                             })

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig


#### メモ ####
# os.path()...ファイルやディレクトリの存在確認、指定したパスのファイル名の取得、パスやファイル名の結合、などの用途で使用
# join()......パスとファイル名などを結合させることができる
# dirname()...指定されたパスからファイル名を除いたものを返す。
# os.environ()...環境変数を取得したり、書き込み・上書きするときに使われる。環境変数とはシステムが参照している共通の変数のことで、環境に関するデータや共通で使用するファイルパスなどを保持するために使われる。
# https://www.sejuku.net/blog/67787#ospath

# SQLALCHEMY_DATABASE_URIは、DriverにPyMySQLを利用した場合の書き方。
# https://qiita.com/shirakiya/items/0114d51e9c189658002e
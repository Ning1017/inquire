import os
from flask import Flask
from dotenv import find_dotenv,load_dotenv
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from .common_utils import Object2Dict
from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

CONFIG_MAP = Object2Dict().from_object(config['development'])

def create_app(config_name=None):
    global CONFIG_MAP
    # 获取环境变量
    load_dotenv(find_dotenv())
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.config.from_pyfile('config.py', silent=True)

    # # 读取default配置
    # app.config.from_object(config[config_name])
    #
    # # 根据环境变量，读取对应配置，override配置
    # app.config.from_envvar('APP_CONFIG_FILE')
    # config_dict = defaultdict()
    #
    # CONFIG_MAP = app.config
    #
    # for key, value in app.config.items():
    #     config_dict[key] = str(value)
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    # set default configuration of the app
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'data.sqlite'),
    # )
    #
    # if config_name is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(config_name)


    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    from .inquire import inquire as inquire_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/main')
    app.register_blueprint(inquire_blueprint, url_prefix='/inquire')

    return app


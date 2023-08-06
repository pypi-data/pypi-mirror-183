from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

TAG = "SqlAlchemyCommon"


class SqlAlchemyCommon(object):

    @staticmethod
    def get_engine(db_type, db_name, db_user=None, db_password=None, db_host=None, db_port=None):
        """
        获取数据库连接引擎
        :param db_type: 数据库类型
        :param db_name: 数据库名称
        :param db_user: 数据库用户名
        :param db_password: 数据库密码
        :param db_host: 数据库主机
        :param db_port: 数据库端口
        :return: 数据库连接引擎
        """
        if db_type == "mysql":
            engine = create_engine(
                "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(db_user, db_password, db_host, db_port, db_name))
        elif db_type == "oracle":
            engine = create_engine(
                "oracle+cx_oracle://{}:{}@{}:{}/{}".format(db_user, db_password, db_host, db_port, db_name))
        elif db_type == "postgresql":
            engine = create_engine(
                "postgresql+psycopg2://{}:{}@{}:{}/{}".format(db_user, db_password, db_host, db_port, db_name))
        elif db_type == "sqlite":
            engine = create_engine("sqlite:///{}".format(db_name))
        elif db_type == "db2":
            engine = create_engine(
                "db2+ibm_db://{}:{}@{}:{}/{}".format(db_user, db_password, db_host, db_port, db_name))
        else:
            raise Exception("Database type error")
        return engine

    @staticmethod
    def get_session(engine):
        """
        获取数据库会话
        :param engine: 数据库连接引擎
        :return: 数据库会话
        """
        session = sessionmaker(bind=engine)
        session = session()
        return session

    @staticmethod
    def get_tab_fields(db_class, db_type, db_name):
        """
        获取表的所有字段
        :param db_class: 表类，如：class
        :param db_type: 数据库类型
        :param db_name: 数据库名称
        :return: 表的所有字段
        """
        db = db_class()
        engine = SqlAlchemyCommon.get_engine(db_type, db_name)
        session = SqlAlchemyCommon.get_session(engine)
        d = session.query(db).all()
        session.close()
        return d

#!/usr/bin/python3
"""
This class will handle the database storage
"""

from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from os import environ
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Sotre datas into the database
    Attributes:
        __engine (any): private class instance
        __session (any): private class instance
    """
    __engine = None
    __session = None

    def __init__(self):
        """initialization of instaces done in this method
        """
        try:
            db_user = environ.get("HBNB_MYSQL_USER")
            db_pwd = environ.get("HBNB_MYSQL_PWD")
            db_host = environ.get("HBNB_MYSQL_HOST")
            db_name = environ.get("HBNB_MYSQL_DB")
            if db_user and db_pwd and db_host and db_name:
                mysql_url = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
                             db_user, db_pwd, db_host, db_name)
                self.__engine = create_engine(mysql_url, pool_pre_ping=True)
            if environ.get("HBNB_ENV") == "test":
                Base.metadata.reflect(bind=self.__engine)
                Base.metadata.drop_all(bind=self.__engine)
        except Exception as e:
            print("Sorry error occurred ", e)
            pass

    def all(self, cls=None):
        """It will query current database session if cls given otherwise
           It will query all the data

        Attr:
            cls (class): it will accept objects of a class

        Returns:
            dict: all queries returned as dictionary
        """
        try:
            classes = {
                        "STATES": State,
                        "CITIES": City,
                        "USERS": User,
                        "PLACES": Place,
                        "REVIEWS": Review,
                        "AMENITIES": Amenity,
                      }
            all_value = {}
            result = []
            if cls:
                result = self.__session.query(cls).all()
            elif cls is None:
                Base.metadata.reflect(bind=self.__engine)
                for table_name, _ in Base.metadata.tables.items():
                    table_name = table_name.upper()
                    if table_name != "PLACE_AMENITY":
                        result.extend(self.__session.query(
                                      classes[table_name]).all())
            if len(result) > 0:
                for value in result:
                    key = "{}.{}".format(value.__class__.__name__,
                                         value.id)
                    all_value[key] = value
            return all_value
        except Exception as e:
            print("Sorry error occurred ", e)
            return {}

    def new(self, obj):
        """ this method will add any changes to the session

        Attr:
            obj (class): contain the instances of the class
        """
        try:
            if obj is not None:
                self.__session.add(obj)
        except Exception as e:
            print("Sorry error occurred ", e)
            pass

    def save(self):
        """It will commit changes to the current database session
        """
        try:
            self.__session.commit()
        except Exception as e:
            print("Sorry error occurred ", e)
            pass

    def delete(self, obj=None):
        """It will delete the given instance from the database

        Attr:
            obj (class): contain instance of the given class
        """
        try:
            if obj is not None:
                self.__session.delete(obj)
        except Exception as e:
            print("Sorry error occurred ", e)
            pass

    def reload(self):
        """create all tables in database and create session on the
        current database
        """
        try:
            Base.metadata.create_all(bind=self.__engine)
            Session = scoped_session(sessionmaker(bind=self.__engine,
                                     expire_on_commit=False))
            self.__session = Session()
        except Exception as e:
            print("Sorry error occurred ", e)

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User

class DBStorage:
    """
    DBStorage class for interacting with the MySQL database.

    Attributes:
        __engine (Engine): SQLAlchemy engine instance.
        __session (Session): SQLAlchemy session instance.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize the DBStorage instance.
        Creates the engine linked to the MySQL database
        Drops all tables if the environment variable HBNB_ENV is set to 'test'
        """
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{db}',
            pool_pre_ping=True
        )
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query all objects from the current database session

        Args:
            cls (class, optional): Class of objects to query.
            If None, query all types.

        Returns:
            dict: Dictionary of queried objects with keys formatted as
        """
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = self.__session.query(
                State).all() + self.__session.query(City).all()
        return {f'{type(obj).__name__}.{obj.id}': obj for obj in objs}

    def new(self, obj):
        """
        Add the object to the current database session.

        Args:
            obj (BaseModel): Object to add to the session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete obj from the current database session.

        Args:
            obj (BaseModel, optional): Object to delete from the session.
            If None, nothing is deleted.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reload the database:
            - Create all tables in the database.
            - Create the current database session using a scoped session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

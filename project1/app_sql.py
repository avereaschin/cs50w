from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('mysql+mysqlconnector://root:psw@localhost/flight_data')
db = scoped_session(sessionmaker(bind=engine))

users = """
        CREATE TABLE users (id SMALLINT PRIMARY KEY AUTO_INCREMENT, USERNAME VARCHAR(15), PASSWORD VARCHAR(128))
"""

db.execute(users)
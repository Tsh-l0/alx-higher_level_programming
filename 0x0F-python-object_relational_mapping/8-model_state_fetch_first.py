#!/usr/bin/python3
"""
Lists all State objects from the database
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def main():
    """
    Lists all the state objects in the database in ascending order
    """
    u_name = sys.argv[1]
    u_passwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
                           'mysql+mysqldb://{}:{}@localhost/{}'.format(
                            u_name, u_passwd, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state is not None:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    main()

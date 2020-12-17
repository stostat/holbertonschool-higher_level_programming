#!/usr/bin/python3
"""Start link class to table in database"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = Session(bind=engine)

    query = session.query(State).filter(State.name.like('%a%'))

    if query is None:
        print("Nothing")
    else:
        for instance in query:
            print("{}: {}".format(instance.id, instance.name))

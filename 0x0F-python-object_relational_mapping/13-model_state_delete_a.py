#!/usr/bin/python3
"""deletes state with like a"""

if __name__ == "__main__":
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    from model_state import Base
    from model_state import State

    if len(argv) == 4:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        query = session.query(State).filter(State.name.ilike('%a%'))
        query.delete(synchronize_session='fetch')
        session.commit()
    else:
        print("Usage: mysql_username mysql_password database_name")

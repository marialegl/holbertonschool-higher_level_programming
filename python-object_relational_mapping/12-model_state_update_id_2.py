#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the engine and bind it to the session
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the State object with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Update the state name if found
    if state:
        state.name = "New Mexico"
        session.commit()
    else:
        print("State not found")

    # Close the session
    session.close()

#!/usr/bin/python3
"""
Fetches all City objects from the database hbtn_0e_14_usa and prints them grouped by state.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the engine and bind it to the session
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities and their respective states
    cities = session.query(City).order_by(City.id).all()

    # Print results grouped by state
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()

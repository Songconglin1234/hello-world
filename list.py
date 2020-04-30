import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

engine = create_engine('mysql+mysqldb://root:test@localhost:3306/flights')
db = scoped_session(sessionmaker(bind = engine))

def main():
   flights = db.execute("select * from flight").fetchall()
   for flight in flights:
     print(f"{flight.origin} to {flight.destination}, {flight.duration} minuts")

   flight_id = int(input("\n FLIGHT ID "))
   flight = db.execute("select origin,destination ,duration FROM flight WHERE id = :id ",{ "id": flight_id }).fetchone()
   print(f"{flight.origin} to {flight.destination}, {flight.duration} ")
   
   db.commit()

if __name__ == '__main__':
   main()
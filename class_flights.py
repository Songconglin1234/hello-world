import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from flask import Flask ,render_template,request

app = Flask(__name__)
engine = create_engine('mysql+mysqldb://root:test@localhost:3306/flights')
db = scoped_session(sessionmaker(bind = engine))

@app.route("/")
def index():
    flights = db.execute("select * from flights ").fetchall()
    return render_template("flights_index.html", flights = flights)

@app.route("/hello",methods = ["POST","GET"])
def hello():
    name = request.form.get("note")
    print(name)
    return render_template("hello.html",name = name)

@app.route("/book",methods = ["post"])
def book():
    name = request.form.get("name")
    #try: 
    flight_id = int(request.form.get("flight_id"))
    db.execute("select * from flights where id = :id", {"id":flight_id})
    
    print(name)
    print(flight_id)
    db.execute("insert into passengers (name,flight_id ) VALUES (:name,:flight_id)",{"name":name, "flight_id":flight_id})
    db.commit()
    return render_template("result.html")
      
@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/flights")
def flights():
    flights = db.execute("select * from flights").fetchall()
    return render_template("flights.html",flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    flight = db.execute("select * from flights where id = :id", {"id":flight_id})
    if(flight is None):
        return(render_template("error.html", message= "No such flight"))

    passengers = db.execute("select name , flight_id from passengers where flight_id = :flight_id",{"flight_id": flight_id}).fetchall()
    print(passengers)
    return render_template("flight.html", flight = flight, passengers = passengers)
        

if __name__ == '__main__':
   app.run(host = '0.0.0.0', port = 5000)
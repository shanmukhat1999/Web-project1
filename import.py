import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

engine= create_engine(os.getenv("DATABASE_URL"))
db =scoped_session(sessionmaker(bind=engine))

def main():
    db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY,name VARCHAR NOT NULL,age INT NOT NULL,phone VARCHAR NOT NULL, username VARCHAR NOT NULL, password VARCHAR NOT NULL)")
    db.execute("CREATE TABLE books (isbn VARCHAR PRIMARY KEY,title VARCHAR NOT NULL,author VARCHAR NOT NULL,year VARCHAR NOT NULL)")
    db.execute("CREATE TABLE reviews (username VARCHAR NOT NULL,isbn VARCHAR NOT NULL,rating INT NOT NULL,review VARCHAR)")

    f=open("books.csv")
    reader =csv.reader(f)
    for isbn,title,author,year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:a,:b,:c,:d)",{"a":isbn,"b":title,"c":author,"d":year})
    print("done")            
    db.commit()

if __name__ == "__main__":
    main()     
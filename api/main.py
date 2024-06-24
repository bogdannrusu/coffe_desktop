from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
import hashlib
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Removing CORS issues
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as necessary for your environment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ban4ever!#",
        database="coffee_le_coupage",
        port=3305
    )
    return connection


class User( BaseModel ):
    username: str
    password: str
    is_active: bool = True


def hash_password(password: str) -> str:
    return hashlib.sha256( password.encode() ).hexdigest()


@app.post( "/register/" )
def register(user: User):
    connection = get_db_connection()
    cursor = connection.cursor()
    hashed_password = hash_password( user.password )
    try:
        cursor.execute(
            "INSERT INTO Users (username, password, is_active) VALUES (%s, %s, %s)",
            (user.username, hashed_password, user.is_active)
        )
        connection.commit()
    except mysql.connector.IntegrityError as e:
        raise HTTPException( status_code=400, detail=f"Username already exists: {str( e )}" )
    except Exception as e:
        raise HTTPException( status_code=500, detail=f"Server error: {str( e )}" )
    finally:
        connection.close()
    return {"message": "User registered successfully"}


@app.post( "/login/" )
def login(user: User):
    connection = get_db_connection()
    cursor = connection.cursor( dictionary=True )
    cursor.execute( "SELECT * FROM Users WHERE username = %s AND password = %s",
                    (user.username, hash_password( user.password )) )
    result = cursor.fetchone()
    connection.close()
    if result is None:
        raise HTTPException( status_code=401, detail="Invalid username or password" )
    if not result['is_active']:
        raise HTTPException( status_code=403, detail="User account is inactive" )
    return {"message": "Login successful"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run( app, host="127.0.0.1", port=8000 )

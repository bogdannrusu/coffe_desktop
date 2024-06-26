from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
import hashlib
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Removing CORS issues
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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


# Login Model
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


# Order Model
class Order( BaseModel ):
    id: int
    coffee_type: str
    quantity: int
    total_price: float
    user_id: int


@app.post( "/orders/" )
def create_order(order: Order):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO orders (coffee_type, quantity, total_price, user_id) VALUES (%s, %s, %s, %s)",
            (order.coffee_type, order.quantity, order.total_price, order.user_id)
        )
        connection.commit()
        order_id = cursor.lastrowid
    except Exception as e:
        raise HTTPException( status_code=500, detail=f"Server error: {str( e )}" )
    finally:
        connection.close()
    return {"id": order_id, "message": "Order created successfully"}


@app.get( "/orders/" )
def read_orders():
    connection = get_db_connection()
    cursor = connection.cursor( dictionary=True )
    cursor.execute( "CALL get_orders_goods();" )
    orders = cursor.fetchall()
    connection.close()
    return orders


@app.get( "/orders/{order_id}" )
def read_order(order_id: int):
    connection = get_db_connection()
    cursor = connection.cursor( dictionary=True )
    cursor.execute( "SELECT * FROM orders WHERE id = %s", (order_id,) )
    order = cursor.fetchone()
    connection.close()
    if order is None:
        raise HTTPException( status_code=404, detail="Order not found" )
    return order


@app.put( "/orders/{order_id}" )
def update_order(order_id: int, order: Order):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "UPDATE orders SET quantity = %s, price = %s WHERE id = %s",
            (order.quantity, order.price, order_id)
        )
        connection.commit()
    except Exception as e:
        raise HTTPException( status_code=500, detail=f"Server error: {str( e )}" )
    finally:
        connection.close()
    return {"message": "Order updated successfully"}


@app.delete( "/orders/{order_id}" )
def delete_order(order_id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute( "DELETE FROM orders WHERE id = %s", (order_id,) )
        connection.commit()
    except Exception as e:
        raise HTTPException( status_code=500, detail=f"Server error: {str( e )}" )
    finally:
        connection.close()
    return {"message": "Order deleted successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run( app, host="127.0.0.1", port=8000 )

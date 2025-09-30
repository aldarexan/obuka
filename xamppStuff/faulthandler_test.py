import mysql.connector
import faulthandler

# Connecting from the server
faulthandler.enable() #Segmentation fault
  

try:
        mydb = mysql.connector.connect(
            host="localhost",  # e.g., "localhost" or an IP address
            port=3306,
            user="root",
            password="",
            database="example"
        )
        print("Successfully connected to the database!")

        # You can now create a cursor and execute queries
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT * FROM your_table_name")
        results = my_cursor.fetchall()

        for row in results:
            print(row)

except mysql.connector.Error as err:
        print(f"Error: {err}")

finally:
        if 'mydb' in locals() and mydb.is_connected():
            my_cursor.close()
            mydb.close()
            print("Database connection closed.")
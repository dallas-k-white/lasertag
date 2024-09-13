import psycopg2

try:
    conn = psycopg2.connect(
        dbname = "photon",
        user = "student",
        password = "student",
        port = "5432"
    )
    
    cursor = conn.cursor()

    cursor.execute("SELECT * from players;")

    record = cursor.fetchone()
    print(record)
    print("Trying.....")
except Exception as error:
    print("Error connecting to Database:", error)

finally:
    if conn:
        conn.close()
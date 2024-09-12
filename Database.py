import psycopg2

try:
    conn = psycopg2.connect(
        dbname = "photon",
        user = "student",
        password = "student",
        host = "",
        port = "5432"
    )
except Exception as error:
    print("Error connecting to Database:", error)

finally:
    if conn:
        conn.close()
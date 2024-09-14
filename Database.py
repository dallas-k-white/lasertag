import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname = "photon",
            user = "student",
            password = "student",
            port = "5432"
        )
        return conn
    except Exception as error:
        print("Error connecting to Database:", error)


def add_player(name: str):
    conn = connect_db()
    try:
        cursor = conn.cursor()

        playerID = get_id_increment()
        cursor.execute("""
        INSERT INTO players (id, codename) values (%s, %s);
        """,
        (playerID, name))

        print("Player " + name + "successfully added")

        conn.commit()
        conn.close()
        cursor.close()

    except Exception as error:
        print("Error:", error)


def delete_player(name: str):
    conn = connect_db()
    try:
        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM players WHERE codename=%s;
        """
        (name,))

        print("Player " + name + " has been deleted")

        conn.commit()
        conn.close()
        cursor.close()

    except Exception as error:
        print("Error:", error)


def get_players():
    conn = connect_db()
    try:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM players;
        """)
        players = cursor.fetchall()
        for p in players:
            print("ID: " + str(p[0]), ", Name: " + str(p[1]))
        
        cursor.close()
        conn.close()

    except Exception as error:
        print("Error:", error)


def get_id_increment() -> int:
    conn = connect_db()
    try:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT id FROM players ORDER BY id DESC LIMIT 1;
        """)
        entry = cursor.fetchone()

        cursor.close()
        conn.close()

        lastID = entry[0]
        lastID += 1
        return lastID

    except Exception as error:
        print("Error:", error)


add_player("Bob")
add_player("Joe")
get_players()
delete_player("Bob")
delete_player("Joe")
get_players()
add_player("Phil")
add_player("Jeff")
get_players

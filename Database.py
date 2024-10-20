import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname = "photon",
            port = "5432"
        )
        return conn
    except Exception as error:
        print("Error connecting to Database:", error)


def find_player(id: int) -> str:
    conn = connect_db()
    try:    
        cursor = conn.cursor()
        player_id = str(id)
        cursor.execute("""
        SELECT codename FROM players WHERE id = %s;
        """,
        (player_id,))
        player = cursor.fetchall()
        if not player:
            conn.close()
            cursor.close()
            return None
        print(player[0][0])
        conn.close()
        cursor.close()
        return str(player[0][0])
    except Exception as error:
        print("Error connecting to Database from find:", error)


def add_player(name: str, id: int):
    conn = connect_db()
    try:
        cursor = conn.cursor()

        #playerID = get_id_increment()
        playerID = id
        cursor.execute("""
        INSERT INTO players (id, codename) values (%s, %s);
        """,
        (playerID, name))

        print("Player " + name + " successfully added")

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
        DELETE FROM players WHERE codename= %s;
        """,
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


def clear_table():
    conn = connect_db()
    try:
        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM players;
        """)
        conn.commit()
        conn.close()
        cursor.close()
    except Exception as error:
        print("Error connecting to Database:", error)

# clear_table()
# add_player("Bob", 1)
# add_player("Joe", 20)
# get_players()
# delete_player("Bob")
# delete_player("Joe")
# get_players()
# add_player("Phil", 99)
# add_player("Jeff", 5)
# get_players()

# delete_player("Heidi")
# name = find_player(99)
# if name is None:
#     print("id Not found adding player: ", name)
#     add_player("Heidi", 99)
# else:
#     print("Player already exists with that ID, Name: ", name)
# name2 = find_player(20)
# if name2 is None:
#     print("id Not found adding player: Harold")
#     add_player("Harold", 20)
# else: 
#     print("Player already exists with that ID, Name: ", nado me2)

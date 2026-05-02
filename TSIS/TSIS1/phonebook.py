from connect import connect
import json

def insert_contact():
    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO contacts(username, email, birthday)
        VALUES (%s, %s, %s)
        ON CONFLICT (username)
        DO UPDATE SET email = EXCLUDED.email, birthday = EXCLUDED.birthday
    """, (name, email, birthday))

    conn.commit()
    cur.close()
    conn.close()

    print("Saved!")


def add_phone():
    name = input("Name: ")
    phone = input("Phone: ")
    type_ = input("Type (home/work/mobile): ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL add_phone(%s,%s,%s)", (name, phone, type_))

    conn.commit()
    cur.close()
    conn.close()


def move_group():
    name = input("Name: ")
    group = input("Group: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL move_to_group(%s,%s)", (name, group))

    conn.commit()
    cur.close()
    conn.close()


def search():
    pattern = input("Search: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()

    if not rows:
        print("No results")
    else:
        for row in rows:
            print(row)

    conn.close()


def export_json():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.username, c.email, c.birthday, g.name, p.phone
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
    """)

    data = cur.fetchall()

    with open("contacts.json", "w") as f:
        json.dump(data, f, indent=4, default=str)

    print("Exported!")

    cur.close()
    conn.close()


def menu():
    while True:
        print("""
1 - Insert/Update
2 - Add phone
3 - Move to group
4 - Search
5 - Export JSON
0 - Exit
""")

        ch = input("Choose: ")

        if ch == "1":
            insert_contact()
        elif ch == "2":
            add_phone()
        elif ch == "3":
            move_group()
        elif ch == "4":
            search()
        elif ch == "5":
            export_json()
        elif ch == "0":
            break


menu()
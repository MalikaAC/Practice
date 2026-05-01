import psycopg2
from connect import connect

conn = connect()
cur = conn.cursor()

# =========================
# INSERT OR UPDATE (CALL procedure)
# =========================
def upsert():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    print("Inserted or updated!")


# =========================
# SEARCH (FUNCTION)
# =========================
def search():
    pattern = input("Enter search text: ")

    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()

    for r in rows:
        print(r)


# =========================
# PAGINATION
# =========================
def paginate():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    cur.execute("SELECT * FROM get_contacts_page(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    for r in rows:
        print(r)


# =========================
# INSERT MANY
# =========================
def insert_many():
    names = input("Names (comma): ").split(",")
    phones = input("Phones (comma): ").split(",")

    cur.execute("CALL insert_many(%s, %s)", (names, phones))
    conn.commit()
    print("Batch insert done!")


# =========================
# DELETE
# =========================
def delete():
    value = input("Enter name or phone: ")

    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()
    print("Deleted!")


# =========================
# MENU
# =========================
def menu():
    while True:
        print("""
1 - Insert/Update
2 - Search
3 - Pagination
4 - Insert many
5 - Delete
0 - Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            upsert()
        elif choice == "2":
            search()
        elif choice == "3":
            paginate()
        elif choice == "4":
            insert_many()
        elif choice == "5":
            delete()
        elif choice == "0":
            break
        else:
            print("Invalid choice")


menu()

cur.close()
conn.close()
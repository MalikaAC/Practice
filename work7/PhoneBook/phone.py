import psycopg2
import csv
#1. Design table(s) for the PhoneBook
conn = psycopg2.connect(
    dbname = "postgres",
    user="postgres",
    password="26082008",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

#2. Implement inserting data from a CSV file
def insert_from_console():
    username = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute(
        "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
        (username, phone)
    )
    conn.commit()
    print("Contact added!")

#3. Implement inserting data entered from the console (user name, phone)
def insert_from_csv():
    filename = input("Enter CSV file name: ")

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    print("CSV data inserted!")

#4. Implement updating a contact's first name or phone number
def update_contact():
    username = input("Enter username to update: ")
    new_name = input("New name (press Enter to skip): ")
    new_phone = input("New phone (press Enter to skip): ")

    if new_name:
        cur.execute(
            "UPDATE phonebook SET username=%s WHERE username=%s",
            (new_name, username)
        )

    if new_phone:
        cur.execute(
            "UPDATE phonebook SET phone=%s WHERE username=%s",
            (new_phone, username)
        )

    conn.commit()
    print("Updated!")

#5. Implement querying contacts with different filters (e.g. by name, by phone prefix)
def search_contacts():
    print("1 - Search by name")
    print("2 - Search by phone prefix")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE username ILIKE %s",
            ('%' + name + '%',)
        )

    elif choice == "2":
        prefix = input("Enter prefix: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE phone LIKE %s",
            (prefix + '%',)
        )

    results = cur.fetchall()

    for row in results:
        print(row)
    
#6. Implement deleting a contact by username or phone number
def delete_contact():
    print("1 - Delete by username")
    print("2 - Delete by phone")

    choice = input("Choose: ")

    if choice == "1":
        username = input("Enter username: ")
        cur.execute(
            "DELETE FROM phonebook WHERE username=%s",
            (username,)
        )

    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute(
            "DELETE FROM phonebook WHERE phone=%s",
            (phone,)
        )

    conn.commit()
    print("Deleted!")


def menu():
    while True:
        print("""
1 - Insert from console
2 - Insert from CSV
3 - Update contact
4 - Search contacts
5 - Delete contact
0 - Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_console()

        elif choice == "2":
            insert_from_csv()

        elif choice == "3":
            update_contact()

        elif choice == "4":
            search_contacts()

        elif choice == "5":
            delete_contact()

        elif choice == "0":
            break

        else:
            print("Invalid choice!")


menu()

cur.close()
conn.close()
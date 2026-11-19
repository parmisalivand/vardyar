
import sqlite3

DATABASE_NAME = "vardyar.db"


def connect_db():
    return sqlite3.connect(DATABASE_NAME)


def create_table():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS missing_persons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            age INTEGER,
            last_seen_location TEXT,
            missing_date TEXT,
            description TEXT
        )
    """)

    connection.commit()
    connection.close()


def add_missing_person(full_name, age, last_seen_location, missing_date, description):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO missing_persons
        (full_name, age, last_seen_location, missing_date, description)
        VALUES (?, ?, ?, ?, ?)
    """, (full_name, age, last_seen_location, missing_date, description))

    connection.commit()
    connection.close()

    print("Report added successfully!")


def get_all_missing_persons():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM missing_persons")

    persons = cursor.fetchall()

    connection.close()

    return persons

def get_missing_person_by_id(person_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM missing_persons
        WHERE id = ?
    """, (person_id,))

    person = cursor.fetchone()

    connection.close()

    return person


def update_missing_person(person_id, full_name, age, last_seen_location, missing_date, description):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE missing_persons
        SET full_name = ?,
            age = ?,
            last_seen_location = ?,
            missing_date = ?,
            description = ?
        WHERE id = ?
    """, (full_name, age, last_seen_location, missing_date, description, person_id))

    connection.commit()
    updated = cursor.rowcount

    connection.close()

    return updated > 0


def delete_missing_person(person_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM missing_persons
        WHERE id = ?
    """, (person_id,))

    connection.commit()
    deleted = cursor.rowcount

    connection.close()

    return deleted > 0


if __name__ == "__main__":
    create_table()
    print("Vardyar is ready!")

    persons = get_all_missing_persons()

    for person in persons:
        print(person)
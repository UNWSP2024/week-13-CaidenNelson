import sqlite3
connection = sqlite3.connect('PhoneBook.db')
cursor = connection.cursor()
PhoneBook = ['']
cursor.execute('create table PhoneBook ( integer, PhoneNum integer, Name text)')

MIN_CHOICE = 1
MAX_CHOICE = 5
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
EXIT = 5

def main():
     choice = 0
     while choice != EXIT:
          display_menu()
          choice = get_menu_choice()

          if choice == CREATE:
              create()
          elif choice == READ:
              read()
          elif choice == UPDATE:
              update()
          elif choice == DELETE:
              delete()
def display_menu():
      print('\n----- Phonebook Menu -----')
      print('1. Add a new Phone Number')
      print('2. Read an item')
      print('3. Update an Phone Number')
      print('4. Delete an Phone Number')
      print('5. Exit the program')

def get_menu_choice():

      choice = int(input('Enter your choice: '))

      while choice < MIN_CHOICE or choice > MAX_CHOICE:
          print(f'Valid choices are {MIN_CHOICE} through {MAX_CHOICE}.')
          choice = int(input('Enter your choice: '))
      return choice
def create():
     print('Add a new Phone number')
     phone_Number = input('Phone Number: ')
     name = input('Persons name: ')
     insert_row(phone_Number, name)

def read():
    phone = input('Enter a Phone Number to search for: ')
    num_found = display_item(phone)
    print(f'{num_found} row(s) found.')

def update():
    read()

    phone = input('Enter the new Phone Number: ')
    name = input('Enter the new name: ')
    phone_updated = update_row(phone, name)
    print(f'{phone_updated} row(s) updated.')

def delete():
    read()
    phone = (input('Select a phone number to delete: '))
    sure = input('Are you sure you want to delete this Phone Number? (y/n): ')
    if sure.lower() == 'y':
        num_deleted = delete_row(phone)
        print(f'{num_deleted} row(s) deleted.')

def insert_row(phone, name):
    conn = None
    try:
        conn = sqlite3.connect('PhoneBook.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO PhoneBook (PhoneNum, Name)
                      VALUES (?, ?)''',(phone, name))
        conn.commit()
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()

def display_item(phone):
    conn = None
    results = []
    try:
        conn = sqlite3.connect('PhoneBook.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM PhoneBook WHERE lower(PhoneNum) == ?''', (phone))
        results = cur.fetchall()
        for row in results:
            print(f'PhoneNum: {row[1]}' f'Name: {row[2]}')
    except sqlite3.Error as err:
            print('Database Error', err)
    finally:
            if conn != None:
                conn.close()
    return len(results)
def update_row(phone, name):
    conn = None
    try:
        conn = sqlite3.connect('PhoneBook.db')
        cur = conn.cursor()
        cur.execute('''UPDATE PhoneBook SET PhoneNum = ? WHERE Name == ?''',
                    (phone, name))
        conn.commit()
        num_updated = cur.rowcount
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()
    return num_updated
def delete_row(phone):
    conn = None
    try:
        conn = sqlite3.connect('PhoneBook.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM PhoneBook WHERE Name == ?''', phone)
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()
    return num_deleted

if __name__ == '__main__':
    main()

#Programmer = Caiden Nelson
#Date = 2.5.24
#Title = Cities

import sqlite3
connection = sqlite3.connect('cities.db')

cursor = connection.cursor()
cursor.execute('create table cities (CityID integer, CityName text, Population real)')

cities = [(1,"New York", "8258035"),
          (2,"los Angelos", "3820914"),
             (3,"Chicago", "2664452"),
            (4,"Houston", "2314157"),
             (5,"Phoenix", "1650070"),
          (6,"Philadelphia", "1550542"),
          (7,"San Antonio", "1495295"),
          (8,"San Diego", "1388320"),
          (9,"Dallas", "1302868"),
          (10,"Jacksonville","985843"),
          (11,"Austin","979882"),
          (12,"Fort Worth","978882"),
          (13,"San Jose","969655"),
          (14,"Columbus","913175"),
          (15,"Charlotte","911311"),
          (16,"Indianapolis","879293"),
          (17,"San Francisco","808988"),
          (18,"Seattle","755078"),
          (19,"Denver","716577"),
          (20,"Oklahoma City","702767")]
cursor.executemany('insert into cities values (?,?,?)', cities)


for row in cursor.execute("select * from cities"):
    print(row)
connection.close()

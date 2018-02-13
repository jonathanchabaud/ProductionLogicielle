import csv
import sqlite3

connection = sqlite3.connect("../data/dataBase.db")
cursor = connection.cursor()

# def csv2sql(file) :
with open('../data/equipements_activites.csv', 'r') as f:
    reader = csv.reader(f)
    columns = next(reader)

    try:
        cursor.execute('drop table equipements_activites')
    except sqlite3.OperationalError:
        print('Table non-existant: skipping drop')


cursor.execute("CREATE TABLE EQUIPEMENTS ("+head+");")
cursor.execute("SELECT * FROM EQUIPEMENTS")
print(cursor.fetchone())



# with open('data/equipements_activites.csv') as csvfile:
#     equip_actDict = csv.DictReader(csvfile, delimiter=",")
#
# with open('data/installations.csv') as csvfile:
#     installDict = csv.DictReader(csvfile, delimiter=",")
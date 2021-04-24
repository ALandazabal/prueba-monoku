# import Python's built-in JSON library
import csv, sys

# import the psycopg2 database adapter for PostgreSQL
import psycopg2
import config as conf

def readData(conn):
    with open('datos.csv', mode='r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for record in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(record)}')
                line_count += 1

            else:
                #create a cursor
                cur = conn.cursor()

                #print("record->",record)

                #print("record_list->",record['fields'])
                #r_fields = record['fields']

                valueBand = str(record[4])

                if valueBand:

                    try:
                        query = f"SELECT id FROM myapi_band WHERE name='{valueBand}'"
                        print("Query->",query)
                        valueCur = cur.execute(query)

                        print('valueCur->'+valueCur)

                        if not valueCur:
                            query = 'INSERT INTO myapi_band(name) VALUES("'+record[4]+'")'

                            print("Query->",query)
                            cur.execute(query)
                            conn.commit()
                    except (Exception, psycopg2.DatabaseError) as error:
                        print(error)


def connectDB():

	conn = None
	try:
		print('Connecting to the PostgreSQL database...')
		conn = psycopg2.connect(host=conf.host,database=conf.database, user=conf.user, password=conf.password, port=conf.port)

		
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	return conn

def closeDB(conn):
	conn.close()
	print('Database connection closed.')


if __name__ == '__main__':
    conn = connectDB()

    if conn is not None:
        print('Connection success!')

        readData(conn)
        
        closeDB(conn)
    else:
        print('Connection failed!')
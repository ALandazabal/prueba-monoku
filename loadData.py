# import Python's built-in JSON library
import csv, sys

# import the psycopg2 database adapter for PostgreSQL
import psycopg2
import config as conf

def readDataCSV(conn):
    with open('prueba_back_monoku_2021_datos.csv', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            #create a cursor
            cur = conn.cursor()
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
            else:
                if row[0]:
                    try:
                        # Query to insert bands
                        query = f"SELECT * FROM myapi_band WHERE name LIKE '%{row[4]}%'"
                        #print(query)
                        cur.execute(query)
                        valuesBand = cur.fetchone()

                        #print(valuesBand[0])


                        if valuesBand is None:
                            query = f"INSERT INTO myapi_band(name) VALUES('{row[4]}')"

                            #print("Query->",query)
                            cur.execute(query)
                            conn.commit()

                            valuesBand = cur.fetchone()

                        # Query to insert Artist
                        query = f"SELECT * FROM myapi_artist WHERE name LIKE '%{row[5]}%'"
                        #print(query)
                        cur.execute(query)
                        valuesArtist = cur.fetchone()

                        #print(valuesArtist)

                        if valuesArtist is None:
                            query = f"INSERT INTO myapi_artist(name, band_id) VALUES('{row[5]}',{valuesBand[0]})"

                            #print("Query->",query)
                            cur.execute(query)
                            conn.commit()

                            valuesArtist = cur.fetchone()

                        # Query to insert Album
                        query = f"SELECT * FROM myapi_album WHERE title LIKE '%{row[3]}%'"
                        #print(query)
                        cur.execute(query)
                        valuesAlbum = cur.fetchone()

                        #print(valuesAlbum)


                        if valuesAlbum is None:
                            query = f"INSERT INTO myapi_album(title, artist_id) VALUES('{row[3]}',{valuesArtist[0]})"

                            #print("Query->",query)
                            cur.execute(query)
                            conn.commit()

                            valuesAlbum = cur.fetchone()

                        # Query to insert Genre
                        query = f"SELECT * FROM myapi_genre WHERE description LIKE '%{row[7]}%'"
                        #print(query)
                        cur.execute(query)
                        valuesGenre = cur.fetchone()

                        #print(valuesGenre)


                        if valuesGenre is None:
                            query = f"INSERT INTO myapi_genre(description) VALUES('{row[7]}')"

                            #print("Query->",query)
                            cur.execute(query)
                            conn.commit()

                            valuesGenre = cur.fetchone()


                        # Query to insert Subgenre
                        query = f"SELECT * FROM myapi_subgenre WHERE description LIKE '%{row[8]}%'"
                        #print(query)
                        cur.execute(query)
                        valuesSubgenre = cur.fetchone()

                        #print(valuesSubgenre)


                        if valuesSubgenre is None:
                            query = f"INSERT INTO myapi_subgenre(description, genre_id) VALUES('{row[8]}',{valuesGenre[0]})"

                            #print("Query->",query)
                            cur.execute(query)
                            conn.commit()

                            valuesSubgenre = cur.fetchone()

                        # Query to insert Tags
                        #print(f"Tags->{row[10]}")
                        tags = row[10].split('; ')

                        for tag in tags:
                            query = f"SELECT * FROM myapi_tag WHERE description LIKE '%{tag}%'"
                            #print(query)
                            cur.execute(query)
                            valuesTag = cur.fetchone()

                            #print(valuesTag)


                            if valuesTag is None:
                                query = f"INSERT INTO myapi_tag(description) VALUES('{tag}')"

                                #print("Query->",query)
                                cur.execute(query)
                                conn.commit()


                        # Query to insert Instruments
                        #print(f"Instruments->{row[11]}")
                        instruments = row[11].split('; ')

                        for instrument in instruments:
                            query = f"SELECT * FROM myapi_instrument WHERE description LIKE '%{instrument}%'"
                            #print(query)
                            cur.execute(query)
                            valuesInstrument = cur.fetchone()

                            #print(valuesInstrument)


                            if valuesInstrument is None:
                                query = f"INSERT INTO myapi_instrument(description) VALUES('{instrument}')"

                                #print("Query->",query)
                                cur.execute(query)
                                conn.commit()

                        
                        # Query to insert Bands
                        #print(f"Bands->{row[9]}")
                        bands = row[9].split('; ')

                        for band in bands:
                            query = f"SELECT * FROM myapi_band WHERE name LIKE '%{band}%'"
                            #print(query)
                            cur.execute(query)
                            valuesBand = cur.fetchone()

                            #print(valuesBand)


                            if valuesBand is None:
                                query = f"INSERT INTO myapi_band(name) VALUES('{band}')"

                                #print("Query->",query)
                                cur.execute(query)
                                conn.commit()


                        # Query to insert Songs
                        query = f"SELECT * FROM myapi_song WHERE external_id = {row[1]}"
                        #print(query)
                        cur.execute(query)
                        valuesSong = cur.fetchone()

                        #print(valuesSong)

                        if valuesSong is None:
                            query = f"INSERT INTO myapi_song(title,duration,date,album_id,external_id) VALUES('{row[2]}','{row[6]}','{row[0]}',{valuesAlbum[0]},{row[1]})"

                            #print("Query->",query)
                            cur.execute(query)
                            conn.commit()

                            valuesSong = cur.fetchone()


                        # Query to insert Songs-subgenre
                        query = f"SELECT * FROM myapi_song_subgenres WHERE song_id = {valuesSong[0]} AND subgenre_id = {valuesSubgenre[0]}"
                        #print(query)
                        cur.execute(query)
                        valuesSongSubg = cur.fetchone()

                        #print(valuesSongSubg)

                        if valuesSongSubg is None:
                            query = f"INSERT INTO myapi_song_subgenres(song_id,subgenre_id) VALUES({valuesSong[0]},{valuesSubgenre[0]})"

                            #print("Query->",query)
                            cur.execute(query)
                            conn.commit()


                        # Query to insert Songs-bands
                        #print(f"Bands->{row[9]}")
                        bands = row[9].split('; ')

                        for band in bands:
                            query = f"SELECT * FROM myapi_band WHERE name LIKE '%{band}%'"
                            #print(query)
                            cur.execute(query)
                            valuesBand = cur.fetchone()

                            #print(valuesBand)

                            query = f"SELECT * FROM myapi_song_bands WHERE song_id = {valuesSong[0]} AND band_id = {valuesBand[0]}"
                            #print(query)
                            cur.execute(query)
                            valuesSongBands = cur.fetchone()

                            #print(valuesSongBands)

                            if valuesSongBands is None:
                                query = f"INSERT INTO myapi_song_bands(song_id,band_id) VALUES({valuesSong[0]},{valuesBand[0]})"

                                #print("Query->",query)
                                cur.execute(query)
                                conn.commit()

                        # Query to insert Songs-instruments
                        #print(f"Instruments->{row[11]}")
                        instruments = row[11].split('; ')

                        for instrument in instruments:
                            query = f"SELECT * FROM myapi_instrument WHERE description LIKE '%{instrument}%'"
                            #print(query)
                            cur.execute(query)
                            valuesInstrument = cur.fetchone()

                            #print(valuesInstrument)

                            query = f"SELECT * FROM myapi_song_instruments WHERE song_id = {valuesSong[0]} AND instrument_id = {valuesInstrument[0]}"
                            #print(query)
                            cur.execute(query)
                            valuesSongInstrument = cur.fetchone()

                            #print(valuesSongInstrument)

                            if valuesSongInstrument is None:
                                query = f"INSERT INTO myapi_song_instruments(song_id,instrument_id) VALUES({valuesSong[0]},{valuesInstrument[0]})"

                                #print("Query->",query)
                                cur.execute(query)
                                conn.commit()

                        # Query to insert Songs-tags
                        #print(f"Tags->{row[10]}")
                        tags = row[10].split('; ')

                        for tag in tags:
                            query = f"SELECT * FROM myapi_tag WHERE description LIKE '%{tag}%'"
                            #print(query)
                            cur.execute(query)
                            valuesTag = cur.fetchone()

                            #print(valuesTag)

                            query = f"SELECT * FROM myapi_song_tags WHERE song_id = {valuesSong[0]} AND tag_id = {valuesTag[0]}"
                            #print(query)
                            cur.execute(query)
                            valuesSongTag = cur.fetchone()

                            #print(valuesSongTag)

                            if valuesSongTag is None:
                                query = f"INSERT INTO myapi_song_tags(song_id,tag_id) VALUES({valuesSong[0]},{valuesTag[0]})"

                                #print("Query->",query)
                                cur.execute(query)
                                conn.commit()


                    except (Exception, psycopg2.DatabaseError) as error:
                        print(error)

            line_count += 1

        print(f'Processed {line_count} lines.')

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

        readDataCSV(conn)
        
        closeDB(conn)
    else:
        print('Connection failed!')
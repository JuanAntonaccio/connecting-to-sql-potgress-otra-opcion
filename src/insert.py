import psycopg2

conn = psycopg2.connect(database="d4gkb7j795avqi",
                        user="ipfmrqtpvkmdfl",
                        password="e2d6ea424e7fa6967f2206535a9fc0e82e1d26b813b18f52d765763c75b70ccd",
                        host="ec2-52-71-23-11.compute-1.amazonaws.com",
                        port="5432")

cursor = conn.cursor()
cursor.execute("INSERT INTO Peliculas (id,name) VALUES(1,'Casablanca'),(2,'Matrix'),(3,'Terminator');")

conn.commit()

conn.close()
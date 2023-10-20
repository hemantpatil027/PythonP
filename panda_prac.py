import sqlite3

import pandas as pd

 

sqliteConnection = sqlite3.connect('sql.db')

cursor = sqliteConnection.cursor()

# print(sqliteConnection)

# print(cursor)

 

# Define the SQL command to create the table if not exists

create_table_query = '''

    CREATE TABLE IF NOT EXISTS po_details (

        id INTEGER PRIMARY KEY,

        po_num TEXT,

        wh_num TEXT,

        asn_num TEXT,

        asn_date TEXT,

        ean_list TEXT    

    );

'''
insert_query = '''

    INSERT INTO po_details (po_num, wh_num, asn_num, asn_date, ean_list)

    VALUES ('PO124', 'WH457', 'ASN7810', '2023-10-03', '132123123123,5675756756,2314124124'),
     ('PO124', 'WH457', 'ASN7811', '2023-10-03', '12312312312,45745745'),
     ('PO126', 'WH457', 'ASN7812', '2023-10-03', '2423413234,1423512515'),
     ('PO127', 'WH457', 'ASN7813', '2023-10-03', '34131234125,2153145353,15434534153'),
     ('PO127', 'WH457', 'ASN7817', '2023-10-03', '34131234125,2153145353,12312312313'),
     ('PO128', 'WH457', 'ASN7819', '2023-10-03', '34131234125,3564563463,12312312313')

'''





cursor.execute(insert_query)

 

# Execute the SQL command

#cursor.execute(create_table_query)
sqliteConnection.commit()
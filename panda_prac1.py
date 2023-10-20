import sqlite3

# Take input from the user for the PO number to search
po_number_to_search = input("Enter PO number to fetch data: ")
asn_number_to_search = input("Enter ASN number to fetch data: ")

# Create or connect to the database
conn = sqlite3.connect('sql.db')
cursor = conn.cursor()

# Execute the SELECT query to retrieve data based on the provided po_num
select_query = '''
    SELECT * FROM po_details
    WHERE po_num = ? AND asn_num = ?;
'''

# Execute the query and fetch the results
cursor.execute(select_query, (po_number_to_search,asn_number_to_search))
result = cursor.fetchall()

# Display the results
if result:
    for row in result:
        print(row)
else:
    print("No data found for the provided PO number.")

# Close the connection
conn.close()

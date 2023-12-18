#!/usr/local/bin/python3
import cgi
import json
import mysql.connector

def main():
    form = cgi.FieldStorage()
    term = form.getvalue( 'plasmidSearch' )
    #term = "NZ"

    conn = mysql.connector.connect(user='kjosep25', password='password', host='localhost', database='kjosep25_final')
    cursor = conn.cursor()
    qry = "SELECT OrgID FROM plasmid_seqs WHERE OrgID LIKE %s LIMIT 5;"
    cursor.execute(qry, ('%' + str(term) + '%',))
    results = [row[0] for row in cursor.fetchall()]

    # Set the content type to JSON
    print("Content-Type: application/json\n")

    # Return the JSON-encoded plasmids
    print(json.dumps(results))

if __name__ == '__main__':
    main()
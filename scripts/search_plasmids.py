#!/usr/local/bin/python3
import mysql.connector


def retrieve_plasmid(term):
    conn = mysql.connector.connect(user='kjosep25', password='password', host='localhost', database='kjosep25_final')
    cursor = conn.cursor()
    qry = "SELECT Sequence FROM plasmid_seqs WHERE OrgId=%s;"
    try:
        cursor.execute(qry, (str(term),))
    except:
        return None
    sequence = cursor.fetchone()
    conn.close()
    return sequence


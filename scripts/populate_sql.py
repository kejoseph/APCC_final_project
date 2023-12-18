#!/usr/local/bin/python3

import os
import mysql.connector


def insert_data(fasta_file):
    # Connect to the database
    conn = mysql.connector.connect(user='kjosep25', password='password', host='localhost', database='kjosep25_final')
    cursor = conn.cursor()
    qry = "INSERT INTO `plasmid_seqs` (`OrgID`, `Sequence`) VALUES (%s, %s)"

    # Read the FASTA file and insert data into the database
    with open(fasta_file, "r") as file:
        current_org_id = None
        current_sequence_data = ""

        for line in file:
            if line.startswith(">"):  # New sequence
                if current_org_id is not None:
                    # Insert the previous sequence into the database
                    print("Current Sequence ID:", current_org_id)
                    print("Current Sequence Data:", len(current_sequence))
                    cursor.execute(qry, (current_org_id, current_sequence))

                # Extract sequence ID from the header
                current_org_id = line[1:].strip()
                current_sequence = ""
            else:
                current_sequence += line.strip()

        # Insert the last sequence into the database
        cursor.execute(qry, (current_org_id, current_sequence))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    insert_data("../All_plasmids.fna")
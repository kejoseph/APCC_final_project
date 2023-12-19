#!/usr/local/bin/python3
import cgi
import json
import search_plasmids, sequence_tools
import sys


def main():
    form = cgi.FieldStorage()
    insert_seq = form.getvalue('gene_sequence')
    #insert_seq = insert_seq.upper()
    term = form.getvalue('plasmid_entry')
    # Here we will grab plasmid term and sequence will entries
    #term = "NZ_CP007042.1"
    #plasmid_auto = fetch_all_plasmids(term)
    #insert_seq = "ATGATAGATAGTATATAGTCTCGCTACGTGCTATCTGCTATGCTGCTCTCGTCGTCTCTCTCTTCAATATTTTATAATATGCTCGTCGCTATCGTAGCT"

    # Grabbing the plasmid sequence from database
    plasmid_seq = search_plasmids.retrieve_plasmid(term)
    if plasmid_seq:
        plasmid_seq = str(plasmid_seq[0])
        # If plasmid sequence found, run the workflow and return restriction site options to the template
        enzymes = sequence_tools.find_plasmid_sites(plasmid_seq)
        enzymes_good = sequence_tools.find_gene_sites(insert_seq, enzymes)
        print("Content-Type: application/json\n\n")
        print(json.dumps(enzymes_good))
    else:
        print(json.dumps({"error": "No plasmid sequence found"}))
        print("No plasmid sequence found for current selection")
    #now we return the final sequence with primers to the template and we are done
    return

if __name__ == '__main__':
    main()

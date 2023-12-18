#!/usr/local/bin/python3
import json
import cgi
import search_plasmids, sequence_tools, design_primers

def main():
    form = cgi.FieldStorage()
    insert_seq = form.getvalue('gene_sequence')
    insert_seq = insert_seq.upper()
    plasmid = form.getvalue('plasmid_entry')
    enzyme_chosen = form.getvalue('selectedEnzyme')  # Get the selected enzyme
    #plasmid = "NZ_CP007042.1"
    #insert_seq = "ATGATAGATAGTATATAGTCTCGCTACGTGCTATCTGCTATGCTGCTCTCGTCGTCTCTCTCTTCAATATTTTATAATATGCTCGTCGCTATCGTAGCT"
    #enzyme_chosen = 'PsiI'
    plasmid_seq = search_plasmids.retrieve_plasmid(plasmid)
    if plasmid_seq:
        plasmid_seq = str(plasmid_seq[0])
        
        # If plasmid sequence found, run the workflow and return restriction site options to the template
        enzymes = sequence_tools.find_plasmid_sites(plasmid_seq) 
    # once restriction enzyme is picked, pull the enzyme position from the dictionary
    enzymes = {str(i): int(site[0]) for i, site in enzymes.items()}
    enzyme_pos = enzymes[enzyme_chosen]
    full_seq = sequence_tools.insert_sequence(plasmid_seq, insert_seq, enzyme_pos)
    overlap = 20

    primers = design_primers.design_gibson_primers(full_seq, enzyme_pos, insert_seq, overlap)

    # After generating the primers and full_seq
    print("Content-Type: application/json\n\n")
    print(json.dumps({'full_seq': full_seq, 'primers': primers}))
    #now we return the final sequence with primers to the template and we are done


if __name__ == '__main__':
    main()

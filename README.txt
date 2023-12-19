# Gibson Cloning Design Tool Tutorial


This tool is designed to facilitate the selection of plasmids, creation of sequences, design of primers for Gibson Assembly cloning. It takes a desired sequence to be inserted into a plasmid/vector, allows user to select the plasmid an insert sequence, and returns the forward and reverse primers for the Gibson Assembly.

Source code can be obtained here: https://github.com/kejoseph/APCC_final_project
If on the JHU BIX server, tool can be run through: http://bfx3.aap.jhu.edu/kjosep25/final/main.html


Utilizes data from Sistrom, Mark (2018). Plasmids database [Dataset]. Dryad. https://doi.org/10.15146/R33X2J
- Also available in the All_plasmids.fna file.

Utilizes tools:
- Biopython - https://biopython.org (Used for restriction enzyme database and sequence parsing and manipulation)

## Usage
To use the Gibson Cloning Design Tool, follow these steps:

1. Enter the gene insert sequence and select a plasmid/vector in the provided form fields, the form will return potential restriction enzymes, if nothing is returned in the dropdown, then no enzymes are available for given input.
2. Click the "Submit" button to initiate the primer design process.
3. Once the primers are designed, the forward and reverse primer sequences will be displayed in the designated sections.
4. You can then copy the final sequence to the clipboard or export it to a TXT file using the provided buttons.

NOTE: The above usage is intended to be used on the JHU BIX server. To use locally or on another server with a SQL database one must take these steps.
1. Downloaded the All_plasmids.fna file from the Plasmids Database mentioned above.
2. Add a table within your desired database called 'plasmid_seqs' with 2 columns: OrgID (VARCHAR(15) and Sequence (MEDIUMTEXT).
3. Place the .fna file and the /scripts/populate_sql.py script in the same directory. Modify the script to reflect the necessary database credentials.
4. Run the script './populate_sql.py', ensuring that the mysql package is installed on your system.
5. This will populate the database with the required plasmid sequences.


## Troubleshooting

If you encounter any issues with the tool, please ensure that the gene insert sequence contains only valid characters (A, C, G, T, N, and whitespace) and that a plasmid/vector is selected before submitting the form.

For further assistance, please refer to the documentation or contact the tool's developer.

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

### NOTE: The above usage is intended to be used on the JHU BIX server. To use locally or on another server with a SQL database one must take the below steps.
1. Downloaded the All_plasmids.fna file from the Plasmids Database mentioned above.
2. Add a table within your desired database called 'plasmid_seqs' with 2 columns: OrgID (VARCHAR(15) and Sequence (MEDIUMTEXT).
3. Place the .fna file and the /scripts/populate_sql.py script in the same directory. Modify the script to reflect the necessary database credentials.
4. Run the script './populate_sql.py', ensuring that the mysql package is installed on your system.
```commandline
usage: python ./populate_sql.py
```
5. This will populate the database with the required plasmid sequences.


## Project Layout
* [`final_project/`](.): The root folder of the project
  * [`README.md`](README.md): Current File. Details proper usage of this project and its components, requirements, and limitations.
  * [`main.html`](main.html): Contains HTML template for this project
  * [`css`](css/): CSS directory for this project
    * [`main.css`](css/main.css): Defines the style of the [`search.html`](search.html)
  * [`js`](js/): JavaScript directory for this project
    * [`main.js`](js/main.js): Contains JavaScript functions for this project
  * [`scripts`](scripts/): Contains main python/CGI scripts of this project
    * [`fetch_all_plasmids`](scripts/fetch_all_plasmids.cgi): Used for autocomplete function (fetches first 5 results matching a query)
    * [`design_primers`](scripts/design_primers.py): Designs primers for a given construct
    * [`get_final_seqs`](scripts/get_final_seqs.cgi): Creates a final sequence given plasmid sequence, insert sequence, and cut site
    * [`get_plasmid`](scripts/get_plasmid.cgi): Queries database and returns plasmid sequence and returns valid restriction enzymes for input
    * [`populate_sql`](scripts/populate_sql.py): Script to populate sql databse with a fasta file
    * [`search_plasmids`](scripts/search_plasmids.py): Defines sql query to pull plasmid from database
    * [`sequence_tools`](scripts/sequence_tools.py): Contains various functions for sequence manipulation and searching



## Troubleshooting

If you encounter any issues with the tool, please ensure that the gene insert sequence contains only valid characters (A, C, G, T, N, and whitespace) and that a plasmid/vector is selected before submitting the form.

For further assistance, please refer to the documentation or contact the tool's developer.

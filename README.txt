# Gibson Cloning Design Tool Tutorial


This tool is designed to facilitate the selection of plasmids, creation of sequences, design of primers for Gibson Assembly cloning. It takes a desired sequence to be inserted into a plasmid/vector, allows user to select the plasmid an insert sequence, and returns the forward and reverse primers for the Gibson Assembly.

Source code can be obtained here:

Utilizes data from Sistrom, Mark (2018). Plasmids database [Dataset]. Dryad. https://doi.org/10.15146/R33X2J
- Also available in the All_plasmids.fna file.

Utilizes tools:
- Biopython - https://biopython.org (Used for restriction enzyme database and sequence parsing and manipulation)

## Usage

To use the Gibson Cloning Design Tool, follow these steps:

1. Enter the gene insert sequence and select a plasmid/vector in the provided form fields.
2. Click the "Submit" button to initiate the primer design process.
3. Once the primers are designed, the forward and reverse primer sequences will be displayed in the designated sections.
4. You can then copy the final sequence to the clipboard or export it to a TXT file using the provided buttons.

## Troubleshooting

If you encounter any issues with the tool, please ensure that the gene insert sequence contains only valid characters (A, C, G, T, N, and whitespace) and that a plasmid/vector is selected before submitting the form.

For further assistance, please refer to the documentation or contact the tool's developer.
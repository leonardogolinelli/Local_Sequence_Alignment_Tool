Python implementation of Smith Waterman's Local Sequence Alignment Algorithm by Leonardo Golinelli
This tool was created for the course Bionformatics Algorithms held by Prof. E.Blanzieri @ CIBIO dept, University of Trento, Italy

Instructions:

0) Make sure **numpy** is installed
1) Fastest way to run: use the jupyter notebook "**notebook.ipynb**": select scoring system and sequences to be aligned then run the cell.
2) Alternatively: run the file "**run.py**" from command line, making sure to use the right shebang, interpreter and environment.
If flags are not specified, default values are chosen. Sequences can be either fed to the command line or added to a .txt file.

To check flags, run _python run.py_ -h or _./run.py -h_

options:
  -h, --help            show this help message and exit
  
  --match MATCH         Score for a match
  
  --mismatch MISMATCH   Score for a mismatch
  
  --gap GAP             Score for a gap
  
  --top_sequence TOP_SEQUENCE
                      Top sequence
                        
  --bottom_sequence BOTTOM_SEQUENCE
                        Bottom sequence
                        
  --sequence_file SEQUENCE_FILE
                        Path to file containing sequences, The first row should contain the top sequence, whereas
                        the second row should contain the bottom sequence


# FastaFetcher
**FastaFetcher** is a module that allows to filter and analyse fasta sequences in a coherent way. 

## Installation
To use this script you can clone the repository from github:

``` bash
git clone git@github.com:AnnaKalygina/FastaFetcher.git

cd FastaFetcher
```
No third-party libraries are required; only the Python standard library is used.
The repository contains the main scripts `fasta_fetcher.py` and `bio_files_processor.py`. Additionally, auxillary function scripts in the utils folder: `fasta_filter_utils.py` and `dna_rna_utils.py`. For a proper functioning the full module must be colned.

## Usage

After installation, you can import the functions and use them in your own scripts as shown above.

```python
from fasta_fetcher import run_dna_rna_tools, filter_fastq
```

## Functions
This repository contains four main functions for fasta sequence analysis: 
- `run_dna_rna_tools()`: For performing operations like transcription, reverse transcription, complement, and complement on DNA and RNA sequences.
- `filter_fastq()`: For filtering FASTQ sequences based on GC content, sequence length, and quality score.
- `convert_multiline_fasta_to_oneline()`: For converting FASTA with multiline sequence to FASTA with oneline sequences.
- `parse_blast_output()`: For parsing BLAST results and extracting the description of sequences with significant alignments.

### run_dna_rna_tools
This function allows you to perform a variety of actions: transcription, reverse transcription, finding reverse and complement - on one or more DNA or RNA sequences. 

#### Available actions:
- **transcribe**: Converts DNA sequences into RNA by replacing `T` with `U`.
- **translate**: Converts RNA sequence to DNA according to the rule of complementation.
- **reverse**: Reverses the sequence - from start to end.
- **complement**: Computes the complement of a DNA or RNA sequence.

#### Arguments:
- `*args`: A variable-length argument list. The first arguments are the sequences, and the last argument is the action to be performed.
When the argument does not contain a single sequence or an action or does not recognise the action being passed it raises the ValueError.

#### Returns:
- A single sequence or a list of sequences processed by the specified action.

#### Example Usage:

``` python
from fasta_fetcher import run_dna_rna_tools

sequences = run_dna_rna_tools("ATGC", "CGTA", "transcribe")
print(sequences)  # Output: ['AUGC', 'CGUA']
```

### filter_fastq

This function filters FASTQ sequences based on their GC content, sequence length, and quality score.

#### Arguments:

- `seqs`: A dictionary where keys are the sequence names, and values are tuples (sequence, quality).
- `gc_bounds`: A tuple indicating the lower and upper bounds of GC content in percentage (default: (0, 100)).
- `length_bounds`: A tuple indicating the lower and upper bounds of sequence length (default: (0, 2^32)).
- `quality_threshold`: The minimum average quality score required for the sequence (default: 0). The quality is calculated according to the phred33 system.

#### Returns:
A dictionary containing the filtered sequences that meet all specified criteria.

#### Example Usage:
``` python 
from fasta_fetcher import filter_fastq

example_fastq = {
    "@SEQ_ID1": ("ACGTACGT", "FFFFFFFF"),
    "@SEQ_ID2": ("GGGGCCCC", "BBBBBBBB"),
}

filtered = filter_fastq(example_fastq, gc_bounds=(40, 60), length_bounds=(8, 100), quality_threshold=30)
print(filtered) 

```
### convert_multiline_fasta_to_oneline

This function converts multiline FASTA to oneline FASTA. 
It assumes that the FASTA file could contain multiple independent seuences that are broken up into several lines. 
Therefore, the function recognizes the name of a sequence and then merges sequence itself into a single line. 
Additionaly, it reduces redundacy if two indentical sequences are stored in the file under the same name. 

#### Arguments
- `input_fasta`: Path to input FASTA file with sequences in multiple lines.
- `output_fasta`: Path to output FASTA file (optional). If not provided, output will be printed. The argument is optional. If not passed the function prints name and sequence to stdout.

#### Returns:
None. Either writes oneline sequences to the `output_fasta` or prints oneline sequences stdout. 

#### Example Usage:
``` python 
from bio_files import convert_multiline_fasta_to_oneline

input_fasta = 'my_dir/example_input_fasta'
output_fatsa = 'my_dir/example_output_fasta'

convert_multiline_fasta_to_oneline(input_fasta, output_fasta)
# The file will appear in the my_dir.
```

#### parse_blast_output
This function reads the input BLAST output file, extracts the first "Description"
for each query, and saves the descriptions in alphabetical order into the output file.

#### Arguments
- `input_fasta`: Path to input FASTA file with sequences in multiple lines.
- `output_fasta`: Path to output FASTA file (optional). If not provided, output will be printed. The argument is optional. If not passed the function prints name and sequence to stdout.

#### Returns:
None. Either writes oneline sequences to the `output_fasta` or prints oneline sequences stdout. 

#### Example Usage:
``` python 
from bio_files import convert_multiline_fasta_to_oneline

input_fasta = 'my_dir/example_input_fasta'
output_fatsa = 'my_dir/example_output_fasta'

parse_blast_output(input_fasta, output_fasta)
# The file will appear in the my_dir.
```

## Additional calculations
### GC Content Calculation

The function `filter_fastq()` filters sequences based on their GC content. The GC content is calculated as:

$$
GC \, \text{content} = \frac{\text{count of G + C bases}}{\text{total length of sequence}} \times 100
$$

For example, if a sequence has 4 bases `G` or `C` out of a total of 8 bases, its GC content would be:

$$
GC \, \text{content} = \frac{4}{8} \times 100 = 50\%
$$

### Quality Score Calculation

The quality score for each sequence is calculated by taking the **ASCII value** of each character in the quality string and subtracting 33 (as per the Phred33 scale):

$$
\text{Quality Score} = \frac{\sum (\text{ord}(char) - 33)}{\text{length of quality string}}
$$

For example, if the quality string is `"BBBBBBBB"` and each character represents a Phred33 score of 33, the average quality score would be:

$$
\text{Average Quality Score} = \frac{(33 - 33) \times 8}{8} = 0
$$




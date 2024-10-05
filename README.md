# FastaFetcher
***FastaFetcher** is a module that allows to filter and analyse fasta sequences in a coherent way. 

## Installation
To use this script you can clone the repository from github:

``` bash
git@github.com:AnnaKalygina/FastaFetcher.git

cd FastaFetcher
```
No third-party libraries are required; only the Python standard library is used.
The repository contains the main script `fasta_fetcher.py` and the auxillary function scripts in the utils folder: `fasta_filter_utils.py` and `dna_rna_utils.py`. For a proper functioning the full module must be colned.

## Usage

After installation, you can import the functions and use them in your own scripts as shown above.

```python
from fasta_fetcher import run_dna_rna_tools, filter_fastq
```

## Functions
This repository contains two main functions for fasta sequence analysis: 
- `run_dna_rna_tools()`: For performing operations like transcription, reverse transcription, complement, and complement on DNA and RNA sequences.
- `filter_fastq()`: For filtering FASTQ sequences based on GC content, sequence length, and quality score.

### `run_dna_rna_tools(*args: str) -> list[str]`
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

###`filter_fastq(seqs, gc_bounds = (0, 100), length_bounds = (0, 2^32), quality_threshold = 0) -> dict[str, tuple[str, str]]`

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

## Additional calculations
## GC Content Calculation

The function `filter_fastq()` filters sequences based on their GC content. The GC content is calculated as:

$$
GC \, \text{content} = \frac{\text{count of G + C bases}}{\text{total length of sequence}} \times 100
$$

For example, if a sequence has 4 bases `G` or `C` out of a total of 8 bases, its GC content would be:

$$
GC \, \text{content} = \frac{4}{8} \times 100 = 50\%
$$

## Quality Score Calculation

The quality score for each sequence is calculated by taking the **ASCII value** of each character in the quality string and subtracting 33 (as per the Phred33 scale):

$$
\text{Quality Score} = \frac{\sum (\text{ord}(char) - 33)}{\text{length of quality string}}
$$

For example, if the quality string is `"BBBBBBBB"` and each character represents a Phred33 score of 33, the average quality score would be:

$$
\text{Average Quality Score} = \frac{(33 - 33) \times 8}{8} = 0
$$




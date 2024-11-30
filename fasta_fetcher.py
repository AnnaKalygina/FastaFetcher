from utils.dna_rna_utils import transcribe, reverse, \
    complement, reverse_complement
from utils.fasta_filter_utils import (
    read_fastq,
    write_fastq,
    get_gc_content,
    get_quality_score,
)
import os

"""
Run dna and rna tools on a sequence or sequences with specified actions.

Args:
    *args: Variable length argument list. Sequences are followed by an action.

Returns:
    Processed sequence or a single sequence.

Raises:
    ValueError: If an invalid action or list are provided.
"""


def run_dna_rna_tools(*args: str) -> list[str]:

    action_map = {
        "transcribe": transcribe,
        "reverse": reverse,
        "complement": complement,
        "reverse_complement": reverse_complement,
    }

    if len(args) <= 1:
        raise ValueError("Invlaid number of arguments is passed.")

    sequences = args[:-1]
    action = args[-1]

    results = []
    if action in action_map:
        for sequence in sequences:
            result = action_map[action](sequence)
            results.append(result)
    else:
        raise ValueError(
            f"The action '{action}' is invalid! Valid actions are: \
                transcribe, reverse transcribe, complement,\
                reverse complement, reverse."
        )
    return results[0] if len(results) == 1 else results


"""
Reads a FASTQ file, filters sequences based on GC content, length, and quality,
and writes the filtered sequences to a new FASTQ file.

Args:
    input_fastq: Path to the input FASTQ file.
    output_fastq: Path to the output FASTQ file.
    gc_bounds: GC content bounds for filtering.
    length_bounds: Length bounds for filtering.
    quality_threshold: Minimum average quality score for filtering.

Returns:
    None
"""


def filter_fastq(
    input_fastq: str,
    output_fastq: str,
    gc_bounds=(0, 100),
    length_bounds=(0, 2**32),
    quality_threshold=0,
):
    output_dir = os.path.dirname(output_fastq)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if os.path.exists(output_fastq):
        raise FileExistsError(f"The file {output_fastq} already exists.")

    if isinstance(gc_bounds, (int, float)):
        gc_bounds = (0, gc_bounds)

    if isinstance(length_bounds, (int, float)):
        length_bounds = (0, length_bounds)

    for name, seq, quality in read_fastq(input_fastq):
        gc_content = get_gc_content(seq)
        length = len(seq)
        quality_score = get_quality_score(quality)

        if (
            gc_bounds[0] <= gc_content <= gc_bounds[1]
            and length_bounds[0] <= length <= length_bounds[1]
            and quality_score >= quality_threshold
        ):
            write_fastq(output_fastq, name, seq, quality)

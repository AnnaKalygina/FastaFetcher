from utils.dna_rna_utils import transcribe, reverse, \
                                complement, reverse_complement
from utils.fasta_filter_utils import get_gc_content, get_quality_score

"""
Run dna and rna tools on a sequence or sequences with specified actions.

Args:
    Variable length argument list. Sequences are followed by an action.

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
Filter FASTQ sequences based on GC content, length, and quality.

Args:
    seqs: A dictionary where keys are sequence names and values are tuples.
    gc_bounds: GC content bounds as a tuple or a single upper bound.
    length_bounds: Length bounds as a tuple or a single upper bound.
    quality_threshold: Minimum average quality score.

Returns:
    A dictionary with sequences that pass the filters.
"""


def filter_fastq(
    seqs: dict[str, tuple[str, str]],
    gc_bounds: tuple[float, float] = (0, 100),
    length_bounds: tuple[float, float] = (0, 2**32),
    quality_threshold: int = 0,
) -> dict[str, tuple[str, str]]:

    # check bounds
    if isinstance(gc_bounds, (int, float)):
        gc_bounds = (0, gc_bounds)

    if isinstance(length_bounds, (int, float)):
        length_bounds = (0, length_bounds)

    # filtered_seq = 'name' : ('sequence', 'quality')
    filtered_seqs = {}

    for name, (seq, quality) in seqs.items():
        gc_content = get_gc_content(seq)
        length = len(seq)
        quality_score = get_quality_score(quality)

        if (
            gc_bounds[0] <= gc_content <= gc_bounds[1]
            and length_bounds[0] <= length <= length_bounds[1]
            and quality_score >= quality_threshold
        ):
            filtered_seqs[name] = (seq, quality)

    return filtered_seqs

#Here are the utils for run_dna_rna_tools.py

dna_to_rna = {
    "A": "U",
    "T": "A",
    "G": "C",
    "C": "G",
    "a": "u",
    "t": "a",
    "g": "c",
    "c": "g",
}

dna_to_dna = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G",
    "a": "t",
    "t": "a",
    "g": "c",
    "c": "g",
}

rna_to_dna = {
    "A": "T",
    "U": "A",
    "G": "C",
    "C": "G",
    "a": "t",
    "u": "a",
    "g": "c",
    "c": "g",
}

rna_to_rna = {
    "A": "U",
    "U": "A",
    "G": "C",
    "C": "G",
    "a": "u",
    "u": "a",
    "g": "c",
    "c": "g",
}

dna_alphabet = ["A", "a", "T", "t", "G", "g", "C", "c"]
rna_alphabet = ["A", "a", "U", "u", "G", "g", "C", "c"]

# Checks

def is_dna(sequence: str) -> bool:
    return set(sequence).issubset(dna_alphabet)


def is_rna(sequence: str) -> bool:
    return set(sequence).issubset(rna_alphabet)

"""
Auxillary functions for the main
First, check the sequence being passed
Print the 'error' statement if the sequence is invalid
"""

def transcribe(sequence):
    if is_dna(sequence):
        dna_to_rna = str.maketrans("Tt", "Uu")
        result = sequence.translate(dna_to_rna)
        return ''.join(result)
    else:
        print(f"The sequence '{sequence}' is not a DNA \
                and could not be transcribed!")
        return None


def reverse(sequence):
    if is_dna(sequence) or is_rna(sequence):
        return sequence[::-1]
    else:
        print(
            f"The sequence '{sequence}' is not a nucleic acid and\
                could not be reversed!")
        return None


def reverse_transcribe(sequence):
    if is_rna(sequence):
        result = [rna_to_dna[x] for x in sequence]
        return "".join(result)
    else:
        print(
            f"The sequence '{sequence}'is not an RNA and could not\
                be reverse transcribed!"
        )
        return None


def complement(sequence, reverse=False):
    if is_dna(sequence):
        result = [dna_to_dna[x] for x in sequence]
        return "".join(result)
    elif is_rna(sequence):
        result = [rna_to_rna[x] for x in sequence]
        return "".join(result)
    else:
        reverse_str = "reverse " if reverse else ""
        print(
            f"The sequence '{sequence}' is not a nucleic acid and\
                {reverse_str}complement could not be found!"
        )
        return None


def reverse_complement(sequence):
    return complement(sequence[::-1], reverse=True)

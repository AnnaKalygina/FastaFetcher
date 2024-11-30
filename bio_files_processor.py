"""
Convert multiline FASTA to single-line FASTA format.
Args:
    input_fasta: Path to input FASTA file with sequences in multiple lines.
    output_fasta: Path to output FASTA file.
                  If not provided, output will be printed.
Returns:
    None. Writes the single-line FASTA sequences to the specified output file
    or prints to stdout.
"""


def convert_multiline_fasta_to_oneline(
    input_fasta: str,
    output_fasta: str = None
):
    with open(input_fasta, "r") as file:
        fasta_dict = {}
        current_seq_name = None
        current_sequence = []

        for line in file:
            line = line.strip()

            if line.startswith(">"):

                if current_seq_name:
                    fasta_dict[current_seq_name] = "".join(current_sequence)
                current_seq_name = line
                current_sequence = []
            else:
                current_sequence.append(line)

        if current_seq_name:
            fasta_dict[current_seq_name] = "".join(current_sequence)

    if output_fasta is None:
        for name, sequence in fasta_dict.items():
            print(name)
            print(sequence)
    else:
        with open(output_fasta, "w") as file:
            for name, sequence in fasta_dict.items():
                file.write(f"{name}\n{sequence}\n")


"""
Parses the BLAST output file to extract the best match descriptions.

Args:
    input_file: Path to the input BLAST output file.
    output_file: Path to the output file where results will be saved.
Returns:
    None. Writes the single-line FASTA sequences to the specified output file.
"""


def parse_blast_output(
    input_file: str,
    output_file: str
) -> None:
    with open(input_file, "r") as file:
        descriptions = set()
        in_alignment_section = False

        for line in file:
            # Traverse till the
            if line.startswith("Sequences producing significant alignments:"):
                in_alignment_section = True
                continue

            if in_alignment_section:
                if line.strip() == "" or line.startswith("Alignments:"):
                    in_alignment_section = False
                    continue

                description = line.split()[0]
                descriptions.add(description)

    sorted_descriptions = sorted(descriptions)

    with open(output_file, "w") as file:
        for description in sorted_descriptions:
            file.write(description + "\n")

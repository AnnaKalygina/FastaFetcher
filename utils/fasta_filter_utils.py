# Here are the utils for the fasta filter
from typing import Generator

"""
Perform fastaq read out line by line.
Args:
    Path to the input_fastq

Returns:
    Processed sequence or a single sequence.
"""


def read_fastq(input_fastq: str) -> Generator[str, str, str]:
    with open(input_fastq, "r") as file:
        while True:
            name_line = file.readline().strip()
            if not name_line:
                break
            name = name_line.split(" ")[0]
            seq_line = file.readline().strip()
            file.readline()
            quality_line = file.readline().strip()

            yield name, seq_line, quality_line


def write_fastq(output_fastq: str, name: str, seq: str, quality: str):
    with open(output_fastq, "w") as file:
        file.write(f"{name}\n{seq}\n+\n{quality}\n")


def get_quality_score(quality: str) -> int:
    return (
        sum(ord(char) - 33 for char in quality) / len(quality)
        if len(quality) > 0
        else 0
    )


def get_gc_content(seq: str) -> int:
    gc_content = sum(1 for x in seq if x in "GgCc") / len(seq) * 100
    return gc_content

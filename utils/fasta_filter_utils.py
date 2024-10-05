# Here are the utils for the fasta filter
def get_quality_score(quality: str) -> int:
    return sum(ord(char) - 33 for char in quality) / len(quality) if len(quality) > 0 else 0

def get_gc_content(seq: str) -> int:
    gc_content = sum(1 for x in seq if x in "GgCc") / len(seq) * 100
    return gc_content
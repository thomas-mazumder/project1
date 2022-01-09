# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    dic = {'A':'U', 'T':'A', 'C':'G', 'G':'C'}
    out = ''
    for char in seq:
        out += dic[char]
    return out

def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA then reverses
    the strand
    """
    return transcribe(seq)[::-1]

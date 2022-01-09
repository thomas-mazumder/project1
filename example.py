from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """
    # Create instance of FastaParser
    fastaparser = FastaParser("data/test.fa")
    # Create instance of FastqParser
    fastqparser = FastqParser("data/test.fq")
    
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    for _, seq in fastaparser:
        print(transcribe(seq))

    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    for _, seq, _ in fastqparser:
        print(transcribe(seq)) 

    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    for _, seq in fastaparser:
        print(reverse_transcribe(seq))       

    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    for _, seq, _ in fastqparser:
        print(reverse_transcribe(seq))

"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()

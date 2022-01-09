# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    p = FastaParser("data/test.fa")
    count = 0
    for record in p:
        assert len(record) == 2
        assert "seq" in record[0]    
        count += 1
    assert count == 2

def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    p = FastqParser("data/test.fq")
    count = 0
    for record in p:
        assert len(record) == 3
        assert "seq" in record[0]
        count += 1
    assert count == 2

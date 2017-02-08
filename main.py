from Bio.Seq import Seq
from Bio.SeqUtils import GC
from Bio.Alphabet import IUPAC, _verify_alphabet


class Primers():
    def __init__(self, sequence):
        self.sequence = sequence

        self.primerMinLength = 17
        self.primerMaxLength = 25
        self.primerMinMeltTemp = 55
        self.primerMaxMeltTemp = 60
        self.primerMinGC = 50
        self.primerMaxGC = 60


""" BELOW FOR TESTING PURPOSES ONLY """
# ask = input('seq? ')
sq = "CCCTAAGTTTGATGAGTATAGAAATGGATCC"
mt = """TTGATGAGTATAGAAATGGATCCACTCGTTATTCTCGGACGAGTGTTCAGTAATGAACCTCTGGAGAGAA
CCATGTATATGATCGTTATCTGGGTTGGACTTCTGCTTTTAAGCCCAGATAACTGGCCTGAATATGTTAA
TGAGAGAATCGGTATTCCTCATGTGTGGCATGTTTTCGTCTTTGCTCTTGCATTTTCGCTAGCAATTAAT
GTGCATCGATTATCAGCTATTGCCAGCGCCAGATATAAGCGATTTAAGCTAAGAAAACGCATTAAGATGC
AAAACGATAAAGTGCGATCAGTAATTCAAAACCTTACAGAAGAGCAATCTATGGTTTTGTGCGCAGCCCT
TAATGAAGGCAGGAAGTATGTGGTTACATCAAAACAATTCCCATACATTAGTGAGTTGATTGAGCTTGGT
GTGTTGAACAAAACTTTTTCCCGATGGAATGGAAAGCATATATTATTCCCTATTGAGGATATTTACTGGA
CTGAATTAGTTGCCAGCTATGATCCATATAATATTGAGATAAAGCCAAGGCCAATATCTAAGTAA"""
sq = Seq(sq, IUPAC.unambiguous_dna)
mt = Seq(mt.strip(), IUPAC.unambiguous_dna)

sequenceInput = ''

while not sequenceInput:
    sequenceInput = raw_input("Wat is de sequentie? ").upper()
    sequenceInput = Seq(sequenceInput, IUPAC.unambiguous_dna)

    _primer = Primers(sequenceInput)

    try:
        if not _verify_alphabet(sequenceInput):
            raise ValueError("De input mag alleen uit A, T, C of G bestaan.")
    except ValueError as e:
        print(e)
        sequenceInput = ''

print(GC(sequenceInput))

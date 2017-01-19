import re


class Primers():
    def __init__(self, sequence):
        self.sequence = sequence

    def checkInput(self):
        """ Checks the input sequence.
            Removes every character that's NOT in CATG
            Raises ValueError if condition is (not) met"""

        self.sequence = re.sub(r'[^CATG]', '', self.sequence.upper())
        if not(20 <= len(self.sequence) <= 500):
            raise ValueError("Sequentie moet tussen 20 en 500 lang zijn. "
                             "Sequentie is nu {}: {:d} teken(s) lang."
                             .format(self.sequence, len(self.sequence)))
        return self.sequence


""" BELOW FOR TESTING PURPOSES ONLY """
ask = input('seq? ')
sq = "CCCTAAGTTTGATGAGTATAGAAATGGATCC"
mt = """TTGATGAGTATAGAAATGGATCCACTCGTTATTCTCGGACGAGTGTTCAGTAATGAACCTCTGGAGAGAA
CCATGTATATGATCGTTATCTGGGTTGGACTTCTGCTTTTAAGCCCAGATAACTGGCCTGAATATGTTAA
TGAGAGAATCGGTATTCCTCATGTGTGGCATGTTTTCGTCTTTGCTCTTGCATTTTCGCTAGCAATTAAT
GTGCATCGATTATCAGCTATTGCCAGCGCCAGATATAAGCGATTTAAGCTAAGAAAACGCATTAAGATGC
AAAACGATAAAGTGCGATCAGTAATTCAAAACCTTACAGAAGAGCAATCTATGGTTTTGTGCGCAGCCCT
TAATGAAGGCAGGAAGTATGTGGTTACATCAAAACAATTCCCATACATTAGTGAGTTGATTGAGCTTGGT
GTGTTGAACAAAACTTTTTCCCGATGGAATGGAAAGCATATATTATTCCCTATTGAGGATATTTACTGGA
CTGAATTAGTTGCCAGCTATGATCCATATAATATTGAGATAAAGCCAAGGCCAATATCTAAGTAA"""
_primer = Primers(ask)
try:
    print(_primer.checkInput())
except ValueError as e:
    print(e)

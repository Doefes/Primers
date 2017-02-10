from Bio.Seq import Seq
from Bio.SeqUtils import GC, MeltingTemp
from Bio.Alphabet import IUPAC, _verify_alphabet


class Primers():
    def __init__(self, sequence):
        self.sequence = sequence
        self.sequenceRevComp = self.sequence.reverse_complement()

        self.primerMinLength = 17
        self.primerMaxLength = 25
        self.primerMinMeltTemp = 55
        self.primerMaxMeltTemp = 60
        self.primerMinGC = 50
        self.primerMaxGC = 60

    def calculateGC(primer):
        """ Move to createPrimerList """
        return GC(primer)

    def calculateMeltingTemp(primer):
        """ Move to createPrimerList """
        return MeltingTemp.Tm_Wallace(primer)

    def checkInput(self):
        if not _verify_alphabet(self.sequence):
            raise ValueError("De input mag alleen uit A, T, C of G bestaan.")


""" BELOW FOR TESTING PURPOSES ONLY """
sequenceInput = ''

while not sequenceInput:
    sequenceInput = raw_input("Wat is de sequentie? ").upper()
    sequenceInput = Seq(sequenceInput, IUPAC.unambiguous_dna)

    _primer = Primers(sequenceInput)

    try:
        _primer.checkInput()
    except ValueError as e:
        print(e)
        sequenceInput = ''

print(_primer.sequence)
print(GC(sequenceInput))
print(MeltingTemp.Tm_Wallace(sequenceInput))

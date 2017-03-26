from Bio.Seq import Seq
from Bio.SeqUtils import GC, MeltingTemp
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

    def checkInput(self):
        if not _verify_alphabet(self.sequence):
            raise ValueError("De input mag alleen uit A, T, C of G bestaan.")

    def selectAnnealingArea(self, sequence, positionStart, positionEnd):
        """ Selects the annealing area and splits the sequence in 3 parts
            Annealingarea, 5end and 3 end
        Args:
            sequence (str) -- sequence to select annealing area on (revComp)DNA
            positionStart (int) -- start position of annealing area
            positionEnd (int) -- end position of annealing area
        Return: (tuple)
            sequence5end (str) -- first part of sequence - for finding primers
            sequence3end (str) -- last part of sequence - for finding primers
        """
        sequence5end = sequence[:positionStart + self.primerMaxLength]
        sequence3end = sequence[positionEnd:]
        sequenceAnnealingArea = sequence[positionStart:positionEnd]
        return sequence5end, sequence3end, sequenceAnnealingArea

    def findPrimers(self, sequence):
        """ Finds all primers based on length, GC content and melting Temp
        Args:
            sequence (str) -- 5'to'3 sequence
        Return:
            primers (list) -- list contains [primer sequence, melting temp, GC]
        """
        primers = []

        for primerLength in range(self.primerMaxLength,
                                  self.primerMinLength-1,
                                  -1):
            """ Outer loop: loops through primer lengths.
                Decrements from 25 to 17 """

            for x in range(len(sequence)-primerLength):
                """ Inner loop: loops through sequence.
                    Increments position each iteration with 1 """
                possiblePrimer = sequence[0+x:primerLength+x]
                if self.primerMinMeltTemp\
                        <= MeltingTemp.Tm_Wallace(possiblePrimer)\
                        <= self.primerMaxMeltTemp:

                    if self.primerMinGC <= GC(possiblePrimer)\
                            <= self.primerMaxGC:

                        primers.append([possiblePrimer,
                                        MeltingTemp.Tm_Wallace(possiblePrimer),
                                        GC(possiblePrimer), primerLength])
            sequence = sequence[:-1]
        return primers


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
print(sequenceInput)
print(_primer.selectAnnealingArea(sequenceInput, 30, 60))

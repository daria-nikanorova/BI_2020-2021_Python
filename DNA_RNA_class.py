class Rna:
    def __init__(self, seq: str):
        self.seq = seq.upper()
        for base in self.seq:
            if base not in ['A', 'U', 'C', 'G']:
                raise ValueError(f'Ambiguous base "{base}" was found, only A, U, G or C are expected.\n'
                                 f'Please, check your RNA sequence and try again')

    def __iter__(self):  # as far as string is iterable, we can use its iter, rather than write special iterator
        return iter(self.seq)

    def __hash__(self):
        return hash(self.seq)

    def __eq__(self, other):  # two instances are equal if their sequences are equal
        if isinstance(other, Rna):
            return self.seq == other.seq
        return False

    def gc_content(self):
        return (self.seq.count('G') + self.seq.count('C')) * 100 / len(self.seq)

    def reverse_complement(self):
        complementary_bases = {"A": "U",
                               "U": "A",
                               "G": "C",
                               "C": "G"}
        rev_comp_seq = str()
        for base in self.seq[::-1]:
            rev_comp_seq += complementary_bases[base]
        return Rna(rev_comp_seq) # this method returns new instance of Rna() class


class Dna:
    def __init__(self, seq: str):
        self.seq = seq.upper()
        for base in self.seq:
            if base not in ['A', 'T', 'C', 'G']:
                raise ValueError(f'Ambiguous base "{base}" was found, only A, T, G or C are expected.\n'
                                 f'Please, check your DNA sequence and try again')

    def __iter__(self):
        return iter(self.seq)

    def __hash__(self):
        return hash(self.seq)

    def __eq__(self, other):
        if isinstance(other, Dna):
            return self.seq == other.seq
        return False

    def gc_content(self):
        return (self.seq.count('G') + self.seq.count('C')) * 100 / len(self.seq)

    def reverse_complement(self):
        complementary_bases = {"A": "T",
                               "T": "A",
                               "G": "C",
                               "C": "G"}
        rev_comp_seq = str()
        for base in self.seq[::-1]:
            rev_comp_seq += complementary_bases[base]
        return Dna(rev_comp_seq) # this method returns new instance of Dna() class

    def transcribe(self):
        complementary_bases_transcription = {"A": "U",
                                             "T": "A",
                                             "G": "C",
                                             "C": "G"}
        transcript = str()
        for base in self.seq:
            transcript += complementary_bases_transcription[base]
        return Rna(transcript) # this method returns new instance of Rna() class


# SUPPLEMENTARY
# I just saved NucleicAcidsIterator class in case the Dna.seq or Rna.seq are not strings
# and need special iterator

# class NucleicAcidsIterator:
#     def __init__(self, nucleic_acid):
#         self._nucleic_acid = nucleic_acid
#         self._i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self._i < len(self._nucleic_acid.seq):
#             self._i += 1
#             return self._nucleic_acid.seq[self._i - 1]
#         else:
#             raise StopIteration
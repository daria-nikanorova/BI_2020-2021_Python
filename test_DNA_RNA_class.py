import unittest
from DNA_RNA_class import Dna, Rna


class TestDnaClass(unittest.TestCase):
    def setUp(self):
        self.Dna_good = 'ATGC'
        self.Dna_good_twin = 'ATGC'
        self.Dna_bad = 'ATGUCGC'
        self.Dna_good_different_case = 'AtGc'
        self.Dna_blank = ''

    def test_good_dna_is_instance_of_Dna_class(self):
        self.assertIsInstance(Dna(self.Dna_good), Dna)
        self.assertIsInstance(Dna(self.Dna_good_different_case), Dna)

    def test_bad_dna_raises_error(self):
        with self.assertRaises(ValueError) as ctx:
            Dna(self.Dna_bad)
        obtained_msg = ctx.exception.args[0]
        expected_msg = f'Ambiguous base "U" was found, only A, T, G or C are expected.\n' \
                       f'Please, check your DNA sequence and try again'
        self.assertEqual(obtained_msg, expected_msg)

    def test_blank_dna_raises_error(self):
        with self.assertRaises(ValueError) as ctx:
            Dna(self.Dna_blank)
        obtained_msg = ctx.exception.args[0]
        expected_msg = 'A DNA sequence must be of positive length.\n' \
                       'Please, check your DNA sequence and try again'
        self.assertEqual(obtained_msg, expected_msg)

    def test_equal_dnas_are_equal(self):
        self.assertEqual(Dna(self.Dna_good), Dna(self.Dna_good_twin))

    def test_gc_content(self):
        self.assertEqual(Dna(self.Dna_good).gc_content(), 50.0)
        self.assertEqual(Dna(self.Dna_good_different_case).gc_content(), 50.0)

    def test_reverse_complement(self):
        self.assertEqual(Dna(self.Dna_good).reverse_complement().seq, Dna("GCAT").seq)
        self.assertEqual(Dna(self.Dna_good_different_case).reverse_complement().seq, Dna("GCAT").seq)

    def test_transcribe(self):
        self.assertEqual(Dna(self.Dna_good).transcribe().seq, Rna("UACG").seq)
        self.assertEqual(Dna(self.Dna_good_different_case).transcribe().seq, Rna("UACG").seq)


class TestRnaClass(unittest.TestCase):
    def setUp(self):
        self.Rna_good = 'UACG'
        self.Rna_good_twin = 'UACG'
        self.Rna_bad = 'ATGUCGC'
        self.Rna_good_different_case = 'UaCg'
        self.Rna_blank = ''

    def test_good_dna_is_instance_of_Dna_class(self):
        self.assertIsInstance(Rna(self.Rna_good), Rna)
        self.assertIsInstance(Rna(self.Rna_good_different_case), Rna)

    def test_bad_dna_raises_error(self):
        with self.assertRaises(ValueError) as ctx:
            Rna(self.Rna_bad)
        obtained_msg = ctx.exception.args[0]
        expected_msg = f'Ambiguous base "T" was found, only A, U, G or C are expected.\n' \
                       f'Please, check your RNA sequence and try again'
        self.assertEqual(obtained_msg, expected_msg)

    def test_blank_rna_raises_error(self):
        with self.assertRaises(ValueError) as ctx:
            Rna(self.Rna_blank)
        obtained_msg = ctx.exception.args[0]
        expected_msg = 'An RNA sequence must be of positive length.\n' \
                       'Please, check your RNA sequence and try again'
        self.assertEqual(obtained_msg, expected_msg)

    def test_equal_rnas_are_equal(self):
        self.assertEqual(Rna(self.Rna_good), Rna(self.Rna_good_twin))

    def test_gc_content(self):
        self.assertEqual(Rna(self.Rna_good).gc_content(), 50.0)
        self.assertEqual(Rna(self.Rna_good_different_case).gc_content(), 50.0)

    def test_reverse_complement(self):
        self.assertEqual(Rna(self.Rna_good).reverse_complement().seq, Rna("CGUA").seq)
        self.assertEqual(Rna(self.Rna_good_different_case).reverse_complement().seq, Rna("CGUA").seq)


if __name__ == '__main__':
    unittest.main()

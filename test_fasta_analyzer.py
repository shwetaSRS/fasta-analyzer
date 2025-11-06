import unittest
from fasta_analyzer import read_fasta, calculate_gc

class TestFastaAnalyzer(unittest.TestCase):
    def test_read_fasta(self):
        sequences = read_fasta("data/example.fasta")
        self.assertTrue(len(sequences) > 0)
        self.assertTrue(all(isinstance(seq, str) for seq in sequences.values()))

    def test_gc_calculation(self):
        gc = calculate_gc("ATGC")
        self.assertAlmostEqual(gc, 50.0)

if __name__ == "__main__":
    unittest.main()

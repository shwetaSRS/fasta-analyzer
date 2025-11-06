# fasta_analyzer.py
# A simple script to read a FASTA file and calculate GC content.

def read_fasta(file_path):
    """Reads sequences from a FASTA file."""
    sequences = {}
    with open(file_path, 'r') as f:
        seq_id = ""
        seq = ""
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if seq_id:
                    sequences[seq_id] = seq
                seq_id = line[1:]
                seq = ""
            else:
                seq += line
        if seq_id:
            sequences[seq_id] = seq
    return sequences


def gc_content(seq):
    """Calculates GC content percentage."""
    gc_count = seq.count("G") + seq.count("C")
    return round(gc_count / len(seq) * 100, 2)


if __name__ == "__main__":
    file_path = "data/example.fasta"
    sequences = read_fasta(file_path)
    print(f"Total sequences: {len(sequences)}\n")

    for seq_id, seq in sequences.items():
        print(f">{seq_id}")
        print(f"Length: {len(seq)} | GC

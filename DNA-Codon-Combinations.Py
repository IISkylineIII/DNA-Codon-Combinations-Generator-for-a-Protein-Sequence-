from itertools import product

amino_acid_codons = {
    'C': ['GCT', 'GCC', 'GCA', 'GCG'],
    'Y': ['TAT', 'TAC'],
    'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'I': ['ATT', 'ATC', 'ATA']
}

amino_sequence = 'CYCLIC'

all_combinations = [amino_acid_codons[aa] for aa in amino_sequence]

all_dna_sequences = product(*all_combinations)

total_sequences = sum(1 for _ in all_dna_sequences)

print(f"Total number of DNA sequences: {total_sequences}")

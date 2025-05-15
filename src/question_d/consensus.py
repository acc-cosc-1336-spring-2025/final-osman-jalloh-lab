# src/question_c/ancestor_consensus.py

def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    for i in range(len(dna_string1) - len(dna_string2) + 1):
        if dna_string1[i:i + len(dna_string2)] == dna_string2:
            positions.append(i + 1)  # 1-based indexing
    return tuple(positions)




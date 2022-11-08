import sys
import stdio


def isPotentialGene(dna):
    if (len(dna) % 3) != 0:
        return False
    if not dna.startwith('ATG'):
        return False
    for i in range(len(dna) - 3):
        if i % 3 == 0:
            if dna[i: i+3] == 'TAA':
                return False
            if dna[i: i+3] == 'TAG':
                return False
            if dna[i: i+3] == 'TGA':
                return False
    if dna.endswith('TAA'):
        return True
    if dna . endswith('TAG'):
        return True
    if dna.endswith('TGA'):
        return True
    return False


dna = "ATGCGCCTGCGTCTGTACTAG"  # sys.argv[1]
stdio.writeln(isPotentialGene(dna))

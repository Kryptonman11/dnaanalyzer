import io
import pandas as pd
from Bio import SeqIO
from dnaclass import Dna


def to_dict(file):
    dna_information, organism, gc_content, nuclotide_table = bio_data(file)
    data = {
        'Organism': organism,
        'Dna length': dna_information,
        'Gc content': gc_content,
        'A': [nuclo_breakdown['A'] for nuclo_breakdown in nuclotide_table],
        'T': [nuclo_breakdown['T'] for nuclo_breakdown in nuclotide_table],
        'C': [nuclo_breakdown['C'] for nuclo_breakdown in nuclotide_table],
        'G': [nuclo_breakdown['G'] for nuclo_breakdown in nuclotide_table]

    }
    return data


def load_to_df(file):
    return pd.DataFrame(to_dict(file))


def bio_data(file):
    dna_information = []
    organism = []
    gc_content = []
    nuclotide_table = []

    handle = io.StringIO(file.getvalue().decode("utf-8"))

    for record in SeqIO.parse(handle, "fasta"):
        dna = Dna(record)
        dna_information.append(dna.dna_seq())
        gc_content.append(dna.gc_content())
        nuclotide_table.append(dna.nuclotide_table())
        organism.append(dna.scientific_name())
    return dna_information, organism, gc_content, nuclotide_table

import re


class Dna:
    def __init__(self, record):
        self.record = record  # Record object
        self.seq = record.seq  # Sequence object

    def scientific_name(self):
        desc = self.record.description
        if "OS=" in desc:
            match = re.search(r"OS=(.*?) OX=", desc)
            if match:
                return match.group(1)

        words = desc.split()
        if len(words) >= 3:
            return " ".join(words[1:3])

        return None

    def dna_seq(self):
        # for i in range(len((self.seq))):
        #     self.seq[i][:n]
        return len(self.seq)

    def gc_content(self):
        return f"{round((self.seq.count('G') + self.seq.count('C')) / len(self.seq) * 100)}%"

    def nuclotide_table(self):
        return {dna: self.seq.count(dna) for dna in 'ATCG'}

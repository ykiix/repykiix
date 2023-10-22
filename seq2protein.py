import json
with open('rna_codon_table.json') as f:
    codon_table = json.load(f)


class Sequence(object):
    _nucl_dna = set(['A', 'T', 'C', 'G'])
    _nucl_rna = set(['A', 'U', 'C', 'G'])

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        string, seq_type = self._parse(file_name)
        if self._check(string, seq_type):
            self.string = string
            self.seq_type = seq_type
        else:
            raise NameError

    def _parse(self) -> str:
        with open(self.file_name) as f:
            seq_type = f.readline()
            string = f.readline()
        return string, seq_type

    def _check(self, string, seq_type) -> None:
        for nucl in string:
            if seq_type == 'DNA' and nucl not in self._nucl_dna:
                return False
            elif seq_type == 'RNA' and nucl not in self._nucl_rna:
                return False
            else:
                return True

    def hamming_distance(self, string2: str) -> int:
        self.string2 = string2
        hd = 0
        if len(self.string) == len(self.string2):
            for i in range(len(self.string)):
                if self.string[i] != self.string2[i]:
                    hd += 1
            return hd
        else:
            return 'Error'

    def transcribe(self) -> None:
        raise NameError

    def count_nucleotides(self) -> None:
        raise NameError

    def to_protein(self) -> None:
        raise NameError


class DNA(Sequence):
    def count_nucleotides(self) -> dict:
        count_A = 0
        count_T = 0
        count_C = 0
        count_G = 0
        for i in range(len(self.string)):
            if self.string[i] == 'A':
                count_A += 1
            if self.string[i] == 'T':
                count_T += 1
            if self.string[i] == 'C':
                count_C += 1
            if self.string[i] == 'G':
                count_G += 1
        return {'A': count_A, 'T': count_T, 'C': count_C, 'G': count_G}

    def transcribe(self) -> str:
        transcript = ''
        for i in range(len(self.string)):
            if self.string[i] == 'T':
                transcript += 'U'
            if self.string[i] == 'A':
                transcript += 'A'
            if self.string[i] == 'G':
                transcript += 'G'
            if self.string[i] == 'C':
                transcript += 'C'
        return transcript

    def complement_dna(self) -> str:
        complementstring = ''
        for i in range(len(self.string)):
            if self.string[i] == 'A':
                complementstring += 'T'
            if self.string[i] == 'T':
                complementstring += 'A'
            if self.string[i] == 'C':
                complementstring += 'G'
            if self.string[i] == 'G':
                complementstring += 'C'
        return complementstring

    def to_protein(self) -> str:
        protein = ''
        m_rna = ''
        for i in range(len(self.string)):
            if self.string[i] == 'A':
                m_rna += 'A'
            if self.string[i] == 'T':
                m_rna += 'U'
            if self.string[i] == 'C':
                m_rna += 'C'
            if self.string[i] == 'G':
                m_rna += 'G'
        for i in range(0, len(m_rna), 3):
            codon = m_rna[i:(i+3)]
            protein += codon_table[codon]
        return protein


class RNA(Sequence):
    def count_nucleotides(self) -> dict:
        count_A = 0
        count_U = 0
        count_C = 0
        count_G = 0
        for i in range(len(self.string)):
            if self.string[i] == 'A':
                count_A += 1
            if self.string[i] == 'U':
                count_U += 1
            if self.string[i] == 'C':
                count_C += 1
            if self.string[i] == 'G':
                count_G += 1
        return {'A': count_A, 'U': count_U, 'C': count_C, 'G': count_G}

    def transcribe(self) -> str:
        transcript = ''
        for i in range(len(self.string)):
            if self.string[i] == 'U':
                transcript += 'T'
            if self.string[i] == 'A':
                transcript += 'A'
            if self.string[i] == 'G':
                transcript += 'G'
            if self.string[i] == 'C':
                transcript += 'C'
        return transcript

    def to_protein(self) -> str:
        protein = ''
        for i in range(0, len(self.string), 3):
            codon = self.string[i:(i+3)]
            protein += codon_table[codon]
        return protein


class Protein(Sequence):
    def count_aminoacids(self) -> dict:
        aminoacids = {'A': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'K': 0,
                      'L': 0, 'M': 0, 'N': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'V': 0, 'W': 0, 'Y': 0}
        for i in range(len(self.string)):
            aminoacids[self.string[i]] += 1
        return aminoacids

    def to_protein(self) -> str:
        return self.string

    def charge(self) -> int:
        z = 0
        for i in range(len(self.string)):
            if self.string[i] == 'K' or self.string[i] == 'R' or self.string[i] == 'H':
                z += 1
            elif self.string[i] == 'D' or self.string[i] == 'E':
                z -= 1
            else:
                z += 0
        return z


file_name = Sequence(input())

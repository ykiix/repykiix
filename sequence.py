class Sequence(object):

    def __init__(self, string: str) -> None:
        self.string = string

    def transcribe(self) -> None:
        raise NameError

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


string = DNA(input())
string2 = DNA(input())
a = string.count_nucleotides()
b = string.transcribe()
c = string.complement_dna()
d = string.hamming_distance(string2.string)
print(a)
print(b)
print(c)
print(d)

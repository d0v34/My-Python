# String
DNA = '''
ACTGTGCTGACTCCCGGTGCTGCCGCTGCCATAGCTAAAGCCCGGGTCCTGGTAGGCAGGCGGGAAGCAG
GGTGGGGGTCCCGGGTACTGGTAGGGGTAGCCCTGACCCAGAGGCGGGGGGGCAGCCGGGTGGGGCAGCG
GGGCCAGCGTGTCCTGAA-CGAAGTCCCACTGGAGCCACTGTTGAGGTTCAGGGTGGCGAGATCTGGCGG
NNNAGGGTAGGTGAGGGCCGCGGAGGGGCCTCCGGCGTTCCCCTCCCCCCCGCCCTGAAACCCGAAGCCC
CCACTCACTGCTGCAGAGATCCCCTGAAAACGTAGTAGCACTGCTCgagacAGGTGATCTGTTGACCTGA
AACCGCAGGAAGCCGTGCTTCAGCAAGCTGCTGGCGTACTTCCGGGCCT---GCCGCTCCTTGAAGCCCT
CCACGTGTGTGTACAGCCAGTCCACCACGTCCGCCCCTGGCCGGCACCAGCGGTCAGCCCGCAGCCTCGA
GGCAAGCAGCCCTGCCNNTGGCACTATCCGC-CGCGGGGACGGCCACTCACCGATGACGGCATNNGCGAT
GGTGATCTTGAGCCACATGCGGTCGCGGATCTCCAGTCCCGAG---GGCAGCTGCATGACCCGGACGACG
GCGCTCATGTCACtcaccgtcagcggcgcctcttccagCCAGCTCTGCAAAGCACAGACAGCCCCGCTTC
GCCCCAGCATCTGAAAGCGGGGGACTCggcAcgCTGCACCCCCAGGGGAGCCTCTGGGCAGAGCCTGCGC
CAGGGCGCAAGCTGGACGGTGCGTGACAGCAGGGCCCCGGCCCACTGCAGGATGCACCCCCGTGAGGCTG
GGGCGTGAGCAGGGGGGTTGGACAtttAGTCTCCCACTTCTACAGACACTTTTCATCAGGATCCTAGGCA
CAAACTGGGCTGAAACCCCACCCTGCAGACCAGGAAGTAATGAGAACAGGGCAGGCCCCTTCCCCTCNNC
GCATGCC-CACCCGAGAGCGCAGGCTGTTAGTCGTGTTAATGGCAGGAAGCAGAATGGAGACCTGGCCCC
TGCCTCTGAA-CCGTGGGTGCTCaactggctaGCCCTACGTACATCCCCTGTTCcggCCAACACACAGAC
ATGAGCAGGATGGGCTGCACAAGGTGGGCACGGGTGCCTGTGCACACGTCTGTGCAGGGAGTTGGGGACA
GGCAACACACACGTGTCACAGCCCCATGACGGggcaattgcGCCATGCTGGCTGAATGGCAGAGACGCCC
CTCCAAGCCTCGGTTTCTGCTGGGGCCCTCAGGAGCTGCCACTTACGTGGAGCACCAGGCACGGAGCTGG
TTAGTGAGGAGGAGCTGGTGCGCGTGACGGCGCTGGAGCAGGGACTCGTACCGTAGCGGGGCAGGGCNNN
TGTCAGTGCCGCCGTGTGGtcagcggcgatCGGCG-GGTCGATGGGCCGCACCGGGTCAGCTGGGTGNAG
ACACGTGGCGATGACAGGCGGACAGATGGACAGGGTGGGAGGGCAGGGTGCAGGGCACAGAGGAGAGAGG
CCTTCAGGCTAGGTAGGCGCCCCCTCCCCATCCCGccccGTGTGCCCCGAGGGCCACTCACCCCGTGGGA
CGGTGAAGTAGCTTCG-GGCGTTGGGTCCAGCACTTGGCCACAGTGAGGCTGNAAATGGCTGCAGGAACG
GTGGTCCCCCCGCAAGGCCCCCATGGTCCCACCTCCCTGCCTGGCCCCTCCCGCTCCAGCGCCNCCAGCC
'''
temp = DNA.strip()
print("Dlugosc sekwecji:", len(temp))
print("Ilosc sekwencji GAGA:", temp.find("GAGA", beg=0, end=len(temp)))

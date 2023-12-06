#Created on Wed Sept 1 13:32:16 2021 by Richard Wall

import pysam, argparse

parser = argparse.ArgumentParser(description='Counts sequences from P. knowlesi KRS mutation library')
parser.add_argument('-i',nargs='?',dest='infile',help='Input BAM file')

args = parser.parse_args()

args.KRS_1TTT = 'TATGAAATTGGTTTTGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1TTT

countKRS_1TTT = 0		
		
bfKRS_1TTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1TTT:		
	if args.KRS_1TTT in line.seq:	
		countKRS_1TTT += 1
		
print 'KRS_1TTT' , args.KRS_1TTT, countKRS_1TTT		
		
args.KRS_1TTC = 'TATGAAATTGGTTTCGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1TTC

countKRS_1TTC = 0		
		
bfKRS_1TTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1TTC:		
	if args.KRS_1TTC in line.seq:	
		countKRS_1TTC += 1
		
print 'KRS_1TTC' , args.KRS_1TTC, countKRS_1TTC		
		
args.KRS_1TTA = 'TATGAAATTGGTTTAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1TTA		
countKRS_1TTA = 0		
		
bfKRS_1TTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1TTA:		
	if args.KRS_1TTA in line.seq:	
		countKRS_1TTA += 1
		
print 'KRS_1TTA' , args.KRS_1TTA, countKRS_1TTA		
		
args.KRS_1TTG = 'TATGAAATTGGTTTGGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1TTG		
countKRS_1TTG = 0		
		
bfKRS_1TTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1TTG:		
	if args.KRS_1TTG in line.seq:	
		countKRS_1TTG += 1
		
print 'KRS_1TTG' , args.KRS_1TTG, countKRS_1TTG		
		
args.KRS_1CTT = 'TATGAAATTGGTCTTGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1CTT		
countKRS_1CTT = 0		
		
bfKRS_1CTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1CTT:		
	if args.KRS_1CTT in line.seq:	
		countKRS_1CTT += 1
		
print 'KRS_1CTT' , args.KRS_1CTT, countKRS_1CTT		
		
args.KRS_1CTC = 'TATGAAATTGGTCTCGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1CTC		
countKRS_1CTC = 0		
		
bfKRS_1CTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1CTC:		
	if args.KRS_1CTC in line.seq:	
		countKRS_1CTC += 1
		
print 'KRS_1CTC' , args.KRS_1CTC, countKRS_1CTC		
		
args.KRS_1CTA = 'TATGAAATTGGTCTAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1CTA		
countKRS_1CTA = 0		

		
bfKRS_1CTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1CTA:		
	if args.KRS_1CTA in line.seq:	
		countKRS_1CTA += 1
		
print 'KRS_1CTA' , args.KRS_1CTA, countKRS_1CTA		
		
args.KRS_1CTG = 'TATGAAATTGGTCTGGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1CTG		
countKRS_1CTG = 0		
		
bfKRS_1CTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1CTG:		
	if args.KRS_1CTG in line.seq:	
		countKRS_1CTG += 1
		
print 'KRS_1CTG' , args.KRS_1CTG, countKRS_1CTG		
		
args.KRS_1ATT = 'TATGAAATTGGTATTGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1ATT		
countKRS_1ATT = 0		
		
bfKRS_1ATT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1ATT:		
	if args.KRS_1ATT in line.seq:	
		countKRS_1ATT += 1
		
print 'KRS_1ATT' , args.KRS_1ATT, countKRS_1ATT		
		
args.KRS_1ATC = 'TATGAAATTGGTATCGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1ATC		
countKRS_1ATC = 0		
		
bfKRS_1ATC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1ATC:		
	if args.KRS_1ATC in line.seq:	
		countKRS_1ATC += 1
		
print 'KRS_1ATC' , args.KRS_1ATC, countKRS_1ATC		
		
args.KRS_1ATA = 'TATGAAATTGGTATAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1ATA		
countKRS_1ATA = 0		
		
bfKRS_1ATA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1ATA:		
	if args.KRS_1ATA in line.seq:	
		countKRS_1ATA += 1
		
print 'KRS_1ATA' , args.KRS_1ATA, countKRS_1ATA		
		
args.KRS_1ATG = 'TATGAAATTGGTATGGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1ATG		
countKRS_1ATG = 0		
		
bfKRS_1ATG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1ATG:		
	if args.KRS_1ATG in line.seq:	
		countKRS_1ATG += 1
		
print 'KRS_1ATG' , args.KRS_1ATG, countKRS_1ATG		
		
args.KRS_1GTT = 'TATGAAATTGGTGTTGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1GTT		
countKRS_1GTT = 0		
		
bfKRS_1GTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1GTT:		
	if args.KRS_1GTT in line.seq:	
		countKRS_1GTT += 1
		
print 'KRS_1GTT' , args.KRS_1GTT, countKRS_1GTT		
		
args.KRS_1GTC = 'TATGAAATTGGTGTCGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1GTC		
countKRS_1GTC = 0		
		
bfKRS_1GTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1GTC:		
	if args.KRS_1GTC in line.seq:	
		countKRS_1GTC += 1
		
print 'KRS_1GTC' , args.KRS_1GTC, countKRS_1GTC		
		
args.KRS_1GTA = 'TATGAAATTGGTGTAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1GTA		
countKRS_1GTA = 0		
		
bfKRS_1GTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1GTA:		
	if args.KRS_1GTA in line.seq:	
		countKRS_1GTA += 1
		
print 'KRS_1GTA' , args.KRS_1GTA, countKRS_1GTA		
		
args.KRS_1GTG = 'TATGAAATTGGTGTGGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1GTG	
countKRS_1GTG = 0		
		
bfKRS_1GTG = pysam.Samfile(args.infile,"rb")

for line in bfKRS_1GTG:		
	if args.KRS_1GTG in line.seq:	
		countKRS_1GTG += 1
		
print 'KRS_1GTG', args.KRS_1GTG, countKRS_1GTG
		
args.KRS_1TCT = 'TATGAAATTGGTTCTGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1TCT		
countKRS_1TCT = 0		
		
bfKRS_1TCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1TCT:		
	if args.KRS_1TCT in line.seq:	
		countKRS_1TCT += 1
		
print 'KRS_1TCT' , args.KRS_1TCT, countKRS_1TCT		
		
args.KRS_1TCC = 'TATGAAATTGGTTCCGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1TCC		
countKRS_1TCC = 0		
		
bfKRS_1TCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1TCC:		
	if args.KRS_1TCC in line.seq:	
		countKRS_1TCC += 1
		
print 'KRS_1TCC' , args.KRS_1TCC, countKRS_1TCC		
		
args.KRS_1TCA = 'TATGAAATTGGTTCAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1TCA		
countKRS_1TCA = 0		
		
bfKRS_1TCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1TCA:		
	if args.KRS_1TCA in line.seq:	
		countKRS_1TCA += 1
		
print 'KRS_1TCA' , args.KRS_1TCA, countKRS_1TCA		
		
args.KRS_1TCG = 'TATGAAATTGGTTCGGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1TCG		
countKRS_1TCG = 0		
		
bfKRS_1TCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1TCG:		
	if args.KRS_1TCG in line.seq:	
		countKRS_1TCG += 1
		
print 'KRS_1TCG' , args.KRS_1TCG, countKRS_1TCG		
		
args.KRS_1CCT = 'TATGAAATTGGTCCTGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1CCT		
countKRS_1CCT = 0		
		
bfKRS_1CCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1CCT:		
	if args.KRS_1CCT in line.seq:	
		countKRS_1CCT += 1
		
print 'KRS_1CCT' , args.KRS_1CCT, countKRS_1CCT		
		
args.KRS_1CCC = 'TATGAAATTGGTCCCGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1CCC		
countKRS_1CCC = 0		
		
bfKRS_1CCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1CCC:		
	if args.KRS_1CCC in line.seq:	
		countKRS_1CCC += 1
		
print 'KRS_1CCC' , args.KRS_1CCC, countKRS_1CCC		
		
args.KRS_1CCA = 'TATGAAATTGGTCCAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1CCA		
countKRS_1CCA = 0		
		
bfKRS_1CCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1CCA:		
	if args.KRS_1CCA in line.seq:	
		countKRS_1CCA += 1
		
print 'KRS_1CCA' , args.KRS_1CCA, countKRS_1CCA		
		
args.KRS_1CCG = 'TATGAAATTGGTCCGGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1CCG		
countKRS_1CCG = 0		
		
bfKRS_1CCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1CCG:		
	if args.KRS_1CCG in line.seq:	
		countKRS_1CCG += 1
		
print 'KRS_1CCG' , args.KRS_1CCG, countKRS_1CCG		
		
args.KRS_1ACT = 'TATGAAATTGGTACTGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1ACT		
countKRS_1ACT = 0		
		
bfKRS_1ACT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1ACT:		
	if args.KRS_1ACT in line.seq:	
		countKRS_1ACT += 1
		
print 'KRS_1ACT' , args.KRS_1ACT, countKRS_1ACT		
		
args.KRS_1ACC = 'TATGAAATTGGTACCGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1ACC		
countKRS_1ACC = 0		
		
bfKRS_1ACC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1ACC:		
	if args.KRS_1ACC in line.seq:	
		countKRS_1ACC += 1
		
print 'KRS_1ACC' , args.KRS_1ACC, countKRS_1ACC		
		
args.KRS_1ACA = 'TATGAAATTGGTACAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1ACA		
countKRS_1ACA = 0		
		
bfKRS_1ACA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1ACA:		
	if args.KRS_1ACA in line.seq:	
		countKRS_1ACA += 1
		
print 'KRS_1ACA' , args.KRS_1ACA, countKRS_1ACA		
		
args.KRS_1ACG = 'TATGAAATTGGTACGGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1ACG		
countKRS_1ACG = 0		
		
bfKRS_1ACG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1ACG:		
	if args.KRS_1ACG in line.seq:	
		countKRS_1ACG += 1
		
print 'KRS_1ACG' , args.KRS_1ACG, countKRS_1ACG		
		
args.KRS_1GCT = 'TATGAAATTGGTGCTGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1GCT		
countKRS_1GCT = 0		
		
bfKRS_1GCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1GCT:		
	if args.KRS_1GCT in line.seq:	
		countKRS_1GCT += 1
		
print 'KRS_1GCT' , args.KRS_1GCT, countKRS_1GCT		
		
args.KRS_1GCC = 'TATGAAATTGGTGCCGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1GCC		
countKRS_1GCC = 0		
		
bfKRS_1GCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1GCC:		
	if args.KRS_1GCC in line.seq:	
		countKRS_1GCC += 1
		
print 'KRS_1GCC' , args.KRS_1GCC, countKRS_1GCC		
		
args.KRS_1GCA = 'TATGAAATTGGTGCAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1GCA		
countKRS_1GCA = 0		
		
bfKRS_1GCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1GCA:		
	if args.KRS_1GCA in line.seq:	
		countKRS_1GCA += 1
		
print 'KRS_1GCA' , args.KRS_1GCA, countKRS_1GCA		
		
args.KRS_1GCG = 'TATGAAATTGGTGCGGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1GCG		
countKRS_1GCG = 0		
		
bfKRS_1GCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1GCG:		
	if args.KRS_1GCG in line.seq:	
		countKRS_1GCG += 1
		
print 'KRS_1GCG' , args.KRS_1GCG, countKRS_1GCG		
		
args.KRS_1TAT = 'TATGAAATTGGTTATGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1TAT		
countKRS_1TAT = 0		
		
bfKRS_1TAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1TAT:		
	if args.KRS_1TAT in line.seq:	
		countKRS_1TAT += 1
		
print 'KRS_1TAT' , args.KRS_1TAT, countKRS_1TAT		
		
args.KRS_1TAC = 'TATGAAATTGGTTACGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1TAC		
countKRS_1TAC = 0		
		
bfKRS_1TAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1TAC:		
	if args.KRS_1TAC in line.seq:	
		countKRS_1TAC += 1
		
print 'KRS_1TAC' , args.KRS_1TAC, countKRS_1TAC		
		
args.KRS_1TAA = 'TATGAAATTGGTTAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1TAA		
countKRS_1TAA = 0		
		
bfKRS_1TAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1TAA:		
	if args.KRS_1TAA in line.seq:	
		countKRS_1TAA += 1
		
print 'KRS_1TAA' , args.KRS_1TAA, countKRS_1TAA		
		
args.KRS_1TAG = 'TATGAAATTGGTTAGGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1TAG		
countKRS_1TAG = 0		
		
bfKRS_1TAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1TAG:		
	if args.KRS_1TAG in line.seq:	
		countKRS_1TAG += 1
		
print 'KRS_1TAG' , args.KRS_1TAG, countKRS_1TAG		
		
args.KRS_1CAT = 'TATGAAATTGGTCATGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1CAT		
countKRS_1CAT = 0		
		
bfKRS_1CAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1CAT:		
	if args.KRS_1CAT in line.seq:	
		countKRS_1CAT += 1
		
print 'KRS_1CAT' , args.KRS_1CAT, countKRS_1CAT		
		
args.KRS_1CAC = 'TATGAAATTGGTCACGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1CAC		
countKRS_1CAC = 0		
		
bfKRS_1CAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1CAC:		
	if args.KRS_1CAC in line.seq:	
		countKRS_1CAC += 1
		
print 'KRS_1CAC' , args.KRS_1CAC, countKRS_1CAC		
		
args.KRS_1CAA = 'TATGAAATTGGTCAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1CAA		
countKRS_1CAA = 0		
		
bfKRS_1CAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1CAA:		
	if args.KRS_1CAA in line.seq:	
		countKRS_1CAA += 1
		
print 'KRS_1CAA' , args.KRS_1CAA, countKRS_1CAA		
		
args.KRS_1CAG = 'TATGAAATTGGTCAGGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1CAG		
countKRS_1CAG = 0		
		
bfKRS_1CAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1CAG:		
	if args.KRS_1CAG in line.seq:	
		countKRS_1CAG += 1
		
print 'KRS_1CAG' , args.KRS_1CAG, countKRS_1CAG		
		
args.KRS_1AAT = 'TATGAAATTGGTAATGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1AAT		
countKRS_1AAT = 0		
		
bfKRS_1AAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1AAT:		
	if args.KRS_1AAT in line.seq:	
		countKRS_1AAT += 1
		
print 'KRS_1AAT' , args.KRS_1AAT, countKRS_1AAT		
		
args.KRS_1AAC = 'TATGAAATTGGTAACGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1AAC		
countKRS_1AAC = 0		
		
bfKRS_1AAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1AAC:		
	if args.KRS_1AAC in line.seq:	
		countKRS_1AAC += 1
		
print 'KRS_1AAC' , args.KRS_1AAC, countKRS_1AAC		
		
args.KRS_1AAA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1AAA		
countKRS_1AAA = 0		
		
bfKRS_1AAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1AAA:		
	if args.KRS_1AAA in line.seq:	
		countKRS_1AAA += 1
		
print 'KRS_1AAA' , args.KRS_1AAA, countKRS_1AAA		
		
args.KRS_1AAG = 'TATGAAATTGGTAAGGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1AAG		
countKRS_1AAG = 0		
		
bfKRS_1AAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1AAG:		
	if args.KRS_1AAG in line.seq:	
		countKRS_1AAG += 1
		
print 'KRS_1AAG' , args.KRS_1AAG, countKRS_1AAG		
		
args.KRS_1GAT = 'TATGAAATTGGTGATGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1GAT		
countKRS_1GAT = 0		
		
bfKRS_1GAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1GAT:		
	if args.KRS_1GAT in line.seq:	
		countKRS_1GAT += 1
		
print 'KRS_1GAT' , args.KRS_1GAT, countKRS_1GAT		
		
args.KRS_1GAC = 'TATGAAATTGGTGACGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1GAC		
countKRS_1GAC = 0		
		
bfKRS_1GAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1GAC:		
	if args.KRS_1GAC in line.seq:	
		countKRS_1GAC += 1
		
print 'KRS_1GAC' , args.KRS_1GAC, countKRS_1GAC		
		
args.KRS_1GAA = 'TATGAAATTGGTGAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1GAA		
countKRS_1GAA = 0		
		
bfKRS_1GAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1GAA:		
	if args.KRS_1GAA in line.seq:	
		countKRS_1GAA += 1
		
print 'KRS_1GAA' , args.KRS_1GAA, countKRS_1GAA		
		
args.KRS_1GAG = 'TATGAAATTGGTGAGGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1GAG		
countKRS_1GAG = 0		
		
bfKRS_1GAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1GAG:		
	if args.KRS_1GAG in line.seq:	
		countKRS_1GAG += 1
		
print 'KRS_1GAG' , args.KRS_1GAG, countKRS_1GAG		
		
args.KRS_1TGT = 'TATGAAATTGGTTGTGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1TGT		
countKRS_1TGT = 0		
		
bfKRS_1TGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1TGT:		
	if args.KRS_1TGT in line.seq:	
		countKRS_1TGT += 1
		
print 'KRS_1TGT' , args.KRS_1TGT, countKRS_1TGT		
		
args.KRS_1TGC = 'TATGAAATTGGTTGCGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1TGC		
countKRS_1TGC = 0		
		
bfKRS_1TGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1TGC:		
	if args.KRS_1TGC in line.seq:	
		countKRS_1TGC += 1
		
print 'KRS_1TGC' , args.KRS_1TGC, countKRS_1TGC		
		
args.KRS_1TGA = 'TATGAAATTGGTTGAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1TGA		
countKRS_1TGA = 0		
		
bfKRS_1TGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1TGA:		
	if args.KRS_1TGA in line.seq:	
		countKRS_1TGA += 1
		
print 'KRS_1TGA' , args.KRS_1TGA, countKRS_1TGA		
		
args.KRS_1TGG = 'TATGAAATTGGTTGGGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1TGG		
countKRS_1TGG = 0		
		
bfKRS_1TGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1TGG:		
	if args.KRS_1TGG in line.seq:	
		countKRS_1TGG += 1
		
print 'KRS_1TGG' , args.KRS_1TGG, countKRS_1TGG		
		
args.KRS_1CGT = 'TATGAAATTGGTCGTGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1CGT		
countKRS_1CGT = 0		
		
bfKRS_1CGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1CGT:		
	if args.KRS_1CGT in line.seq:	
		countKRS_1CGT += 1
		
print 'KRS_1CGT' , args.KRS_1CGT, countKRS_1CGT		
		
args.KRS_1CGC = 'TATGAAATTGGTCGCGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1CGC		
countKRS_1CGC = 0		
		
bfKRS_1CGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1CGC:		
	if args.KRS_1CGC in line.seq:	
		countKRS_1CGC += 1
		
print 'KRS_1CGC' , args.KRS_1CGC, countKRS_1CGC		
		
args.KRS_1CGA = 'TATGAAATTGGTCGAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1CGA		
countKRS_1CGA = 0		
		
bfKRS_1CGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1CGA:		
	if args.KRS_1CGA in line.seq:	
		countKRS_1CGA += 1
		
print 'KRS_1CGA' , args.KRS_1CGA, countKRS_1CGA		
		
args.KRS_1CGG = 'TATGAAATTGGTCGGGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1CGG		
countKRS_1CGG = 0		
		
bfKRS_1CGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1CGG:		
	if args.KRS_1CGG in line.seq:	
		countKRS_1CGG += 1
		
print 'KRS_1CGG' , args.KRS_1CGG, countKRS_1CGG		
		
args.KRS_1AGT = 'TATGAAATTGGTAGTGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1AGT		
countKRS_1AGT = 0		
		
bfKRS_1AGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1AGT:		
	if args.KRS_1AGT in line.seq:	
		countKRS_1AGT += 1
		
print 'KRS_1AGT' , args.KRS_1AGT, countKRS_1AGT		
		
args.KRS_1AGC = 'TATGAAATTGGTAGCGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1AGC		
countKRS_1AGC = 0		
		
bfKRS_1AGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1AGC:		
	if args.KRS_1AGC in line.seq:	
		countKRS_1AGC += 1
		
print 'KRS_1AGC' , args.KRS_1AGC, countKRS_1AGC		
		
args.KRS_1AGA = 'TATGAAATTGGTAGAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1AGA		
countKRS_1AGA = 0		
		
bfKRS_1AGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1AGA:		
	if args.KRS_1AGA in line.seq:	
		countKRS_1AGA += 1
		
print 'KRS_1AGA' , args.KRS_1AGA, countKRS_1AGA		
		
args.KRS_1AGG = 'TATGAAATTGGTAGGGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1AGG		
countKRS_1AGG = 0		
		
bfKRS_1AGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1AGG:		
	if args.KRS_1AGG in line.seq:	
		countKRS_1AGG += 1
		
print 'KRS_1AGG' , args.KRS_1AGG, countKRS_1AGG		
		
args.KRS_1GGT = 'TATGAAATTGGTGGTGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1GGT		
countKRS_1GGT = 0		
		
bfKRS_1GGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1GGT:		
	if args.KRS_1GGT in line.seq:	
		countKRS_1GGT += 1
		
print 'KRS_1GGT' , args.KRS_1GGT, countKRS_1GGT		
		
args.KRS_1GGC = 'TATGAAATTGGTGGCGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1GGC		
countKRS_1GGC = 0		
		
bfKRS_1GGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1GGC:		
	if args.KRS_1GGC in line.seq:	
		countKRS_1GGC += 1
		
print 'KRS_1GGC' , args.KRS_1GGC, countKRS_1GGC		
		
args.KRS_1GGA = 'TATGAAATTGGTGGAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1GGA		
countKRS_1GGA = 0		
		
bfKRS_1GGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1GGA:		
	if args.KRS_1GGA in line.seq:	
		countKRS_1GGA += 1
		
print 'KRS_1GGA' , args.KRS_1GGA, countKRS_1GGA		
		
args.KRS_1GGG = 'TATGAAATTGGTGGGGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS_1GGG		
countKRS_1GGG = 0		
		
bfKRS_1GGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS_1GGG:		
	if args.KRS_1GGG in line.seq:	
		countKRS_1GGG += 1
		
print 'KRS_1GGG' , args.KRS_1GGG, countKRS_1GGG	

args.KRS21TTT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTTTTGGGCATATGCT' #sequence KRS21TTT		
countKRS21TTT = 0		
		
bfKRS21TTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21TTT:		
	if args.KRS21TTT in line.seq:	
		countKRS21TTT += 1
		
print 'KRS21TTT' , args.KRS21TTT, countKRS21TTT		
		
args.KRS21TTC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTTCTGGGCATATGCT' #sequence KRS21TTC		
countKRS21TTC = 0		
		
bfKRS21TTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21TTC:		
	if args.KRS21TTC in line.seq:	
		countKRS21TTC += 1
		
print 'KRS21TTC' , args.KRS21TTC, countKRS21TTC		
		
args.KRS21TTA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTTATGGGCATATGCT' #sequence KRS21TTA		
countKRS21TTA = 0		
		
bfKRS21TTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21TTA:		
	if args.KRS21TTA in line.seq:	
		countKRS21TTA += 1
		
print 'KRS21TTA' , args.KRS21TTA, countKRS21TTA		
		
args.KRS21TTG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTTGTGGGCATATGCT' #sequence KRS21TTG		
countKRS21TTG = 0		
		
bfKRS21TTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21TTG:		
	if args.KRS21TTG in line.seq:	
		countKRS21TTG += 1
		
print 'KRS21TTG' , args.KRS21TTG, countKRS21TTG		
		
args.KRS21CTT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTCTTTGGGCATATGCT' #sequence KRS21CTT		
countKRS21CTT = 0		
		
bfKRS21CTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21CTT:		
	if args.KRS21CTT in line.seq:	
		countKRS21CTT += 1
		
print 'KRS21CTT' , args.KRS21CTT, countKRS21CTT		
		
args.KRS21CTC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTCTCTGGGCATATGCT' #sequence KRS21CTC		
countKRS21CTC = 0		
		
bfKRS21CTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21CTC:		
	if args.KRS21CTC in line.seq:	
		countKRS21CTC += 1
		
print 'KRS21CTC' , args.KRS21CTC, countKRS21CTC		
		
args.KRS21CTA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTCTATGGGCATATGCT' #sequence KRS21CTA		
countKRS21CTA = 0		
		
bfKRS21CTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21CTA:		
	if args.KRS21CTA in line.seq:	
		countKRS21CTA += 1
		
print 'KRS21CTA' , args.KRS21CTA, countKRS21CTA		
		
args.KRS21CTG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTCTGTGGGCATATGCT' #sequence KRS21CTG		
countKRS21CTG = 0		
		
bfKRS21CTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21CTG:		
	if args.KRS21CTG in line.seq:	
		countKRS21CTG += 1
		
print 'KRS21CTG' , args.KRS21CTG, countKRS21CTG		
		
args.KRS21ATT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTATTTGGGCATATGCT' #sequence KRS21ATT		
countKRS21ATT = 0		
		
bfKRS21ATT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21ATT:		
	if args.KRS21ATT in line.seq:	
		countKRS21ATT += 1
		
print 'KRS21ATT' , args.KRS21ATT, countKRS21ATT		
		
args.KRS21ATC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTATCTGGGCATATGCT' #sequence KRS21ATC		
countKRS21ATC = 0		
		
bfKRS21ATC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21ATC:		
	if args.KRS21ATC in line.seq:	
		countKRS21ATC += 1
		
print 'KRS21ATC' , args.KRS21ATC, countKRS21ATC		
		
args.KRS21ATA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTATATGGGCATATGCT' #sequence KRS21ATA		
countKRS21ATA = 0		
		
bfKRS21ATA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21ATA:		
	if args.KRS21ATA in line.seq:	
		countKRS21ATA += 1
		
print 'KRS21ATA' , args.KRS21ATA, countKRS21ATA		
		
args.KRS21ATG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTATGTGGGCATATGCT' #sequence KRS21ATG		
countKRS21ATG = 0		
		
bfKRS21ATG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21ATG:		
	if args.KRS21ATG in line.seq:	
		countKRS21ATG += 1
		
print 'KRS21ATG' , args.KRS21ATG, countKRS21ATG		
		
args.KRS21GTT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTGTTTGGGCATATGCT' #sequence KRS21GTT		
countKRS21GTT = 0		
		
bfKRS21GTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21GTT:		
	if args.KRS21GTT in line.seq:	
		countKRS21GTT += 1
		
print 'KRS21GTT' , args.KRS21GTT, countKRS21GTT		
		
args.KRS21GTC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTGTCTGGGCATATGCT' #sequence KRS21GTC		
countKRS21GTC = 0		
		
bfKRS21GTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21GTC:		
	if args.KRS21GTC in line.seq:	
		countKRS21GTC += 1
		
print 'KRS21GTC' , args.KRS21GTC, countKRS21GTC		
		
args.KRS21GTA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTGTATGGGCATATGCT' #sequence KRS21GTA		
countKRS21GTA = 0		
		
bfKRS21GTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21GTA:		
	if args.KRS21GTA in line.seq:	
		countKRS21GTA += 1
		
print 'KRS21GTA' , args.KRS21GTA, countKRS21GTA		
		
args.KRS21GTG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTGTGTGGGCATATGCT' #sequence KRS21GTG

countKRS21GTG = 0
		
bfKRS21GTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21GTG:		
	if args.KRS21GTG in line.seq:	
		countKRS21GTG += 1
		
print 'KRS21GTG' , args.KRS21GTG, countKRS21GTG		
		
args.KRS21TCT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTCTTGGGCATATGCT' #sequence KRS21TCT		
countKRS21TCT = 0		
		
bfKRS21TCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21TCT:		
	if args.KRS21TCT in line.seq:	
		countKRS21TCT += 1
		
print 'KRS21TCT' , args.KRS21TCT, countKRS21TCT		
		
args.KRS21TCC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTCCTGGGCATATGCT' #sequence KRS21TCC		
countKRS21TCC = 0		
		
bfKRS21TCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21TCC:		
	if args.KRS21TCC in line.seq:	
		countKRS21TCC += 1
		
print 'KRS21TCC' , args.KRS21TCC, countKRS21TCC		
		
args.KRS21TCA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTCATGGGCATATGCT' #sequence KRS21TCA		
countKRS21TCA = 0		
		
bfKRS21TCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21TCA:		
	if args.KRS21TCA in line.seq:	
		countKRS21TCA += 1
		
print 'KRS21TCA' , args.KRS21TCA, countKRS21TCA		
		
args.KRS21TCG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTCGTGGGCATATGCT' #sequence KRS21TCG		
countKRS21TCG = 0		
		
bfKRS21TCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21TCG:		
	if args.KRS21TCG in line.seq:	
		countKRS21TCG += 1
		
print 'KRS21TCG' , args.KRS21TCG, countKRS21TCG		
		
args.KRS21CCT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTCCTTGGGCATATGCT' #sequence KRS21CCT		
countKRS21CCT = 0		
		
bfKRS21CCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21CCT:		
	if args.KRS21CCT in line.seq:	
		countKRS21CCT += 1
		
print 'KRS21CCT' , args.KRS21CCT, countKRS21CCT		
		
args.KRS21CCC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTCCCTGGGCATATGCT' #sequence KRS21CCC		
countKRS21CCC = 0		
		
bfKRS21CCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21CCC:		
	if args.KRS21CCC in line.seq:	
		countKRS21CCC += 1
		
print 'KRS21CCC' , args.KRS21CCC, countKRS21CCC		
		
args.KRS21CCA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTCCATGGGCATATGCT' #sequence KRS21CCA		
countKRS21CCA = 0		
		
bfKRS21CCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21CCA:		
	if args.KRS21CCA in line.seq:	
		countKRS21CCA += 1
		
print 'KRS21CCA' , args.KRS21CCA, countKRS21CCA		
		
args.KRS21CCG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTCCGTGGGCATATGCT' #sequence KRS21CCG		
countKRS21CCG = 0		
		
bfKRS21CCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21CCG:		
	if args.KRS21CCG in line.seq:	
		countKRS21CCG += 1
		
print 'KRS21CCG' , args.KRS21CCG, countKRS21CCG		
		
args.KRS21ACT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTACTTGGGCATATGCT' #sequence KRS21ACT		
countKRS21ACT = 0		
		
bfKRS21ACT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21ACT:		
	if args.KRS21ACT in line.seq:	
		countKRS21ACT += 1
		
print 'KRS21ACT' , args.KRS21ACT, countKRS21ACT		
		
args.KRS21ACC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTACCTGGGCATATGCT' #sequence KRS21ACC		
countKRS21ACC = 0		
		
bfKRS21ACC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21ACC:		
	if args.KRS21ACC in line.seq:	
		countKRS21ACC += 1
		
print 'KRS21ACC' , args.KRS21ACC, countKRS21ACC		
		
args.KRS21ACA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTACATGGGCATATGCT' #sequence KRS21ACA		
countKRS21ACA = 0		
		
bfKRS21ACA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21ACA:		
	if args.KRS21ACA in line.seq:	
		countKRS21ACA += 1
		
print 'KRS21ACA' , args.KRS21ACA, countKRS21ACA		
		
args.KRS21ACG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTACGTGGGCATATGCT' #sequence KRS21ACG		
countKRS21ACG = 0		
		
bfKRS21ACG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21ACG:		
	if args.KRS21ACG in line.seq:	
		countKRS21ACG += 1
		
print 'KRS21ACG' , args.KRS21ACG, countKRS21ACG		
		
args.KRS21GCT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTGCTTGGGCATATGCT' #sequence KRS21GCT		
countKRS21GCT = 0		
		
bfKRS21GCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21GCT:		
	if args.KRS21GCT in line.seq:	
		countKRS21GCT += 1
		
print 'KRS21GCT' , args.KRS21GCT, countKRS21GCT		
		
args.KRS21GCC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTGCCTGGGCATATGCT' #sequence KRS21GCC		
countKRS21GCC = 0		
		
bfKRS21GCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21GCC:		
	if args.KRS21GCC in line.seq:	
		countKRS21GCC += 1
		
print 'KRS21GCC' , args.KRS21GCC, countKRS21GCC		
		
args.KRS21GCA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTGCATGGGCATATGCT' #sequence KRS21GCA		
countKRS21GCA = 0		
		
bfKRS21GCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21GCA:		
	if args.KRS21GCA in line.seq:	
		countKRS21GCA += 1
		
print 'KRS21GCA' , args.KRS21GCA, countKRS21GCA		
		
args.KRS21GCG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTGCGTGGGCATATGCT' #sequence KRS21GCG		
countKRS21GCG = 0		
		
bfKRS21GCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21GCG:		
	if args.KRS21GCG in line.seq:	
		countKRS21GCG += 1
		
print 'KRS21GCG' , args.KRS21GCG, countKRS21GCG		
		
args.KRS21TAT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS21TAT		
countKRS21TAT = 0		
		
bfKRS21TAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21TAT:		
	if args.KRS21TAT in line.seq:	
		countKRS21TAT += 1
		
print 'KRS21TAT' , args.KRS21TAT, countKRS21TAT		
		
args.KRS21TAC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTACTGGGCATATGCT' #sequence KRS21TAC		
countKRS21TAC = 0		
		
bfKRS21TAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21TAC:		
	if args.KRS21TAC in line.seq:	
		countKRS21TAC += 1
		
print 'KRS21TAC' , args.KRS21TAC, countKRS21TAC		
		
args.KRS21TAA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTAATGGGCATATGCT' #sequence KRS21TAA		
countKRS21TAA = 0		
		
bfKRS21TAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21TAA:		
	if args.KRS21TAA in line.seq:	
		countKRS21TAA += 1
		
print 'KRS21TAA' , args.KRS21TAA, countKRS21TAA		
		
args.KRS21TAG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTAGTGGGCATATGCT' #sequence KRS21TAG		
countKRS21TAG = 0		
		
bfKRS21TAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21TAG:		
	if args.KRS21TAG in line.seq:	
		countKRS21TAG += 1
		
print 'KRS21TAG' , args.KRS21TAG, countKRS21TAG		
		
args.KRS21CAT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTCATTGGGCATATGCT' #sequence KRS21CAT		
countKRS21CAT = 0		
		
bfKRS21CAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21CAT:		
	if args.KRS21CAT in line.seq:	
		countKRS21CAT += 1
		
print 'KRS21CAT' , args.KRS21CAT, countKRS21CAT		
		
args.KRS21CAC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTCACTGGGCATATGCT' #sequence KRS21CAC		
countKRS21CAC = 0		
		
bfKRS21CAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21CAC:		
	if args.KRS21CAC in line.seq:	
		countKRS21CAC += 1
		
print 'KRS21CAC' , args.KRS21CAC, countKRS21CAC		
		
args.KRS21CAA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTCAATGGGCATATGCT' #sequence KRS21CAA		
countKRS21CAA = 0		
		
bfKRS21CAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21CAA:		
	if args.KRS21CAA in line.seq:	
		countKRS21CAA += 1
		
print 'KRS21CAA' , args.KRS21CAA, countKRS21CAA		
		
args.KRS21CAG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTCAGTGGGCATATGCT' #sequence KRS21CAG		
countKRS21CAG = 0		
		
bfKRS21CAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21CAG:		
	if args.KRS21CAG in line.seq:	
		countKRS21CAG += 1
		
print 'KRS21CAG' , args.KRS21CAG, countKRS21CAG		
		
args.KRS21AAT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTAATTGGGCATATGCT' #sequence KRS21AAT		
countKRS21AAT = 0		
		
bfKRS21AAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21AAT:		
	if args.KRS21AAT in line.seq:	
		countKRS21AAT += 1
		
print 'KRS21AAT' , args.KRS21AAT, countKRS21AAT		
		
args.KRS21AAC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTAACTGGGCATATGCT' #sequence KRS21AAC		
countKRS21AAC = 0		
		
bfKRS21AAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21AAC:		
	if args.KRS21AAC in line.seq:	
		countKRS21AAC += 1
		
print 'KRS21AAC' , args.KRS21AAC, countKRS21AAC		
		
args.KRS21AAA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTAAATGGGCATATGCT' #sequence KRS21AAA		
countKRS21AAA = 0		
		
bfKRS21AAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21AAA:		
	if args.KRS21AAA in line.seq:	
		countKRS21AAA += 1
		
print 'KRS21AAA' , args.KRS21AAA, countKRS21AAA		
		
args.KRS21AAG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTAAGTGGGCATATGCT' #sequence KRS21AAG		
countKRS21AAG = 0		
		
bfKRS21AAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21AAG:		
	if args.KRS21AAG in line.seq:	
		countKRS21AAG += 1
		
print 'KRS21AAG' , args.KRS21AAG, countKRS21AAG		
		
args.KRS21GAT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTGATTGGGCATATGCT' #sequence KRS21GAT		
countKRS21GAT = 0		
		
bfKRS21GAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21GAT:		
	if args.KRS21GAT in line.seq:	
		countKRS21GAT += 1
		
print 'KRS21GAT' , args.KRS21GAT, countKRS21GAT		
		
args.KRS21GAC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTGACTGGGCATATGCT' #sequence KRS21GAC		
countKRS21GAC = 0		
		
bfKRS21GAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21GAC:		
	if args.KRS21GAC in line.seq:	
		countKRS21GAC += 1
		
print 'KRS21GAC' , args.KRS21GAC, countKRS21GAC		
		
args.KRS21GAA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTGAATGGGCATATGCT' #sequence KRS21GAA		
countKRS21GAA = 0		
		
bfKRS21GAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21GAA:		
	if args.KRS21GAA in line.seq:	
		countKRS21GAA += 1
		
print 'KRS21GAA' , args.KRS21GAA, countKRS21GAA		
		
args.KRS21GAG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTGAGTGGGCATATGCT' #sequence KRS21GAG		
countKRS21GAG = 0		
		
bfKRS21GAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21GAG:		
	if args.KRS21GAG in line.seq:	
		countKRS21GAG += 1
		
print 'KRS21GAG' , args.KRS21GAG, countKRS21GAG		
		
args.KRS21TGT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTGTTGGGCATATGCT' #sequence KRS21TGT		
countKRS21TGT = 0		
		
bfKRS21TGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21TGT:		
	if args.KRS21TGT in line.seq:	
		countKRS21TGT += 1
		
print 'KRS21TGT' , args.KRS21TGT, countKRS21TGT		
		
args.KRS21TGC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTGCTGGGCATATGCT' #sequence KRS21TGC		
countKRS21TGC = 0		
		
bfKRS21TGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21TGC:		
	if args.KRS21TGC in line.seq:	
		countKRS21TGC += 1
		
print 'KRS21TGC' , args.KRS21TGC, countKRS21TGC		
		
args.KRS21TGA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTGATGGGCATATGCT' #sequence KRS21TGA		
countKRS21TGA = 0		
		
bfKRS21TGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21TGA:		
	if args.KRS21TGA in line.seq:	
		countKRS21TGA += 1
		
print 'KRS21TGA' , args.KRS21TGA, countKRS21TGA		
		
args.KRS21TGG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTGGTGGGCATATGCT' #sequence KRS21TGG		
countKRS21TGG = 0		
		
bfKRS21TGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21TGG:		
	if args.KRS21TGG in line.seq:	
		countKRS21TGG += 1
		
print 'KRS21TGG' , args.KRS21TGG, countKRS21TGG		
		
args.KRS21CGT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTCGTTGGGCATATGCT' #sequence KRS21CGT		
countKRS21CGT = 0		
		
bfKRS21CGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21CGT:		
	if args.KRS21CGT in line.seq:	
		countKRS21CGT += 1
		
print 'KRS21CGT' , args.KRS21CGT, countKRS21CGT		
		
args.KRS21CGC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTCGCTGGGCATATGCT' #sequence KRS21CGC		
countKRS21CGC = 0		
		
bfKRS21CGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21CGC:		
	if args.KRS21CGC in line.seq:	
		countKRS21CGC += 1
		
print 'KRS21CGC' , args.KRS21CGC, countKRS21CGC		
		
args.KRS21CGA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTCGATGGGCATATGCT' #sequence KRS21CGA		
countKRS21CGA = 0		
		
bfKRS21CGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21CGA:		
	if args.KRS21CGA in line.seq:	
		countKRS21CGA += 1
		
print 'KRS21CGA' , args.KRS21CGA, countKRS21CGA		
		
args.KRS21CGG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTCGGTGGGCATATGCT' #sequence KRS21CGG		
countKRS21CGG = 0		
		
bfKRS21CGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21CGG:		
	if args.KRS21CGG in line.seq:	
		countKRS21CGG += 1
		
print 'KRS21CGG' , args.KRS21CGG, countKRS21CGG		
		
args.KRS21AGT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTAGTTGGGCATATGCT' #sequence KRS21AGT		
countKRS21AGT = 0		
		
bfKRS21AGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21AGT:		
	if args.KRS21AGT in line.seq:	
		countKRS21AGT += 1
		
print 'KRS21AGT' , args.KRS21AGT, countKRS21AGT		
		
args.KRS21AGC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTAGCTGGGCATATGCT' #sequence KRS21AGC		
countKRS21AGC = 0		
		
bfKRS21AGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21AGC:		
	if args.KRS21AGC in line.seq:	
		countKRS21AGC += 1
		
print 'KRS21AGC' , args.KRS21AGC, countKRS21AGC		
		
args.KRS21AGA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTAGATGGGCATATGCT' #sequence KRS21AGA		
countKRS21AGA = 0		
		
bfKRS21AGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21AGA:		
	if args.KRS21AGA in line.seq:	
		countKRS21AGA += 1
		
print 'KRS21AGA' , args.KRS21AGA, countKRS21AGA		
		
args.KRS21AGG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTAGGTGGGCATATGCT' #sequence KRS21AGG		
countKRS21AGG = 0		
		
bfKRS21AGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21AGG:		
	if args.KRS21AGG in line.seq:	
		countKRS21AGG += 1
		
print 'KRS21AGG' , args.KRS21AGG, countKRS21AGG		
		
args.KRS21GGT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTGGTTGGGCATATGCT' #sequence KRS21GGT		
countKRS21GGT = 0		
		
bfKRS21GGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21GGT:		
	if args.KRS21GGT in line.seq:	
		countKRS21GGT += 1
		
print 'KRS21GGT' , args.KRS21GGT, countKRS21GGT		
		
args.KRS21GGC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTGGCTGGGCATATGCT' #sequence KRS21GGC		
countKRS21GGC = 0		
		
bfKRS21GGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21GGC:		
	if args.KRS21GGC in line.seq:	
		countKRS21GGC += 1
		
print 'KRS21GGC' , args.KRS21GGC, countKRS21GGC		
		
args.KRS21GGA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTGGATGGGCATATGCT' #sequence KRS21GGA		
countKRS21GGA = 0		
		
bfKRS21GGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21GGA:		
	if args.KRS21GGA in line.seq:	
		countKRS21GGA += 1
		
print 'KRS21GGA' , args.KRS21GGA, countKRS21GGA		
		
args.KRS21GGG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTGGGTGGGCATATGCT' #sequence KRS21GGG		
countKRS21GGG = 0		
		
bfKRS21GGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS21GGG:		
	if args.KRS21GGG in line.seq:	
		countKRS21GGG += 1
		
print 'KRS21GGG' , args.KRS21GGG, countKRS21GGG		


bfKRSfull_length = pysam.Samfile(args.infile,"rb")		
		
countKRSfull_length = bfKRSfull_length.count('Pf3D7_13_v3', 232, 322)			
		
print 'KRSfull_length' , 'Full_length_count', countKRSfull_length



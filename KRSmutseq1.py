#Created on Wed Sept 1 13:32:16 2021 by Richard Wall

import pysam, argparse

parser = argparse.ArgumentParser(description='Counts sequences from P. knowlesi KRS mutation library')
parser.add_argument('-i',nargs='?',dest='infile',help='Input BAM file')

args = parser.parse_args()

args.KRS1TTT = 'TATGAAATTGGTAAATTTTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1TTT		
countKRS1TTT = 0		
		
bfKRS1TTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1TTT:		
	if args.KRS1TTT in line.seq:	
		countKRS1TTT += 1
		
print 'KRS1TTT' , args.KRS1TTT, countKRS1TTT		
		
args.KRS1TTC = 'TATGAAATTGGTAAATTCTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1TTC		
countKRS1TTC = 0		
		
bfKRS1TTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1TTC:		
	if args.KRS1TTC in line.seq:	
		countKRS1TTC += 1
		
print 'KRS1TTC' , args.KRS1TTC, countKRS1TTC		
		
args.KRS1TTA = 'TATGAAATTGGTAAATTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1TTA		
countKRS1TTA = 0		
		
bfKRS1TTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1TTA:		
	if args.KRS1TTA in line.seq:	
		countKRS1TTA += 1
		
print 'KRS1TTA' , args.KRS1TTA, countKRS1TTA		
		
args.KRS1TTG = 'TATGAAATTGGTAAATTGTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1TTG		
countKRS1TTG = 0		
		
bfKRS1TTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1TTG:		
	if args.KRS1TTG in line.seq:	
		countKRS1TTG += 1
		
print 'KRS1TTG' , args.KRS1TTG, countKRS1TTG		
		
args.KRS1CTT = 'TATGAAATTGGTAAACTTTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1CTT		
countKRS1CTT = 0		
		
bfKRS1CTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1CTT:		
	if args.KRS1CTT in line.seq:	
		countKRS1CTT += 1
		
print 'KRS1CTT' , args.KRS1CTT, countKRS1CTT		
		
args.KRS1CTC = 'TATGAAATTGGTAAACTCTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1CTC		
countKRS1CTC = 0		
		
bfKRS1CTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1CTC:		
	if args.KRS1CTC in line.seq:	
		countKRS1CTC += 1
		
print 'KRS1CTC' , args.KRS1CTC, countKRS1CTC		
		
args.KRS1CTA = 'TATGAAATTGGTAAACTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1CTA		
countKRS1CTA = 0		

		
bfKRS1CTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1CTA:		
	if args.KRS1CTA in line.seq:	
		countKRS1CTA += 1
		
print 'KRS1CTA' , args.KRS1CTA, countKRS1CTA		
		
args.KRS1CTG = 'TATGAAATTGGTAAACTGTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1CTG		
countKRS1CTG = 0		
		
bfKRS1CTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1CTG:		
	if args.KRS1CTG in line.seq:	
		countKRS1CTG += 1
		
print 'KRS1CTG' , args.KRS1CTG, countKRS1CTG		
		
args.KRS1ATT = 'TATGAAATTGGTAAAATTTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1ATT		
countKRS1ATT = 0		
		
bfKRS1ATT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1ATT:		
	if args.KRS1ATT in line.seq:	
		countKRS1ATT += 1
		
print 'KRS1ATT' , args.KRS1ATT, countKRS1ATT		
		
args.KRS1ATC = 'TATGAAATTGGTAAAATCTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1ATC		
countKRS1ATC = 0		
		
bfKRS1ATC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1ATC:		
	if args.KRS1ATC in line.seq:	
		countKRS1ATC += 1
		
print 'KRS1ATC' , args.KRS1ATC, countKRS1ATC		
		
args.KRS1ATA = 'TATGAAATTGGTAAAATATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1ATA		
countKRS1ATA = 0		
		
bfKRS1ATA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1ATA:		
	if args.KRS1ATA in line.seq:	
		countKRS1ATA += 1
		
print 'KRS1ATA' , args.KRS1ATA, countKRS1ATA		
		
args.KRS1ATG = 'TATGAAATTGGTAAAATGTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1ATG		
countKRS1ATG = 0		
		
bfKRS1ATG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1ATG:		
	if args.KRS1ATG in line.seq:	
		countKRS1ATG += 1
		
print 'KRS1ATG' , args.KRS1ATG, countKRS1ATG		
		
args.KRS1GTT = 'TATGAAATTGGTAAAGTTTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1GTT		
countKRS1GTT = 0		
		
bfKRS1GTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1GTT:		
	if args.KRS1GTT in line.seq:	
		countKRS1GTT += 1
		
print 'KRS1GTT' , args.KRS1GTT, countKRS1GTT		
		
args.KRS1GTC = 'TATGAAATTGGTAAAGTCTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1GTC		
countKRS1GTC = 0		
		
bfKRS1GTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1GTC:		
	if args.KRS1GTC in line.seq:	
		countKRS1GTC += 1
		
print 'KRS1GTC' , args.KRS1GTC, countKRS1GTC		
		
args.KRS1GTA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1GTA		
countKRS1GTA = 0		
		
bfKRS1GTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1GTA:		
	if args.KRS1GTA in line.seq:	
		countKRS1GTA += 1
		
print 'KRS1GTA' , args.KRS1GTA, countKRS1GTA		
		
args.KRS1GTG = 'TATGAAATTGGTAAAGTGTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1GTG	
countKRS1GTG = 0		
		
bfKRS1GTG = pysam.Samfile(args.infile,"rb")

for line in bfKRS1GTG:		
	if args.KRS1GTG in line.seq:	
		countKRS1GTG += 1
		
print 'KRS1GTG', args.KRS1GTG, countKRS1GTG
		
args.KRS1TCT = 'TATGAAATTGGTAAATCTTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1TCT		
countKRS1TCT = 0		
		
bfKRS1TCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1TCT:		
	if args.KRS1TCT in line.seq:	
		countKRS1TCT += 1
		
print 'KRS1TCT' , args.KRS1TCT, countKRS1TCT		
		
args.KRS1TCC = 'TATGAAATTGGTAAATCCTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1TCC		
countKRS1TCC = 0		
		
bfKRS1TCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1TCC:		
	if args.KRS1TCC in line.seq:	
		countKRS1TCC += 1
		
print 'KRS1TCC' , args.KRS1TCC, countKRS1TCC		
		
args.KRS1TCA = 'TATGAAATTGGTAAATCATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1TCA		
countKRS1TCA = 0		
		
bfKRS1TCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1TCA:		
	if args.KRS1TCA in line.seq:	
		countKRS1TCA += 1
		
print 'KRS1TCA' , args.KRS1TCA, countKRS1TCA		
		
args.KRS1TCG = 'TATGAAATTGGTAAATCGTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1TCG		
countKRS1TCG = 0		
		
bfKRS1TCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1TCG:		
	if args.KRS1TCG in line.seq:	
		countKRS1TCG += 1
		
print 'KRS1TCG' , args.KRS1TCG, countKRS1TCG		
		
args.KRS1CCT = 'TATGAAATTGGTAAACCTTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1CCT		
countKRS1CCT = 0		
		
bfKRS1CCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1CCT:		
	if args.KRS1CCT in line.seq:	
		countKRS1CCT += 1
		
print 'KRS1CCT' , args.KRS1CCT, countKRS1CCT		
		
args.KRS1CCC = 'TATGAAATTGGTAAACCCTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1CCC		
countKRS1CCC = 0		
		
bfKRS1CCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1CCC:		
	if args.KRS1CCC in line.seq:	
		countKRS1CCC += 1
		
print 'KRS1CCC' , args.KRS1CCC, countKRS1CCC		
		
args.KRS1CCA = 'TATGAAATTGGTAAACCATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1CCA		
countKRS1CCA = 0		
		
bfKRS1CCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1CCA:		
	if args.KRS1CCA in line.seq:	
		countKRS1CCA += 1
		
print 'KRS1CCA' , args.KRS1CCA, countKRS1CCA		
		
args.KRS1CCG = 'TATGAAATTGGTAAACCGTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1CCG		
countKRS1CCG = 0		
		
bfKRS1CCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1CCG:		
	if args.KRS1CCG in line.seq:	
		countKRS1CCG += 1
		
print 'KRS1CCG' , args.KRS1CCG, countKRS1CCG		
		
args.KRS1ACT = 'TATGAAATTGGTAAAACTTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1ACT		
countKRS1ACT = 0		
		
bfKRS1ACT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1ACT:		
	if args.KRS1ACT in line.seq:	
		countKRS1ACT += 1
		
print 'KRS1ACT' , args.KRS1ACT, countKRS1ACT		
		
args.KRS1ACC = 'TATGAAATTGGTAAAACCTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1ACC		
countKRS1ACC = 0		
		
bfKRS1ACC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1ACC:		
	if args.KRS1ACC in line.seq:	
		countKRS1ACC += 1
		
print 'KRS1ACC' , args.KRS1ACC, countKRS1ACC		
		
args.KRS1ACA = 'TATGAAATTGGTAAAACATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1ACA		
countKRS1ACA = 0		
		
bfKRS1ACA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1ACA:		
	if args.KRS1ACA in line.seq:	
		countKRS1ACA += 1
		
print 'KRS1ACA' , args.KRS1ACA, countKRS1ACA		
		
args.KRS1ACG = 'TATGAAATTGGTAAAACGTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1ACG		
countKRS1ACG = 0		
		
bfKRS1ACG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1ACG:		
	if args.KRS1ACG in line.seq:	
		countKRS1ACG += 1
		
print 'KRS1ACG' , args.KRS1ACG, countKRS1ACG		
		
args.KRS1GCT = 'TATGAAATTGGTAAAGCTTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1GCT		
countKRS1GCT = 0		
		
bfKRS1GCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1GCT:		
	if args.KRS1GCT in line.seq:	
		countKRS1GCT += 1
		
print 'KRS1GCT' , args.KRS1GCT, countKRS1GCT		
		
args.KRS1GCC = 'TATGAAATTGGTAAAGCCTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1GCC		
countKRS1GCC = 0		
		
bfKRS1GCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1GCC:		
	if args.KRS1GCC in line.seq:	
		countKRS1GCC += 1
		
print 'KRS1GCC' , args.KRS1GCC, countKRS1GCC		
		
args.KRS1GCA = 'TATGAAATTGGTAAAGCATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1GCA		
countKRS1GCA = 0		
		
bfKRS1GCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1GCA:		
	if args.KRS1GCA in line.seq:	
		countKRS1GCA += 1
		
print 'KRS1GCA' , args.KRS1GCA, countKRS1GCA		
		
args.KRS1GCG = 'TATGAAATTGGTAAAGCGTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1GCG		
countKRS1GCG = 0		
		
bfKRS1GCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1GCG:		
	if args.KRS1GCG in line.seq:	
		countKRS1GCG += 1
		
print 'KRS1GCG' , args.KRS1GCG, countKRS1GCG		
		
args.KRS1TAT = 'TATGAAATTGGTAAATATTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1TAT		
countKRS1TAT = 0		
		
bfKRS1TAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1TAT:		
	if args.KRS1TAT in line.seq:	
		countKRS1TAT += 1
		
print 'KRS1TAT' , args.KRS1TAT, countKRS1TAT		
		
args.KRS1TAC = 'TATGAAATTGGTAAATACTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1TAC		
countKRS1TAC = 0		
		
bfKRS1TAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1TAC:		
	if args.KRS1TAC in line.seq:	
		countKRS1TAC += 1
		
print 'KRS1TAC' , args.KRS1TAC, countKRS1TAC		
		
args.KRS1TAA = 'TATGAAATTGGTAAATAATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1TAA		
countKRS1TAA = 0		
		
bfKRS1TAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1TAA:		
	if args.KRS1TAA in line.seq:	
		countKRS1TAA += 1
		
print 'KRS1TAA' , args.KRS1TAA, countKRS1TAA		
		
args.KRS1TAG = 'TATGAAATTGGTAAATAGTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1TAG		
countKRS1TAG = 0		
		
bfKRS1TAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1TAG:		
	if args.KRS1TAG in line.seq:	
		countKRS1TAG += 1
		
print 'KRS1TAG' , args.KRS1TAG, countKRS1TAG		
		
args.KRS1CAT = 'TATGAAATTGGTAAACATTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1CAT		
countKRS1CAT = 0		
		
bfKRS1CAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1CAT:		
	if args.KRS1CAT in line.seq:	
		countKRS1CAT += 1
		
print 'KRS1CAT' , args.KRS1CAT, countKRS1CAT		
		
args.KRS1CAC = 'TATGAAATTGGTAAACACTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1CAC		
countKRS1CAC = 0		
		
bfKRS1CAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1CAC:		
	if args.KRS1CAC in line.seq:	
		countKRS1CAC += 1
		
print 'KRS1CAC' , args.KRS1CAC, countKRS1CAC		
		
args.KRS1CAA = 'TATGAAATTGGTAAACAATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1CAA		
countKRS1CAA = 0		
		
bfKRS1CAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1CAA:		
	if args.KRS1CAA in line.seq:	
		countKRS1CAA += 1
		
print 'KRS1CAA' , args.KRS1CAA, countKRS1CAA		
		
args.KRS1CAG = 'TATGAAATTGGTAAACAGTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1CAG		
countKRS1CAG = 0		
		
bfKRS1CAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1CAG:		
	if args.KRS1CAG in line.seq:	
		countKRS1CAG += 1
		
print 'KRS1CAG' , args.KRS1CAG, countKRS1CAG		
		
args.KRS1AAT = 'TATGAAATTGGTAAAAATTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1AAT		
countKRS1AAT = 0		
		
bfKRS1AAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1AAT:		
	if args.KRS1AAT in line.seq:	
		countKRS1AAT += 1
		
print 'KRS1AAT' , args.KRS1AAT, countKRS1AAT		
		
args.KRS1AAC = 'TATGAAATTGGTAAAAACTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1AAC		
countKRS1AAC = 0		
		
bfKRS1AAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1AAC:		
	if args.KRS1AAC in line.seq:	
		countKRS1AAC += 1
		
print 'KRS1AAC' , args.KRS1AAC, countKRS1AAC		
		
args.KRS1AAA = 'TATGAAATTGGTAAAAAATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1AAA		
countKRS1AAA = 0		
		
bfKRS1AAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1AAA:		
	if args.KRS1AAA in line.seq:	
		countKRS1AAA += 1
		
print 'KRS1AAA' , args.KRS1AAA, countKRS1AAA		
		
args.KRS1AAG = 'TATGAAATTGGTAAAAAGTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1AAG		
countKRS1AAG = 0		
		
bfKRS1AAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1AAG:		
	if args.KRS1AAG in line.seq:	
		countKRS1AAG += 1
		
print 'KRS1AAG' , args.KRS1AAG, countKRS1AAG		
		
args.KRS1GAT = 'TATGAAATTGGTAAAGATTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1GAT		
countKRS1GAT = 0		
		
bfKRS1GAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1GAT:		
	if args.KRS1GAT in line.seq:	
		countKRS1GAT += 1
		
print 'KRS1GAT' , args.KRS1GAT, countKRS1GAT		
		
args.KRS1GAC = 'TATGAAATTGGTAAAGACTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1GAC		
countKRS1GAC = 0		
		
bfKRS1GAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1GAC:		
	if args.KRS1GAC in line.seq:	
		countKRS1GAC += 1
		
print 'KRS1GAC' , args.KRS1GAC, countKRS1GAC		
		
args.KRS1GAA = 'TATGAAATTGGTAAAGAATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1GAA		
countKRS1GAA = 0		
		
bfKRS1GAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1GAA:		
	if args.KRS1GAA in line.seq:	
		countKRS1GAA += 1
		
print 'KRS1GAA' , args.KRS1GAA, countKRS1GAA		
		
args.KRS1GAG = 'TATGAAATTGGTAAAGAGTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1GAG		
countKRS1GAG = 0		
		
bfKRS1GAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1GAG:		
	if args.KRS1GAG in line.seq:	
		countKRS1GAG += 1
		
print 'KRS1GAG' , args.KRS1GAG, countKRS1GAG		
		
args.KRS1TGT = 'TATGAAATTGGTAAATGTTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1TGT		
countKRS1TGT = 0		
		
bfKRS1TGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1TGT:		
	if args.KRS1TGT in line.seq:	
		countKRS1TGT += 1
		
print 'KRS1TGT' , args.KRS1TGT, countKRS1TGT		
		
args.KRS1TGC = 'TATGAAATTGGTAAATGCTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1TGC		
countKRS1TGC = 0		
		
bfKRS1TGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1TGC:		
	if args.KRS1TGC in line.seq:	
		countKRS1TGC += 1
		
print 'KRS1TGC' , args.KRS1TGC, countKRS1TGC		
		
args.KRS1TGA = 'TATGAAATTGGTAAATGATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1TGA		
countKRS1TGA = 0		
		
bfKRS1TGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1TGA:		
	if args.KRS1TGA in line.seq:	
		countKRS1TGA += 1
		
print 'KRS1TGA' , args.KRS1TGA, countKRS1TGA		
		
args.KRS1TGG = 'TATGAAATTGGTAAATGGTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1TGG		
countKRS1TGG = 0		
		
bfKRS1TGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1TGG:		
	if args.KRS1TGG in line.seq:	
		countKRS1TGG += 1
		
print 'KRS1TGG' , args.KRS1TGG, countKRS1TGG		
		
args.KRS1CGT = 'TATGAAATTGGTAAACGTTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1CGT		
countKRS1CGT = 0		
		
bfKRS1CGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1CGT:		
	if args.KRS1CGT in line.seq:	
		countKRS1CGT += 1
		
print 'KRS1CGT' , args.KRS1CGT, countKRS1CGT		
		
args.KRS1CGC = 'TATGAAATTGGTAAACGCTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1CGC		
countKRS1CGC = 0		
		
bfKRS1CGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1CGC:		
	if args.KRS1CGC in line.seq:	
		countKRS1CGC += 1
		
print 'KRS1CGC' , args.KRS1CGC, countKRS1CGC		
		
args.KRS1CGA = 'TATGAAATTGGTAAACGATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1CGA		
countKRS1CGA = 0		
		
bfKRS1CGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1CGA:		
	if args.KRS1CGA in line.seq:	
		countKRS1CGA += 1
		
print 'KRS1CGA' , args.KRS1CGA, countKRS1CGA		
		
args.KRS1CGG = 'TATGAAATTGGTAAACGGTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1CGG		
countKRS1CGG = 0		
		
bfKRS1CGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1CGG:		
	if args.KRS1CGG in line.seq:	
		countKRS1CGG += 1
		
print 'KRS1CGG' , args.KRS1CGG, countKRS1CGG		
		
args.KRS1AGT = 'TATGAAATTGGTAAAAGTTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1AGT		
countKRS1AGT = 0		
		
bfKRS1AGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1AGT:		
	if args.KRS1AGT in line.seq:	
		countKRS1AGT += 1
		
print 'KRS1AGT' , args.KRS1AGT, countKRS1AGT		
		
args.KRS1AGC = 'TATGAAATTGGTAAAAGCTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1AGC		
countKRS1AGC = 0		
		
bfKRS1AGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1AGC:		
	if args.KRS1AGC in line.seq:	
		countKRS1AGC += 1
		
print 'KRS1AGC' , args.KRS1AGC, countKRS1AGC		
		
args.KRS1AGA = 'TATGAAATTGGTAAAAGATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1AGA		
countKRS1AGA = 0		
		
bfKRS1AGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1AGA:		
	if args.KRS1AGA in line.seq:	
		countKRS1AGA += 1
		
print 'KRS1AGA' , args.KRS1AGA, countKRS1AGA		
		
args.KRS1AGG = 'TATGAAATTGGTAAAAGGTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1AGG		
countKRS1AGG = 0		
		
bfKRS1AGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1AGG:		
	if args.KRS1AGG in line.seq:	
		countKRS1AGG += 1
		
print 'KRS1AGG' , args.KRS1AGG, countKRS1AGG		
		
args.KRS1GGT = 'TATGAAATTGGTAAAGGTTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1GGT		
countKRS1GGT = 0		
		
bfKRS1GGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1GGT:		
	if args.KRS1GGT in line.seq:	
		countKRS1GGT += 1
		
print 'KRS1GGT' , args.KRS1GGT, countKRS1GGT		
		
args.KRS1GGC = 'TATGAAATTGGTAAAGGCTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1GGC		
countKRS1GGC = 0		
		
bfKRS1GGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1GGC:		
	if args.KRS1GGC in line.seq:	
		countKRS1GGC += 1
		
print 'KRS1GGC' , args.KRS1GGC, countKRS1GGC		
		
args.KRS1GGA = 'TATGAAATTGGTAAAGGATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1GGA		
countKRS1GGA = 0		
		
bfKRS1GGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1GGA:		
	if args.KRS1GGA in line.seq:	
		countKRS1GGA += 1
		
print 'KRS1GGA' , args.KRS1GGA, countKRS1GGA		
		
args.KRS1GGG = 'TATGAAATTGGTAAAGGGTTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS1GGG		
countKRS1GGG = 0		
		
bfKRS1GGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS1GGG:		
	if args.KRS1GGG in line.seq:	
		countKRS1GGG += 1
		
print 'KRS1GGG' , args.KRS1GGG, countKRS1GGG		

args.KRS2TTT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2TTT		
countKRS2TTT = 0		
		
bfKRS2TTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2TTT:		
	if args.KRS2TTT in line.seq:	
		countKRS2TTT += 1
		
print 'KRS2TTT' , args.KRS2TTT, countKRS2TTT		
		
args.KRS2TTC = 'TATGAAATTGGTAAAGTATTCAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2TTC		
countKRS2TTC = 0		
		
bfKRS2TTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2TTC:		
	if args.KRS2TTC in line.seq:	
		countKRS2TTC += 1
		
print 'KRS2TTC' , args.KRS2TTC, countKRS2TTC		
		
args.KRS2TTA = 'TATGAAATTGGTAAAGTATTAAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2TTA		
countKRS2TTA = 0		
		
bfKRS2TTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2TTA:		
	if args.KRS2TTA in line.seq:	
		countKRS2TTA += 1
		
print 'KRS2TTA' , args.KRS2TTA, countKRS2TTA		
		
args.KRS2TTG = 'TATGAAATTGGTAAAGTATTGAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2TTG		
countKRS2TTG = 0		
		
bfKRS2TTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2TTG:		
	if args.KRS2TTG in line.seq:	
		countKRS2TTG += 1
		
print 'KRS2TTG' , args.KRS2TTG, countKRS2TTG		
		
args.KRS2CTT = 'TATGAAATTGGTAAAGTACTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2CTT		
countKRS2CTT = 0		
		
bfKRS2CTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2CTT:		
	if args.KRS2CTT in line.seq:	
		countKRS2CTT += 1
		
print 'KRS2CTT' , args.KRS2CTT, countKRS2CTT		
		
args.KRS2CTC = 'TATGAAATTGGTAAAGTACTCAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2CTC		
countKRS2CTC = 0		
		
bfKRS2CTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2CTC:		
	if args.KRS2CTC in line.seq:	
		countKRS2CTC += 1
		
print 'KRS2CTC' , args.KRS2CTC, countKRS2CTC		
		
args.KRS2CTA = 'TATGAAATTGGTAAAGTACTAAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2CTA		
countKRS2CTA = 0		
		
bfKRS2CTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2CTA:		
	if args.KRS2CTA in line.seq:	
		countKRS2CTA += 1
		
print 'KRS2CTA' , args.KRS2CTA, countKRS2CTA		
		
args.KRS2CTG = 'TATGAAATTGGTAAAGTACTGAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2CTG		
countKRS2CTG = 0		
		
bfKRS2CTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2CTG:		
	if args.KRS2CTG in line.seq:	
		countKRS2CTG += 1
		
print 'KRS2CTG' , args.KRS2CTG, countKRS2CTG		
		
args.KRS2ATT = 'TATGAAATTGGTAAAGTAATTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2ATT		
countKRS2ATT = 0		
		
bfKRS2ATT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2ATT:		
	if args.KRS2ATT in line.seq:	
		countKRS2ATT += 1
		
print 'KRS2ATT' , args.KRS2ATT, countKRS2ATT		
		
args.KRS2ATC = 'TATGAAATTGGTAAAGTAATCAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2ATC		
countKRS2ATC = 0		
		
bfKRS2ATC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2ATC:		
	if args.KRS2ATC in line.seq:	
		countKRS2ATC += 1
		
print 'KRS2ATC' , args.KRS2ATC, countKRS2ATC		
		
args.KRS2ATA = 'TATGAAATTGGTAAAGTAATAAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2ATA		
countKRS2ATA = 0		
		
bfKRS2ATA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2ATA:		
	if args.KRS2ATA in line.seq:	
		countKRS2ATA += 1
		
print 'KRS2ATA' , args.KRS2ATA, countKRS2ATA		
		
args.KRS2ATG = 'TATGAAATTGGTAAAGTAATGAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2ATG		
countKRS2ATG = 0		
		
bfKRS2ATG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2ATG:		
	if args.KRS2ATG in line.seq:	
		countKRS2ATG += 1
		
print 'KRS2ATG' , args.KRS2ATG, countKRS2ATG		
		
args.KRS2GTT = 'TATGAAATTGGTAAAGTAGTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2GTT		
countKRS2GTT = 0		
		
bfKRS2GTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2GTT:		
	if args.KRS2GTT in line.seq:	
		countKRS2GTT += 1
		
print 'KRS2GTT' , args.KRS2GTT, countKRS2GTT		
		
args.KRS2GTC = 'TATGAAATTGGTAAAGTAGTCAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2GTC		
countKRS2GTC = 0		
		
bfKRS2GTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2GTC:		
	if args.KRS2GTC in line.seq:	
		countKRS2GTC += 1
		
print 'KRS2GTC' , args.KRS2GTC, countKRS2GTC		
		
args.KRS2GTA = 'TATGAAATTGGTAAAGTAGTAAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2GTA		
countKRS2GTA = 0		
		
bfKRS2GTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2GTA:		
	if args.KRS2GTA in line.seq:	
		countKRS2GTA += 1
		
print 'KRS2GTA' , args.KRS2GTA, countKRS2GTA		
		
args.KRS2GTG = 'TATGAAATTGGTAAAGTAGTGAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2GTG

countKRS2GTG = 0		
		
bfKRS2GTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2GTG:		
	if args.KRS2GTG in line.seq:	
		countKRS2GTG += 1
		
print 'KRS2GTG' , args.KRS2GTG, countKRS2GTG		
		
args.KRS2TCT = 'TATGAAATTGGTAAAGTATCTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2TCT		
countKRS2TCT = 0		
		
bfKRS2TCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2TCT:		
	if args.KRS2TCT in line.seq:	
		countKRS2TCT += 1
		
print 'KRS2TCT' , args.KRS2TCT, countKRS2TCT		
		
args.KRS2TCC = 'TATGAAATTGGTAAAGTATCCAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2TCC		
countKRS2TCC = 0		
		
bfKRS2TCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2TCC:		
	if args.KRS2TCC in line.seq:	
		countKRS2TCC += 1
		
print 'KRS2TCC' , args.KRS2TCC, countKRS2TCC		
		
args.KRS2TCA = 'TATGAAATTGGTAAAGTATCAAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2TCA		
countKRS2TCA = 0		
		
bfKRS2TCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2TCA:		
	if args.KRS2TCA in line.seq:	
		countKRS2TCA += 1
		
print 'KRS2TCA' , args.KRS2TCA, countKRS2TCA		
		
args.KRS2TCG = 'TATGAAATTGGTAAAGTATCGAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2TCG		
countKRS2TCG = 0		
		
bfKRS2TCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2TCG:		
	if args.KRS2TCG in line.seq:	
		countKRS2TCG += 1
		
print 'KRS2TCG' , args.KRS2TCG, countKRS2TCG		
		
args.KRS2CCT = 'TATGAAATTGGTAAAGTACCTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2CCT		
countKRS2CCT = 0		
		
bfKRS2CCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2CCT:		
	if args.KRS2CCT in line.seq:	
		countKRS2CCT += 1
		
print 'KRS2CCT' , args.KRS2CCT, countKRS2CCT		
		
args.KRS2CCC = 'TATGAAATTGGTAAAGTACCCAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2CCC		
countKRS2CCC = 0		
		
bfKRS2CCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2CCC:		
	if args.KRS2CCC in line.seq:	
		countKRS2CCC += 1
		
print 'KRS2CCC' , args.KRS2CCC, countKRS2CCC		
		
args.KRS2CCA = 'TATGAAATTGGTAAAGTACCAAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2CCA		
countKRS2CCA = 0		
		
bfKRS2CCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2CCA:		
	if args.KRS2CCA in line.seq:	
		countKRS2CCA += 1
		
print 'KRS2CCA' , args.KRS2CCA, countKRS2CCA		
		
args.KRS2CCG = 'TATGAAATTGGTAAAGTACCGAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2CCG		
countKRS2CCG = 0		
		
bfKRS2CCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2CCG:		
	if args.KRS2CCG in line.seq:	
		countKRS2CCG += 1
		
print 'KRS2CCG' , args.KRS2CCG, countKRS2CCG		
		
args.KRS2ACT = 'TATGAAATTGGTAAAGTAACTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2ACT		
countKRS2ACT = 0		
		
bfKRS2ACT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2ACT:		
	if args.KRS2ACT in line.seq:	
		countKRS2ACT += 1
		
print 'KRS2ACT' , args.KRS2ACT, countKRS2ACT		
		
args.KRS2ACC = 'TATGAAATTGGTAAAGTAACCAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2ACC		
countKRS2ACC = 0		
		
bfKRS2ACC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2ACC:		
	if args.KRS2ACC in line.seq:	
		countKRS2ACC += 1
		
print 'KRS2ACC' , args.KRS2ACC, countKRS2ACC		
		
args.KRS2ACA = 'TATGAAATTGGTAAAGTAACAAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2ACA		
countKRS2ACA = 0		
		
bfKRS2ACA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2ACA:		
	if args.KRS2ACA in line.seq:	
		countKRS2ACA += 1
		
print 'KRS2ACA' , args.KRS2ACA, countKRS2ACA		
		
args.KRS2ACG = 'TATGAAATTGGTAAAGTAACGAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2ACG		
countKRS2ACG = 0		
		
bfKRS2ACG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2ACG:		
	if args.KRS2ACG in line.seq:	
		countKRS2ACG += 1
		
print 'KRS2ACG' , args.KRS2ACG, countKRS2ACG		
		
args.KRS2GCT = 'TATGAAATTGGTAAAGTAGCTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2GCT		
countKRS2GCT = 0		
		
bfKRS2GCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2GCT:		
	if args.KRS2GCT in line.seq:	
		countKRS2GCT += 1
		
print 'KRS2GCT' , args.KRS2GCT, countKRS2GCT		
		
args.KRS2GCC = 'TATGAAATTGGTAAAGTAGCCAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2GCC		
countKRS2GCC = 0		
		
bfKRS2GCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2GCC:		
	if args.KRS2GCC in line.seq:	
		countKRS2GCC += 1
		
print 'KRS2GCC' , args.KRS2GCC, countKRS2GCC		
		
args.KRS2GCA = 'TATGAAATTGGTAAAGTAGCAAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2GCA		
countKRS2GCA = 0		
		
bfKRS2GCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2GCA:		
	if args.KRS2GCA in line.seq:	
		countKRS2GCA += 1
		
print 'KRS2GCA' , args.KRS2GCA, countKRS2GCA		
		
args.KRS2GCG = 'TATGAAATTGGTAAAGTAGCGAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2GCG		
countKRS2GCG = 0		
		
bfKRS2GCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2GCG:		
	if args.KRS2GCG in line.seq:	
		countKRS2GCG += 1
		
print 'KRS2GCG' , args.KRS2GCG, countKRS2GCG		
		
args.KRS2TAT = 'TATGAAATTGGTAAAGTATATAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2TAT		
countKRS2TAT = 0		
		
bfKRS2TAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2TAT:		
	if args.KRS2TAT in line.seq:	
		countKRS2TAT += 1
		
print 'KRS2TAT' , args.KRS2TAT, countKRS2TAT		
		
args.KRS2TAC = 'TATGAAATTGGTAAAGTATACAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2TAC		
countKRS2TAC = 0		
		
bfKRS2TAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2TAC:		
	if args.KRS2TAC in line.seq:	
		countKRS2TAC += 1
		
print 'KRS2TAC' , args.KRS2TAC, countKRS2TAC		
		
args.KRS2TAA = 'TATGAAATTGGTAAAGTATAAAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2TAA		
countKRS2TAA = 0		
		
bfKRS2TAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2TAA:		
	if args.KRS2TAA in line.seq:	
		countKRS2TAA += 1
		
print 'KRS2TAA' , args.KRS2TAA, countKRS2TAA		
		
args.KRS2TAG = 'TATGAAATTGGTAAAGTATAGAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2TAG		
countKRS2TAG = 0		
		
bfKRS2TAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2TAG:		
	if args.KRS2TAG in line.seq:	
		countKRS2TAG += 1
		
print 'KRS2TAG' , args.KRS2TAG, countKRS2TAG		
		
args.KRS2CAT = 'TATGAAATTGGTAAAGTACATAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2CAT		
countKRS2CAT = 0		
		
bfKRS2CAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2CAT:		
	if args.KRS2CAT in line.seq:	
		countKRS2CAT += 1
		
print 'KRS2CAT' , args.KRS2CAT, countKRS2CAT		
		
args.KRS2CAC = 'TATGAAATTGGTAAAGTACACAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2CAC		
countKRS2CAC = 0		
		
bfKRS2CAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2CAC:		
	if args.KRS2CAC in line.seq:	
		countKRS2CAC += 1
		
print 'KRS2CAC' , args.KRS2CAC, countKRS2CAC		
		
args.KRS2CAA = 'TATGAAATTGGTAAAGTACAAAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2CAA		
countKRS2CAA = 0		
		
bfKRS2CAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2CAA:		
	if args.KRS2CAA in line.seq:	
		countKRS2CAA += 1
		
print 'KRS2CAA' , args.KRS2CAA, countKRS2CAA		
		
args.KRS2CAG = 'TATGAAATTGGTAAAGTACAGAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2CAG		
countKRS2CAG = 0		
		
bfKRS2CAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2CAG:		
	if args.KRS2CAG in line.seq:	
		countKRS2CAG += 1
		
print 'KRS2CAG' , args.KRS2CAG, countKRS2CAG		
		
args.KRS2AAT = 'TATGAAATTGGTAAAGTAAATAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2AAT		
countKRS2AAT = 0		
		
bfKRS2AAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2AAT:		
	if args.KRS2AAT in line.seq:	
		countKRS2AAT += 1
		
print 'KRS2AAT' , args.KRS2AAT, countKRS2AAT		
		
args.KRS2AAC = 'TATGAAATTGGTAAAGTAAACAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2AAC		
countKRS2AAC = 0		
		
bfKRS2AAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2AAC:		
	if args.KRS2AAC in line.seq:	
		countKRS2AAC += 1
		
print 'KRS2AAC' , args.KRS2AAC, countKRS2AAC		
		
args.KRS2AAA = 'TATGAAATTGGTAAAGTAAAAAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2AAA		
countKRS2AAA = 0		
		
bfKRS2AAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2AAA:		
	if args.KRS2AAA in line.seq:	
		countKRS2AAA += 1
		
print 'KRS2AAA' , args.KRS2AAA, countKRS2AAA		
		
args.KRS2AAG = 'TATGAAATTGGTAAAGTAAAGAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2AAG		
countKRS2AAG = 0		
		
bfKRS2AAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2AAG:		
	if args.KRS2AAG in line.seq:	
		countKRS2AAG += 1
		
print 'KRS2AAG' , args.KRS2AAG, countKRS2AAG		
		
args.KRS2GAT = 'TATGAAATTGGTAAAGTAGATAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2GAT		
countKRS2GAT = 0		
		
bfKRS2GAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2GAT:		
	if args.KRS2GAT in line.seq:	
		countKRS2GAT += 1
		
print 'KRS2GAT' , args.KRS2GAT, countKRS2GAT		
		
args.KRS2GAC = 'TATGAAATTGGTAAAGTAGACAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2GAC		
countKRS2GAC = 0		
		
bfKRS2GAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2GAC:		
	if args.KRS2GAC in line.seq:	
		countKRS2GAC += 1
		
print 'KRS2GAC' , args.KRS2GAC, countKRS2GAC		
		
args.KRS2GAA = 'TATGAAATTGGTAAAGTAGAAAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2GAA		
countKRS2GAA = 0		
		
bfKRS2GAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2GAA:		
	if args.KRS2GAA in line.seq:	
		countKRS2GAA += 1
		
print 'KRS2GAA' , args.KRS2GAA, countKRS2GAA		
		
args.KRS2GAG = 'TATGAAATTGGTAAAGTAGAGAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2GAG		
countKRS2GAG = 0		
		
bfKRS2GAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2GAG:		
	if args.KRS2GAG in line.seq:	
		countKRS2GAG += 1
		
print 'KRS2GAG' , args.KRS2GAG, countKRS2GAG		
		
args.KRS2TGT = 'TATGAAATTGGTAAAGTATGTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2TGT		
countKRS2TGT = 0		
		
bfKRS2TGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2TGT:		
	if args.KRS2TGT in line.seq:	
		countKRS2TGT += 1
		
print 'KRS2TGT' , args.KRS2TGT, countKRS2TGT		
		
args.KRS2TGC = 'TATGAAATTGGTAAAGTATGCAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2TGC		
countKRS2TGC = 0		
		
bfKRS2TGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2TGC:		
	if args.KRS2TGC in line.seq:	
		countKRS2TGC += 1
		
print 'KRS2TGC' , args.KRS2TGC, countKRS2TGC		
		
args.KRS2TGA = 'TATGAAATTGGTAAAGTATGAAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2TGA		
countKRS2TGA = 0		
		
bfKRS2TGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2TGA:		
	if args.KRS2TGA in line.seq:	
		countKRS2TGA += 1
		
print 'KRS2TGA' , args.KRS2TGA, countKRS2TGA		
		
args.KRS2TGG = 'TATGAAATTGGTAAAGTATGGAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2TGG		
countKRS2TGG = 0		
		
bfKRS2TGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2TGG:		
	if args.KRS2TGG in line.seq:	
		countKRS2TGG += 1
		
print 'KRS2TGG' , args.KRS2TGG, countKRS2TGG		
		
args.KRS2CGT = 'TATGAAATTGGTAAAGTACGTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2CGT		
countKRS2CGT = 0		
		
bfKRS2CGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2CGT:		
	if args.KRS2CGT in line.seq:	
		countKRS2CGT += 1
		
print 'KRS2CGT' , args.KRS2CGT, countKRS2CGT		
		
args.KRS2CGC = 'TATGAAATTGGTAAAGTACGCAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2CGC		
countKRS2CGC = 0		
		
bfKRS2CGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2CGC:		
	if args.KRS2CGC in line.seq:	
		countKRS2CGC += 1
		
print 'KRS2CGC' , args.KRS2CGC, countKRS2CGC		
		
args.KRS2CGA = 'TATGAAATTGGTAAAGTACGAAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2CGA		
countKRS2CGA = 0		
		
bfKRS2CGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2CGA:		
	if args.KRS2CGA in line.seq:	
		countKRS2CGA += 1
		
print 'KRS2CGA' , args.KRS2CGA, countKRS2CGA		
		
args.KRS2CGG = 'TATGAAATTGGTAAAGTACGGAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2CGG		
countKRS2CGG = 0		
		
bfKRS2CGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2CGG:		
	if args.KRS2CGG in line.seq:	
		countKRS2CGG += 1
		
print 'KRS2CGG' , args.KRS2CGG, countKRS2CGG		
		
args.KRS2AGT = 'TATGAAATTGGTAAAGTAAGTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2AGT		
countKRS2AGT = 0		
		
bfKRS2AGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2AGT:		
	if args.KRS2AGT in line.seq:	
		countKRS2AGT += 1
		
print 'KRS2AGT' , args.KRS2AGT, countKRS2AGT		
		
args.KRS2AGC = 'TATGAAATTGGTAAAGTAAGCAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2AGC		
countKRS2AGC = 0		
		
bfKRS2AGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2AGC:		
	if args.KRS2AGC in line.seq:	
		countKRS2AGC += 1
		
print 'KRS2AGC' , args.KRS2AGC, countKRS2AGC		
		
args.KRS2AGA = 'TATGAAATTGGTAAAGTAAGAAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2AGA		
countKRS2AGA = 0		
		
bfKRS2AGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2AGA:		
	if args.KRS2AGA in line.seq:	
		countKRS2AGA += 1
		
print 'KRS2AGA' , args.KRS2AGA, countKRS2AGA		
		
args.KRS2AGG = 'TATGAAATTGGTAAAGTAAGGAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2AGG		
countKRS2AGG = 0		
		
bfKRS2AGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2AGG:		
	if args.KRS2AGG in line.seq:	
		countKRS2AGG += 1
		
print 'KRS2AGG' , args.KRS2AGG, countKRS2AGG		
		
args.KRS2GGT = 'TATGAAATTGGTAAAGTAGGTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2GGT		
countKRS2GGT = 0		
		
bfKRS2GGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2GGT:		
	if args.KRS2GGT in line.seq:	
		countKRS2GGT += 1
		
print 'KRS2GGT' , args.KRS2GGT, countKRS2GGT		
		
args.KRS2GGC = 'TATGAAATTGGTAAAGTAGGCAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2GGC		
countKRS2GGC = 0		
		
bfKRS2GGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2GGC:		
	if args.KRS2GGC in line.seq:	
		countKRS2GGC += 1
		
print 'KRS2GGC' , args.KRS2GGC, countKRS2GGC		
		
args.KRS2GGA = 'TATGAAATTGGTAAAGTAGGAAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2GGA		
countKRS2GGA = 0		
		
bfKRS2GGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2GGA:		
	if args.KRS2GGA in line.seq:	
		countKRS2GGA += 1
		
print 'KRS2GGA' , args.KRS2GGA, countKRS2GGA		
		
args.KRS2GGG = 'TATGAAATTGGTAAAGTAGGGAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS2GGG		
countKRS2GGG = 0		
		
bfKRS2GGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS2GGG:		
	if args.KRS2GGG in line.seq:	
		countKRS2GGG += 1
		
print 'KRS2GGG' , args.KRS2GGG, countKRS2GGG		



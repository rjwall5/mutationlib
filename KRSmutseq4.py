#Created on Wed Sept 1 13:32:16 2021 by Richard Wall

import pysam, argparse

parser = argparse.ArgumentParser(description='Counts sequences from P. knowlesi KRS mutation library')
parser.add_argument('-i',nargs='?',dest='infile',help='Input BAM file')

args = parser.parse_args()
	
args.KRS7TTT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTTTTGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7TTT		
countKRS7TTT = 0		
		
bfKRS7TTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7TTT:		
	if args.KRS7TTT in line.seq:	
		countKRS7TTT += 1
		
print 'KRS7TTT' , args.KRS7TTT, countKRS7TTT		
		
args.KRS7TTC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTTTCGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7TTC		
countKRS7TTC = 0		
		
bfKRS7TTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7TTC:		
	if args.KRS7TTC in line.seq:	
		countKRS7TTC += 1
		
print 'KRS7TTC' , args.KRS7TTC, countKRS7TTC		
		
args.KRS7TTA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTTTAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7TTA		
countKRS7TTA = 0		
		
bfKRS7TTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7TTA:		
	if args.KRS7TTA in line.seq:	
		countKRS7TTA += 1
		
print 'KRS7TTA' , args.KRS7TTA, countKRS7TTA		
		
args.KRS7TTG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTTTGGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7TTG		
countKRS7TTG = 0		
		
bfKRS7TTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7TTG:		
	if args.KRS7TTG in line.seq:	
		countKRS7TTG += 1
		
print 'KRS7TTG' , args.KRS7TTG, countKRS7TTG		
		
args.KRS7CTT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTCTTGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7CTT		
countKRS7CTT = 0		
		
bfKRS7CTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7CTT:		
	if args.KRS7CTT in line.seq:	
		countKRS7CTT += 1
		
print 'KRS7CTT' , args.KRS7CTT, countKRS7CTT		
		
args.KRS7CTC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTCTCGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7CTC		
countKRS7CTC = 0		
		
bfKRS7CTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7CTC:		
	if args.KRS7CTC in line.seq:	
		countKRS7CTC += 1
		
print 'KRS7CTC' , args.KRS7CTC, countKRS7CTC		
		
args.KRS7CTA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTCTAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7CTA		
countKRS7CTA = 0		
		
bfKRS7CTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7CTA:		
	if args.KRS7CTA in line.seq:	
		countKRS7CTA += 1
		
print 'KRS7CTA' , args.KRS7CTA, countKRS7CTA		
		
args.KRS7CTG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTCTGGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7CTG		
countKRS7CTG = 0		
		
bfKRS7CTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7CTG:		
	if args.KRS7CTG in line.seq:	
		countKRS7CTG += 1
		
print 'KRS7CTG' , args.KRS7CTG, countKRS7CTG		
		
args.KRS7ATT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATTGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7ATT		
countKRS7ATT = 0		
		
bfKRS7ATT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7ATT:		
	if args.KRS7ATT in line.seq:	
		countKRS7ATT += 1
		
print 'KRS7ATT' , args.KRS7ATT, countKRS7ATT		
		
args.KRS7ATC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATCGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7ATC		
countKRS7ATC = 0		
		
bfKRS7ATC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7ATC:		
	if args.KRS7ATC in line.seq:	
		countKRS7ATC += 1
		
print 'KRS7ATC' , args.KRS7ATC, countKRS7ATC		
		
args.KRS7ATA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7ATA		
countKRS7ATA = 0		
		
bfKRS7ATA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7ATA:		
	if args.KRS7ATA in line.seq:	
		countKRS7ATA += 1
		
print 'KRS7ATA' , args.KRS7ATA, countKRS7ATA		
		
args.KRS7ATG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATGGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7ATG		
countKRS7ATG = 0		
		
bfKRS7ATG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7ATG:		
	if args.KRS7ATG in line.seq:	
		countKRS7ATG += 1
		
print 'KRS7ATG' , args.KRS7ATG, countKRS7ATG		
		
args.KRS7GTT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTGTTGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7GTT		
countKRS7GTT = 0		
		
bfKRS7GTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7GTT:		
	if args.KRS7GTT in line.seq:	
		countKRS7GTT += 1
		
print 'KRS7GTT' , args.KRS7GTT, countKRS7GTT		
		
args.KRS7GTC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTGTCGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7GTC		
countKRS7GTC = 0		
		
bfKRS7GTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7GTC:		
	if args.KRS7GTC in line.seq:	
		countKRS7GTC += 1
		
print 'KRS7GTC' , args.KRS7GTC, countKRS7GTC		
		
args.KRS7GTA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTGTAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7GTA		
countKRS7GTA = 0		
		
bfKRS7GTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7GTA:		
	if args.KRS7GTA in line.seq:	
		countKRS7GTA += 1
		
print 'KRS7GTA' , args.KRS7GTA, countKRS7GTA		
		
args.KRS7GTG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTGTGGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7GTG

countKRS7GTG = 0
		
bfKRS7GTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7GTG:		
	if args.KRS7GTG in line.seq:	
		countKRS7GTG += 1
		
print 'KRS7GTG' , args.KRS7GTG, countKRS7GTG		
		
args.KRS7TCT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTTCTGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7TCT		
countKRS7TCT = 0		
		
bfKRS7TCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7TCT:		
	if args.KRS7TCT in line.seq:	
		countKRS7TCT += 1
		
print 'KRS7TCT' , args.KRS7TCT, countKRS7TCT		
		
args.KRS7TCC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTTCCGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7TCC		
countKRS7TCC = 0		
		
bfKRS7TCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7TCC:		
	if args.KRS7TCC in line.seq:	
		countKRS7TCC += 1
		
print 'KRS7TCC' , args.KRS7TCC, countKRS7TCC		
		
args.KRS7TCA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTTCAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7TCA		
countKRS7TCA = 0		
		
bfKRS7TCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7TCA:		
	if args.KRS7TCA in line.seq:	
		countKRS7TCA += 1
		
print 'KRS7TCA' , args.KRS7TCA, countKRS7TCA		
		
args.KRS7TCG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTTCGGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7TCG		
countKRS7TCG = 0		
		
bfKRS7TCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7TCG:		
	if args.KRS7TCG in line.seq:	
		countKRS7TCG += 1
		
print 'KRS7TCG' , args.KRS7TCG, countKRS7TCG		
		
args.KRS7CCT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTCCTGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7CCT		
countKRS7CCT = 0		
		
bfKRS7CCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7CCT:		
	if args.KRS7CCT in line.seq:	
		countKRS7CCT += 1
		
print 'KRS7CCT' , args.KRS7CCT, countKRS7CCT		
		
args.KRS7CCC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTCCCGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7CCC		
countKRS7CCC = 0		
		
bfKRS7CCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7CCC:		
	if args.KRS7CCC in line.seq:	
		countKRS7CCC += 1
		
print 'KRS7CCC' , args.KRS7CCC, countKRS7CCC		
		
args.KRS7CCA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTCCAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7CCA		
countKRS7CCA = 0		
		
bfKRS7CCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7CCA:		
	if args.KRS7CCA in line.seq:	
		countKRS7CCA += 1
		
print 'KRS7CCA' , args.KRS7CCA, countKRS7CCA		
		
args.KRS7CCG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTCCGGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7CCG		
countKRS7CCG = 0		
		
bfKRS7CCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7CCG:		
	if args.KRS7CCG in line.seq:	
		countKRS7CCG += 1
		
print 'KRS7CCG' , args.KRS7CCG, countKRS7CCG		
		
args.KRS7ACT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTACTGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7ACT		
countKRS7ACT = 0		
		
bfKRS7ACT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7ACT:		
	if args.KRS7ACT in line.seq:	
		countKRS7ACT += 1
		
print 'KRS7ACT' , args.KRS7ACT, countKRS7ACT		
		
args.KRS7ACC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTACCGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7ACC		
countKRS7ACC = 0		
		
bfKRS7ACC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7ACC:		
	if args.KRS7ACC in line.seq:	
		countKRS7ACC += 1
		
print 'KRS7ACC' , args.KRS7ACC, countKRS7ACC		
		
args.KRS7ACA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTACAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7ACA		
countKRS7ACA = 0		
		
bfKRS7ACA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7ACA:		
	if args.KRS7ACA in line.seq:	
		countKRS7ACA += 1
		
print 'KRS7ACA' , args.KRS7ACA, countKRS7ACA		
		
args.KRS7ACG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTACGGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7ACG		
countKRS7ACG = 0		
		
bfKRS7ACG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7ACG:		
	if args.KRS7ACG in line.seq:	
		countKRS7ACG += 1
		
print 'KRS7ACG' , args.KRS7ACG, countKRS7ACG		
		
args.KRS7GCT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTGCTGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7GCT		
countKRS7GCT = 0		
		
bfKRS7GCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7GCT:		
	if args.KRS7GCT in line.seq:	
		countKRS7GCT += 1
		
print 'KRS7GCT' , args.KRS7GCT, countKRS7GCT		
		
args.KRS7GCC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTGCCGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7GCC		
countKRS7GCC = 0		
		
bfKRS7GCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7GCC:		
	if args.KRS7GCC in line.seq:	
		countKRS7GCC += 1
		
print 'KRS7GCC' , args.KRS7GCC, countKRS7GCC		
		
args.KRS7GCA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTGCAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7GCA		
countKRS7GCA = 0		
		
bfKRS7GCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7GCA:		
	if args.KRS7GCA in line.seq:	
		countKRS7GCA += 1
		
print 'KRS7GCA' , args.KRS7GCA, countKRS7GCA		
		
args.KRS7GCG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTGCGGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7GCG		
countKRS7GCG = 0		
		
bfKRS7GCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7GCG:		
	if args.KRS7GCG in line.seq:	
		countKRS7GCG += 1
		
print 'KRS7GCG' , args.KRS7GCG, countKRS7GCG		
		
args.KRS7TAT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTTATGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7TAT		
countKRS7TAT = 0		
		
bfKRS7TAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7TAT:		
	if args.KRS7TAT in line.seq:	
		countKRS7TAT += 1
		
print 'KRS7TAT' , args.KRS7TAT, countKRS7TAT		
		
args.KRS7TAC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTTACGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7TAC		
countKRS7TAC = 0		
		
bfKRS7TAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7TAC:		
	if args.KRS7TAC in line.seq:	
		countKRS7TAC += 1
		
print 'KRS7TAC' , args.KRS7TAC, countKRS7TAC		
		
args.KRS7TAA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTTAAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7TAA		
countKRS7TAA = 0		
		
bfKRS7TAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7TAA:		
	if args.KRS7TAA in line.seq:	
		countKRS7TAA += 1
		
print 'KRS7TAA' , args.KRS7TAA, countKRS7TAA		
		
args.KRS7TAG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTTAGGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7TAG		
countKRS7TAG = 0		
		
bfKRS7TAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7TAG:		
	if args.KRS7TAG in line.seq:	
		countKRS7TAG += 1
		
print 'KRS7TAG' , args.KRS7TAG, countKRS7TAG		
		
args.KRS7CAT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTCATGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7CAT		
countKRS7CAT = 0		
		
bfKRS7CAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7CAT:		
	if args.KRS7CAT in line.seq:	
		countKRS7CAT += 1
		
print 'KRS7CAT' , args.KRS7CAT, countKRS7CAT		
		
args.KRS7CAC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTCACGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7CAC		
countKRS7CAC = 0		
		
bfKRS7CAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7CAC:		
	if args.KRS7CAC in line.seq:	
		countKRS7CAC += 1
		
print 'KRS7CAC' , args.KRS7CAC, countKRS7CAC		
		
args.KRS7CAA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTCAAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7CAA		
countKRS7CAA = 0		
		
bfKRS7CAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7CAA:		
	if args.KRS7CAA in line.seq:	
		countKRS7CAA += 1
		
print 'KRS7CAA' , args.KRS7CAA, countKRS7CAA		
		
args.KRS7CAG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTCAGGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7CAG		
countKRS7CAG = 0		
		
bfKRS7CAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7CAG:		
	if args.KRS7CAG in line.seq:	
		countKRS7CAG += 1
		
print 'KRS7CAG' , args.KRS7CAG, countKRS7CAG		
		
args.KRS7AAT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTAATGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7AAT		
countKRS7AAT = 0		
		
bfKRS7AAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7AAT:		
	if args.KRS7AAT in line.seq:	
		countKRS7AAT += 1
		
print 'KRS7AAT' , args.KRS7AAT, countKRS7AAT		
		
args.KRS7AAC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTAACGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7AAC		
countKRS7AAC = 0		
		
bfKRS7AAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7AAC:		
	if args.KRS7AAC in line.seq:	
		countKRS7AAC += 1
		
print 'KRS7AAC' , args.KRS7AAC, countKRS7AAC		
		
args.KRS7AAA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTAAAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7AAA		
countKRS7AAA = 0		
		
bfKRS7AAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7AAA:		
	if args.KRS7AAA in line.seq:	
		countKRS7AAA += 1
		
print 'KRS7AAA' , args.KRS7AAA, countKRS7AAA		
		
args.KRS7AAG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTAAGGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7AAG		
countKRS7AAG = 0		
		
bfKRS7AAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7AAG:		
	if args.KRS7AAG in line.seq:	
		countKRS7AAG += 1
		
print 'KRS7AAG' , args.KRS7AAG, countKRS7AAG		
		
args.KRS7GAT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTGATGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7GAT		
countKRS7GAT = 0		
		
bfKRS7GAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7GAT:		
	if args.KRS7GAT in line.seq:	
		countKRS7GAT += 1
		
print 'KRS7GAT' , args.KRS7GAT, countKRS7GAT		
		
args.KRS7GAC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTGACGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7GAC		
countKRS7GAC = 0		
		
bfKRS7GAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7GAC:		
	if args.KRS7GAC in line.seq:	
		countKRS7GAC += 1
		
print 'KRS7GAC' , args.KRS7GAC, countKRS7GAC		
		
args.KRS7GAA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTGAAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7GAA		
countKRS7GAA = 0		
		
bfKRS7GAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7GAA:		
	if args.KRS7GAA in line.seq:	
		countKRS7GAA += 1
		
print 'KRS7GAA' , args.KRS7GAA, countKRS7GAA		
		
args.KRS7GAG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTGAGGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7GAG		
countKRS7GAG = 0		
		
bfKRS7GAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7GAG:		
	if args.KRS7GAG in line.seq:	
		countKRS7GAG += 1
		
print 'KRS7GAG' , args.KRS7GAG, countKRS7GAG		
		
args.KRS7TGT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTTGTGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7TGT		
countKRS7TGT = 0		
		
bfKRS7TGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7TGT:		
	if args.KRS7TGT in line.seq:	
		countKRS7TGT += 1
		
print 'KRS7TGT' , args.KRS7TGT, countKRS7TGT		
		
args.KRS7TGC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTTGCGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7TGC		
countKRS7TGC = 0		
		
bfKRS7TGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7TGC:		
	if args.KRS7TGC in line.seq:	
		countKRS7TGC += 1
		
print 'KRS7TGC' , args.KRS7TGC, countKRS7TGC		
		
args.KRS7TGA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTTGAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7TGA		
countKRS7TGA = 0		
		
bfKRS7TGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7TGA:		
	if args.KRS7TGA in line.seq:	
		countKRS7TGA += 1
		
print 'KRS7TGA' , args.KRS7TGA, countKRS7TGA		
		
args.KRS7TGG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTTGGGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7TGG		
countKRS7TGG = 0		
		
bfKRS7TGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7TGG:		
	if args.KRS7TGG in line.seq:	
		countKRS7TGG += 1
		
print 'KRS7TGG' , args.KRS7TGG, countKRS7TGG		
		
args.KRS7CGT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTCGTGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7CGT		
countKRS7CGT = 0		
		
bfKRS7CGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7CGT:		
	if args.KRS7CGT in line.seq:	
		countKRS7CGT += 1
		
print 'KRS7CGT' , args.KRS7CGT, countKRS7CGT		
		
args.KRS7CGC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTCGCGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7CGC		
countKRS7CGC = 0		
		
bfKRS7CGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7CGC:		
	if args.KRS7CGC in line.seq:	
		countKRS7CGC += 1
		
print 'KRS7CGC' , args.KRS7CGC, countKRS7CGC		
		
args.KRS7CGA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTCGAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7CGA		
countKRS7CGA = 0		
		
bfKRS7CGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7CGA:		
	if args.KRS7CGA in line.seq:	
		countKRS7CGA += 1
		
print 'KRS7CGA' , args.KRS7CGA, countKRS7CGA		
		
args.KRS7CGG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTCGGGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7CGG		
countKRS7CGG = 0		
		
bfKRS7CGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7CGG:		
	if args.KRS7CGG in line.seq:	
		countKRS7CGG += 1
		
print 'KRS7CGG' , args.KRS7CGG, countKRS7CGG		
		
args.KRS7AGT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTAGTGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7AGT		
countKRS7AGT = 0		
		
bfKRS7AGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7AGT:		
	if args.KRS7AGT in line.seq:	
		countKRS7AGT += 1
		
print 'KRS7AGT' , args.KRS7AGT, countKRS7AGT		
		
args.KRS7AGC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTAGCGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7AGC		
countKRS7AGC = 0		
		
bfKRS7AGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7AGC:		
	if args.KRS7AGC in line.seq:	
		countKRS7AGC += 1
		
print 'KRS7AGC' , args.KRS7AGC, countKRS7AGC		
		
args.KRS7AGA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTAGAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7AGA		
countKRS7AGA = 0		
		
bfKRS7AGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7AGA:		
	if args.KRS7AGA in line.seq:	
		countKRS7AGA += 1
		
print 'KRS7AGA' , args.KRS7AGA, countKRS7AGA		
		
args.KRS7AGG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTAGGGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7AGG		
countKRS7AGG = 0		
		
bfKRS7AGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7AGG:		
	if args.KRS7AGG in line.seq:	
		countKRS7AGG += 1
		
print 'KRS7AGG' , args.KRS7AGG, countKRS7AGG		
		
args.KRS7GGT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTGGTGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7GGT		
countKRS7GGT = 0		
		
bfKRS7GGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7GGT:		
	if args.KRS7GGT in line.seq:	
		countKRS7GGT += 1
		
print 'KRS7GGT' , args.KRS7GGT, countKRS7GGT		
		
args.KRS7GGC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTGGCGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7GGC		
countKRS7GGC = 0		
		
bfKRS7GGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7GGC:		
	if args.KRS7GGC in line.seq:	
		countKRS7GGC += 1
		
print 'KRS7GGC' , args.KRS7GGC, countKRS7GGC		
		
args.KRS7GGA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTGGAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7GGA		
countKRS7GGA = 0		
		
bfKRS7GGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7GGA:		
	if args.KRS7GGA in line.seq:	
		countKRS7GGA += 1
		
print 'KRS7GGA' , args.KRS7GGA, countKRS7GGA		
		
args.KRS7GGG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTGGGGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS7GGG		
countKRS7GGG = 0		
		
bfKRS7GGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS7GGG:		
	if args.KRS7GGG in line.seq:	
		countKRS7GGG += 1
		
print 'KRS7GGG' , args.KRS7GGG, countKRS7GGG		

args.KRS8TTT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATATTTAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8TTT		
countKRS8TTT = 0		
		
bfKRS8TTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8TTT:		
	if args.KRS8TTT in line.seq:	
		countKRS8TTT += 1
		
print 'KRS8TTT' , args.KRS8TTT, countKRS8TTT		
		
args.KRS8TTC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATATTCAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8TTC		
countKRS8TTC = 0		
		
bfKRS8TTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8TTC:		
	if args.KRS8TTC in line.seq:	
		countKRS8TTC += 1
		
print 'KRS8TTC' , args.KRS8TTC, countKRS8TTC		
		
args.KRS8TTA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATATTAAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8TTA		
countKRS8TTA = 0		
		
bfKRS8TTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8TTA:		
	if args.KRS8TTA in line.seq:	
		countKRS8TTA += 1
		
print 'KRS8TTA' , args.KRS8TTA, countKRS8TTA		
		
args.KRS8TTG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATATTGAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8TTG		
countKRS8TTG = 0		
		
bfKRS8TTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8TTG:		
	if args.KRS8TTG in line.seq:	
		countKRS8TTG += 1
		
print 'KRS8TTG' , args.KRS8TTG, countKRS8TTG		
		
args.KRS8CTT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATACTTAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8CTT		
countKRS8CTT = 0		
		
bfKRS8CTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8CTT:		
	if args.KRS8CTT in line.seq:	
		countKRS8CTT += 1
		
print 'KRS8CTT' , args.KRS8CTT, countKRS8CTT		
		
args.KRS8CTC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATACTCAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8CTC		
countKRS8CTC = 0		
		
bfKRS8CTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8CTC:		
	if args.KRS8CTC in line.seq:	
		countKRS8CTC += 1
		
print 'KRS8CTC' , args.KRS8CTC, countKRS8CTC		
		
args.KRS8CTA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATACTAAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8CTA		
countKRS8CTA = 0		
		
bfKRS8CTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8CTA:		
	if args.KRS8CTA in line.seq:	
		countKRS8CTA += 1
		
print 'KRS8CTA' , args.KRS8CTA, countKRS8CTA		
		
args.KRS8CTG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATACTGAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8CTG		
countKRS8CTG = 0		
		
bfKRS8CTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8CTG:		
	if args.KRS8CTG in line.seq:	
		countKRS8CTG += 1
		
print 'KRS8CTG' , args.KRS8CTG, countKRS8CTG		
		
args.KRS8ATT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAATTAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8ATT		
countKRS8ATT = 0		
		
bfKRS8ATT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8ATT:		
	if args.KRS8ATT in line.seq:	
		countKRS8ATT += 1
		
print 'KRS8ATT' , args.KRS8ATT, countKRS8ATT		
		
args.KRS8ATC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAATCAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8ATC		
countKRS8ATC = 0		
		
bfKRS8ATC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8ATC:		
	if args.KRS8ATC in line.seq:	
		countKRS8ATC += 1
		
print 'KRS8ATC' , args.KRS8ATC, countKRS8ATC		
		
args.KRS8ATA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAATAAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8ATA		
countKRS8ATA = 0		
		
bfKRS8ATA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8ATA:		
	if args.KRS8ATA in line.seq:	
		countKRS8ATA += 1
		
print 'KRS8ATA' , args.KRS8ATA, countKRS8ATA		
		
args.KRS8ATG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAATGAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8ATG		
countKRS8ATG = 0		
		
bfKRS8ATG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8ATG:		
	if args.KRS8ATG in line.seq:	
		countKRS8ATG += 1
		
print 'KRS8ATG' , args.KRS8ATG, countKRS8ATG		
		
args.KRS8GTT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGTTAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8GTT		
countKRS8GTT = 0		
		
bfKRS8GTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8GTT:		
	if args.KRS8GTT in line.seq:	
		countKRS8GTT += 1
		
print 'KRS8GTT' , args.KRS8GTT, countKRS8GTT		
		
args.KRS8GTC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGTCAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8GTC		
countKRS8GTC = 0		
		
bfKRS8GTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8GTC:		
	if args.KRS8GTC in line.seq:	
		countKRS8GTC += 1
		
print 'KRS8GTC' , args.KRS8GTC, countKRS8GTC		
		
args.KRS8GTA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGTAAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8GTA		
countKRS8GTA = 0		
		
bfKRS8GTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8GTA:		
	if args.KRS8GTA in line.seq:	
		countKRS8GTA += 1
		
print 'KRS8GTA' , args.KRS8GTA, countKRS8GTA		
		
args.KRS8GTG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGTGAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8GTG

countKRS8GTG = 0		
		
bfKRS8GTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8GTG:		
	if args.KRS8GTG in line.seq:	
		countKRS8GTG += 1
		
print 'KRS8GTG' , args.KRS8GTG, countKRS8GTG		
		
args.KRS8TCT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATATCTAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8TCT		
countKRS8TCT = 0		
		
bfKRS8TCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8TCT:		
	if args.KRS8TCT in line.seq:	
		countKRS8TCT += 1
		
print 'KRS8TCT' , args.KRS8TCT, countKRS8TCT		
		
args.KRS8TCC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATATCCAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8TCC		
countKRS8TCC = 0		
		
bfKRS8TCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8TCC:		
	if args.KRS8TCC in line.seq:	
		countKRS8TCC += 1
		
print 'KRS8TCC' , args.KRS8TCC, countKRS8TCC		
		
args.KRS8TCA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATATCAAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8TCA		
countKRS8TCA = 0		
		
bfKRS8TCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8TCA:		
	if args.KRS8TCA in line.seq:	
		countKRS8TCA += 1
		
print 'KRS8TCA' , args.KRS8TCA, countKRS8TCA		
		
args.KRS8TCG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATATCGAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8TCG		
countKRS8TCG = 0		
		
bfKRS8TCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8TCG:		
	if args.KRS8TCG in line.seq:	
		countKRS8TCG += 1
		
print 'KRS8TCG' , args.KRS8TCG, countKRS8TCG		
		
args.KRS8CCT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATACCTAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8CCT		
countKRS8CCT = 0		
		
bfKRS8CCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8CCT:		
	if args.KRS8CCT in line.seq:	
		countKRS8CCT += 1
		
print 'KRS8CCT' , args.KRS8CCT, countKRS8CCT		
		
args.KRS8CCC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATACCCAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8CCC		
countKRS8CCC = 0		
		
bfKRS8CCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8CCC:		
	if args.KRS8CCC in line.seq:	
		countKRS8CCC += 1
		
print 'KRS8CCC' , args.KRS8CCC, countKRS8CCC		
		
args.KRS8CCA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATACCAAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8CCA		
countKRS8CCA = 0		
		
bfKRS8CCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8CCA:		
	if args.KRS8CCA in line.seq:	
		countKRS8CCA += 1
		
print 'KRS8CCA' , args.KRS8CCA, countKRS8CCA		
		
args.KRS8CCG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATACCGAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8CCG		
countKRS8CCG = 0		
		
bfKRS8CCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8CCG:		
	if args.KRS8CCG in line.seq:	
		countKRS8CCG += 1
		
print 'KRS8CCG' , args.KRS8CCG, countKRS8CCG		
		
args.KRS8ACT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAACTAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8ACT		
countKRS8ACT = 0		
		
bfKRS8ACT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8ACT:		
	if args.KRS8ACT in line.seq:	
		countKRS8ACT += 1
		
print 'KRS8ACT' , args.KRS8ACT, countKRS8ACT		
		
args.KRS8ACC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAACCAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8ACC		
countKRS8ACC = 0		
		
bfKRS8ACC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8ACC:		
	if args.KRS8ACC in line.seq:	
		countKRS8ACC += 1
		
print 'KRS8ACC' , args.KRS8ACC, countKRS8ACC		
		
args.KRS8ACA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAACAAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8ACA		
countKRS8ACA = 0		
		
bfKRS8ACA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8ACA:		
	if args.KRS8ACA in line.seq:	
		countKRS8ACA += 1
		
print 'KRS8ACA' , args.KRS8ACA, countKRS8ACA		
		
args.KRS8ACG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAACGAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8ACG		
countKRS8ACG = 0		
		
bfKRS8ACG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8ACG:		
	if args.KRS8ACG in line.seq:	
		countKRS8ACG += 1
		
print 'KRS8ACG' , args.KRS8ACG, countKRS8ACG		
		
args.KRS8GCT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGCTAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8GCT		
countKRS8GCT = 0		
		
bfKRS8GCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8GCT:		
	if args.KRS8GCT in line.seq:	
		countKRS8GCT += 1
		
print 'KRS8GCT' , args.KRS8GCT, countKRS8GCT		
		
args.KRS8GCC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGCCAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8GCC		
countKRS8GCC = 0		
		
bfKRS8GCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8GCC:		
	if args.KRS8GCC in line.seq:	
		countKRS8GCC += 1
		
print 'KRS8GCC' , args.KRS8GCC, countKRS8GCC		
		
args.KRS8GCA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGCAAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8GCA		
countKRS8GCA = 0		
		
bfKRS8GCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8GCA:		
	if args.KRS8GCA in line.seq:	
		countKRS8GCA += 1
		
print 'KRS8GCA' , args.KRS8GCA, countKRS8GCA		
		
args.KRS8GCG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGCGAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8GCG		
countKRS8GCG = 0		
		
bfKRS8GCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8GCG:		
	if args.KRS8GCG in line.seq:	
		countKRS8GCG += 1
		
print 'KRS8GCG' , args.KRS8GCG, countKRS8GCG		
		
args.KRS8TAT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATATATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8TAT		
countKRS8TAT = 0		
		
bfKRS8TAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8TAT:		
	if args.KRS8TAT in line.seq:	
		countKRS8TAT += 1
		
print 'KRS8TAT' , args.KRS8TAT, countKRS8TAT		
		
args.KRS8TAC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATATACAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8TAC		
countKRS8TAC = 0		
		
bfKRS8TAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8TAC:		
	if args.KRS8TAC in line.seq:	
		countKRS8TAC += 1
		
print 'KRS8TAC' , args.KRS8TAC, countKRS8TAC		
		
args.KRS8TAA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATATAAAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8TAA		
countKRS8TAA = 0		
		
bfKRS8TAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8TAA:		
	if args.KRS8TAA in line.seq:	
		countKRS8TAA += 1
		
print 'KRS8TAA' , args.KRS8TAA, countKRS8TAA		
		
args.KRS8TAG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATATAGAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8TAG		
countKRS8TAG = 0		
		
bfKRS8TAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8TAG:		
	if args.KRS8TAG in line.seq:	
		countKRS8TAG += 1
		
print 'KRS8TAG' , args.KRS8TAG, countKRS8TAG		
		
args.KRS8CAT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATACATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8CAT		
countKRS8CAT = 0		
		
bfKRS8CAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8CAT:		
	if args.KRS8CAT in line.seq:	
		countKRS8CAT += 1
		
print 'KRS8CAT' , args.KRS8CAT, countKRS8CAT		
		
args.KRS8CAC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATACACAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8CAC		
countKRS8CAC = 0		
		
bfKRS8CAC = pysam.Samfile(args.infile,"rb")
		
for line in bfKRS8CAC:		
	if args.KRS8CAC in line.seq:	
		countKRS8CAC += 1
		
print 'KRS8CAC' , args.KRS8CAC, countKRS8CAC		
		
args.KRS8CAA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATACAAAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8CAA		
countKRS8CAA = 0		
		
bfKRS8CAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8CAA:		
	if args.KRS8CAA in line.seq:	
		countKRS8CAA += 1
		
print 'KRS8CAA' , args.KRS8CAA, countKRS8CAA		
		
args.KRS8CAG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATACAGAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8CAG		
countKRS8CAG = 0		
		
bfKRS8CAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8CAG:		
	if args.KRS8CAG in line.seq:	
		countKRS8CAG += 1
		
print 'KRS8CAG' , args.KRS8CAG, countKRS8CAG		
		
args.KRS8AAT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAAATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8AAT		
countKRS8AAT = 0		
		
bfKRS8AAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8AAT:		
	if args.KRS8AAT in line.seq:	
		countKRS8AAT += 1
		
print 'KRS8AAT' , args.KRS8AAT, countKRS8AAT		
		
args.KRS8AAC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAAACAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8AAC		
countKRS8AAC = 0		
		
bfKRS8AAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8AAC:		
	if args.KRS8AAC in line.seq:	
		countKRS8AAC += 1
		
print 'KRS8AAC' , args.KRS8AAC, countKRS8AAC		
		
args.KRS8AAA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAAAAAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8AAA		
countKRS8AAA = 0		
		
bfKRS8AAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8AAA:		
	if args.KRS8AAA in line.seq:	
		countKRS8AAA += 1
		
print 'KRS8AAA' , args.KRS8AAA, countKRS8AAA		
		
args.KRS8AAG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAAAGAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8AAG		
countKRS8AAG = 0		
		
bfKRS8AAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8AAG:		
	if args.KRS8AAG in line.seq:	
		countKRS8AAG += 1
		
print 'KRS8AAG' , args.KRS8AAG, countKRS8AAG		
		
args.KRS8GAT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8GAT		
countKRS8GAT = 0		
		
bfKRS8GAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8GAT:		
	if args.KRS8GAT in line.seq:	
		countKRS8GAT += 1
		
print 'KRS8GAT' , args.KRS8GAT, countKRS8GAT		
		
args.KRS8GAC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGACAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8GAC		
countKRS8GAC = 0		
		
bfKRS8GAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8GAC:		
	if args.KRS8GAC in line.seq:	
		countKRS8GAC += 1
		
print 'KRS8GAC' , args.KRS8GAC, countKRS8GAC		
		
args.KRS8GAA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGAAAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8GAA		
countKRS8GAA = 0		
		
bfKRS8GAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8GAA:		
	if args.KRS8GAA in line.seq:	
		countKRS8GAA += 1
		
print 'KRS8GAA' , args.KRS8GAA, countKRS8GAA		
		
args.KRS8GAG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGAGAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8GAG		
countKRS8GAG = 0		
		
bfKRS8GAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8GAG:		
	if args.KRS8GAG in line.seq:	
		countKRS8GAG += 1
		
print 'KRS8GAG' , args.KRS8GAG, countKRS8GAG		
		
args.KRS8TGT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATATGTAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8TGT		
countKRS8TGT = 0		
		
bfKRS8TGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8TGT:		
	if args.KRS8TGT in line.seq:	
		countKRS8TGT += 1
		
print 'KRS8TGT' , args.KRS8TGT, countKRS8TGT		
		
args.KRS8TGC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATATGCAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8TGC		
countKRS8TGC = 0		
		
bfKRS8TGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8TGC:		
	if args.KRS8TGC in line.seq:	
		countKRS8TGC += 1
		
print 'KRS8TGC' , args.KRS8TGC, countKRS8TGC		
		
args.KRS8TGA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATATGAAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8TGA		
countKRS8TGA = 0		
		
bfKRS8TGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8TGA:		
	if args.KRS8TGA in line.seq:	
		countKRS8TGA += 1
		
print 'KRS8TGA' , args.KRS8TGA, countKRS8TGA		
		
args.KRS8TGG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATATGGAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8TGG		
countKRS8TGG = 0		
		
bfKRS8TGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8TGG:		
	if args.KRS8TGG in line.seq:	
		countKRS8TGG += 1
		
print 'KRS8TGG' , args.KRS8TGG, countKRS8TGG		
		
args.KRS8CGT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATACGTAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8CGT		
countKRS8CGT = 0		
		
bfKRS8CGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8CGT:		
	if args.KRS8CGT in line.seq:	
		countKRS8CGT += 1
		
print 'KRS8CGT' , args.KRS8CGT, countKRS8CGT		
		
args.KRS8CGC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATACGCAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8CGC		
countKRS8CGC = 0		
		
bfKRS8CGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8CGC:		
	if args.KRS8CGC in line.seq:	
		countKRS8CGC += 1
		
print 'KRS8CGC' , args.KRS8CGC, countKRS8CGC		
		
args.KRS8CGA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATACGAAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8CGA		
countKRS8CGA = 0		
		
bfKRS8CGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8CGA:		
	if args.KRS8CGA in line.seq:	
		countKRS8CGA += 1
		
print 'KRS8CGA' , args.KRS8CGA, countKRS8CGA		
		
args.KRS8CGG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATACGGAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8CGG		
countKRS8CGG = 0		
		
bfKRS8CGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8CGG:		
	if args.KRS8CGG in line.seq:	
		countKRS8CGG += 1
		
print 'KRS8CGG' , args.KRS8CGG, countKRS8CGG		
		
args.KRS8AGT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAAGTAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8AGT		
countKRS8AGT = 0		
		
bfKRS8AGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8AGT:		
	if args.KRS8AGT in line.seq:	
		countKRS8AGT += 1
		
print 'KRS8AGT' , args.KRS8AGT, countKRS8AGT		
		
args.KRS8AGC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAAGCAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8AGC		
countKRS8AGC = 0		
		
bfKRS8AGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8AGC:		
	if args.KRS8AGC in line.seq:	
		countKRS8AGC += 1
		
print 'KRS8AGC' , args.KRS8AGC, countKRS8AGC		
		
args.KRS8AGA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAAGAAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8AGA		
countKRS8AGA = 0		
		
bfKRS8AGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8AGA:		
	if args.KRS8AGA in line.seq:	
		countKRS8AGA += 1
		
print 'KRS8AGA' , args.KRS8AGA, countKRS8AGA		
		
args.KRS8AGG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAAGGAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8AGG		
countKRS8AGG = 0		
		
bfKRS8AGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8AGG:		
	if args.KRS8AGG in line.seq:	
		countKRS8AGG += 1
		
print 'KRS8AGG' , args.KRS8AGG, countKRS8AGG		
		
args.KRS8GGT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGGTAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8GGT		
countKRS8GGT = 0		
		
bfKRS8GGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8GGT:		
	if args.KRS8GGT in line.seq:	
		countKRS8GGT += 1
		
print 'KRS8GGT' , args.KRS8GGT, countKRS8GGT		
		
args.KRS8GGC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGGCAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8GGC		
countKRS8GGC = 0		
		
bfKRS8GGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8GGC:		
	if args.KRS8GGC in line.seq:	
		countKRS8GGC += 1
		
print 'KRS8GGC' , args.KRS8GGC, countKRS8GGC		
		
args.KRS8GGA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGGAAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8GGA		
countKRS8GGA = 0		
		
bfKRS8GGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8GGA:		
	if args.KRS8GGA in line.seq:	
		countKRS8GGA += 1
		
print 'KRS8GGA' , args.KRS8GGA, countKRS8GGA		
		
args.KRS8GGG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGGGAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS8GGG		
countKRS8GGG = 0		
		
bfKRS8GGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS8GGG:		
	if args.KRS8GGG in line.seq:	
		countKRS8GGG += 1
		
print 'KRS8GGG' , args.KRS8GGG, countKRS8GGG		


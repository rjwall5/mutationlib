#Created on Wed Sept 1 13:32:16 2021 by Richard Wall

import pysam, argparse

parser = argparse.ArgumentParser(description='Counts sequences from P. knowlesi KRS mutation library')
parser.add_argument('-i',nargs='?',dest='infile',help='Input BAM file')

args = parser.parse_args()


args.KRS5TTT = 'TATGAAATTGGTAAAGTATTTAGAAATTTTGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5TTT		
countKRS5TTT = 0		
		
bfKRS5TTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5TTT:		
	if args.KRS5TTT in line.seq:	
		countKRS5TTT += 1
		
print 'KRS5TTT' , args.KRS5TTT, countKRS5TTT		
		
args.KRS5TTC = 'TATGAAATTGGTAAAGTATTTAGAAATTTCGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5TTC		
countKRS5TTC = 0		
		
bfKRS5TTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5TTC:		
	if args.KRS5TTC in line.seq:	
		countKRS5TTC += 1
		
print 'KRS5TTC' , args.KRS5TTC, countKRS5TTC		
		
args.KRS5TTA = 'TATGAAATTGGTAAAGTATTTAGAAATTTAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5TTA		
countKRS5TTA = 0		
		
bfKRS5TTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5TTA:		
	if args.KRS5TTA in line.seq:	
		countKRS5TTA += 1
		
print 'KRS5TTA' , args.KRS5TTA, countKRS5TTA		
		
args.KRS5TTG = 'TATGAAATTGGTAAAGTATTTAGAAATTTGGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5TTG		
countKRS5TTG = 0		
		
bfKRS5TTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5TTG:		
	if args.KRS5TTG in line.seq:	
		countKRS5TTG += 1
		
print 'KRS5TTG' , args.KRS5TTG, countKRS5TTG		
		
args.KRS5CTT = 'TATGAAATTGGTAAAGTATTTAGAAATCTTGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5CTT		
countKRS5CTT = 0		
		
bfKRS5CTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5CTT:		
	if args.KRS5CTT in line.seq:	
		countKRS5CTT += 1
		
print 'KRS5CTT' , args.KRS5CTT, countKRS5CTT		
		
args.KRS5CTC = 'TATGAAATTGGTAAAGTATTTAGAAATCTCGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5CTC		
countKRS5CTC = 0		
		
bfKRS5CTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5CTC:		
	if args.KRS5CTC in line.seq:	
		countKRS5CTC += 1
		
print 'KRS5CTC' , args.KRS5CTC, countKRS5CTC		
		
args.KRS5CTA = 'TATGAAATTGGTAAAGTATTTAGAAATCTAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5CTA		
countKRS5CTA = 0		
		
bfKRS5CTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5CTA:		
	if args.KRS5CTA in line.seq:	
		countKRS5CTA += 1
		
print 'KRS5CTA' , args.KRS5CTA, countKRS5CTA		
		
args.KRS5CTG = 'TATGAAATTGGTAAAGTATTTAGAAATCTGGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5CTG		
countKRS5CTG = 0		
		
bfKRS5CTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5CTG:		
	if args.KRS5CTG in line.seq:	
		countKRS5CTG += 1
		
print 'KRS5CTG' , args.KRS5CTG, countKRS5CTG		
		
args.KRS5ATT = 'TATGAAATTGGTAAAGTATTTAGAAATATTGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5ATT		
countKRS5ATT = 0		
		
bfKRS5ATT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5ATT:		
	if args.KRS5ATT in line.seq:	
		countKRS5ATT += 1
		
print 'KRS5ATT' , args.KRS5ATT, countKRS5ATT		
		
args.KRS5ATC = 'TATGAAATTGGTAAAGTATTTAGAAATATCGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5ATC		
countKRS5ATC = 0		
		
bfKRS5ATC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5ATC:		
	if args.KRS5ATC in line.seq:	
		countKRS5ATC += 1
		
print 'KRS5ATC' , args.KRS5ATC, countKRS5ATC		
		
args.KRS5ATA = 'TATGAAATTGGTAAAGTATTTAGAAATATAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5ATA		
countKRS5ATA = 0		
		
bfKRS5ATA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5ATA:		
	if args.KRS5ATA in line.seq:	
		countKRS5ATA += 1
		
print 'KRS5ATA' , args.KRS5ATA, countKRS5ATA		
		
args.KRS5ATG = 'TATGAAATTGGTAAAGTATTTAGAAATATGGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5ATG		
countKRS5ATG = 0		
		
bfKRS5ATG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5ATG:		
	if args.KRS5ATG in line.seq:	
		countKRS5ATG += 1
		
print 'KRS5ATG' , args.KRS5ATG, countKRS5ATG		
		
args.KRS5GTT = 'TATGAAATTGGTAAAGTATTTAGAAATGTTGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5GTT		
countKRS5GTT = 0		
		
bfKRS5GTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5GTT:		
	if args.KRS5GTT in line.seq:	
		countKRS5GTT += 1
		
print 'KRS5GTT' , args.KRS5GTT, countKRS5GTT		
		
args.KRS5GTC = 'TATGAAATTGGTAAAGTATTTAGAAATGTCGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5GTC		
countKRS5GTC = 0		
		
bfKRS5GTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5GTC:		
	if args.KRS5GTC in line.seq:	
		countKRS5GTC += 1
		
print 'KRS5GTC' , args.KRS5GTC, countKRS5GTC		
		
args.KRS5GTA = 'TATGAAATTGGTAAAGTATTTAGAAATGTAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5GTA		
countKRS5GTA = 0		
		
bfKRS5GTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5GTA:		
	if args.KRS5GTA in line.seq:	
		countKRS5GTA += 1
		
print 'KRS5GTA' , args.KRS5GTA, countKRS5GTA		
		
args.KRS5GTG = 'TATGAAATTGGTAAAGTATTTAGAAATGTGGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5GTG

countKRS5GTG = 0		
		
bfKRS5GTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5GTG:		
	if args.KRS5GTG in line.seq:	
		countKRS5GTG += 1
		
print 'KRS5GTG' , args.KRS5GTG, countKRS5GTG		
		
args.KRS5TCT = 'TATGAAATTGGTAAAGTATTTAGAAATTCTGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5TCT		
countKRS5TCT = 0		
		
bfKRS5TCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5TCT:		
	if args.KRS5TCT in line.seq:	
		countKRS5TCT += 1
		
print 'KRS5TCT' , args.KRS5TCT, countKRS5TCT		
		
args.KRS5TCC = 'TATGAAATTGGTAAAGTATTTAGAAATTCCGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5TCC		
countKRS5TCC = 0		
		
bfKRS5TCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5TCC:		
	if args.KRS5TCC in line.seq:	
		countKRS5TCC += 1
		
print 'KRS5TCC' , args.KRS5TCC, countKRS5TCC		
		
args.KRS5TCA = 'TATGAAATTGGTAAAGTATTTAGAAATTCAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5TCA		
countKRS5TCA = 0		
		
bfKRS5TCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5TCA:		
	if args.KRS5TCA in line.seq:	
		countKRS5TCA += 1
		
print 'KRS5TCA' , args.KRS5TCA, countKRS5TCA		
		
args.KRS5TCG = 'TATGAAATTGGTAAAGTATTTAGAAATTCGGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5TCG		
countKRS5TCG = 0		
		
bfKRS5TCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5TCG:		
	if args.KRS5TCG in line.seq:	
		countKRS5TCG += 1
		
print 'KRS5TCG' , args.KRS5TCG, countKRS5TCG		
		
args.KRS5CCT = 'TATGAAATTGGTAAAGTATTTAGAAATCCTGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5CCT		
countKRS5CCT = 0		
		
bfKRS5CCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5CCT:		
	if args.KRS5CCT in line.seq:	
		countKRS5CCT += 1
		
print 'KRS5CCT' , args.KRS5CCT, countKRS5CCT		
		
args.KRS5CCC = 'TATGAAATTGGTAAAGTATTTAGAAATCCCGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5CCC		
countKRS5CCC = 0		
		
bfKRS5CCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5CCC:		
	if args.KRS5CCC in line.seq:	
		countKRS5CCC += 1
		
print 'KRS5CCC' , args.KRS5CCC, countKRS5CCC		
		
args.KRS5CCA = 'TATGAAATTGGTAAAGTATTTAGAAATCCAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5CCA		
countKRS5CCA = 0		
		
bfKRS5CCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5CCA:		
	if args.KRS5CCA in line.seq:	
		countKRS5CCA += 1
		
print 'KRS5CCA' , args.KRS5CCA, countKRS5CCA		
		
args.KRS5CCG = 'TATGAAATTGGTAAAGTATTTAGAAATCCGGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5CCG		
countKRS5CCG = 0		
		
bfKRS5CCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5CCG:		
	if args.KRS5CCG in line.seq:	
		countKRS5CCG += 1
		
print 'KRS5CCG' , args.KRS5CCG, countKRS5CCG		
		
args.KRS5ACT = 'TATGAAATTGGTAAAGTATTTAGAAATACTGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5ACT		
countKRS5ACT = 0		
		
bfKRS5ACT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5ACT:		
	if args.KRS5ACT in line.seq:	
		countKRS5ACT += 1
		
print 'KRS5ACT' , args.KRS5ACT, countKRS5ACT		
		
args.KRS5ACC = 'TATGAAATTGGTAAAGTATTTAGAAATACCGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5ACC		
countKRS5ACC = 0		
		
bfKRS5ACC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5ACC:		
	if args.KRS5ACC in line.seq:	
		countKRS5ACC += 1
		
print 'KRS5ACC' , args.KRS5ACC, countKRS5ACC		
		
args.KRS5ACA = 'TATGAAATTGGTAAAGTATTTAGAAATACAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5ACA		
countKRS5ACA = 0		
		
bfKRS5ACA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5ACA:		
	if args.KRS5ACA in line.seq:	
		countKRS5ACA += 1
		
print 'KRS5ACA' , args.KRS5ACA, countKRS5ACA		
		
args.KRS5ACG = 'TATGAAATTGGTAAAGTATTTAGAAATACGGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5ACG		
countKRS5ACG = 0		
		
bfKRS5ACG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5ACG:		
	if args.KRS5ACG in line.seq:	
		countKRS5ACG += 1
		
print 'KRS5ACG' , args.KRS5ACG, countKRS5ACG		
		
args.KRS5GCT = 'TATGAAATTGGTAAAGTATTTAGAAATGCTGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5GCT		
countKRS5GCT = 0		
		
bfKRS5GCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5GCT:		
	if args.KRS5GCT in line.seq:	
		countKRS5GCT += 1
		
print 'KRS5GCT' , args.KRS5GCT, countKRS5GCT		
		
args.KRS5GCC = 'TATGAAATTGGTAAAGTATTTAGAAATGCCGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5GCC		
countKRS5GCC = 0		
		
bfKRS5GCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5GCC:		
	if args.KRS5GCC in line.seq:	
		countKRS5GCC += 1
		
print 'KRS5GCC' , args.KRS5GCC, countKRS5GCC		
		
args.KRS5GCA = 'TATGAAATTGGTAAAGTATTTAGAAATGCAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5GCA		
countKRS5GCA = 0		
		
bfKRS5GCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5GCA:		
	if args.KRS5GCA in line.seq:	
		countKRS5GCA += 1
		
print 'KRS5GCA' , args.KRS5GCA, countKRS5GCA		
		
args.KRS5GCG = 'TATGAAATTGGTAAAGTATTTAGAAATGCGGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5GCG		
countKRS5GCG = 0		
		
bfKRS5GCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5GCG:		
	if args.KRS5GCG in line.seq:	
		countKRS5GCG += 1
		
print 'KRS5GCG' , args.KRS5GCG, countKRS5GCG		
		
args.KRS5TAT = 'TATGAAATTGGTAAAGTATTTAGAAATTATGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5TAT		
countKRS5TAT = 0		
		
bfKRS5TAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5TAT:		
	if args.KRS5TAT in line.seq:	
		countKRS5TAT += 1
		
print 'KRS5TAT' , args.KRS5TAT, countKRS5TAT		
		
args.KRS5TAC = 'TATGAAATTGGTAAAGTATTTAGAAATTACGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5TAC		
countKRS5TAC = 0		
		
bfKRS5TAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5TAC:		
	if args.KRS5TAC in line.seq:	
		countKRS5TAC += 1
		
print 'KRS5TAC' , args.KRS5TAC, countKRS5TAC		
		
args.KRS5TAA = 'TATGAAATTGGTAAAGTATTTAGAAATTAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5TAA		
countKRS5TAA = 0		
		
bfKRS5TAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5TAA:		
	if args.KRS5TAA in line.seq:	
		countKRS5TAA += 1
		
print 'KRS5TAA' , args.KRS5TAA, countKRS5TAA		
		
args.KRS5TAG = 'TATGAAATTGGTAAAGTATTTAGAAATTAGGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5TAG		
countKRS5TAG = 0		
		
bfKRS5TAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5TAG:		
	if args.KRS5TAG in line.seq:	
		countKRS5TAG += 1
		
print 'KRS5TAG' , args.KRS5TAG, countKRS5TAG		
		
args.KRS5CAT = 'TATGAAATTGGTAAAGTATTTAGAAATCATGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5CAT		
countKRS5CAT = 0		
		
bfKRS5CAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5CAT:		
	if args.KRS5CAT in line.seq:	
		countKRS5CAT += 1
		
print 'KRS5CAT' , args.KRS5CAT, countKRS5CAT		
		
args.KRS5CAC = 'TATGAAATTGGTAAAGTATTTAGAAATCACGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5CAC		
countKRS5CAC = 0		
		
bfKRS5CAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5CAC:		
	if args.KRS5CAC in line.seq:	
		countKRS5CAC += 1
		
print 'KRS5CAC' , args.KRS5CAC, countKRS5CAC		
		
args.KRS5CAA = 'TATGAAATTGGTAAAGTATTTAGAAATCAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5CAA		
countKRS5CAA = 0		
		
bfKRS5CAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5CAA:		
	if args.KRS5CAA in line.seq:	
		countKRS5CAA += 1
		
print 'KRS5CAA' , args.KRS5CAA, countKRS5CAA		
		
args.KRS5CAG = 'TATGAAATTGGTAAAGTATTTAGAAATCAGGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5CAG		
countKRS5CAG = 0		
		
bfKRS5CAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5CAG:		
	if args.KRS5CAG in line.seq:	
		countKRS5CAG += 1
		
print 'KRS5CAG' , args.KRS5CAG, countKRS5CAG		
		
args.KRS5AAT = 'TATGAAATTGGTAAAGTATTTAGAAATAATGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5AAT		
countKRS5AAT = 0		
		
bfKRS5AAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5AAT:		
	if args.KRS5AAT in line.seq:	
		countKRS5AAT += 1
		
print 'KRS5AAT' , args.KRS5AAT, countKRS5AAT		
		
args.KRS5AAC = 'TATGAAATTGGTAAAGTATTTAGAAATAACGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5AAC		
countKRS5AAC = 0		
		
bfKRS5AAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5AAC:		
	if args.KRS5AAC in line.seq:	
		countKRS5AAC += 1
		
print 'KRS5AAC' , args.KRS5AAC, countKRS5AAC		
		
args.KRS5AAA = 'TATGAAATTGGTAAAGTATTTAGAAATAAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5AAA		
countKRS5AAA = 0		
		
bfKRS5AAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5AAA:		
	if args.KRS5AAA in line.seq:	
		countKRS5AAA += 1
		
print 'KRS5AAA' , args.KRS5AAA, countKRS5AAA		
		
args.KRS5AAG = 'TATGAAATTGGTAAAGTATTTAGAAATAAGGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5AAG		
countKRS5AAG = 0		
		
bfKRS5AAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5AAG:		
	if args.KRS5AAG in line.seq:	
		countKRS5AAG += 1
		
print 'KRS5AAG' , args.KRS5AAG, countKRS5AAG		
		
args.KRS5GAT = 'TATGAAATTGGTAAAGTATTTAGAAATGATGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5GAT		
countKRS5GAT = 0		
		
bfKRS5GAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5GAT:		
	if args.KRS5GAT in line.seq:	
		countKRS5GAT += 1
		
print 'KRS5GAT' , args.KRS5GAT, countKRS5GAT		
		
args.KRS5GAC = 'TATGAAATTGGTAAAGTATTTAGAAATGACGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5GAC		
countKRS5GAC = 0		
		
bfKRS5GAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5GAC:		
	if args.KRS5GAC in line.seq:	
		countKRS5GAC += 1
		
print 'KRS5GAC' , args.KRS5GAC, countKRS5GAC		
		
args.KRS5GAA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5GAA		
countKRS5GAA = 0		
		
bfKRS5GAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5GAA:		
	if args.KRS5GAA in line.seq:	
		countKRS5GAA += 1
		
print 'KRS5GAA' , args.KRS5GAA, countKRS5GAA		
		
args.KRS5GAG = 'TATGAAATTGGTAAAGTATTTAGAAATGAGGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5GAG		
countKRS5GAG = 0		
		
bfKRS5GAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5GAG:		
	if args.KRS5GAG in line.seq:	
		countKRS5GAG += 1
		
print 'KRS5GAG' , args.KRS5GAG, countKRS5GAG		
		
args.KRS5TGT = 'TATGAAATTGGTAAAGTATTTAGAAATTGTGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5TGT		
countKRS5TGT = 0		
		
bfKRS5TGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5TGT:		
	if args.KRS5TGT in line.seq:	
		countKRS5TGT += 1
		
print 'KRS5TGT' , args.KRS5TGT, countKRS5TGT		
		
args.KRS5TGC = 'TATGAAATTGGTAAAGTATTTAGAAATTGCGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5TGC		
countKRS5TGC = 0		
		
bfKRS5TGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5TGC:		
	if args.KRS5TGC in line.seq:	
		countKRS5TGC += 1
		
print 'KRS5TGC' , args.KRS5TGC, countKRS5TGC		
		
args.KRS5TGA = 'TATGAAATTGGTAAAGTATTTAGAAATTGAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5TGA		
countKRS5TGA = 0		
		
bfKRS5TGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5TGA:		
	if args.KRS5TGA in line.seq:	
		countKRS5TGA += 1
		
print 'KRS5TGA' , args.KRS5TGA, countKRS5TGA		
		
args.KRS5TGG = 'TATGAAATTGGTAAAGTATTTAGAAATTGGGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5TGG		
countKRS5TGG = 0		
		
bfKRS5TGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5TGG:		
	if args.KRS5TGG in line.seq:	
		countKRS5TGG += 1
		
print 'KRS5TGG' , args.KRS5TGG, countKRS5TGG		
		
args.KRS5CGT = 'TATGAAATTGGTAAAGTATTTAGAAATCGTGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5CGT		
countKRS5CGT = 0		
		
bfKRS5CGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5CGT:		
	if args.KRS5CGT in line.seq:	
		countKRS5CGT += 1
		
print 'KRS5CGT' , args.KRS5CGT, countKRS5CGT		
		
args.KRS5CGC = 'TATGAAATTGGTAAAGTATTTAGAAATCGCGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5CGC		
countKRS5CGC = 0		
		
bfKRS5CGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5CGC:		
	if args.KRS5CGC in line.seq:	
		countKRS5CGC += 1
		
print 'KRS5CGC' , args.KRS5CGC, countKRS5CGC		
		
args.KRS5CGA = 'TATGAAATTGGTAAAGTATTTAGAAATCGAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5CGA		
countKRS5CGA = 0		
		
bfKRS5CGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5CGA:		
	if args.KRS5CGA in line.seq:	
		countKRS5CGA += 1
		
print 'KRS5CGA' , args.KRS5CGA, countKRS5CGA		
		
args.KRS5CGG = 'TATGAAATTGGTAAAGTATTTAGAAATCGGGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5CGG		
countKRS5CGG = 0		
		
bfKRS5CGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5CGG:		
	if args.KRS5CGG in line.seq:	
		countKRS5CGG += 1
		
print 'KRS5CGG' , args.KRS5CGG, countKRS5CGG		
		
args.KRS5AGT = 'TATGAAATTGGTAAAGTATTTAGAAATAGTGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5AGT		
countKRS5AGT = 0		
		
bfKRS5AGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5AGT:		
	if args.KRS5AGT in line.seq:	
		countKRS5AGT += 1
		
print 'KRS5AGT' , args.KRS5AGT, countKRS5AGT		
		
args.KRS5AGC = 'TATGAAATTGGTAAAGTATTTAGAAATAGCGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5AGC		
countKRS5AGC = 0		
		
bfKRS5AGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5AGC:		
	if args.KRS5AGC in line.seq:	
		countKRS5AGC += 1
		
print 'KRS5AGC' , args.KRS5AGC, countKRS5AGC		
		
args.KRS5AGA = 'TATGAAATTGGTAAAGTATTTAGAAATAGAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5AGA		
countKRS5AGA = 0		
		
bfKRS5AGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5AGA:		
	if args.KRS5AGA in line.seq:	
		countKRS5AGA += 1
		
print 'KRS5AGA' , args.KRS5AGA, countKRS5AGA		
		
args.KRS5AGG = 'TATGAAATTGGTAAAGTATTTAGAAATAGGGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5AGG		
countKRS5AGG = 0		
		
bfKRS5AGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5AGG:		
	if args.KRS5AGG in line.seq:	
		countKRS5AGG += 1
		
print 'KRS5AGG' , args.KRS5AGG, countKRS5AGG		
		
args.KRS5GGT = 'TATGAAATTGGTAAAGTATTTAGAAATGGTGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5GGT		
countKRS5GGT = 0		
		
bfKRS5GGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5GGT:		
	if args.KRS5GGT in line.seq:	
		countKRS5GGT += 1
		
print 'KRS5GGT' , args.KRS5GGT, countKRS5GGT		
		
args.KRS5GGC = 'TATGAAATTGGTAAAGTATTTAGAAATGGCGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5GGC		
countKRS5GGC = 0		
		
bfKRS5GGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5GGC:		
	if args.KRS5GGC in line.seq:	
		countKRS5GGC += 1
		
print 'KRS5GGC' , args.KRS5GGC, countKRS5GGC		
		
args.KRS5GGA = 'TATGAAATTGGTAAAGTATTTAGAAATGGAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5GGA		
countKRS5GGA = 0		
		
bfKRS5GGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5GGA:		
	if args.KRS5GGA in line.seq:	
		countKRS5GGA += 1
		
print 'KRS5GGA' , args.KRS5GGA, countKRS5GGA		
		
args.KRS5GGG = 'TATGAAATTGGTAAAGTATTTAGAAATGGGGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS5GGG		
countKRS5GGG = 0		
		
bfKRS5GGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS5GGG:		
	if args.KRS5GGG in line.seq:	
		countKRS5GGG += 1
		
print 'KRS5GGG' , args.KRS5GGG, countKRS5GGG		

args.KRS6TTT = 'TATGAAATTGGTAAAGTATTTAGAAATGAATTTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6TTT		
countKRS6TTT = 0		
		
bfKRS6TTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6TTT:		
	if args.KRS6TTT in line.seq:	
		countKRS6TTT += 1
		
print 'KRS6TTT' , args.KRS6TTT, countKRS6TTT		
		
args.KRS6TTC = 'TATGAAATTGGTAAAGTATTTAGAAATGAATTCATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6TTC		
countKRS6TTC = 0		
		
bfKRS6TTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6TTC:		
	if args.KRS6TTC in line.seq:	
		countKRS6TTC += 1
		
print 'KRS6TTC' , args.KRS6TTC, countKRS6TTC		
		
args.KRS6TTA = 'TATGAAATTGGTAAAGTATTTAGAAATGAATTAATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6TTA		
countKRS6TTA = 0		
		
bfKRS6TTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6TTA:		
	if args.KRS6TTA in line.seq:	
		countKRS6TTA += 1
		
print 'KRS6TTA' , args.KRS6TTA, countKRS6TTA		
		
args.KRS6TTG = 'TATGAAATTGGTAAAGTATTTAGAAATGAATTGATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6TTG		
countKRS6TTG = 0		
		
bfKRS6TTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6TTG:		
	if args.KRS6TTG in line.seq:	
		countKRS6TTG += 1
		
print 'KRS6TTG' , args.KRS6TTG, countKRS6TTG		
		
args.KRS6CTT = 'TATGAAATTGGTAAAGTATTTAGAAATGAACTTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6CTT		
countKRS6CTT = 0		
		
bfKRS6CTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6CTT:		
	if args.KRS6CTT in line.seq:	
		countKRS6CTT += 1
		
print 'KRS6CTT' , args.KRS6CTT, countKRS6CTT		
		
args.KRS6CTC = 'TATGAAATTGGTAAAGTATTTAGAAATGAACTCATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6CTC		
countKRS6CTC = 0		
		
bfKRS6CTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6CTC:		
	if args.KRS6CTC in line.seq:	
		countKRS6CTC += 1
		
print 'KRS6CTC' , args.KRS6CTC, countKRS6CTC		
		
args.KRS6CTA = 'TATGAAATTGGTAAAGTATTTAGAAATGAACTAATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6CTA		
countKRS6CTA = 0		
		
bfKRS6CTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6CTA:		
	if args.KRS6CTA in line.seq:	
		countKRS6CTA += 1
		
print 'KRS6CTA' , args.KRS6CTA, countKRS6CTA		
		
args.KRS6CTG = 'TATGAAATTGGTAAAGTATTTAGAAATGAACTGATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6CTG		
countKRS6CTG = 0		
		
bfKRS6CTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6CTG:		
	if args.KRS6CTG in line.seq:	
		countKRS6CTG += 1
		
print 'KRS6CTG' , args.KRS6CTG, countKRS6CTG		
		
args.KRS6ATT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAATTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6ATT		
countKRS6ATT = 0		
		
bfKRS6ATT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6ATT:		
	if args.KRS6ATT in line.seq:	
		countKRS6ATT += 1
		
print 'KRS6ATT' , args.KRS6ATT, countKRS6ATT		
		
args.KRS6ATC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAATCATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6ATC		
countKRS6ATC = 0		
		
bfKRS6ATC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6ATC:		
	if args.KRS6ATC in line.seq:	
		countKRS6ATC += 1
		
print 'KRS6ATC' , args.KRS6ATC, countKRS6ATC		
		
args.KRS6ATA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAATAATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6ATA		
countKRS6ATA = 0		
		
bfKRS6ATA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6ATA:		
	if args.KRS6ATA in line.seq:	
		countKRS6ATA += 1
		
print 'KRS6ATA' , args.KRS6ATA, countKRS6ATA		
		
args.KRS6ATG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAATGATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6ATG		
countKRS6ATG = 0		
		
bfKRS6ATG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6ATG:		
	if args.KRS6ATG in line.seq:	
		countKRS6ATG += 1
		
print 'KRS6ATG' , args.KRS6ATG, countKRS6ATG		
		
args.KRS6GTT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGTTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6GTT		
countKRS6GTT = 0		
		
bfKRS6GTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6GTT:		
	if args.KRS6GTT in line.seq:	
		countKRS6GTT += 1
		
print 'KRS6GTT' , args.KRS6GTT, countKRS6GTT		
		
args.KRS6GTC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGTCATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6GTC		
countKRS6GTC = 0		
		
bfKRS6GTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6GTC:		
	if args.KRS6GTC in line.seq:	
		countKRS6GTC += 1
		
print 'KRS6GTC' , args.KRS6GTC, countKRS6GTC		
		
args.KRS6GTA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGTAATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6GTA		
countKRS6GTA = 0		
		
bfKRS6GTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6GTA:		
	if args.KRS6GTA in line.seq:	
		countKRS6GTA += 1
		
print 'KRS6GTA' , args.KRS6GTA, countKRS6GTA		
		
args.KRS6GTG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGTGATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6GTG

countKRS6GTG = 0		
		
bfKRS6GTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6GTG:		
	if args.KRS6GTG in line.seq:	
		countKRS6GTG += 1
		
print 'KRS6GTG' , args.KRS6GTG, countKRS6GTG		
		
args.KRS6TCT = 'TATGAAATTGGTAAAGTATTTAGAAATGAATCTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6TCT		
countKRS6TCT = 0		
		
bfKRS6TCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6TCT:		
	if args.KRS6TCT in line.seq:	
		countKRS6TCT += 1
		
print 'KRS6TCT' , args.KRS6TCT, countKRS6TCT		
		
args.KRS6TCC = 'TATGAAATTGGTAAAGTATTTAGAAATGAATCCATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6TCC		
countKRS6TCC = 0		
		
bfKRS6TCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6TCC:		
	if args.KRS6TCC in line.seq:	
		countKRS6TCC += 1
		
print 'KRS6TCC' , args.KRS6TCC, countKRS6TCC		
		
args.KRS6TCA = 'TATGAAATTGGTAAAGTATTTAGAAATGAATCAATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6TCA		
countKRS6TCA = 0		
		
bfKRS6TCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6TCA:		
	if args.KRS6TCA in line.seq:	
		countKRS6TCA += 1
		
print 'KRS6TCA' , args.KRS6TCA, countKRS6TCA		
		
args.KRS6TCG = 'TATGAAATTGGTAAAGTATTTAGAAATGAATCGATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6TCG		
countKRS6TCG = 0		
		
bfKRS6TCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6TCG:		
	if args.KRS6TCG in line.seq:	
		countKRS6TCG += 1
		
print 'KRS6TCG' , args.KRS6TCG, countKRS6TCG		
		
args.KRS6CCT = 'TATGAAATTGGTAAAGTATTTAGAAATGAACCTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6CCT		
countKRS6CCT = 0		
		
bfKRS6CCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6CCT:		
	if args.KRS6CCT in line.seq:	
		countKRS6CCT += 1
		
print 'KRS6CCT' , args.KRS6CCT, countKRS6CCT		
		
args.KRS6CCC = 'TATGAAATTGGTAAAGTATTTAGAAATGAACCCATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6CCC		
countKRS6CCC = 0		
		
bfKRS6CCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6CCC:		
	if args.KRS6CCC in line.seq:	
		countKRS6CCC += 1
		
print 'KRS6CCC' , args.KRS6CCC, countKRS6CCC		
		
args.KRS6CCA = 'TATGAAATTGGTAAAGTATTTAGAAATGAACCAATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6CCA		
countKRS6CCA = 0		
		
bfKRS6CCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6CCA:		
	if args.KRS6CCA in line.seq:	
		countKRS6CCA += 1
		
print 'KRS6CCA' , args.KRS6CCA, countKRS6CCA		
		
args.KRS6CCG = 'TATGAAATTGGTAAAGTATTTAGAAATGAACCGATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6CCG		
countKRS6CCG = 0		
		
bfKRS6CCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6CCG:		
	if args.KRS6CCG in line.seq:	
		countKRS6CCG += 1
		
print 'KRS6CCG' , args.KRS6CCG, countKRS6CCG		
		
args.KRS6ACT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAACTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6ACT		
countKRS6ACT = 0		
		
bfKRS6ACT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6ACT:		
	if args.KRS6ACT in line.seq:	
		countKRS6ACT += 1
		
print 'KRS6ACT' , args.KRS6ACT, countKRS6ACT		
		
args.KRS6ACC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAACCATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6ACC		
countKRS6ACC = 0		
		
bfKRS6ACC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6ACC:		
	if args.KRS6ACC in line.seq:	
		countKRS6ACC += 1
		
print 'KRS6ACC' , args.KRS6ACC, countKRS6ACC		
		
args.KRS6ACA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAACAATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6ACA		
countKRS6ACA = 0		
		
bfKRS6ACA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6ACA:		
	if args.KRS6ACA in line.seq:	
		countKRS6ACA += 1
		
print 'KRS6ACA' , args.KRS6ACA, countKRS6ACA		
		
args.KRS6ACG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAACGATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6ACG		
countKRS6ACG = 0		
		
bfKRS6ACG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6ACG:		
	if args.KRS6ACG in line.seq:	
		countKRS6ACG += 1
		
print 'KRS6ACG' , args.KRS6ACG, countKRS6ACG		
		
args.KRS6GCT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGCTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6GCT		
countKRS6GCT = 0		
		
bfKRS6GCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6GCT:		
	if args.KRS6GCT in line.seq:	
		countKRS6GCT += 1
		
print 'KRS6GCT' , args.KRS6GCT, countKRS6GCT		
		
args.KRS6GCC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGCCATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6GCC		
countKRS6GCC = 0		
		
bfKRS6GCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6GCC:		
	if args.KRS6GCC in line.seq:	
		countKRS6GCC += 1
		
print 'KRS6GCC' , args.KRS6GCC, countKRS6GCC		
		
args.KRS6GCA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGCAATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6GCA		
countKRS6GCA = 0		
		
bfKRS6GCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6GCA:		
	if args.KRS6GCA in line.seq:	
		countKRS6GCA += 1
		
print 'KRS6GCA' , args.KRS6GCA, countKRS6GCA		
		
args.KRS6GCG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGCGATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6GCG		
countKRS6GCG = 0		
		
bfKRS6GCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6GCG:		
	if args.KRS6GCG in line.seq:	
		countKRS6GCG += 1
		
print 'KRS6GCG' , args.KRS6GCG, countKRS6GCG		
		
args.KRS6TAT = 'TATGAAATTGGTAAAGTATTTAGAAATGAATATATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6TAT		
countKRS6TAT = 0		
		
bfKRS6TAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6TAT:		
	if args.KRS6TAT in line.seq:	
		countKRS6TAT += 1
		
print 'KRS6TAT' , args.KRS6TAT, countKRS6TAT		
		
args.KRS6TAC = 'TATGAAATTGGTAAAGTATTTAGAAATGAATACATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6TAC		
countKRS6TAC = 0		
		
bfKRS6TAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6TAC:		
	if args.KRS6TAC in line.seq:	
		countKRS6TAC += 1
		
print 'KRS6TAC' , args.KRS6TAC, countKRS6TAC		
		
args.KRS6TAA = 'TATGAAATTGGTAAAGTATTTAGAAATGAATAAATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6TAA		
countKRS6TAA = 0		
		
bfKRS6TAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6TAA:		
	if args.KRS6TAA in line.seq:	
		countKRS6TAA += 1
		
print 'KRS6TAA' , args.KRS6TAA, countKRS6TAA		
		
args.KRS6TAG = 'TATGAAATTGGTAAAGTATTTAGAAATGAATAGATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6TAG		
countKRS6TAG = 0		
		
bfKRS6TAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6TAG:		
	if args.KRS6TAG in line.seq:	
		countKRS6TAG += 1
		
print 'KRS6TAG' , args.KRS6TAG, countKRS6TAG		
		
args.KRS6CAT = 'TATGAAATTGGTAAAGTATTTAGAAATGAACATATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6CAT		
countKRS6CAT = 0		
		
bfKRS6CAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6CAT:		
	if args.KRS6CAT in line.seq:	
		countKRS6CAT += 1
		
print 'KRS6CAT' , args.KRS6CAT, countKRS6CAT		
		
args.KRS6CAC = 'TATGAAATTGGTAAAGTATTTAGAAATGAACACATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6CAC		
countKRS6CAC = 0		
		
bfKRS6CAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6CAC:		
	if args.KRS6CAC in line.seq:	
		countKRS6CAC += 1
		
print 'KRS6CAC' , args.KRS6CAC, countKRS6CAC		
		
args.KRS6CAA = 'TATGAAATTGGTAAAGTATTTAGAAATGAACAAATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6CAA		
countKRS6CAA = 0		
		
bfKRS6CAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6CAA:		
	if args.KRS6CAA in line.seq:	
		countKRS6CAA += 1
		
print 'KRS6CAA' , args.KRS6CAA, countKRS6CAA		
		
args.KRS6CAG = 'TATGAAATTGGTAAAGTATTTAGAAATGAACAGATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6CAG		
countKRS6CAG = 0		
		
bfKRS6CAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6CAG:		
	if args.KRS6CAG in line.seq:	
		countKRS6CAG += 1
		
print 'KRS6CAG' , args.KRS6CAG, countKRS6CAG		
		
args.KRS6AAT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAAATATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6AAT		
countKRS6AAT = 0		
		
bfKRS6AAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6AAT:		
	if args.KRS6AAT in line.seq:	
		countKRS6AAT += 1
		
print 'KRS6AAT' , args.KRS6AAT, countKRS6AAT		
		
args.KRS6AAC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAAACATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6AAC		
countKRS6AAC = 0		
		
bfKRS6AAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6AAC:		
	if args.KRS6AAC in line.seq:	
		countKRS6AAC += 1
		
print 'KRS6AAC' , args.KRS6AAC, countKRS6AAC		
		
args.KRS6AAA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAAAAATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6AAA		
countKRS6AAA = 0		
		
bfKRS6AAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6AAA:		
	if args.KRS6AAA in line.seq:	
		countKRS6AAA += 1
		
print 'KRS6AAA' , args.KRS6AAA, countKRS6AAA		
		
args.KRS6AAG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAAAGATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6AAG		
countKRS6AAG = 0		
		
bfKRS6AAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6AAG:		
	if args.KRS6AAG in line.seq:	
		countKRS6AAG += 1
		
print 'KRS6AAG' , args.KRS6AAG, countKRS6AAG		
		
args.KRS6GAT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGATATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6GAT		
countKRS6GAT = 0		
		
bfKRS6GAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6GAT:		
	if args.KRS6GAT in line.seq:	
		countKRS6GAT += 1
		
print 'KRS6GAT' , args.KRS6GAT, countKRS6GAT		
		
args.KRS6GAC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGACATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6GAC		
countKRS6GAC = 0		
		
bfKRS6GAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6GAC:		
	if args.KRS6GAC in line.seq:	
		countKRS6GAC += 1
		
print 'KRS6GAC' , args.KRS6GAC, countKRS6GAC		
		
args.KRS6GAA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGAAATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6GAA		
countKRS6GAA = 0		
		
bfKRS6GAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6GAA:		
	if args.KRS6GAA in line.seq:	
		countKRS6GAA += 1
		
print 'KRS6GAA' , args.KRS6GAA, countKRS6GAA		
		
args.KRS6GAG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGAGATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6GAG		
countKRS6GAG = 0		
		
bfKRS6GAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6GAG:		
	if args.KRS6GAG in line.seq:	
		countKRS6GAG += 1
		
print 'KRS6GAG' , args.KRS6GAG, countKRS6GAG		
		
args.KRS6TGT = 'TATGAAATTGGTAAAGTATTTAGAAATGAATGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6TGT		
countKRS6TGT = 0		
		
bfKRS6TGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6TGT:		
	if args.KRS6TGT in line.seq:	
		countKRS6TGT += 1
		
print 'KRS6TGT' , args.KRS6TGT, countKRS6TGT		
		
args.KRS6TGC = 'TATGAAATTGGTAAAGTATTTAGAAATGAATGCATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6TGC		
countKRS6TGC = 0		
		
bfKRS6TGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6TGC:		
	if args.KRS6TGC in line.seq:	
		countKRS6TGC += 1
		
print 'KRS6TGC' , args.KRS6TGC, countKRS6TGC		
		
args.KRS6TGA = 'TATGAAATTGGTAAAGTATTTAGAAATGAATGAATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6TGA		
countKRS6TGA = 0		
		
bfKRS6TGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6TGA:		
	if args.KRS6TGA in line.seq:	
		countKRS6TGA += 1
		
print 'KRS6TGA' , args.KRS6TGA, countKRS6TGA		
		
args.KRS6TGG = 'TATGAAATTGGTAAAGTATTTAGAAATGAATGGATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6TGG		
countKRS6TGG = 0		
		
bfKRS6TGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6TGG:		
	if args.KRS6TGG in line.seq:	
		countKRS6TGG += 1
		
print 'KRS6TGG' , args.KRS6TGG, countKRS6TGG		
		
args.KRS6CGT = 'TATGAAATTGGTAAAGTATTTAGAAATGAACGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6CGT		
countKRS6CGT = 0		
		
bfKRS6CGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6CGT:		
	if args.KRS6CGT in line.seq:	
		countKRS6CGT += 1
		
print 'KRS6CGT' , args.KRS6CGT, countKRS6CGT		
		
args.KRS6CGC = 'TATGAAATTGGTAAAGTATTTAGAAATGAACGCATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6CGC		
countKRS6CGC = 0		
		
bfKRS6CGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6CGC:		
	if args.KRS6CGC in line.seq:	
		countKRS6CGC += 1
		
print 'KRS6CGC' , args.KRS6CGC, countKRS6CGC		
		
args.KRS6CGA = 'TATGAAATTGGTAAAGTATTTAGAAATGAACGAATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6CGA		
countKRS6CGA = 0		
		
bfKRS6CGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6CGA:		
	if args.KRS6CGA in line.seq:	
		countKRS6CGA += 1
		
print 'KRS6CGA' , args.KRS6CGA, countKRS6CGA		
		
args.KRS6CGG = 'TATGAAATTGGTAAAGTATTTAGAAATGAACGGATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6CGG		
countKRS6CGG = 0		
		
bfKRS6CGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6CGG:		
	if args.KRS6CGG in line.seq:	
		countKRS6CGG += 1
		
print 'KRS6CGG' , args.KRS6CGG, countKRS6CGG		
		
args.KRS6AGT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAAGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6AGT		
countKRS6AGT = 0		
		
bfKRS6AGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6AGT:		
	if args.KRS6AGT in line.seq:	
		countKRS6AGT += 1
		
print 'KRS6AGT' , args.KRS6AGT, countKRS6AGT		
		
args.KRS6AGC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAAGCATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6AGC		
countKRS6AGC = 0		
		
bfKRS6AGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6AGC:		
	if args.KRS6AGC in line.seq:	
		countKRS6AGC += 1
		
print 'KRS6AGC' , args.KRS6AGC, countKRS6AGC		
		
args.KRS6AGA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAAGAATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6AGA		
countKRS6AGA = 0		
		
bfKRS6AGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6AGA:		
	if args.KRS6AGA in line.seq:	
		countKRS6AGA += 1
		
print 'KRS6AGA' , args.KRS6AGA, countKRS6AGA		
		
args.KRS6AGG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAAGGATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6AGG		
countKRS6AGG = 0		
		
bfKRS6AGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6AGG:		
	if args.KRS6AGG in line.seq:	
		countKRS6AGG += 1
		
print 'KRS6AGG' , args.KRS6AGG, countKRS6AGG		
		
args.KRS6GGT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6GGT		
countKRS6GGT = 0		
		
bfKRS6GGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6GGT:		
	if args.KRS6GGT in line.seq:	
		countKRS6GGT += 1
		
print 'KRS6GGT' , args.KRS6GGT, countKRS6GGT		
		
args.KRS6GGC = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGCATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6GGC		
countKRS6GGC = 0		
		
bfKRS6GGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6GGC:		
	if args.KRS6GGC in line.seq:	
		countKRS6GGC += 1
		
print 'KRS6GGC' , args.KRS6GGC, countKRS6GGC		
		
args.KRS6GGA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGAATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6GGA		
countKRS6GGA = 0		
		
bfKRS6GGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6GGA:		
	if args.KRS6GGA in line.seq:	
		countKRS6GGA += 1
		
print 'KRS6GGA' , args.KRS6GGA, countKRS6GGA		
		
args.KRS6GGG = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGGATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS6GGG		
countKRS6GGG = 0		
		
bfKRS6GGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS6GGG:		
	if args.KRS6GGG in line.seq:	
		countKRS6GGG += 1
		
print 'KRS6GGG' , args.KRS6GGG, countKRS6GGG		


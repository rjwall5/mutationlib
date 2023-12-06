#Created on Wed Sept 1 13:32:16 2021 by Richard Wall

import pysam, argparse

parser = argparse.ArgumentParser(description='Counts sequences from P. knowlesi KRS mutation library')
parser.add_argument('-i',nargs='?',dest='infile',help='Input BAM file')

args = parser.parse_args()
		
args.KRS3TTT = 'TATGAAATTGGTAAAGTATTTTTTAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3TTT		
countKRS3TTT = 0		
		
bfKRS3TTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3TTT:		
	if args.KRS3TTT in line.seq:	
		countKRS3TTT += 1
		
print 'KRS3TTT' , args.KRS3TTT, countKRS3TTT		
		
args.KRS3TTC = 'TATGAAATTGGTAAAGTATTTTTCAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3TTC		
countKRS3TTC = 0		
		
bfKRS3TTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3TTC:		
	if args.KRS3TTC in line.seq:	
		countKRS3TTC += 1
		
print 'KRS3TTC' , args.KRS3TTC, countKRS3TTC		
		
args.KRS3TTA = 'TATGAAATTGGTAAAGTATTTTTAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3TTA		
countKRS3TTA = 0		
		
bfKRS3TTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3TTA:		
	if args.KRS3TTA in line.seq:	
		countKRS3TTA += 1
		
print 'KRS3TTA' , args.KRS3TTA, countKRS3TTA		
		
args.KRS3TTG = 'TATGAAATTGGTAAAGTATTTTTGAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3TTG		
countKRS3TTG = 0		
		
bfKRS3TTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3TTG:		
	if args.KRS3TTG in line.seq:	
		countKRS3TTG += 1
		
print 'KRS3TTG' , args.KRS3TTG, countKRS3TTG		
		
args.KRS3CTT = 'TATGAAATTGGTAAAGTATTTCTTAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3CTT		
countKRS3CTT = 0		
		
bfKRS3CTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3CTT:		
	if args.KRS3CTT in line.seq:	
		countKRS3CTT += 1
		
print 'KRS3CTT' , args.KRS3CTT, countKRS3CTT		
		
args.KRS3CTC = 'TATGAAATTGGTAAAGTATTTCTCAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3CTC		
countKRS3CTC = 0		
		
bfKRS3CTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3CTC:		
	if args.KRS3CTC in line.seq:	
		countKRS3CTC += 1
		
print 'KRS3CTC' , args.KRS3CTC, countKRS3CTC		
		
args.KRS3CTA = 'TATGAAATTGGTAAAGTATTTCTAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3CTA		
countKRS3CTA = 0		
		
bfKRS3CTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3CTA:		
	if args.KRS3CTA in line.seq:	
		countKRS3CTA += 1
		
print 'KRS3CTA' , args.KRS3CTA, countKRS3CTA		
		
args.KRS3CTG = 'TATGAAATTGGTAAAGTATTTCTGAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3CTG		
countKRS3CTG = 0		
		
bfKRS3CTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3CTG:		
	if args.KRS3CTG in line.seq:	
		countKRS3CTG += 1
		
print 'KRS3CTG' , args.KRS3CTG, countKRS3CTG		
		
args.KRS3ATT = 'TATGAAATTGGTAAAGTATTTATTAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3ATT		
countKRS3ATT = 0		
		
bfKRS3ATT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3ATT:		
	if args.KRS3ATT in line.seq:	
		countKRS3ATT += 1
		
print 'KRS3ATT' , args.KRS3ATT, countKRS3ATT		
		
args.KRS3ATC = 'TATGAAATTGGTAAAGTATTTATCAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3ATC		
countKRS3ATC = 0		
		
bfKRS3ATC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3ATC:		
	if args.KRS3ATC in line.seq:	
		countKRS3ATC += 1
		
print 'KRS3ATC' , args.KRS3ATC, countKRS3ATC		
		
args.KRS3ATA = 'TATGAAATTGGTAAAGTATTTATAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3ATA		
countKRS3ATA = 0		
		
bfKRS3ATA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3ATA:		
	if args.KRS3ATA in line.seq:	
		countKRS3ATA += 1
		
print 'KRS3ATA' , args.KRS3ATA, countKRS3ATA		
		
args.KRS3ATG = 'TATGAAATTGGTAAAGTATTTATGAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3ATG		
countKRS3ATG = 0		
		
bfKRS3ATG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3ATG:		
	if args.KRS3ATG in line.seq:	
		countKRS3ATG += 1
		
print 'KRS3ATG' , args.KRS3ATG, countKRS3ATG		
		
args.KRS3GTT = 'TATGAAATTGGTAAAGTATTTGTTAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3GTT		
countKRS3GTT = 0		
		
bfKRS3GTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3GTT:		
	if args.KRS3GTT in line.seq:	
		countKRS3GTT += 1
		
print 'KRS3GTT' , args.KRS3GTT, countKRS3GTT		
		
args.KRS3GTC = 'TATGAAATTGGTAAAGTATTTGTCAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3GTC		
countKRS3GTC = 0		
		
bfKRS3GTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3GTC:		
	if args.KRS3GTC in line.seq:	
		countKRS3GTC += 1
		
print 'KRS3GTC' , args.KRS3GTC, countKRS3GTC		
		
args.KRS3GTA = 'TATGAAATTGGTAAAGTATTTGTAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3GTA		
countKRS3GTA = 0		
		
bfKRS3GTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3GTA:		
	if args.KRS3GTA in line.seq:	
		countKRS3GTA += 1
		
print 'KRS3GTA' , args.KRS3GTA, countKRS3GTA		
		
args.KRS3GTG = 'TATGAAATTGGTAAAGTATTTGTGAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3GTG

countKRS3GTG = 0		
		
bfKRS3GTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3GTG:		
	if args.KRS3GTG in line.seq:	
		countKRS3GTG += 1
		
print 'KRS3GTG' , args.KRS3GTG, countKRS3GTG		
		
args.KRS3TCT = 'TATGAAATTGGTAAAGTATTTTCTAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3TCT		
countKRS3TCT = 0		
		
bfKRS3TCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3TCT:		
	if args.KRS3TCT in line.seq:	
		countKRS3TCT += 1
		
print 'KRS3TCT' , args.KRS3TCT, countKRS3TCT		
		
args.KRS3TCC = 'TATGAAATTGGTAAAGTATTTTCCAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3TCC		
countKRS3TCC = 0		
		
bfKRS3TCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3TCC:		
	if args.KRS3TCC in line.seq:	
		countKRS3TCC += 1
		
print 'KRS3TCC' , args.KRS3TCC, countKRS3TCC		
		
args.KRS3TCA = 'TATGAAATTGGTAAAGTATTTTCAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3TCA		
countKRS3TCA = 0		
		
bfKRS3TCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3TCA:		
	if args.KRS3TCA in line.seq:	
		countKRS3TCA += 1
		
print 'KRS3TCA' , args.KRS3TCA, countKRS3TCA		
		
args.KRS3TCG = 'TATGAAATTGGTAAAGTATTTTCGAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3TCG		
countKRS3TCG = 0		
		
bfKRS3TCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3TCG:		
	if args.KRS3TCG in line.seq:	
		countKRS3TCG += 1
		
print 'KRS3TCG' , args.KRS3TCG, countKRS3TCG		
		
args.KRS3CCT = 'TATGAAATTGGTAAAGTATTTCCTAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3CCT		
countKRS3CCT = 0		
		
bfKRS3CCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3CCT:		
	if args.KRS3CCT in line.seq:	
		countKRS3CCT += 1
		
print 'KRS3CCT' , args.KRS3CCT, countKRS3CCT		
		
args.KRS3CCC = 'TATGAAATTGGTAAAGTATTTCCCAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3CCC		
countKRS3CCC = 0		
		
bfKRS3CCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3CCC:		
	if args.KRS3CCC in line.seq:	
		countKRS3CCC += 1
		
print 'KRS3CCC' , args.KRS3CCC, countKRS3CCC		
		
args.KRS3CCA = 'TATGAAATTGGTAAAGTATTTCCAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3CCA		
countKRS3CCA = 0		
		
bfKRS3CCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3CCA:		
	if args.KRS3CCA in line.seq:	
		countKRS3CCA += 1
		
print 'KRS3CCA' , args.KRS3CCA, countKRS3CCA		
		
args.KRS3CCG = 'TATGAAATTGGTAAAGTATTTCCGAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3CCG		
countKRS3CCG = 0		
		
bfKRS3CCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3CCG:		
	if args.KRS3CCG in line.seq:	
		countKRS3CCG += 1
		
print 'KRS3CCG' , args.KRS3CCG, countKRS3CCG		
		
args.KRS3ACT = 'TATGAAATTGGTAAAGTATTTACTAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3ACT		
countKRS3ACT = 0		
		
bfKRS3ACT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3ACT:		
	if args.KRS3ACT in line.seq:	
		countKRS3ACT += 1
		
print 'KRS3ACT' , args.KRS3ACT, countKRS3ACT		
		
args.KRS3ACC = 'TATGAAATTGGTAAAGTATTTACCAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3ACC		
countKRS3ACC = 0		
		
bfKRS3ACC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3ACC:		
	if args.KRS3ACC in line.seq:	
		countKRS3ACC += 1
		
print 'KRS3ACC' , args.KRS3ACC, countKRS3ACC		
		
args.KRS3ACA = 'TATGAAATTGGTAAAGTATTTACAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3ACA		
countKRS3ACA = 0		
		
bfKRS3ACA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3ACA:		
	if args.KRS3ACA in line.seq:	
		countKRS3ACA += 1
		
print 'KRS3ACA' , args.KRS3ACA, countKRS3ACA		
		
args.KRS3ACG = 'TATGAAATTGGTAAAGTATTTACGAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3ACG		
countKRS3ACG = 0		
		
bfKRS3ACG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3ACG:		
	if args.KRS3ACG in line.seq:	
		countKRS3ACG += 1
		
print 'KRS3ACG' , args.KRS3ACG, countKRS3ACG		
		
args.KRS3GCT = 'TATGAAATTGGTAAAGTATTTGCTAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3GCT		
countKRS3GCT = 0		
		
bfKRS3GCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3GCT:		
	if args.KRS3GCT in line.seq:	
		countKRS3GCT += 1
		
print 'KRS3GCT' , args.KRS3GCT, countKRS3GCT		
		
args.KRS3GCC = 'TATGAAATTGGTAAAGTATTTGCCAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3GCC		
countKRS3GCC = 0		
		
bfKRS3GCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3GCC:		
	if args.KRS3GCC in line.seq:	
		countKRS3GCC += 1
		
print 'KRS3GCC' , args.KRS3GCC, countKRS3GCC		
		
args.KRS3GCA = 'TATGAAATTGGTAAAGTATTTGCAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3GCA		
countKRS3GCA = 0		
		
bfKRS3GCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3GCA:		
	if args.KRS3GCA in line.seq:	
		countKRS3GCA += 1
		
print 'KRS3GCA' , args.KRS3GCA, countKRS3GCA		
		
args.KRS3GCG = 'TATGAAATTGGTAAAGTATTTGCGAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3GCG		
countKRS3GCG = 0		
		
bfKRS3GCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3GCG:		
	if args.KRS3GCG in line.seq:	
		countKRS3GCG += 1
		
print 'KRS3GCG' , args.KRS3GCG, countKRS3GCG		
		
args.KRS3TAT = 'TATGAAATTGGTAAAGTATTTTATAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3TAT		
countKRS3TAT = 0		
		
bfKRS3TAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3TAT:		
	if args.KRS3TAT in line.seq:	
		countKRS3TAT += 1
		
print 'KRS3TAT' , args.KRS3TAT, countKRS3TAT		
		
args.KRS3TAC = 'TATGAAATTGGTAAAGTATTTTACAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3TAC		
countKRS3TAC = 0		
		
bfKRS3TAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3TAC:		
	if args.KRS3TAC in line.seq:	
		countKRS3TAC += 1
		
print 'KRS3TAC' , args.KRS3TAC, countKRS3TAC		
		
args.KRS3TAA = 'TATGAAATTGGTAAAGTATTTTAAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3TAA		
countKRS3TAA = 0		
		
bfKRS3TAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3TAA:		
	if args.KRS3TAA in line.seq:	
		countKRS3TAA += 1
		
print 'KRS3TAA' , args.KRS3TAA, countKRS3TAA		
		
args.KRS3TAG = 'TATGAAATTGGTAAAGTATTTTAGAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3TAG		
countKRS3TAG = 0		
		
bfKRS3TAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3TAG:		
	if args.KRS3TAG in line.seq:	
		countKRS3TAG += 1
		
print 'KRS3TAG' , args.KRS3TAG, countKRS3TAG		
		
args.KRS3CAT = 'TATGAAATTGGTAAAGTATTTCATAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3CAT		
countKRS3CAT = 0		
		
bfKRS3CAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3CAT:		
	if args.KRS3CAT in line.seq:	
		countKRS3CAT += 1
		
print 'KRS3CAT' , args.KRS3CAT, countKRS3CAT		
		
args.KRS3CAC = 'TATGAAATTGGTAAAGTATTTCACAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3CAC		
countKRS3CAC = 0		
		
bfKRS3CAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3CAC:		
	if args.KRS3CAC in line.seq:	
		countKRS3CAC += 1
		
print 'KRS3CAC' , args.KRS3CAC, countKRS3CAC		
		
args.KRS3CAA = 'TATGAAATTGGTAAAGTATTTCAAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3CAA		
countKRS3CAA = 0		
		
bfKRS3CAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3CAA:		
	if args.KRS3CAA in line.seq:	
		countKRS3CAA += 1
		
print 'KRS3CAA' , args.KRS3CAA, countKRS3CAA		
		
args.KRS3CAG = 'TATGAAATTGGTAAAGTATTTCAGAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3CAG		
countKRS3CAG = 0		
		
bfKRS3CAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3CAG:		
	if args.KRS3CAG in line.seq:	
		countKRS3CAG += 1
		
print 'KRS3CAG' , args.KRS3CAG, countKRS3CAG		
		
args.KRS3AAT = 'TATGAAATTGGTAAAGTATTTAATAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3AAT		
countKRS3AAT = 0		
		
bfKRS3AAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3AAT:		
	if args.KRS3AAT in line.seq:	
		countKRS3AAT += 1
		
print 'KRS3AAT' , args.KRS3AAT, countKRS3AAT		
		
args.KRS3AAC = 'TATGAAATTGGTAAAGTATTTAACAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3AAC		
countKRS3AAC = 0		
		
bfKRS3AAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3AAC:		
	if args.KRS3AAC in line.seq:	
		countKRS3AAC += 1
		
print 'KRS3AAC' , args.KRS3AAC, countKRS3AAC		
		
args.KRS3AAA = 'TATGAAATTGGTAAAGTATTTAAAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3AAA		
countKRS3AAA = 0		
		
bfKRS3AAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3AAA:		
	if args.KRS3AAA in line.seq:	
		countKRS3AAA += 1
		
print 'KRS3AAA' , args.KRS3AAA, countKRS3AAA		
		
args.KRS3AAG = 'TATGAAATTGGTAAAGTATTTAAGAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3AAG		
countKRS3AAG = 0		
		
bfKRS3AAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3AAG:		
	if args.KRS3AAG in line.seq:	
		countKRS3AAG += 1
		
print 'KRS3AAG' , args.KRS3AAG, countKRS3AAG		
		
args.KRS3GAT = 'TATGAAATTGGTAAAGTATTTGATAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3GAT		
countKRS3GAT = 0		
		
bfKRS3GAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3GAT:		
	if args.KRS3GAT in line.seq:	
		countKRS3GAT += 1
		
print 'KRS3GAT' , args.KRS3GAT, countKRS3GAT		
		
args.KRS3GAC = 'TATGAAATTGGTAAAGTATTTGACAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3GAC		
countKRS3GAC = 0		
		
bfKRS3GAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3GAC:		
	if args.KRS3GAC in line.seq:	
		countKRS3GAC += 1
		
print 'KRS3GAC' , args.KRS3GAC, countKRS3GAC		
		
args.KRS3GAA = 'TATGAAATTGGTAAAGTATTTGAAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3GAA		
countKRS3GAA = 0		
		
bfKRS3GAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3GAA:		
	if args.KRS3GAA in line.seq:	
		countKRS3GAA += 1
		
print 'KRS3GAA' , args.KRS3GAA, countKRS3GAA		
		
args.KRS3GAG = 'TATGAAATTGGTAAAGTATTTGAGAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3GAG		
countKRS3GAG = 0		
		
bfKRS3GAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3GAG:		
	if args.KRS3GAG in line.seq:	
		countKRS3GAG += 1
		
print 'KRS3GAG' , args.KRS3GAG, countKRS3GAG		
		
args.KRS3TGT = 'TATGAAATTGGTAAAGTATTTTGTAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3TGT		
countKRS3TGT = 0		
		
bfKRS3TGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3TGT:		
	if args.KRS3TGT in line.seq:	
		countKRS3TGT += 1
		
print 'KRS3TGT' , args.KRS3TGT, countKRS3TGT		
		
args.KRS3TGC = 'TATGAAATTGGTAAAGTATTTTGCAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3TGC		
countKRS3TGC = 0		
		
bfKRS3TGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3TGC:		
	if args.KRS3TGC in line.seq:	
		countKRS3TGC += 1
		
print 'KRS3TGC' , args.KRS3TGC, countKRS3TGC		
		
args.KRS3TGA = 'TATGAAATTGGTAAAGTATTTTGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3TGA		
countKRS3TGA = 0		
		
bfKRS3TGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3TGA:		
	if args.KRS3TGA in line.seq:	
		countKRS3TGA += 1
		
print 'KRS3TGA' , args.KRS3TGA, countKRS3TGA		
		
args.KRS3TGG = 'TATGAAATTGGTAAAGTATTTTGGAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3TGG		
countKRS3TGG = 0		
		
bfKRS3TGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3TGG:		
	if args.KRS3TGG in line.seq:	
		countKRS3TGG += 1
		
print 'KRS3TGG' , args.KRS3TGG, countKRS3TGG		
		
args.KRS3CGT = 'TATGAAATTGGTAAAGTATTTCGTAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3CGT		
countKRS3CGT = 0		
		
bfKRS3CGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3CGT:		
	if args.KRS3CGT in line.seq:	
		countKRS3CGT += 1
		
print 'KRS3CGT' , args.KRS3CGT, countKRS3CGT		
		
args.KRS3CGC = 'TATGAAATTGGTAAAGTATTTCGCAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3CGC		
countKRS3CGC = 0		
		
bfKRS3CGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3CGC:		
	if args.KRS3CGC in line.seq:	
		countKRS3CGC += 1
		
print 'KRS3CGC' , args.KRS3CGC, countKRS3CGC		
		
args.KRS3CGA = 'TATGAAATTGGTAAAGTATTTCGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3CGA		
countKRS3CGA = 0		
		
bfKRS3CGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3CGA:		
	if args.KRS3CGA in line.seq:	
		countKRS3CGA += 1
		
print 'KRS3CGA' , args.KRS3CGA, countKRS3CGA		
		
args.KRS3CGG = 'TATGAAATTGGTAAAGTATTTCGGAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3CGG		
countKRS3CGG = 0		
		
bfKRS3CGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3CGG:		
	if args.KRS3CGG in line.seq:	
		countKRS3CGG += 1
		
print 'KRS3CGG' , args.KRS3CGG, countKRS3CGG		
		
args.KRS3AGT = 'TATGAAATTGGTAAAGTATTTAGTAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3AGT		
countKRS3AGT = 0		
		
bfKRS3AGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3AGT:		
	if args.KRS3AGT in line.seq:	
		countKRS3AGT += 1
		
print 'KRS3AGT' , args.KRS3AGT, countKRS3AGT		
		
args.KRS3AGC = 'TATGAAATTGGTAAAGTATTTAGCAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3AGC		
countKRS3AGC = 0		
		
bfKRS3AGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3AGC:		
	if args.KRS3AGC in line.seq:	
		countKRS3AGC += 1
		
print 'KRS3AGC' , args.KRS3AGC, countKRS3AGC		
		
args.KRS3AGA = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3AGA		
countKRS3AGA = 0		
		
bfKRS3AGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3AGA:		
	if args.KRS3AGA in line.seq:	
		countKRS3AGA += 1
		
print 'KRS3AGA' , args.KRS3AGA, countKRS3AGA		
		
args.KRS3AGG = 'TATGAAATTGGTAAAGTATTTAGGAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3AGG		
countKRS3AGG = 0		
		
bfKRS3AGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3AGG:		
	if args.KRS3AGG in line.seq:	
		countKRS3AGG += 1
		
print 'KRS3AGG' , args.KRS3AGG, countKRS3AGG		
		
args.KRS3GGT = 'TATGAAATTGGTAAAGTATTTGGTAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3GGT		
countKRS3GGT = 0		
		
bfKRS3GGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3GGT:		
	if args.KRS3GGT in line.seq:	
		countKRS3GGT += 1
		
print 'KRS3GGT' , args.KRS3GGT, countKRS3GGT		
		
args.KRS3GGC = 'TATGAAATTGGTAAAGTATTTGGCAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3GGC		
countKRS3GGC = 0		
		
bfKRS3GGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3GGC:		
	if args.KRS3GGC in line.seq:	
		countKRS3GGC += 1
		
print 'KRS3GGC' , args.KRS3GGC, countKRS3GGC		
		
args.KRS3GGA = 'TATGAAATTGGTAAAGTATTTGGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3GGA		
countKRS3GGA = 0		
		
bfKRS3GGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3GGA:		
	if args.KRS3GGA in line.seq:	
		countKRS3GGA += 1
		
print 'KRS3GGA' , args.KRS3GGA, countKRS3GGA		
		
args.KRS3GGG = 'TATGAAATTGGTAAAGTATTTGGGAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS3GGG		
countKRS3GGG = 0		
		
bfKRS3GGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS3GGG:		
	if args.KRS3GGG in line.seq:	
		countKRS3GGG += 1
		
print 'KRS3GGG' , args.KRS3GGG, countKRS3GGG		

args.KRS4TTT = 'TATGAAATTGGTAAAGTATTTAGATTTGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4TTT		
countKRS4TTT = 0		
		
bfKRS4TTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4TTT:		
	if args.KRS4TTT in line.seq:	
		countKRS4TTT += 1
		
print 'KRS4TTT' , args.KRS4TTT, countKRS4TTT		
		
args.KRS4TTC = 'TATGAAATTGGTAAAGTATTTAGATTCGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4TTC		
countKRS4TTC = 0		
		
bfKRS4TTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4TTC:		
	if args.KRS4TTC in line.seq:	
		countKRS4TTC += 1
		
print 'KRS4TTC' , args.KRS4TTC, countKRS4TTC		
		
args.KRS4TTA = 'TATGAAATTGGTAAAGTATTTAGATTAGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4TTA		
countKRS4TTA = 0		
		
bfKRS4TTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4TTA:		
	if args.KRS4TTA in line.seq:	
		countKRS4TTA += 1
		
print 'KRS4TTA' , args.KRS4TTA, countKRS4TTA		
		
args.KRS4TTG = 'TATGAAATTGGTAAAGTATTTAGATTGGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4TTG		
countKRS4TTG = 0		
		
bfKRS4TTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4TTG:		
	if args.KRS4TTG in line.seq:	
		countKRS4TTG += 1
		
print 'KRS4TTG' , args.KRS4TTG, countKRS4TTG		
		
args.KRS4CTT = 'TATGAAATTGGTAAAGTATTTAGACTTGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4CTT		
countKRS4CTT = 0		
		
bfKRS4CTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4CTT:		
	if args.KRS4CTT in line.seq:	
		countKRS4CTT += 1
		
print 'KRS4CTT' , args.KRS4CTT, countKRS4CTT		
		
args.KRS4CTC = 'TATGAAATTGGTAAAGTATTTAGACTCGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4CTC		
countKRS4CTC = 0		
		
bfKRS4CTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4CTC:		
	if args.KRS4CTC in line.seq:	
		countKRS4CTC += 1
		
print 'KRS4CTC' , args.KRS4CTC, countKRS4CTC		
		
args.KRS4CTA = 'TATGAAATTGGTAAAGTATTTAGACTAGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4CTA		
countKRS4CTA = 0		
		
bfKRS4CTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4CTA:		
	if args.KRS4CTA in line.seq:	
		countKRS4CTA += 1
		
print 'KRS4CTA' , args.KRS4CTA, countKRS4CTA		
		
args.KRS4CTG = 'TATGAAATTGGTAAAGTATTTAGACTGGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4CTG		
countKRS4CTG = 0		
		
bfKRS4CTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4CTG:		
	if args.KRS4CTG in line.seq:	
		countKRS4CTG += 1
		
print 'KRS4CTG' , args.KRS4CTG, countKRS4CTG		
		
args.KRS4ATT = 'TATGAAATTGGTAAAGTATTTAGAATTGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4ATT		
countKRS4ATT = 0		
		
bfKRS4ATT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4ATT:		
	if args.KRS4ATT in line.seq:	
		countKRS4ATT += 1
		
print 'KRS4ATT' , args.KRS4ATT, countKRS4ATT		
		
args.KRS4ATC = 'TATGAAATTGGTAAAGTATTTAGAATCGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4ATC		
countKRS4ATC = 0		
		
bfKRS4ATC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4ATC:		
	if args.KRS4ATC in line.seq:	
		countKRS4ATC += 1
		
print 'KRS4ATC' , args.KRS4ATC, countKRS4ATC		
		
args.KRS4ATA = 'TATGAAATTGGTAAAGTATTTAGAATAGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4ATA		
countKRS4ATA = 0		
		
bfKRS4ATA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4ATA:		
	if args.KRS4ATA in line.seq:	
		countKRS4ATA += 1
		
print 'KRS4ATA' , args.KRS4ATA, countKRS4ATA		
		
args.KRS4ATG = 'TATGAAATTGGTAAAGTATTTAGAATGGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4ATG		
countKRS4ATG = 0		
		
bfKRS4ATG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4ATG:		
	if args.KRS4ATG in line.seq:	
		countKRS4ATG += 1
		
print 'KRS4ATG' , args.KRS4ATG, countKRS4ATG		
		
args.KRS4GTT = 'TATGAAATTGGTAAAGTATTTAGAGTTGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4GTT		
countKRS4GTT = 0		
		
bfKRS4GTT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4GTT:		
	if args.KRS4GTT in line.seq:	
		countKRS4GTT += 1
		
print 'KRS4GTT' , args.KRS4GTT, countKRS4GTT		
		
args.KRS4GTC = 'TATGAAATTGGTAAAGTATTTAGAGTCGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4GTC		
countKRS4GTC = 0		
		
bfKRS4GTC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4GTC:		
	if args.KRS4GTC in line.seq:	
		countKRS4GTC += 1
		
print 'KRS4GTC' , args.KRS4GTC, countKRS4GTC		
		
args.KRS4GTA = 'TATGAAATTGGTAAAGTATTTAGAGTAGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4GTA		
countKRS4GTA = 0		
		
bfKRS4GTA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4GTA:		
	if args.KRS4GTA in line.seq:	
		countKRS4GTA += 1
		
print 'KRS4GTA' , args.KRS4GTA, countKRS4GTA		
		
args.KRS4GTG = 'TATGAAATTGGTAAAGTATTTAGAGTGGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4GTG

countKRS4GTG = 0		
		
bfKRS4GTG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4GTG:		
	if args.KRS4GTG in line.seq:	
		countKRS4GTG += 1
		
print 'KRS4GTG' , args.KRS4GTG, countKRS4GTG		
		
args.KRS4TCT = 'TATGAAATTGGTAAAGTATTTAGATCTGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4TCT		
countKRS4TCT = 0		
		
bfKRS4TCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4TCT:		
	if args.KRS4TCT in line.seq:	
		countKRS4TCT += 1
		
print 'KRS4TCT' , args.KRS4TCT, countKRS4TCT		
		
args.KRS4TCC = 'TATGAAATTGGTAAAGTATTTAGATCCGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4TCC		
countKRS4TCC = 0		
		
bfKRS4TCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4TCC:		
	if args.KRS4TCC in line.seq:	
		countKRS4TCC += 1
		
print 'KRS4TCC' , args.KRS4TCC, countKRS4TCC		
		
args.KRS4TCA = 'TATGAAATTGGTAAAGTATTTAGATCAGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4TCA		
countKRS4TCA = 0		
		
bfKRS4TCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4TCA:		
	if args.KRS4TCA in line.seq:	
		countKRS4TCA += 1
		
print 'KRS4TCA' , args.KRS4TCA, countKRS4TCA		
		
args.KRS4TCG = 'TATGAAATTGGTAAAGTATTTAGATCGGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4TCG		
countKRS4TCG = 0		
		
bfKRS4TCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4TCG:		
	if args.KRS4TCG in line.seq:	
		countKRS4TCG += 1
		
print 'KRS4TCG' , args.KRS4TCG, countKRS4TCG		
		
args.KRS4CCT = 'TATGAAATTGGTAAAGTATTTAGACCTGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4CCT		
countKRS4CCT = 0		
		
bfKRS4CCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4CCT:		
	if args.KRS4CCT in line.seq:	
		countKRS4CCT += 1
		
print 'KRS4CCT' , args.KRS4CCT, countKRS4CCT		
		
args.KRS4CCC = 'TATGAAATTGGTAAAGTATTTAGACCCGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4CCC		
countKRS4CCC = 0		
		
bfKRS4CCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4CCC:		
	if args.KRS4CCC in line.seq:	
		countKRS4CCC += 1
		
print 'KRS4CCC' , args.KRS4CCC, countKRS4CCC		
		
args.KRS4CCA = 'TATGAAATTGGTAAAGTATTTAGACCAGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4CCA		
countKRS4CCA = 0		
		
bfKRS4CCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4CCA:		
	if args.KRS4CCA in line.seq:	
		countKRS4CCA += 1
		
print 'KRS4CCA' , args.KRS4CCA, countKRS4CCA		
		
args.KRS4CCG = 'TATGAAATTGGTAAAGTATTTAGACCGGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4CCG		
countKRS4CCG = 0		
		
bfKRS4CCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4CCG:		
	if args.KRS4CCG in line.seq:	
		countKRS4CCG += 1
		
print 'KRS4CCG' , args.KRS4CCG, countKRS4CCG		
		
args.KRS4ACT = 'TATGAAATTGGTAAAGTATTTAGAACTGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4ACT		
countKRS4ACT = 0		
		
bfKRS4ACT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4ACT:		
	if args.KRS4ACT in line.seq:	
		countKRS4ACT += 1
		
print 'KRS4ACT' , args.KRS4ACT, countKRS4ACT		
		
args.KRS4ACC = 'TATGAAATTGGTAAAGTATTTAGAACCGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4ACC		
countKRS4ACC = 0		
		
bfKRS4ACC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4ACC:		
	if args.KRS4ACC in line.seq:	
		countKRS4ACC += 1
		
print 'KRS4ACC' , args.KRS4ACC, countKRS4ACC		
		
args.KRS4ACA = 'TATGAAATTGGTAAAGTATTTAGAACAGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4ACA		
countKRS4ACA = 0		
		
bfKRS4ACA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4ACA:		
	if args.KRS4ACA in line.seq:	
		countKRS4ACA += 1
		
print 'KRS4ACA' , args.KRS4ACA, countKRS4ACA		
		
args.KRS4ACG = 'TATGAAATTGGTAAAGTATTTAGAACGGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4ACG		
countKRS4ACG = 0		
		
bfKRS4ACG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4ACG:		
	if args.KRS4ACG in line.seq:	
		countKRS4ACG += 1
		
print 'KRS4ACG' , args.KRS4ACG, countKRS4ACG		
		
args.KRS4GCT = 'TATGAAATTGGTAAAGTATTTAGAGCTGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4GCT		
countKRS4GCT = 0		
		
bfKRS4GCT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4GCT:		
	if args.KRS4GCT in line.seq:	
		countKRS4GCT += 1
		
print 'KRS4GCT' , args.KRS4GCT, countKRS4GCT		
		
args.KRS4GCC = 'TATGAAATTGGTAAAGTATTTAGAGCCGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4GCC		
countKRS4GCC = 0		
		
bfKRS4GCC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4GCC:		
	if args.KRS4GCC in line.seq:	
		countKRS4GCC += 1
		
print 'KRS4GCC' , args.KRS4GCC, countKRS4GCC		
		
args.KRS4GCA = 'TATGAAATTGGTAAAGTATTTAGAGCAGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4GCA		
countKRS4GCA = 0		
		
bfKRS4GCA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4GCA:		
	if args.KRS4GCA in line.seq:	
		countKRS4GCA += 1
		
print 'KRS4GCA' , args.KRS4GCA, countKRS4GCA		
		
args.KRS4GCG = 'TATGAAATTGGTAAAGTATTTAGAGCGGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4GCG		
countKRS4GCG = 0		
		
bfKRS4GCG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4GCG:		
	if args.KRS4GCG in line.seq:	
		countKRS4GCG += 1
		
print 'KRS4GCG' , args.KRS4GCG, countKRS4GCG		
		
args.KRS4TAT = 'TATGAAATTGGTAAAGTATTTAGATATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4TAT		
countKRS4TAT = 0		
		
bfKRS4TAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4TAT:		
	if args.KRS4TAT in line.seq:	
		countKRS4TAT += 1
		
print 'KRS4TAT' , args.KRS4TAT, countKRS4TAT		
		
args.KRS4TAC = 'TATGAAATTGGTAAAGTATTTAGATACGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4TAC		
countKRS4TAC = 0		
		
bfKRS4TAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4TAC:		
	if args.KRS4TAC in line.seq:	
		countKRS4TAC += 1
		
print 'KRS4TAC' , args.KRS4TAC, countKRS4TAC		
		
args.KRS4TAA = 'TATGAAATTGGTAAAGTATTTAGATAAGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4TAA		
countKRS4TAA = 0		
		
bfKRS4TAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4TAA:		
	if args.KRS4TAA in line.seq:	
		countKRS4TAA += 1
		
print 'KRS4TAA' , args.KRS4TAA, countKRS4TAA		
		
args.KRS4TAG = 'TATGAAATTGGTAAAGTATTTAGATAGGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4TAG		
countKRS4TAG = 0		
		
bfKRS4TAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4TAG:		
	if args.KRS4TAG in line.seq:	
		countKRS4TAG += 1
		
print 'KRS4TAG' , args.KRS4TAG, countKRS4TAG		
		
args.KRS4CAT = 'TATGAAATTGGTAAAGTATTTAGACATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4CAT		
countKRS4CAT = 0		
		
bfKRS4CAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4CAT:		
	if args.KRS4CAT in line.seq:	
		countKRS4CAT += 1
		
print 'KRS4CAT' , args.KRS4CAT, countKRS4CAT		
		
args.KRS4CAC = 'TATGAAATTGGTAAAGTATTTAGACACGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4CAC		
countKRS4CAC = 0		
		
bfKRS4CAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4CAC:		
	if args.KRS4CAC in line.seq:	
		countKRS4CAC += 1
		
print 'KRS4CAC' , args.KRS4CAC, countKRS4CAC		
		
args.KRS4CAA = 'TATGAAATTGGTAAAGTATTTAGACAAGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4CAA		
countKRS4CAA = 0		
		
bfKRS4CAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4CAA:		
	if args.KRS4CAA in line.seq:	
		countKRS4CAA += 1
		
print 'KRS4CAA' , args.KRS4CAA, countKRS4CAA		
		
args.KRS4CAG = 'TATGAAATTGGTAAAGTATTTAGACAGGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4CAG		
countKRS4CAG = 0		
		
bfKRS4CAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4CAG:		
	if args.KRS4CAG in line.seq:	
		countKRS4CAG += 1
		
print 'KRS4CAG' , args.KRS4CAG, countKRS4CAG		
		
args.KRS4AAT = 'TATGAAATTGGTAAAGTATTTAGAAATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4AAT		
countKRS4AAT = 0		
		
bfKRS4AAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4AAT:		
	if args.KRS4AAT in line.seq:	
		countKRS4AAT += 1
		
print 'KRS4AAT' , args.KRS4AAT, countKRS4AAT		
		
args.KRS4AAC = 'TATGAAATTGGTAAAGTATTTAGAAACGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4AAC		
countKRS4AAC = 0		
		
bfKRS4AAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4AAC:		
	if args.KRS4AAC in line.seq:	
		countKRS4AAC += 1
		
print 'KRS4AAC' , args.KRS4AAC, countKRS4AAC		
		
args.KRS4AAA = 'TATGAAATTGGTAAAGTATTTAGAAAAGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4AAA		
countKRS4AAA = 0		
		
bfKRS4AAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4AAA:		
	if args.KRS4AAA in line.seq:	
		countKRS4AAA += 1
		
print 'KRS4AAA' , args.KRS4AAA, countKRS4AAA		
		
args.KRS4AAG = 'TATGAAATTGGTAAAGTATTTAGAAAGGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4AAG		
countKRS4AAG = 0		
		
bfKRS4AAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4AAG:		
	if args.KRS4AAG in line.seq:	
		countKRS4AAG += 1
		
print 'KRS4AAG' , args.KRS4AAG, countKRS4AAG		
		
args.KRS4GAT = 'TATGAAATTGGTAAAGTATTTAGAGATGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4GAT		
countKRS4GAT = 0		
		
bfKRS4GAT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4GAT:		
	if args.KRS4GAT in line.seq:	
		countKRS4GAT += 1
		
print 'KRS4GAT' , args.KRS4GAT, countKRS4GAT		
		
args.KRS4GAC = 'TATGAAATTGGTAAAGTATTTAGAGACGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4GAC		
countKRS4GAC = 0		
		
bfKRS4GAC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4GAC:		
	if args.KRS4GAC in line.seq:	
		countKRS4GAC += 1
		
print 'KRS4GAC' , args.KRS4GAC, countKRS4GAC		
		
args.KRS4GAA = 'TATGAAATTGGTAAAGTATTTAGAGAAGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4GAA		
countKRS4GAA = 0		
		
bfKRS4GAA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4GAA:		
	if args.KRS4GAA in line.seq:	
		countKRS4GAA += 1
		
print 'KRS4GAA' , args.KRS4GAA, countKRS4GAA		
		
args.KRS4GAG = 'TATGAAATTGGTAAAGTATTTAGAGAGGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4GAG		
countKRS4GAG = 0		
		
bfKRS4GAG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4GAG:		
	if args.KRS4GAG in line.seq:	
		countKRS4GAG += 1
		
print 'KRS4GAG' , args.KRS4GAG, countKRS4GAG		
		
args.KRS4TGT = 'TATGAAATTGGTAAAGTATTTAGATGTGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4TGT		
countKRS4TGT = 0		
		
bfKRS4TGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4TGT:		
	if args.KRS4TGT in line.seq:	
		countKRS4TGT += 1
		
print 'KRS4TGT' , args.KRS4TGT, countKRS4TGT		
		
args.KRS4TGC = 'TATGAAATTGGTAAAGTATTTAGATGCGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4TGC		
countKRS4TGC = 0		
		
bfKRS4TGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4TGC:		
	if args.KRS4TGC in line.seq:	
		countKRS4TGC += 1
		
print 'KRS4TGC' , args.KRS4TGC, countKRS4TGC		
		
args.KRS4TGA = 'TATGAAATTGGTAAAGTATTTAGATGAGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4TGA		
countKRS4TGA = 0		
		
bfKRS4TGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4TGA:		
	if args.KRS4TGA in line.seq:	
		countKRS4TGA += 1
		
print 'KRS4TGA' , args.KRS4TGA, countKRS4TGA		
		
args.KRS4TGG = 'TATGAAATTGGTAAAGTATTTAGATGGGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4TGG		
countKRS4TGG = 0		
		
bfKRS4TGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4TGG:		
	if args.KRS4TGG in line.seq:	
		countKRS4TGG += 1
		
print 'KRS4TGG' , args.KRS4TGG, countKRS4TGG		
		
args.KRS4CGT = 'TATGAAATTGGTAAAGTATTTAGACGTGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4CGT		
countKRS4CGT = 0		
		
bfKRS4CGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4CGT:		
	if args.KRS4CGT in line.seq:	
		countKRS4CGT += 1
		
print 'KRS4CGT' , args.KRS4CGT, countKRS4CGT		
		
args.KRS4CGC = 'TATGAAATTGGTAAAGTATTTAGACGCGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4CGC		
countKRS4CGC = 0		
		
bfKRS4CGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4CGC:		
	if args.KRS4CGC in line.seq:	
		countKRS4CGC += 1
		
print 'KRS4CGC' , args.KRS4CGC, countKRS4CGC		
		
args.KRS4CGA = 'TATGAAATTGGTAAAGTATTTAGACGAGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4CGA		
countKRS4CGA = 0		
		
bfKRS4CGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4CGA:		
	if args.KRS4CGA in line.seq:	
		countKRS4CGA += 1
		
print 'KRS4CGA' , args.KRS4CGA, countKRS4CGA		
		
args.KRS4CGG = 'TATGAAATTGGTAAAGTATTTAGACGGGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4CGG		
countKRS4CGG = 0		
		
bfKRS4CGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4CGG:		
	if args.KRS4CGG in line.seq:	
		countKRS4CGG += 1
		
print 'KRS4CGG' , args.KRS4CGG, countKRS4CGG		
		
args.KRS4AGT = 'TATGAAATTGGTAAAGTATTTAGAAGTGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4AGT		
countKRS4AGT = 0		
		
bfKRS4AGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4AGT:		
	if args.KRS4AGT in line.seq:	
		countKRS4AGT += 1
		
print 'KRS4AGT' , args.KRS4AGT, countKRS4AGT		
		
args.KRS4AGC = 'TATGAAATTGGTAAAGTATTTAGAAGCGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4AGC		
countKRS4AGC = 0		
		
bfKRS4AGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4AGC:		
	if args.KRS4AGC in line.seq:	
		countKRS4AGC += 1
		
print 'KRS4AGC' , args.KRS4AGC, countKRS4AGC		
		
args.KRS4AGA = 'TATGAAATTGGTAAAGTATTTAGAAGAGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4AGA		
countKRS4AGA = 0		
		
bfKRS4AGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4AGA:		
	if args.KRS4AGA in line.seq:	
		countKRS4AGA += 1
		
print 'KRS4AGA' , args.KRS4AGA, countKRS4AGA		
		
args.KRS4AGG = 'TATGAAATTGGTAAAGTATTTAGAAGGGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4AGG		
countKRS4AGG = 0		
		
bfKRS4AGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4AGG:		
	if args.KRS4AGG in line.seq:	
		countKRS4AGG += 1
		
print 'KRS4AGG' , args.KRS4AGG, countKRS4AGG		
		
args.KRS4GGT = 'TATGAAATTGGTAAAGTATTTAGAGGTGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4GGT		
countKRS4GGT = 0		
		
bfKRS4GGT = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4GGT:		
	if args.KRS4GGT in line.seq:	
		countKRS4GGT += 1
		
print 'KRS4GGT' , args.KRS4GGT, countKRS4GGT		
		
args.KRS4GGC = 'TATGAAATTGGTAAAGTATTTAGAGGCGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4GGC		
countKRS4GGC = 0		
		
bfKRS4GGC = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4GGC:		
	if args.KRS4GGC in line.seq:	
		countKRS4GGC += 1
		
print 'KRS4GGC' , args.KRS4GGC, countKRS4GGC		
		
args.KRS4GGA = 'TATGAAATTGGTAAAGTATTTAGAGGAGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4GGA		
countKRS4GGA = 0		
		
bfKRS4GGA = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4GGA:		
	if args.KRS4GGA in line.seq:	
		countKRS4GGA += 1
		
print 'KRS4GGA' , args.KRS4GGA, countKRS4GGA		
		
args.KRS4GGG = 'TATGAAATTGGTAAAGTATTTAGAGGGGAAGGTATAGATAATACACATAATCCTGAATTTACTTCGTGTGAATTTTATTGGGCATATGCT' #sequence KRS4GGG		
countKRS4GGG = 0		
		
bfKRS4GGG = pysam.Samfile(args.infile,"rb")		
		
for line in bfKRS4GGG:		
	if args.KRS4GGG in line.seq:	
		countKRS4GGG += 1
		
print 'KRS4GGG' , args.KRS4GGG, countKRS4GGG		


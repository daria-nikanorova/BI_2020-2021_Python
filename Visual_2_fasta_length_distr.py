from Bio import SeqIO
import matplotlib.pyplot as plt

#set parameters for all future graphs
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['figure.figsize'] = [15, 8]
plt.rcParams['font.size'] = 15

records = []

for record in SeqIO.parse("data/SRR1705858.fasta", "fasta"):
    records += [len(record.seq)]

num_of_reads = [records.count(i) for i in set(records)]
lengths = list(set(records))

#print((num_of_reads), (lengths))
plt.plot(lengths, num_of_reads, color = '#e31a1c')

#add title
plt.title('Sequence length distribution')

#add axes labels
plt.xlabel('Sequence length (bp)')
plt.ylabel('Number of sequences')

#add grid
plt.grid()

#save plot
plt.savefig('Sequence_length_distribution.png')

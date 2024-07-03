# Code for mCaller
~/nanopolish/nanopolish index -d fast5/ dS.fastq
bwa index 1448A.fasta

bwa mem -x ont2d -t 20 ../../ref/1448A.fasta dS.fastq | samtools view -Sb - | samtools sort -T mcaller.sorted -o mcaller.sorted.bam

samtools index mcaller.sorted.bam

~/nanopolish/nanopolish eventalign -t 20 --scale-events -n -r dS.fastq -b mcaller.sorted.bam -g ../../ref/1448A.fasta > mCaller.eventalign.tsv

mCaller.py <-m GATC or -p positions.txt> -r <reference>.fasta -d r95_twobase_model_NN_6_m6A.pkl -e <filename>.eventalign.tsv -f <filename>.fastq -b A

nohup ~/mCaller/mCaller.py -m A -t 20 -r /media/lu/lu2023/ref/1448A.fasta -d ~/mCaller/r95_twobase_model_NN_6_m6A.pkl -e 0104dSmCaller.eventalign.tsv  -f /media/lu/lu2023/6mA/0104KO_dSample/dS.fastq -b A &

 ~/mCaller/make_bed.py -f 0104dSmCaller.eventalign.diffs.6 -d 15 -t 0

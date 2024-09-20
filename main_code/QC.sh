## run dorado basecaller for each sample
## For R10.4.1 5kHz
dorado basecaller dna_r10.4.1_e8.2_400bps_sup@v4.3.0 -r pod5/ > basecall.bam 
## For R10.4.1 4kHz (ecoli, kp)
dorado basecaller ../dna_r10.4.1_e8.2_400bps_sup@v4.1.0 -r all.pod5 >  basecall.bam 
samtools bam2fq basecall.bam>final.fastq

## run giraffe 
giraffe estimate --input  final.fastq --cpu 64
giraffe observe --input  final.fastq --cpu 64 --ref ./1448a.fasta

## run minimap2
minimap2 --MD -t 32 -ax map-ont 1448a.fasta.fasta final.fastq | samtools view -hbS -F 3844 - | samtools sort -@ 32 -o genomic.bam 
samtools index genomic.bam

## run samtools depth
samtools depth genomic.bam -a >coverage.txt

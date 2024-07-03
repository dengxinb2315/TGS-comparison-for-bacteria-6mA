## run dorado basecaller for each sample
dorado basecaller dna_r10.4.1_e8.2_400bps_sup@v4.3.0 -r pod5/ > basecall.bam 
samtools bam2fq basecall.bam>final.fastq

## run giraffe 
giraffe estimate --input  final.fastq --cpu 64
giraffe observe --input  final.fastq --cpu 64 --ref ./1448a.fasta

## run minimap2
minimap2 --MD -t 32 -ax map-ont 1448a.fasta.fasta final.fastq | samtools view -hbS -F 32 - | samtools sort -@ 32 -o genomic.bam 
samtools index genomic.bam

## run samtools depth
samtools depth genomic.bam -a >coverage.txt

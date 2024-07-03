## Dorado command
dorado basecaller dna_r10.4.1_e8.2_400bps_sup@v4.3.0 --modified-bases 6mA -r barcode01/ >mod_6mA_barcode01.bam
dorado aligner DC3000.fasta mod_6mA_barcode01.bam>DC3000_WT.bam
samtools sort -@ 16 DC3000_WT.bam >DC3000_WT_sorted.bam
modkit pileup DC3000_WT_sorted.bam DC_wt.bed  --ref DC3000.fasta

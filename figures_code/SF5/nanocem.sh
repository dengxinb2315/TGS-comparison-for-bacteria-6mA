$element is the position such as 5113
## current feature showcase
# r9
current_events_magnifier f5c_ev -i WT/file -c WGA/file --chrom NC_005773.3 --strand + --pos $element --pore r9 --len 10 --ref ../1448A.fasta -o nanoCEM_result_f5c_ev_$element --norm -t 64
# r10
current_events_magnifier f5c_ev -i WT/file -c WGA/file --chrom NC_005773.3 --strand + --pos $element --pore r10 --len 10 --ref ../1448A.fasta -o nanoCEM_result_f5c_ev_$element --norm -t 64

## alignment feature showcase
alignment_magnifier -i WGS/final.fastq -c WGA/final.fastq -r ./1448A.fasta --strand + --pos $element --len 10 --chrom NC_005773.3

$element is the position such as 5113
# r9 flow cell
current_events_magnifier f5c_ev -i WT/file -c WGA/file --chrom NC_005773.3 --strand + --pos $element --pore r9 --len 10 --ref ../1448A.fasta -o nanoCEM_result_f5c_ev_$element --norm -t 64

# r10 flow cell
current_events_magnifier f5c_ev -i WT/file -c WGA/file --chrom NC_005773.3 --strand + --pos $element --pore r10 --len 10 --ref ../1448A.fasta -o nanoCEM_result_f5c_ev_$element --norm -t 64
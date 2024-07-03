# preprocessing fast5 files
nanodisco preprocess -p 4 -f dataset/sample_WGA -s WGA -o analysis/preprocessed_subset -r ref.fa
nanodisco preprocess -p 4 -f dataset/sample_WGS -s WGS -o analysis/preprocessed_subset -r ref.fa

# computing current differences
nanodisco difference -nj 4 -nc 1 -p 5 -i analysis/preprocessed_subset -o analysis/difference_subset -w WGA -n WGS -r ref.fa

 # merging current differences files
nanodisco merge -d analysis/difference_subset -o analysis -b sample

# motif detection
nanodisco motif -p 4 -b bacterial -d dataset/sample.RDS -o analysis -r ref.fa
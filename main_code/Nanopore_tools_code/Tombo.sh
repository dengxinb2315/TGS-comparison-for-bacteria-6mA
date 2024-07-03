## Tombo command:

# Tombo model_comp
tombo detect_modifications model_sample_compare  --fast5-basedirs single_1/fast5/ --control-fast5-basedirs single_2/fast5/  --processes 32 --statistics-file-basename sample.model_samp_comp_detect
tombo text_output browser_files --statistics-filename sample.model_samp_comp_detect.tombo.stats  --browser-file-basename sample.model_samp_comp_detect.tombo.stats --file-types statistic
# Tombo level_comp
tombo detect_modifications level_sample_compare  --fast5-basedirs single_1/fast5/ --alternate-fast5-basedirs single_2/fast5/  --processes 32 --statistics-file-basename sample.level_samp_comp_detect --store-p-value
tombo text_output browser_files --statistics-filename sample.level_samp_comp_detect.tombo.stats  --browser-file-basename sample.level_samp_comp_detect --file-types statistic
# Tombo de_novo
tombo detect_modifications de_novo --fast5-basedirs all_wga_fast5/ --rna --statistics-file-basename tombo_denovo --processes 32
tombo text_output browser_files --statistics-filename tombo_denovo.tombo.stats  --browser-file-basename sample.de_novo.tombo.stats --file-types statistic




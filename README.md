# TGS-comparison-for-bacteria-6mA

This GitHub repository contains all the custom scripts and shell commands used in our paper, **Comprehensive Comparison of Third-Generation Sequencing Tools for Bacteria 6mA Profiling**.

## Graphic abstract
![abstract](readme_fig/workflow.png)
## Data available
Because Oxford Nanopore's basecall model is updated frequently, we recommend using the latest basecaller model for re-calling.All raw signal files are uploaded to the NCBI (BIOPROJECT:[PRJNA1119015](https://ncbi.nlm.nih.gov/bioproject/?term=PRJNA1119015))

## Code available

**Notes:** The scripts are ordered according to their appearance in the figures.

### Envs

Mandatory software:

| Name         | Version  | Source|
|:-------------|:---------|:--------|
| **samtools** | v1.17    |conda|
| **minimap2** | v2.17    |conda|
| **python**   | \>=3.9.2 |conda|
| **nanoCEM**  | 0.0.5.8  |Pypi|
| **plotnine** | 0.9.1    |Pypi|

Optional software:


| Name            | Version | Source|
|:----------------|:--------|:--------|
| **tombo**       | v1.5    |conda|
| **nanopolish**  | v1.14.1 |conda|
| **harmmerhead** | 0.1.3   |Pypi|

### QC analysis

1. For each sample, we run the commands in [QC.sh](main_code/QC.sh). The basecalled **fastq** file and the alignment result (**bam** file) with the reference can be collected,
while giraffe will help to calculate the estimated features such as Q score and read length.
2. Python scripts in [Figure_1](figures_code/Fig1) will help to calculate the yield info and merge all sample's feature file and plot the distribution.

### Run all methods
Following the workflow, we executed all the commands for m6A modification detection tools found in [Main_shell](main_code/Nanopore_tools_code)

Besides, we provided a script called [read_tombo.py](main_code/Nanopore_tools_code/read_tombo.py) to merge the result from `tombo text_output` and output a **bed** file

    Usage: read_tombo.py [-h] [-t TOMBO_RESULT] [--ref REF] [--output OUTPUT]
    optional arguments:                                                      
      -h, --help            show this help message and exit                  
      -t TOMBO_RESULT, --tombo_result TOMBO_RESULT                       
                            suffix of tombo result                           
      --ref REF             reference path                                   
      --output OUTPUT       output path   

### Motif and site analysis

### Outliers analysis

### Showcase and application
After obtaining many modification sites, 
we used [nanoCEM](https://github.com/lrslab/nanoCEM) to showcase the analysis focusing on current and alignment feature, the commands are saved in [nanocem.sh](figures_code/SF5/nanocem.sh)

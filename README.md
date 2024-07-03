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

### Figure 1

1. For each sample, we run the commands in [QC.py](main_code/QC.sh). The basecalled **fastq** file and the alignment result (**bam** file) with the reference can be collected,
while giraffe will help to calculate the estimated features such as Q score and read length.
2. Python scripts in [Figure_1](Fig1) will help to calculate the yield info and merge all sample's feature file and plot the distribution.

### Figure 2
1. Following the workflow, we executed all the commands for m6A modification detection tools found in [Main_shell](main_code/Nanopore_tools_code)
2. 
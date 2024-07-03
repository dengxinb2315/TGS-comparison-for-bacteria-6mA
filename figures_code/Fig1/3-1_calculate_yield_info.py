import pysam
import pandas as pd
import numpy as np


def count_fastq(file_path):
    total_reads = 0
    total_bases = 0

    with open(file_path, 'r') as file:
        line_num = 0
        for line in file:
            line_num += 1

            if line_num % 4 == 2:  # 每个read的序列行
                total_reads += 1
                total_bases += len(line.strip())

    return total_reads, total_bases
def count_bam(bam_path):
    bam_file = pysam.AlignmentFile(bam_path, 'rb')
    read_num = 0
    align_num = 0
    read_name_dict = {}
    for read in bam_file.fetch():
        if read.is_secondary or read.is_supplementary:
            continue
        align_num = align_num + read.query_alignment_length
        if read.qname in read_name_dict:
            # print(1)
            read_name_dict[read.qname] = read_name_dict[read.qname] + 1
        else:
            read_name_dict[read.qname] = 1
        read_num = read_num + 1
    return read_num, align_num

input_path = "fastq_dir/"
folder_list={
    "1448A_WT":'1448A/WT',
    # "1448A_WGA1": '1448A/WGA1',
    # "1448A_WGA2": '1448A/WGA2',
    "1448A_WGA": '1448A/WGA',
    "1448A_0104KO":'1448A/0104_sub',
    "1448A_WT_R10":'1448A/R10_WT',
    "1448A_WGA_R10": '1448A/R10_WGA',
    "1448A_0104KO_R10": '1448A/R10_0104',
}

result_df=[]
for key,item in folder_list.items():
    fastq_path = input_path+item+"/final.fastq"
    bam_path=input_path+item+"/genomic.bam"
    total_read,total_base=count_fastq(fastq_path)
    aligned_read,aligned_base=count_bam(bam_path)
    data_list=[total_read,total_base,aligned_read,aligned_base,total_read-aligned_read,total_base-aligned_base,key]
    print(key,aligned_read/total_read,aligned_base/total_base)
    result_df.append(data_list)
result_df = pd.DataFrame(result_df)
result_df.columns=['total_read','total_base','aligned_read','aligned_base','not_aligned_read','not_aligned_base','group']
result_df.to_csv('aligned_num.csv',index=None)
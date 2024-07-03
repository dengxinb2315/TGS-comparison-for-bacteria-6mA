import pandas as pd
import numpy as np


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
    # "DC3000_WT_R10": 'DC3000/R10_WT',
    # "DC3000_WGA_R10": 'DC3000/R10_WGA',
    # "DC3000_WT1": 'DC3000/WT1',
    # "DC3000_WGA1": 'DC3000/WGA1',
    # "DC3000_WT2": 'DC3000/WT2',
    # "DC3000_WGA2": 'DC3000/WGA2',
}

df = pd.DataFrame()
for key,value in folder_list.items():
    input_file = input_path + value+"/results/estimated_quality/final_estimated_accuracy.txt"
    tem_df=pd.read_csv(input_file,sep='\t')
    tem_df['ID'] = tem_df['ID'].str[1:]
    input_map_file = input_path + value + '/results/observed_quality/final_observed_accuracy.txt'
    tem_df_map = pd.read_csv(input_map_file, sep='\t')
    tem_df_map = tem_df_map[['ID']]
    tem_df_map['Type']='Map'
    temp = pd.merge(tem_df,tem_df_map,how='left',on='ID')
    temp.fillna('Unmap',inplace=True)
    temp['Sample'] = key
    df = pd.concat([df, temp])
    print(key,tem_df['Q_value'].median(),temp[temp['Type']=='Map']['Q_value'].median())
print(1)
df.to_csv("estimate.csv",index=None)

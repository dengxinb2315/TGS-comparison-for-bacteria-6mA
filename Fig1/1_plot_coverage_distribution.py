import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
import plotnine as p9
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']

input_path = "fastq_dir/"
folder_list={
    "1448A_WT":'1448A/WT',
    "1448A_WGA": '1448A/WGA',
    "1448A_0104KO":'1448A/0104_sub',
    "1448A_WT_R10":'1448A/R10_WT',
    "1448A_WGA_R10": '1448A/R10_WGA',
    "1448A_0104KO_R10": '1448A/R10_0104',
}

df = pd.DataFrame()
for key,value in folder_list.items():
    input_map_file = input_path + value + 'coverage.txt'
    temp = pd.read_csv(input_map_file, sep='\t',header=None).sample(frac=0.1)
    temp['Sample'] = key
    print(key, temp[2].median(),(temp[2]>=50).sum()/temp.shape[0])
    df = pd.concat([df, temp])
name_list = ['1448A_WT',
'1448A_0104KO',
'1448A_WGA',
"1448A_WT_R10",
'1448A_0104KO_R10',
"1448A_WGA_R10",
# 'DC3000_WT_R10',
# 'DC3000_WGA_R10',
             ]
name_list.reverse()
category = pd.api.types.CategoricalDtype(categories=name_list, ordered=True)
df['Sample'] = df['Sample'].astype(category)
print(df.shape)
df.columns=['chrom','pos','coverage','Sample']
plot = p9.ggplot(df, p9.aes(x='Sample', y="coverage", fill='Sample')) \
       + p9.theme_bw() \
       + p9.ylim(0,1500)\
       + p9.labs(y="Coverage", x='') \
       + p9.scale_fill_manual(values={'1448A_WT':"#FFE4E0",
                                '1448A_WGA1':"#9BBFCF",
                                '1448A_WGA2':"#9BBFCF",
                                '1448A_WGA':"#C7A58B",
                                '1448A_0104KO':"#F8AC8C",
                                "1448A_WT_R10":"#D6E6E2",
                                '1448A_0104KO_R10':"#9AC9DB",
                                "1448A_WGA_R10":"#97AFB9",
                                'DC3000_WT_R10':"#6FB0F1",
                                'DC3000_WGA_R10':"#A4C1B4",
                                    'Unmap': "#D7D7D7"}) \
       + p9.theme(
    figure_size=(4.5, 3.5),
    axis_text=p9.element_text(size=12, family="Arial"),
    axis_title=p9.element_text(size=12, family="Arial"),
    panel_grid_minor=p9.element_blank(),
    title=p9.element_text(size=12, family="Arial"),
    legend_text=p9.element_text(size=8, family="Arial"),
    strip_background=p9.element_rect(alpha=0),
    strip_text=p9.element_text(size=12, family="Arial"),
    legend_position='none'
    )
plot = plot + p9.geom_density_ridges(color='none', width=1.5, style='right')
plot = plot + p9.geom_boxplot(outlier_shape='', width=0.1)
plot = plot + p9.coord_flip()
# result_df.to_csv("/t1/zhguo/Data/Ecoli_RNA/count_information/Q_value.csv",index=None)
print(plot)

plot.save("coverage_distribution.pdf",dpi=300)

import plotnine as p9
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

input_path = "fastq_dir/"
input_file = input_path + "/estimate.csv"

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']

df = pd.read_csv(input_file).sample(frac=0.5)

name_list = [
'1448A_WT',
'1448A_0104KO',
'1448A_WGA',
"1448A_WT_R10",
'1448A_0104KO_R10',
"1448A_WGA_R10",
# 'DC3000_WT_R10',
# 'DC3000_WGA_R10',
             ]

name_list.reverse()
df = pd.melt(df, id_vars=['Sample', 'Type'], value_vars=['Q_value', 'Read_length'])
# filter
df_group = df.groupby('variable')
df = pd.DataFrame()
for key, value in df_group:
    if key == 'Read_length':
        print(value.shape)
        value = value[value['value'] < 3500]
        print(value.shape)
    else:
        print(value.shape)
        value = value[value['value'] < 35]
        print(value.shape)
    df = pd.concat([df, value], axis=0)
# sort
df['Type'] = df.apply(lambda x: x['Sample'] if x['Type'] == 'Map' else x['Type'], axis=1)
category = pd.api.types.CategoricalDtype(categories=name_list, ordered=True)
df['Sample'] = df['Sample'].astype(category)
category = pd.api.types.CategoricalDtype(categories=["Unmap", '1448A_WT',
                                    '1448A_0104KO', '1448A_WGA',
                                    "1448A_WT_R10",  '1448A_0104KO_R10',
                                    "1448A_WGA_R10"], ordered=True)
df['Type'] = df['Type'].astype(category)
category = pd.api.types.CategoricalDtype(categories=['Q_value', 'Read_length'], ordered=True)
df['variable'] = df['variable'].astype(category)

pp = p9.ggplot(df, p9.aes(x='Sample', y='value', fill='Type')) \
     + p9.theme_bw() \
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
     + p9.labs(y="", x='') \
     + p9.theme(
    figure_size=(10, 5),
    axis_text=p9.element_text(size=12, family='Arial'),
    axis_title=p9.element_text(size=12, family='Arial'),
    panel_grid_minor=p9.element_blank(),
    title=p9.element_text(size=12, family='Arial'),
    strip_background=p9.element_rect(alpha=0),
    strip_text=p9.element_text(size=12, family='Arial'),
    legend_position='none'
) \
     + p9.facet_grid('~ variable', scales='free_x') \
     + p9.geom_violin(style='left-right',position=p9.position_dodge(0),width=2,color='none') \
     + p9.coord_flip()
print(pp)

# + p9.geom_boxplot(width=0.5 ,position=p9.position_dodge(0.7)) \

pp.save("Figure_estimated_feature_violinplot.pdf", dpi=300)

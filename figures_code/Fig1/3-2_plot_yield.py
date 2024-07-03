import plotnine as p9
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']


input_file = 'sample_data/aligned_num.csv'
df = pd.read_csv(input_file)

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
# color_list = ['#EFA8A9', '#FFE4E4', '#FFE4E4']
df = df[['aligned_read','aligned_base','not_aligned_read','not_aligned_base','group']]
df = pd.melt(df, value_vars=['aligned_read','aligned_base','not_aligned_read','not_aligned_base'], id_vars=['group'])
df['Type'] = df['variable'].apply(lambda x: "Read numbers" if x[-4:] == 'read' else "Base numbers")
df['value'] = df.apply(lambda x: x['value']/1000 if x['Type'] == "Read numbers" else x['value']/1000000, axis=1)
df['value'] = df['value'].round(2)
df['Map'] = df['variable'].apply(lambda x: "Unmap" if 'not' in x else "Map")
category = pd.api.types.CategoricalDtype(categories=name_list, ordered=True)
df['group'] = df['group'].astype(category)

df['Map']=df.apply(lambda x: x['group'] if x['Map']=='Map' else'Unmap',axis=1)
category = pd.api.types.CategoricalDtype(categories=["Unmap",'1448A_WT',
'1448A_0104KO',
'1448A_WGA',
"1448A_WT_R10",
'1448A_0104KO_R10',
"1448A_WGA_R10",
], ordered=True)
df['Map'] = df['Map'].astype(category)
category = pd.api.types.CategoricalDtype(categories=['Read numbers','Base numbers'], ordered=True)
df['Type'] = df['Type'].astype(category)
# + p9.scale_fill_manual(values={'WGA1': '#FFE4E4',
#                                'WGA2': '#FFE4E4',
#                                'WT': '#EFA8A9',
#                                'Unmap': "#D7D7D7"}) \
#  \

pp = p9.ggplot(df, p9.aes(x='group',y='value',fill='Map'))\
    + p9.geom_bar(stat='identity',width=0.75,alpha=1)\
    + p9.theme_bw() \
    + p9.labs(y="", x='')\
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
    + p9.geom_text(p9.aes(label="value"),size=10,family='Arial',position=p9.position_stack(0.5))\
    + p9.theme(
            figure_size=(10, 5),
            axis_text=p9.element_text(size=12,family='Arial'),
            axis_title=p9.element_text(size=12,family='Arial'),
            panel_grid_minor=p9.element_blank(),
            title=p9.element_text(size=12,family='Arial'),
            legend_title=p9.element_blank(),
            legend_position='none',
            strip_background = p9.element_rect(alpha=0),
            legend_text=p9.element_text(size=10,family='Arial')
                      )\
    + p9.coord_flip()\
    + p9.facet_grid('~ Type',scales='free_x')
print(pp)
pp.save("yield.pdf",dpi=300)
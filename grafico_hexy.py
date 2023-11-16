import plotly.figure_factory as ff
import pandas as pd

#entrada de dados
df = pd.read_excel("americaLatina.xlsx")
df.head()
print(df)
#grafico
fig = ff.create_hexbin_mapbox(data_frame = df, 
                              lat = "latitude",
                              lon = "longitude", 
                              mapbox_style = "carto-positron", 
                              min_count = 1, 
                              show_original_data = True,
                              original_data_marker = dict(size = 10,
                                                          opacity = 0.6,
                                                          color = "black"),
                              zoom = 2,
                              color = "PIB per capita",
                              labels = {"color": "PIB per capita"},
                              nx_hexagon = 6,
                              opacity = 0.9,
                              color_continuous_scale = "Magma_r")
fig.show()
import folium
import geopandas as gpd
from shapely import wkt
import pandas as pd
from folium.plugins import HeatMap
import pickle
def faz_mapa(title, legend, data, colunas,coluna_chave ):
    cisps = gpd.read_file('../datasets/cisp_geo_data/lm_cisp_bd.shp')
    m = folium.Map(location=[-22.9068, -43.1729], zoom_start=11, tiles='cartodbpositron')
    folium.Choropleth(
    geo_data=cisps.to_json(),          
    name=title,
    data=data,                  
    columns=colunas,    
    key_on='feature.properties.' + coluna_chave, 
    fill_color='YlOrRd',                 
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name=legend
    ).add_to(m)
    n = title + ".html"
    m.save(n)
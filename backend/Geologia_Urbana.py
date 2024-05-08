# Se importan Las librerias

import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import geopandas as gpd
import plotly.express as px

# Titulo de la tercera seccion
Tituto3 = html.H3('Geología Urbana')

#Se importan las bases de datos
Localidades_2 = gpd.read_file('data\Localidades')
Geologia_urbana = gpd.read_file('data\Geologia Urbana')
DensidadPoblacional_2=gpd.read_file('data\Centroides_Manzanas.geojson')

#Parte izquierda de la tercera seccion - GEOLOGIA URBANA

#Se define la funcion a utilizar en funcion de la seleccion de las localidades para retornar el mapa
def consultarLocalidad_2(localidad_consultada_2):

    #Se recorta la base de datos de las localidades con la localidad buscada
    localidad_buscada_2 = Localidades_2.query(f"LocNombre == '{localidad_consultada_2}'")
    
    #Se cambia a las coordenadas de las bases de datos deseadas
    Geologia_urbana_4686 = Geologia_urbana.to_crs(epsg=4686)
    
    #Se sobrepone la base de datos recortada con la base de datos de la geologia urbana
    Geologia_urbana_Localidad = gpd.overlay(
    localidad_buscada_2, Geologia_urbana_4686, how='intersection')

    #Se grafica la localidad elegida con la base de datos de geologia urbana
    fig_2 = px.choropleth_mapbox(
        geojson=Geologia_urbana_Localidad.geometry,
        locations=Geologia_urbana_Localidad.index,
        color_continuous_scale="Viridis",
        opacity=0.3       
    )

    #Se agrega diseño a la grafica
    fig_2.update_layout(

        mapbox_style="open-street-map",
        mapbox_zoom=10,
        mapbox_center = {"lat": 4.60971, "lon": -74.08175},
    )
    return fig_2


#Se define el container de la parte izquierda de la tercera sección
GeologiaUrbana = dbc.Container(
    [
       html.H3('Localidad'),
       html.Hr(),
       html.Div([
           dcc.Dropdown(Localidades_2['LocNombre'].unique(), 'CIUDAD BOLIVAR' , id='localidad_consultada_2',
                        style={'background-color':'#FFCC80',"font-weight": "bold"}),
            html.Hr(),
            dcc.Graph(
                id="mapa_2",
                style={
                    'width': '100%', 
                    "height": "600px",'background-color':'#FFCC80'
                    },
        )
       ])
    ],
    fluid=True
)

#Parte derecha de la tercera seccion - GEOLOGIA URBANA

def consultarGeologiaUrbana(geologiaurbana_consultada):

    #Se cambia a las coordenadas de las bases de datos deseadas
    Geologia_urbana_4686 = Geologia_urbana.to_crs(epsg=4686)
    DensidadPoblacional_4686_2 = DensidadPoblacional_2.to_crs(epsg=4686)

    #Se recorta la base de datos de la geologia urbana con la geologia urbana buscada
    Geologia_urbana_buscada = Geologia_urbana_4686.query(f"LEY_GEO == '{geologiaurbana_consultada}'")
        
    #Se sobrepone la base de datos recortada con la base de datos de la Densidad Poblacional
    DensidadPoblacional_Geologia_urbana = gpd.overlay(
    DensidadPoblacional_4686_2, Geologia_urbana_buscada, how='intersection')

    PoblacionTotal_2=DensidadPoblacional_Geologia_urbana["PER_S010"].sum()

    return 'Dentro de la clasificación geológica ' + str(geologiaurbana_consultada) + ' se encuentran ' + str(PoblacionTotal_2) + ' habitantes en la ciudad de Bogotá'

#Se define el container de la parte derecha de la tercera sección
Poblacion_GeologiaUrbana = dbc.Container(
    [
        html.H3('Geológia Urbana'),
        html.Hr(),
        dcc.RadioItems(Geologia_urbana['LEY_GEO'].unique(),'Pgb', id='geologiaurbana_consultada',
                    style={'background-color':'#FFCC80',"font-weight": "bold",'textAlign':'left'}),
        html.Hr(),
        html.H3('Cantidad de Habitantes en Bogotá D.C.'),
        html.Hr(),
        html.H5(id='Poblacion_Total_2',style={'background-color':'#FFCC80'})
    ]
)

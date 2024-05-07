# Se importan Las librerias

import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import geopandas as gpd
import plotly.express as px

# Titulo de la tercera seccion
Tituto4 = html.H3('Geología Rural')

#Se importan las bases de datos
Localidades_3 = gpd.read_file('data\Localidades')
Geologia_rural = gpd.read_file('data\Geología Rural')
DensidadPoblacional=gpd.read_file('data\Centroides_Manzanas.geojson')

#Parte izquierda de la cuarta seccion - GEOLOGIA RURAL

#Se define la funcion a utilizar en funcion de la seleccion de las localidades para retornar el mapa
def consultarLocalidad_3(localidad_consultada_3):

    #Se recorta la base de datos de las localidades con la localidad buscada
    localidad_buscada_3 = Localidades_3.query(f"LocNombre == '{localidad_consultada_3}'")
    
    #Se cambia a las coordenadas de las bases de datos deseadas
    Geologia_rural_4686 = Geologia_rural.to_crs(epsg=4686)
    
    #Se sobrepone la base de datos recortada con la base de datos de la geologia rural
    Geologia_rural_Localidad = gpd.overlay(
    localidad_buscada_3, Geologia_rural_4686, how='intersection')

    #Se grafica la localidad elegida con la base de datos de geologia rural
    fig_3 = px.choropleth_mapbox(
        geojson=Geologia_rural_Localidad.geometry,
        locations=Geologia_rural_Localidad.index,
        color_continuous_scale="Viridis",
        opacity=0.3       
    )

    #Se agrega diseño a la grafica
    fig_3.update_layout(

        mapbox_style="open-street-map",
        mapbox_zoom=10,
        mapbox_center = {"lat": 4.60971, "lon": -74.08175},
    )
    return fig_3


#Se define el container de la parte izquierda de la cuarta sección
GeologiaRural = dbc.Container(
    [
       html.H3('Localidad'),
       html.Hr(),
       html.Div([
           dcc.Dropdown(Localidades_3['LocNombre'].unique(), 'CIUDAD BOLIVAR' , id='localidad_consultada_3',
                        style={'background-color':'#FFCC80',"font-weight": "bold"}),
            html.Hr(),
            dcc.Graph(
                id="mapa_3",
                style={
                    'width': '100%', 
                    "height": "600px",'background-color':'#FFCC80'
                    },
        )
       ])
    ],
    fluid=True
)

#Parte derecha de la cuarta seccion - GEOLOGIA RURAL

#Se define el container de la parte derecha de la cuarta sección
Poblacion_GeologiaRural = dbc.Container(
    [
        html.H3('Geológia Rural'),
        html.Hr(),
        dcc.RadioItems(Geologia_rural['UNIDAD'].unique(), id='geologiarural_consultada',
                    style={'background-color':'#FFCC80',"font-weight": "bold",'textAlign':'left'}),
        html.Hr(),
        html.H3('Cantidad de Habitantes'),
        html.Hr(),
        html.H5('Dentro de la unidad geológica de Rb5 (K2E1g) se encuentra: 204 Habitantes dentro de la localidad de CIUDAD BOLIVAR',style={'background-color':'#FFCC80'})
    ]
)
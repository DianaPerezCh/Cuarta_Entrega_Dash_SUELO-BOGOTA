# Se importan Las librerias

import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import geopandas as gpd
import plotly.express as px

# Titulo de la segunda seccion
Tituto2 = html.H3('Zonificación Geotécnica')

#Se importan las bases de datos
Localidades_1 = gpd.read_file('data\Localidades')
zonificaciongeotecnica = gpd.read_file('data\Zonificación Geotécnica')
DensidadPoblacional=gpd.read_file('data\Centroides_Manzanas.geojson')

#Parte izquierda de la segunda seccion - ZONIFICACION GEOTECNICA

#Se define la funcion a utilizar en funcion de la seleccion de las localidades para retornar el mapa
def consultarLocalidad_1(localidad_consultada_1):

    #Se recorta la base de datos de las localidades con la localidad buscada
    localidad_buscada_1 = Localidades_1.query(f"LocNombre == '{localidad_consultada_1}'")
    
    #Se cambia a las coordenadas de las bases de datos deseadas
    zonificaciongeotecnica_4686 = zonificaciongeotecnica.to_crs(epsg=4686)
    
    #Se sobrepone la base de datos recortada con la base de datos de la zonificacion geotecnica
    zonificaciongeotecnica_Localidad= gpd.overlay(
    localidad_buscada_1, zonificaciongeotecnica_4686, how='intersection')

    #Se grafica la localidad elegida con la base de datos de la zonificacion geotecnica
    fig_1 = px.choropleth_mapbox(
        geojson=zonificaciongeotecnica_Localidad.geometry,
        locations=zonificaciongeotecnica_Localidad.index,
        color_continuous_scale="Viridis",
        opacity=0.3, 
    )

    #Se agrega diseño a la grafica
    fig_1.update_layout(

        mapbox_style="open-street-map",
        mapbox_zoom=10,
        mapbox_center = {"lat": 4.60971, "lon": -74.08175},
    )
    return fig_1

#Se define el container de la parte izquierda de la segunda sección
zonificacionGeotecnica = dbc.Container(
    [
       html.H3('Localidad'),
       html.Hr(),
       html.Div([
           dcc.Dropdown(Localidades_1['LocNombre'].unique(), 'CIUDAD BOLIVAR' , id='localidad_consultada_1',
                        style={'background-color':'#FFCC80',"font-weight": "bold"}),
            html.Hr(),
            dcc.Graph(
                id="mapa_1",
                style={
                    'width': '100%', 
                    "height": "600px",'background-color':'#FFCC80'
                    },
        )
       ])
    ],
    fluid=True
)

#Parte derecha de la primera seccion - ZONIFICACION GEOTECNICA

#Se define el container de la parte derecha de la segunda sección

Poblacion_zonificacionGeotecnica = dbc.Container(
    [
        html.H3('Geotecnia'),
        html.Hr(),
        dcc.RadioItems(zonificaciongeotecnica['GEOTECNIA'].unique(), id='zonificacionGeotecnica_consultada',
                    style={'background-color':'#FFCC80',"font-weight": "bold",'textAlign':'left'}),
        html.Hr(),
        html.H3('Cantidad de Habitantes'),
        html.Hr(),
        html.H5('Dentro de la zonificación de geotecnia Cerros A se encuentra: 115670 Habitantes dentro de la localidad de CIUDAD BOLIVAR',style={'background-color':'#FFCC80'})
    ]
)

# Se importan Las librerias

import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import geopandas as gpd
import plotly.express as px

# Titulo de la primera seccion
Tituto1 = html.H3('Zonas de Respuesta Sismica')

#Se importan las bases de datos
Localidades = gpd.read_file('data\Localidades')
ZonaSismica = gpd.read_file('data\Respuesta Sísmica')
DensidadPoblacional=gpd.read_file('data\Centroides_Manzanas.geojson')

#Parte izquierda de la primera seccion - ZONA DE RESPUESTA SISMICA

#Se define la funcion a utilizar en funcion de la seleccion de las localidades para retornar el mapa
def consultarLocalidad(localidad_consultada):

    #Se recorta la base de datos de las localidades con la localidad buscada
    localidad_buscada = Localidades.query(f"LocNombre == '{localidad_consultada}'")
    
    #Se cambia a las coordenadas de las bases de datos deseadas
    ZonaSismica_4686 = ZonaSismica.to_crs(epsg=4686)
    
    #Se sobrepone la base de datos recortada con la base de datos de la Zona sismica
    ZonaSismica_Localidad = gpd.overlay(
    localidad_buscada, ZonaSismica_4686, how='intersection')

    #Se elige el index deseado para ver marquilla en plano
    ZonaSismica_Localidad=ZonaSismica_Localidad.set_index("RESSIS")

    #Se grafica la localidad elegida con la base de datos de la Zona Sismica
    fig = px.choropleth_mapbox(
        geojson=ZonaSismica_Localidad.geometry,
        locations=ZonaSismica_Localidad.index,
        color_continuous_scale="Viridis",
        opacity=0.3      
    )

    #Se agrega diseño a la grafica
    fig.update_layout(

        mapbox_style="open-street-map",
        mapbox_zoom=10,
        mapbox_center = {"lat": 4.60971, "lon": -74.08175},
    )
    return fig

#Se crea espacio para la columna en blanca divisoria.
Division = ''

#Se define el container de la parte izquierda de la primera sección
RespuestaSismica = dbc.Container(
    [
       html.H3('Localidad'),
       html.Hr(),
       html.Div([
           dcc.Dropdown(Localidades['LocNombre'].unique(), 'CIUDAD BOLIVAR' , id='localidad_consultada',
                        style={'background-color':'#FFCC80',"font-weight": "bold"}),
            html.Hr(),
            dcc.Graph(
                id="mapa",
                style={
                    'width': '100%', 
                    "height": "600px",'background-color':'#FFCC80'
                    },
        )
       ])
    ],
    fluid=True
)

#Parte derecha de la primera seccion - ZONA DE RESPUESTA SISMICA

#Se define la funcion a utilizar en funcion de la seleccion de las zonas de respuesta sismica
def consultarzonassismica(Zonasismica_consultada):

    #Se cambia a las coordenadas de las bases de datos deseadas
    ZonaSismica_4686 = ZonaSismica.to_crs(epsg=4686)
    DensidadPoblacional_4686 = DensidadPoblacional.to_crs(epsg=4686)

    #Se recorta la base de datos de las zonas de respuesta sismica con la zonas de respuesta sismica buscada
    Zonasismica_buscada = ZonaSismica_4686.query(f"RESSIS == '{Zonasismica_consultada}'")
        
    #Se sobrepone la base de datos recortada con la base de datos de la Densidad Poblacional
    DensidadPoblacional_Zonasismica = gpd.overlay(
    DensidadPoblacional_4686, Zonasismica_buscada, how='intersection')

    PoblacionTotal=DensidadPoblacional_Zonasismica["PER_S010"].sum()

    return 'Dentro de la zona de respuesta sismica ' + str(Zonasismica_consultada) + ' se encuentran ' + str(PoblacionTotal) + ' habitantes en la ciudad de Bogotá'


#Se define el container de la parte derecha de la primera sección
Poblacion_RespuestaSismica = dbc.Container(
    [
        html.H3('Zonificación del suelo'),
        html.Hr(),
        dcc.RadioItems(ZonaSismica['RESSIS'].unique(), 'Lacustre 200', id='Zonasismica_consultada',
                    style={'background-color':'#FFCC80',"font-weight": "bold",'textAlign':'left'}),
        html.Hr(),
        html.H3('Cantidad de Habitantes en Bogotá D.C.'),
        html.Hr(),
        html.H5(id='Poblacion_Total',style={'background-color':'#FFCC80'})
    ]
)
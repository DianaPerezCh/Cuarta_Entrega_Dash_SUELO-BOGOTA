# Se importan Las librerias
import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from PIL import Image

# Se crean las variables de las imagenes para ser insertadas en el Container de presentacion

#Imagen del escudo
imagen1= Image.open('Escudo.png')
Escudo = html.Img(src=imagen1, width='200', height='170')

#Imagen de la facultad
imagen2= Image.open('facultad.png')
Facultad = html.Img(src=imagen2, width='240', height='170')

# Se crean las variables de los textos para ser insertadas en el Container de presentacion

# Presentacion Titulo
Datosacademicos = html.Div([
        html.H3('Universidad Distrital Francisco Jose de Caldas'),
        html.H3('Facultad Tecnologica'),
        html.H3('Proyecto Curricular de Ingeniería Civil'),
        html.H3('Programación II'),
    ])

# Nombre del proyecto - Descripcion
ProyectoTitulo = html.H2('SUELOS-BOGOTÁ')
ProyectoContenido=html.H4('Consulta las caracteristicas que se encuentran en el suelo en la ciudad de Bogotá por localidades, como la respuesta sísmica del suelo, la zonificación geotécnica, la geología urbana y la geología rural recopilados por el Instituto Distrital de Gestión del Riesgo y el Cambio Climático - IDIGER, al igual que la cantidad de habitantes segun el censo 2010 que se encuentran en la clasificación.'
                          )
    

#Recopilación de la presentacion del HTML 
presentacion = dbc.Container(
    [
        html.Hr(),
        dbc.Row([
            dbc.Col(Escudo, md=3, style={'background-color':'black','textAlign':'center'}),
            dbc.Col(Datosacademicos, md=6,style={'background-color':'black','textAlign':'center',"color":"white"}, ),
            dbc.Col(Facultad, md=3,style={'background-color':'black','textAlign':'center'}, )
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(ProyectoTitulo, md=12,style={'background-color':'#922B21','textAlign':'center',"color":"white"}, ),
            dbc.Col(ProyectoContenido, md=12,style={'background-color':'#A93226','textAlign':'center',"color":"white"}, ),
        ]),
        html.Hr(),
            ]
)

# Finalización 
BasesdeDatos = html.Div([
        html.H3('BASES DE DATOS'),
        html.H4('Respuesta Sísmica. Bogotá D.C'),
        html.H5('https://datosabiertos.bogota.gov.co/dataset/respuesta-sismica'),
        html.H4('Zonificación Geotécnica. Bogotá D.C'),
        html.H5('https://datosabiertos.bogota.gov.co/dataset/zonificacion-geotecnica'),
        html.H4('Geología Urbana - Insumo Estudios Básicos de Amenaza por Movimientos en Masa. Bogotá D.C.'),
        html.H5('https://datosabiertos.bogota.gov.co/dataset/geologia-para-bogota'),
        html.H4('Geología Rural - Insumo Estudios Básicos de Amenaza por Movimientos en Masa. Bogotá D.C'),
        html.H5('https://datosabiertos.bogota.gov.co/dataset/geologia-rural'),
        html.H4('Centroides - Manzanas'),

    ])

#Recopilación de la finalización del HTML 
Finalizacion = dbc.Container( [
    html.Hr(),
    dbc.Col(BasesdeDatos, md=12,style={'background-color':'black','textAlign':'center',"color":"white"}, ),
    html.Hr(),
    ]
)
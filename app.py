# Se importan Las librerias
import dash
from dash import Dash, html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from PIL import Image

# Se importa el frontend y el backend
from frontend.Presentacion import presentacion, Finalizacion
from backend.respuesta_sismica import Tituto1, RespuestaSismica, consultarLocalidad, Division, Poblacion_RespuestaSismica, consultarzonassismica
from backend.Zonificacion_Geotecnica import Tituto2, zonificacionGeotecnica, consultarLocalidad_1, Poblacion_zonificacionGeotecnica, consultarZonificaciongeotecnica
from backend.Geologia_Urbana import Tituto3, GeologiaUrbana, consultarLocalidad_2, Poblacion_GeologiaUrbana, consultarGeologiaUrbana
from backend.Geologia_Rural import Tituto4, GeologiaRural, consultarLocalidad_3, Poblacion_GeologiaRural, consultarGeologiaRural


# Cuerpo de la aplicación
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    # Se carga el frontend de la presentacion
    presentacion,
    # Se carga el backend al 40% de la sección 1 - RESPUESTA SISMICA
            dbc.Row([
            dbc.Col(Tituto1, md=12,style={'background-color':'#186A3B','textAlign':'center',"color":"white"}, ),
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(RespuestaSismica, md=7,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(Poblacion_RespuestaSismica, md=4,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
        ]),
        html.Hr(),
    # Se carga el backend al 40% de la sección 2 - ZONIFICACIÓN GEOTECNICA
        dbc.Row([
            dbc.Col(Tituto2, md=12,style={'background-color':'#186A3B','textAlign':'center',"color":"white"}, ),
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(zonificacionGeotecnica, md=7,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(Poblacion_zonificacionGeotecnica, md=4,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
        ]),
        html.Hr(),
    # Se carga el backend al 40% de la sección 3 - GEOLÓGIA URBANA
        dbc.Row([
            dbc.Col(Tituto3, md=12,style={'background-color':'#186A3B','textAlign':'center',"color":"white"}, ),
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(GeologiaUrbana, md=7,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(Poblacion_GeologiaUrbana, md=4,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
        ]),
        html.Hr(),
    # Se carga el backend al 40% de la sección 4 - GEOLÓGIA RURAL
        dbc.Row([
            dbc.Col(Tituto4, md=12,style={'background-color':'#186A3B','textAlign':'center',"color":"white"}, ),
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(GeologiaRural, md=7,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(Poblacion_GeologiaRural, md=4,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
        ]),
        html.Hr(),
    # Se carga el frontend de la finalización
    Finalizacion
    ]
    )

#Conexion con la funcion del mapa - Seccion 1 - Parte 1
@app.callback(
    Output("mapa", "figure"),
    Input("localidad_consultada", "value")
)

#Funcion a conectar del mapa  - Seccion 1 - Parte 1
def update_map(localidad_consultada):
    return consultarLocalidad(localidad_consultada)

#Conexion con la funcion del mapa - Seccion 1 - Parte 2
@app.callback(
    Output("Poblacion_Total", "children"),
    Input("Zonasismica_consultada", "value")
)

#Funcion a conectar del mapa  - Seccion 1 - Parte 2
def update_poblacion(Zonasismica_consultada):
    return consultarzonassismica(Zonasismica_consultada)

#Conexion con la funcion del mapa  - Seccion 2 - Parte 1
@app.callback(
    Output("mapa_1", "figure"),
    Input("localidad_consultada_1", "value")
)

#Funcion a conectar del mapa  - Seccion 2 - Parte 1
def update_map_1(localidad_consultada_1):
    return consultarLocalidad_1(localidad_consultada_1)

#Conexion con la funcion del mapa - Seccion 2 - Parte 2
@app.callback(
    Output("Poblacion_Total_1", "children"),
    Input("zonificacionGeotecnica_consultada", "value")
)

#Funcion a conectar del mapa  - Seccion 2 - Parte 2
def update_poblacion_1(zonificacionGeotecnica_consultada):
    return consultarZonificaciongeotecnica(zonificacionGeotecnica_consultada)

#Conexion con la funcion del mapa  - Seccion 3 - Parte 1
@app.callback(
    Output("mapa_2", "figure"),
    Input("localidad_consultada_2", "value")
)

#Funcion a conectar del mapa  - Seccion 3 - Parte 1
def update_map_2(localidad_consultada_2):
    return consultarLocalidad_2(localidad_consultada_2)

#Conexion con la funcion del mapa - Seccion 3 - Parte 2
@app.callback(
    Output("Poblacion_Total_2", "children"),
    Input("geologiaurbana_consultada", "value")
)

#Funcion a conectar del mapa  - Seccion 3 - Parte 2
def update_poblacion_2(geologiaurbana_consultada):
    return consultarGeologiaUrbana(geologiaurbana_consultada)

#Conexion con la funcion del mapa  - Seccion - Parte 1
@app.callback(
    Output("mapa_3", "figure"),
    Input("localidad_consultada_3", "value")
)

#Funcion a conectar del mapa  - Seccion 4 - Parte 1
def update_map_3(localidad_consultada_3):
    return consultarLocalidad_3(localidad_consultada_3)

#Conexion con la funcion del mapa - Seccion 4 - Parte 2
@app.callback(
    Output("Poblacion_Total_3", "children"),
    Input("geologiarural_consultada", "value")
)

#Funcion a conectar del mapa  - Seccion 4 - Parte 2
def update_poblacion_3(geologiarural_consultada):
    return consultarGeologiaRural(geologiarural_consultada)

if __name__ == '__main__' :
    app.run_server(debug=True)

from flask import Flask, render_template, request
import sys
from GestorRankingVinos import GestorRankingVinos
from PantallaRankingVinos import PantallaRankingVinos  # Import the class, not the module
from TodasLasClases import DTOVino
from Vino import *
sys.path.append('C:/Users/Roberto/source/repos/robertoutn/PPAI_BON_VINO/')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generar_ranking_vinos')
def generar_ranking_vinos():
    gestor = GestorRankingVinos(lista_de_vinos)
    pantalla_ranking = PantallaRankingVinos('360x720', 'BonVino - Generar ranking de vinos', 'Clases/extras/icono.ico', '#5C1D05', gestor)
    gestor.pantalla = pantalla_ranking
    pantalla_ranking.opcGenerarRankingVinos()
    return 'Ranking generated'

@app.route('/importar_vinos', methods=['GET', 'POST'])
def importar_vinos():
    global lista_de_vinos
    lista_de_vinos = cargar_vinos(lista_de_vinos)
    return 'Import successful'

def cargar_vinos(lista_vinos):
    vinos = DTOVino.consultar_vinos(lista_vinos)
    return lista_vinos

lista_de_vinos = []

if __name__ == '__main__':
    app.run(debug=True)
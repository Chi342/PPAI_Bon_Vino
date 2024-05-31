#!/usr/bin/python
#-*- coding: utf-8 -*-

import xlsxwriter

class InterfazExcel:
    def __init__(self):
        pass

    def exportarExcel(self, vinos):
        """
        Exporta los datos de los vinos a un archivo de Excel.

        Parámetros:
        - vinos: una lista de vinos con sus respectivos datos.

        """
        workbook = xlsxwriter.Workbook('RankingVinos.xlsx')
        worksheet = workbook.add_worksheet()

        letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        if len(vinos) < 10:
            largo = len(vinos)
        else:   
            largo = 10
        for i in range(largo):
            for j in range(len(vinos[i])-1):
                casilla = letras[j] + str(i+1)
                worksheet.write(casilla, vinos[i][j+1])
        workbook.close()
        


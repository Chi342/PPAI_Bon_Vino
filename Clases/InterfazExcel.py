#!/usr/bin/python
#-*- coding: utf-8 -*-


import xlsxwriter


class InterfazExcel:
    def __init__(self):
        pass

    def exportarExcel(self, vinos):
        workbook = xlsxwriter.Workbook('RankingVinos.xlsx')
        worksheet = workbook.add_worksheet()
        # # Add column names
        # column_names = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5', 'Column6', 'Column7', 'Column8', 'Column9', 'Column10']
        # for i, column_name in enumerate(column_names):
        #     worksheet.write(0, i, column_name)
        # Add data
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
        


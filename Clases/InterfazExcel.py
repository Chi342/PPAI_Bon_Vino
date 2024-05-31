#!/usr/bin/python
#-*- coding: utf-8 -*-


import xlsxwriter


class InterfazExcel:
    def __init__(self):
        pass

    def exportarExcel(self, vinos):
        workbook = xlsxwriter.Workbook('RankingVinos.xlsx')
        worksheet = workbook.add_worksheet()
        letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        for i in range(len(vinos)):
            for j in range((len(vinos[i]))):
                casilla = letras[j] + str(i)
                worksheet.write(casilla, vinos[i][j])
        workbook.close()


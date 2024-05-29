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


vino1 = ['Balbo', 1500, 'Sauvignon', 'Bon Vino', 'Mendoza', 'Argentina', 100]
vino2 = ['Balbo', 1500, 'Sauvignon', 'Bon Vino', 'Mendoza', 'Argentina', 100]
vino3 = ['Balbo', 1500, 'Sauvignon', 'Bon Vino', 'Mendoza', 'Argentina', 100]
vino4 = ['Balbo', 1500, 'Sauvignon', 'Bon Vino', 'Mendoza', 'Argentina', 100]
vino5 = ['Balbo', 1500, 'Sauvignon', 'Bon Vino', 'Mendoza', 'Argentina', 100]
vino6 = ['Balbo', 1500, 'Sauvignon', 'Bon Vino', 'Mendoza', 'Argentina', 100]
vino7 = ['Balbo', 1500, 'Sauvignon', 'Bon Vino', 'Mendoza', 'Argentina', 100]
vino8 = ['Balbo', 1500, 'Sauvignon', 'Bon Vino', 'Mendoza', 'Argentina', 100]
vino9 = ['Balbo', 1500, 'Sauvignon', 'Bon Vino', 'Mendoza', 'Argentina', 100]
vino10 = ['Balbo', 1500, 'Sauvignon', 'Bon Vino', 'Mendoza', 'Argentina', 100]
Vinos = [vino1, vino2, vino3, vino4, vino5, vino6, vino7, vino8, vino9, vino10]
intExcel = InterfazExcel()
intExcel.exportarExcel(Vinos)

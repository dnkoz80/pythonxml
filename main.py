import urllib.request
import pandas as pd
import os
import xml.etree.ElementTree as ET
import xlsxwriter
import csv
def get_data_web(url):
   web_file=urllib.request.urlopen(url)
   return web_file.read()

def get_data_local(path_to_xml):

   return os.listdir(path_to_xml)

def spisok_dir_file(path_to_dir_koren):

##########Получаем СПИСОК ПАПОК№№№№№№№№№№№№№№№№№№№№№№№№№№№№
   all_file_pach=[]
   dirS=[path_to_dir_koren+d+'/' for d in os.listdir(path_to_dir_koren) if os.path.isdir(os.path.join(path_to_dir_koren,d)  )]

##########Получаем СПИСОК ФАЙЛОВ (только xml )И ФОРМИРУЕМ ПОЛНЫЙ ПУТЬ№№№№№№№№№№№№№№№№№№№№№№№№№№№№
   for dir_one in dirS:
       file_list=[dir_one+f for f in os.listdir(dir_one) if os.path.isfile(os.path.join(dir_one,f)) and f.endswith(".xml")]
       all_file_pach=all_file_pach +file_list
   print('len(all_file_pach)', len(all_file_pach))
   print('all_file_pach',all_file_pach)

   return(all_file_pach)

def parser_xlswr(path_to_file,worksheet,CadastralNumber_find ,path_to_file_1):
    tree = ET.parse(path_to_file)

    ################парсер№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№3

    Packages = tree.getroot()

    Parcels=(Packages.iter('Parcel'))
    print('[Parcels]-',Parcels)

    for Parcel in Parcels:
        print('[Parcel]-',Parcel.attrib)
        OrdinateS=Parcel.iter('Ordinate')
        #print('OrdinateS--',OrdinateS)
        for Ordinate in OrdinateS:
            print('OrdinateS--',Ordinate.attrib)
            worksheet.write(1, 0, 1)

    # for Package in Packages[1][0][0][0][0][0][0][0][2]:
    #
    #     CadastrNumber = Package.get('CadastralNumber')
    #
    #     if Package.get('CadastralNumber') == CadastralNumber_find:
    #
    #         for Spelement_Unit in Package.iter('Ordinate'):
    #             X = Spelement_Unit.get('X')
    #             Y = Spelement_Unit.get('Y')
    #
    #             #print(CadastrNumber)
    #             #print('Координата X=', X, 'Координата Y=', Y, )
    #             worksheet.write(row, 0, CadastrNumber)
    #             worksheet.write(row, 1, X)
    #             worksheet.write(row, 2, Y)
    #             row = row + 1
    #             CadastrNumber = ''

    return()


if __name__ == '__main__':

    path_to_dir_koren = 'D:/TEMP/sravnenie/'
    CadastralNumber_find = '70:14:0100010:254'
       # открываем новый файл на запись
    workbook = xlsxwriter.Workbook('D:/TEMP/sravnenie/CadastralNumber.xlsx')
       # создаем там "лист"
    worksheet = workbook.add_worksheet()
 #################################################
    path_to_fileS = spisok_dir_file(path_to_dir_koren)
    #for  path_to_file in path_to_fileS:
    #path_to_file_1='D:/TEMP/sravnenie/temp_test/ZK_100000000000_051601070000_70_14_0100010_02122014_0000 (1).xml'
    path_to_file_1 = 'D:/TEMP/sravnenie/temp_test/ZK_100000000000_051601070000_70_14_0100010_02122014_00000000.xml'
    path_to_file = 'D:/TEMP/sravnenie/temp_test/ZK_100000000000_051601070000_70_14_0100010_02122014_00000000.xml'
    parser_xlswr(path_to_file,worksheet,CadastralNumber_find,path_to_file_1 )

    myData =  {'X': '4318320.75', 'Y': '351534.55', 'Ord_Nmb': '2'}
    #myFile = open('D:/TEMP/sravnenie/CadastralNumber.csv', 'w')
    with open('D:/TEMP/sravnenie/CadastralNumber.csv', 'w') as csvfile:
        #fieldnames = ['X', 'Y', 'Ord_Nmb']

        writer = csv.DictWriter(csvfile)
        writer.writeheader()
        writer.writerow(myData)
    workbook.close()

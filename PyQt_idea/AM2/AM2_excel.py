#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================================== #
# PROJET:
#   Create a program which recovery every data of your company
# =============================================================================================== #
__author__ = 'Nicolas M'
__version__ = '1.0'
__maintainer__ = 'Nicolas M'
__status__ = 'beta'
__date__ = '03 octobre 2014'
# =============================================================================================== #
# Module:
#
# =============================================================================================== #
# LIMITATION:
# CGU n°6
# =============================================================================================== #
# Evolutions:
# Export Excel
# =============================================================================================== #

from math import floor
from PySide import QtGui
from datetime import date, timedelta
from matplotlib import pylab
from matplotlib import pyplot as plt
from matplotlib import dates
from threading import Timer

import time
import datetime
import pickle
import urllib.request
import re
import json
import numpy as np
import sys

import PyGuiModeles.AM2_managerModele as PM

def substr_day(date, offset):
    return date - timedelta(days=offset)

def toFormat(n, ext):
    """Affiche un nombre entier n, en utilisant sep comme séparateur des milliers"""
    sep = " "
    s = str(floor(n))
    l = len(s)
    nc = 0
    res = ""
    for i in range(l-1, -1, -1):
        res = s[i] + res
        nc += 1
        if nc == 3:
            res = sep + res
            nc = 0
    if res.startswith(sep):
        res = res[1:]
    if n < 0 and res[1] == sep:
        res = list(res)
        del res[1]
        res = "".join(res)
    return res + " " + ext

def withDecimale(n , ext):
    return str(float("{0:.2f}".format(n))) + " " + ext

def getIDline(my_name):
    for each_line in Line_list:
        if Line_list[each_line].name==my_name:
            return Line_list[each_line].id

    return 'Error'

def getIDplane(my_name):
    for each_flight in Plane_List:
        if Plane_List[each_flight].name==my_name:
            return Plane_List[each_flight].id

    return 'Error'

class New_Financial:
    def __init__(self, date):
        self.date=date
        self.valorisation = 0
        self.resultat = 0
        self.salaire = 0
        self.frais_day = 0
        self.ts = 0
        self.rank = 0
        self.CA = 0

    def to_int(self):
        self.valorisation = int(re.sub(u'[^0-9]','',str(self.valorisation),flags=0))
        self.resultat = int(re.sub(u'[^0-9]','',str(self.resultat),flags=0))
        self.salaire = int(re.sub(u'[^0-9]','',str(self.salaire),flags=0))
        self.frais_day = int(re.sub(u'[^0-9]','',str(self.frais_day),flags=0))
        self.ts = int(re.sub(u'[^0-9]','',str(self.ts),flags=0))
        self.rank = int(re.sub(u'[^0-9]','',str(self.rank),flags=0))
        self.CA = int(re.sub(u'[^0-9]','',str(self.CA),flags=0))
        self.date = time.strptime(self.date, "%Y-%m-%d")

class New_Line:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.distance = 0
        self.categorie = 0
        self.Audit_Price = np.zeros(4)
        self.Audit_Pax = np.zeros(4)
        self.Current_Price = np.zeros(4)
        self.Current_Pax = np.zeros(4)
        self.Current_Free_Pax = np.zeros(4)
        self.Opti_Price = np.zeros(4)
        self.Opti_Pax = np.zeros(4)
        self.Pax_to_opti = np.zeros(4)
        self.Pax_to_opti_G = 0
        self.CA_Audit = np.zeros(4)
        self.CA_Current = np.zeros(4)
        self.CA_Opti = np.zeros(4)
        self.CA_Audit_G = 0
        self.CA_Current_G = 0
        self.CA_Opti_G = 0
        self.Eff_Current = np.zeros(4)
        self.Eff_Opti = np.zeros(4)
        self.Eff_Current_G = 0
        self.Eff_Opti_G = 0
        self.ID_lineOne = 0
        self.ID_lineTwo = 0
        self.arrive=""
        self.depart=""
        self.Fiability_Audit = ""
        self.Revenus_Aux = []
        self.Frais = []
        self.rotation=0

    def ca_max(self):
        self.CA_Audit=(np.array(self.Audit_Price)*np.array(self.Audit_Pax))+np.array(self.Revenus_Aux)
        self.CA_Audit_G = sum(self.CA_Audit)+sum(self.Revenus_Aux)

    def ca_current(self):
        a = np.array(self.Current_Free_Pax).clip(0)
        self.CA_Current = np.array(self.Current_Price)*(np.array(self.Current_Pax)-a)+np.array(self.Revenus_Aux)
        self.CA_Current_G = sum(self.CA_Current)+sum(self.Revenus_Aux)

    def ca_opti(self):
        self.CA_Opti = (np.array(self.Opti_Price)*np.array(self.Opti_Pax))+np.array(self.Revenus_Aux)
        self.CA_Opti_G = sum(self.CA_Opti)+sum(self.Revenus_Aux)

    def calcul_price(self):
        for i in range(4):
            a = self.Audit_Price[i]
            b = self.Audit_Pax[i]
            c = self.Opti_Pax[i]
            if (c<=b):
                R=-a/3*(c/b-4)
            else:
                R=-3*a*(c/b-4/3)

            if (R<0):
                R=0

            self.Opti_Price[i]=floor(R)

    def efficiency_current(self):
        self.Eff_Current=100*np.array(self.CA_Current)/np.array(self.CA_Audit)
        self.Eff_Current_G = 100 * sum(np.array(self.CA_Current)) / sum(np.array(self.CA_Audit))

    def efficiency_opti(self):
        self.Eff_Opti=100*np.array(self.CA_Opti)/np.array(self.CA_Audit)
        self.Eff_Opti_G = 100 * sum(np.array(self.CA_Opti)) / sum(np.array(self.CA_Audit))

    def place_restantes(self):
        self.Current_Free_Pax= np.array(self.Current_Pax)-np.array(self.Opti_Pax)

    def pax_to_opti(self):
        self.Pax_to_opti = np.array(self.Audit_Pax)-np.array(self.Opti_Pax)
        self.Pax_to_opti_G = sum(np.array(self.Pax_to_opti)*np.array([1, 1.8, 4.2, 1]))/2

    def getHub(self):
        Name_Hub_List[self.ID_lineOne]=self.name[:3]
        Name_Line_List[self.ID_lineTwo]=self.name[6:]

class New_Plane:
    def __init__(self, id):
        self.id=id
        self.name=""
        self.categorie=0
        self.range=0
        self.isRental=False
        self.isCargo=False
        self.seats=np.zeros(4)
        self.consumption=0
        self.utilizationPercentage=0
        self.type=""
        self.speed=0
        self.destination=[]
        self.hub=0
        self.buy_date=''
        self.buy_price=0
        self.resultat=0
        self.rentabilite=0
        self.nb_vol=0
        self.h_de_vol=0
        self.age=0
        self.dist_piste=0

    def remove_double(self):
        self.destination=list(set(self.destination))

    def calc_renta(self):
        a = int(re.sub(u'[^0-9]','',self.buy_price,flags=0))
        b = int(re.sub(u'[^0-9]','',self.resultat,flags=0))
        self.rentabilite = 100*b/a

class Departure:
    def __init__(self, inc, TOtime, Pid, Lid):
        self.num = inc
        self.takeofftime = TOtime
        self.plane_ID = Pid
        self.line_ID = Lid

    def horaire(self):
        h = (self.takeofftime % 86400)/ 3600
        m = (self.takeofftime % 3600)/ 60
        return "%d:%02d" % (h, m)

class Mon_IHM(PM.Ui_MainWindow):
    def __init__(self, MainWindow, parent=None):
        #Initialisation de la classe
        PM.Ui_MainWindow.setupUi(self, MainWindow)
        self.Btn_PHPSESSID.clicked.connect(self.updates_objects)
        self.update_finance.clicked.connect(self.updates_finances)
        self.calendar.selectionChanged.connect(self.display_finance)
        self.ma_date.setDate(date.today())
        self.plot_finance.clicked.connect(self.plot_finances)
        self.btn_plot_all_line.clicked.connect(self.plot_all_line)
        self.btn_plot_sg_line.clicked.connect(self.plot_single_line)
        self.load_objects()
        self.load_finance()
        if (time.localtime()[3]>=0 and time.localtime()[3] < 5):
            self.update_finance.setDisabled(True)
            self.print_console("La fonction de MAJ des Finance est desactivée entre minuit et 5h",0)

    def generate_lists(self):
        dico = []
        dico2 = []

        for each_line in Line_list:
            dico.append(Line_list[each_line].name)

        for each_plane in Plane_List:
            dico2.append(Plane_List[each_plane].name)

        self.lst_lines.addItems(sorted(dico))
        self.lst_planes.addItems(sorted(dico2))
        self.lst_lines.currentIndexChanged.connect(self.display_line)
        self.lst_planes.currentIndexChanged.connect(self.display_plane)

    def display_line(self, index):
        selectedID = getIDline(self.lst_lines.itemText(index))
        self.id_line.setText(str(Line_list[selectedID].id))
        self.name_line.setText(str(Line_list[selectedID].name))
        self.dist_line.setText(toFormat(Line_list[selectedID].distance, "Km"))
        self.cat_line.setText(str(Line_list[selectedID].categorie))
        self.audit_line.setText(str(Line_list[selectedID].Fiability_Audit))
        self.nb_rotation.setText(str(Line_list[selectedID].rotation) + " rot/sem.")
        self.kero_frais.setText(toFormat(Line_list[selectedID].Frais[0], "$"))
        self.aero_frais.setText(toFormat(Line_list[selectedID].Frais[1], "$"))
        self.autre_frais.setText(toFormat(Line_list[selectedID].Frais[2], "$"))
        self.total_frais.setText(toFormat(sum(Line_list[selectedID].Frais), "$"))

        self.T1.setText(toFormat(Line_list[selectedID].Audit_Pax[0], "Pax"))
        self.T1_2.setText(toFormat(Line_list[selectedID].Audit_Pax[1], "Pax"))
        self.T1_3.setText(toFormat(Line_list[selectedID].Audit_Pax[2], "Pax"))
        self.T1_4.setText(toFormat(Line_list[selectedID].Audit_Pax[3], "Pax"))
        self.T1_5.setText(toFormat(Line_list[selectedID].Current_Pax[0], "Pax"))
        self.T1_6.setText(toFormat(Line_list[selectedID].Current_Pax[1], "Pax"))
        self.T1_7.setText(toFormat(Line_list[selectedID].Current_Pax[2], "Pax"))
        self.T1_8.setText(toFormat(Line_list[selectedID].Current_Pax[3], "Pax"))
        self.T1_9.setText(toFormat(Line_list[selectedID].Current_Price[0], "$"))
        self.T1_10.setText(toFormat(Line_list[selectedID].Current_Price[1], "$"))
        self.T1_11.setText(toFormat(Line_list[selectedID].Current_Price[2], "$"))
        self.T1_12.setText(toFormat(Line_list[selectedID].Current_Price[3], "$"))
        self.T1_13.setText(toFormat(Line_list[selectedID].Current_Free_Pax[0], "Pax"))
        self.T1_14.setText(toFormat(Line_list[selectedID].Current_Free_Pax[1], "Pax"))
        self.T1_15.setText(toFormat(Line_list[selectedID].Current_Free_Pax[2], "Pax"))
        self.T1_16.setText(toFormat(Line_list[selectedID].Current_Free_Pax[3], "Pax"))
        self.T1_17.setText(toFormat(Line_list[selectedID].Opti_Pax[0], "Pax"))
        self.T1_18.setText(toFormat(Line_list[selectedID].Opti_Pax[1], "Pax"))
        self.T1_19.setText(toFormat(Line_list[selectedID].Opti_Pax[2], "Pax"))
        self.T1_20.setText(toFormat(Line_list[selectedID].Opti_Pax[3], "Pax"))
        self.T1_21.setText(toFormat(Line_list[selectedID].Opti_Price[0], "$"))
        self.T1_22.setText(toFormat(Line_list[selectedID].Opti_Price[1], "$"))
        self.T1_23.setText(toFormat(Line_list[selectedID].Opti_Price[2], "$"))
        self.T1_24.setText(toFormat(Line_list[selectedID].Opti_Price[3], "$"))
        self.T1_25.setText(toFormat(Line_list[selectedID].Audit_Price[0], "$"))
        self.T1_26.setText(toFormat(Line_list[selectedID].Audit_Price[1], "$"))
        self.T1_27.setText(toFormat(Line_list[selectedID].Audit_Price[2], "$"))
        self.T1_28.setText(toFormat(Line_list[selectedID].Audit_Price[3], "$"))
        self.T2.setText(toFormat(Line_list[selectedID].CA_Audit[0], "$"))
        self.T2_2.setText(toFormat(Line_list[selectedID].CA_Audit[1], "$"))
        self.T2_3.setText(toFormat(Line_list[selectedID].CA_Audit[2], "$"))
        self.T2_4.setText(toFormat(Line_list[selectedID].CA_Audit[3], "$"))
        self.T2_5.setText(toFormat(Line_list[selectedID].CA_Current[0], "$"))
        self.T2_6.setText(toFormat(Line_list[selectedID].CA_Current[1], "$"))
        self.T2_7.setText(toFormat(Line_list[selectedID].CA_Current[2], "$"))
        self.T2_8.setText(toFormat(Line_list[selectedID].CA_Current[3], "$"))
        self.T2_9.setText(toFormat(Line_list[selectedID].CA_Opti[0], "$"))
        self.T2_10.setText(toFormat(Line_list[selectedID].CA_Opti[1], "$"))
        self.T2_11.setText(toFormat(Line_list[selectedID].CA_Opti[2], "$"))
        self.T2_12.setText(toFormat(Line_list[selectedID].CA_Opti[3], "$"))
        self.T2_13.setText(toFormat(Line_list[selectedID].CA_Audit_G, "$"))
        self.T2_14.setText(toFormat(Line_list[selectedID].CA_Current_G, "$"))
        self.T2_15.setText(toFormat(Line_list[selectedID].CA_Opti_G, "$"))

        self.T3.setText(withDecimale(Line_list[selectedID].Eff_Current[0], "%"))
        self.T3_2.setText(withDecimale(Line_list[selectedID].Eff_Current[1], "%"))
        self.T3_3.setText(withDecimale(Line_list[selectedID].Eff_Current[2], "%"))
        self.T3_4.setText(withDecimale(Line_list[selectedID].Eff_Current[3], "%"))
        self.T3_5.setText(withDecimale(Line_list[selectedID].Eff_Opti[0], "%"))
        self.T3_6.setText(withDecimale(Line_list[selectedID].Eff_Opti[1], "%"))
        self.T3_7.setText(withDecimale(Line_list[selectedID].Eff_Opti[2], "%"))
        self.T3_8.setText(withDecimale(Line_list[selectedID].Eff_Opti[3], "%"))
        self.T3_9.setText(withDecimale(Line_list[selectedID].Eff_Opti_G, "%"))
        self.T3_10.setText(withDecimale(Line_list[selectedID].Eff_Current_G, "%"))

        self.T4.setText(toFormat(Line_list[selectedID].Pax_to_opti[0], "Pax"))
        self.T4_2.setText(toFormat(Line_list[selectedID].Pax_to_opti[1], "Pax"))
        self.T4_3.setText(toFormat(Line_list[selectedID].Pax_to_opti[2], "Pax"))
        self.T4_4.setText(toFormat(Line_list[selectedID].Pax_to_opti[3], "Pax"))
        self.T4_5.setText(toFormat(Line_list[selectedID].Pax_to_opti_G, "Pax"))

        self.Raux.setText(toFormat(Line_list[selectedID].Revenus_Aux[0], "$"))
        self.Raux_2.setText(toFormat(Line_list[selectedID].Revenus_Aux[1], "$"))
        self.Raux_3.setText(toFormat(Line_list[selectedID].Revenus_Aux[2], "$"))
        self.Raux_4.setText(toFormat(Line_list[selectedID].Revenus_Aux[3], "$"))
        self.Raux_5.setText(toFormat(sum(Line_list[selectedID].Revenus_Aux), "$"))

    def display_plane(self, index):
        selectedID = getIDplane(self.lst_planes.itemText(index))
        self.id_plane.setText(str(Plane_List[selectedID].id))
        self.mdl_plane.setText(str(Plane_List[selectedID].type))
        self.name_plane.setText(str(Plane_List[selectedID].name))
        self.cat_plane.setText(str(Plane_List[selectedID].categorie))
        self.use_plane.setText(str(Plane_List[selectedID].utilizationPercentage) + " %")
        self.buy_date.setText(Plane_List[selectedID].buy_date)
        self.buy_price.setText(Plane_List[selectedID].buy_price)
        self.result.setText(Plane_List[selectedID].resultat)
        self.renta.setText(withDecimale(Plane_List[selectedID].rentabilite, "%"))
        self.nb_fly.setText(Plane_List[selectedID].nb_vol + " vols")
        self.h_fly.setText(Plane_List[selectedID].h_de_vol + " h")
        self.old.setText(Plane_List[selectedID].age)
        self.dist_pist.setText(Plane_List[selectedID].dist_piste)

        mystr = ' / '.join( str(p) for p in Plane_List[selectedID].seats)
        self.seats_plane.setText(mystr)
        self.hub_plane.setText(Name_Hub_List[Plane_List[selectedID].hub])

        if (Plane_List[selectedID].isRental==False):
            self.rental.setChecked(0)

        if (Plane_List[selectedID].isRental==False):
            self.cargo.setChecked(0)

        self.speed_plane.setText(str(Plane_List[selectedID].speed))
        self.conso_plane.setText(str(Plane_List[selectedID].consumption))
        self.rayon_plane.setText(str(Plane_List[selectedID].range))

        mystr2=''
        for numline in Plane_List[selectedID].destination:
            dist = Line_list[numline].distance
            vit=int(re.sub(u'[^0-9]','',Plane_List[selectedID].speed,flags=0))

            time = 2*dist/vit+2
            if (time-floor(time) < 0.25):
                timer = ' ( '+str(floor(time))+' h 15 )'
            elif(time-floor(time) >= 0.25 and time-floor(time) < 0.5):
                timer=' ( '+str(floor(time))+' h 30 )'
            elif(time-floor(time) >= 0.5 and time-floor(time) < 0.75):
                timer=' ( '+str(floor(time))+' h 45 )'
            else:
                timer=' ( '+str(floor(time+1))+' h 00 )'

            mystr2 = mystr2 + Line_list[numline].name+timer+'\n'

        self.dest_plane.setText(mystr2)

    def display_departure(self):
        now = time.localtime()
        sec = now.tm_wday*86400 + now.tm_hour*3600 + now.tm_min*60 + now.tm_sec
        cran = 0
        cran_max = 12
        tab = []
        for each_dep in Departure_List:
            if (each_dep.takeofftime < sec or cran >= cran_max ):
                pass
            else:
                cran = cran + 1
                depart = Line_list[each_dep.line_ID].depart[0] +" - " +Line_list[each_dep.line_ID].depart[1]
                arrive = Line_list[each_dep.line_ID].arrive[0] +" - " +Line_list[each_dep.line_ID].arrive[1]
                idp = Plane_List[each_dep.plane_ID].name
                heure = each_dep.horaire()
                tab.append([idp, depart, arrive, heure])

        if (cran < cran_max):
            for i in range(cran_max-cran):
                depart = Line_list[each_dep.line_ID].depart[0] +" - " +Line_list[each_dep.line_ID].depart[1]
                arrive = Line_list[each_dep.line_ID].arrive[0] +" - " +Line_list[each_dep.line_ID].arrive[1]
                idp = Plane_List[each_dep.plane_ID].name
                heure = each_dep.horaire()
                tab.append([idp, depart, arrive, heure])

        self.current_time.setText(time.strftime("%H:%M"))
        self.departure_plane_1.setText(tab[0][0])
        self.departure_depart_1.setText( tab[0][1])
        self.departure_arrive_1.setText( tab[0][2])
        self.departure_heure_1.setText( tab[0][3])
        self.departure_plane_2.setText( tab[1][0])
        self.departure_depart_2.setText(tab[1][1])
        self.departure_arrive_2.setText( tab[1][2])
        self.departure_heure_2.setText( tab[1][3])
        self.departure_plane_3.setText( tab[2][0])
        self.departure_depart_3.setText(tab[2][1])
        self.departure_arrive_3.setText( tab[2][2])
        self.departure_heure_3.setText( tab[2][3])
        self.departure_plane_4.setText( tab[3][0])
        self.departure_depart_4.setText(tab[3][1])
        self.departure_arrive_4.setText( tab[3][2])
        self.departure_heure_4.setText( tab[3][3])
        self.departure_plane_5.setText( tab[4][0])
        self.departure_depart_5.setText(tab[4][1])
        self.departure_arrive_5.setText( tab[4][2])
        self.departure_heure_5.setText( tab[4][3])
        self.departure_plane_6.setText( tab[5][0])
        self.departure_depart_6.setText(tab[5][1])
        self.departure_arrive_6.setText( tab[5][2])
        self.departure_heure_6.setText( tab[5][3])
        self.departure_plane_7.setText( tab[6][0])
        self.departure_depart_7.setText(tab[6][1])
        self.departure_arrive_7.setText(tab[6][2])
        self.departure_heure_7.setText( tab[6][3])
        self.departure_plane_8.setText( tab[7][0])
        self.departure_depart_8.setText( tab[7][1])
        self.departure_arrive_8.setText( tab[7][2])
        self.departure_heure_8.setText( tab[7][3])
        self.departure_plane_9.setText( tab[8][0])
        self.departure_depart_9.setText( tab[8][1])
        self.departure_arrive_9.setText( tab[8][2])
        self.departure_heure_9.setText( tab[8][3])
        self.departure_plane_10.setText( tab[9][0])
        self.departure_depart_10.setText( tab[9][1])
        self.departure_arrive_10.setText( tab[9][2])
        self.departure_heure_10.setText( tab[9][3])
        self.departure_plane_11.setText( tab[10][0])
        self.departure_depart_11.setText(tab[10][1])
        self.departure_arrive_11.setText( tab[10][2])
        self.departure_heure_11.setText( tab[10][3])
        self.departure_plane_12.setText( tab[11][0])
        self.departure_depart_12.setText(tab[11][1])
        self.departure_arrive_12.setText( tab[11][2])
        self.departure_heure_12.setText( tab[11][3])
        Timer(60.0, self.display_departure).start()

    def load_finance(self):
        try:
            global Financial_List
            Financial_List = pickle.load( open( "finance.p", "rb" ) )
        except:
            pass

    def display_finance(self):
        selected_date = self.calendar.selectedDate()
        str_selected_date = selected_date.toString("yyyy-MM-dd")

        try:
            self.ma_date.setDate(selected_date)
            self.valorisation.setText(toFormat(Financial_List[str_selected_date].valorisation, "$"))
            self.result_day.setText(toFormat(Financial_List[str_selected_date].resultat, "$"))
            self.salaire.setText(toFormat(Financial_List[str_selected_date].salaire, "$"))
            self.frais_day.setText(toFormat(Financial_List[str_selected_date].frais_day, "$"))
            self.ts.setText(toFormat(Financial_List[str_selected_date].ts, "$"))
            self.place.setText(toFormat(Financial_List[str_selected_date].rank, "ème"))
            self.CA_day.setText(toFormat(Financial_List[str_selected_date].CA, "$"))
        except:
            self.ma_date.setDate(selected_date)
            self.valorisation.setText("N.C")
            self.result_day.setText("N.C")
            self.salaire.setText("N.C")
            self.frais_day.setText("N.C")
            self.CA_day.setText("N.C")
            self.ts.setText("N.C")
            self.place.setText("N.C")

    def print_console(self, text, percentage):
        print(text)
        self.plainTextEdit.appendPlainText('>> '+text)
        self.progressBar.setValue(percentage)
        QtGui.QApplication.processEvents()

    def open_conn(self):
        try:
            #Connexion au compte
            global opener
            self.print_console("Connecting...", 1)
            opener = urllib.request.URLopener()
            opener.addheader('cookie', "PHPSESSID="+self.lineEdit.text())
            opener.addheader('Content-Type',"application/x-www-form-urlencoded;charset=utf-8")
            opener.addheader('User-agent', 'Mozilla/5.0')
            self.print_console("Connected...", 1)
        except:
            self.print_console("Error :(", 1)

    def updates_objects(self):
        self.open_conn()
        try:
            self.print_console("Downloading JSON" , 2)

            xhr = opener.open("http://www.airlines-manager.com/network/planning")
            response = xhr.read().decode("utf-8")

            pattern4 = re.compile('<div class="hidden" id="jsonAircraftList">(.+?)</div>')
            pattern5 = re.compile('<div class="hidden" id="jsonLineList">(.+?)</div>')

            json_aircraft = re.findall(pattern4,response)[0]
            json_line = re.findall(pattern5,response)[0]

            PaxAtt={}
            Offre={}

            self.print_console("Extracting datas from : jsonLineList", 4)

            #Extractions des différentes lignes et remplissage de la classe Line
            parsed_json_line = json.loads(json_line)
            for each_line in parsed_json_line:
                PaxAtt[each_line['id']] = [each_line['paxAttEco'],each_line['paxAttBus'],each_line['paxAttFirst'],each_line['paxAttCargo']]
                Offre[each_line['id']] = np.zeros((7, 4))
                Line_list[each_line['id']] = New_Line(each_line['name'],each_line['id'])
                Line_list[each_line['id']].Current_Pax = [each_line['paxAttEco'],each_line['paxAttBus'],each_line['paxAttFirst'],each_line['paxAttCargo']]
                Line_list[each_line['id']].distance = each_line['distance']
                Line_list[each_line['id']].categorie = each_line['category']
                Line_list[each_line['id']].ID_lineOne = each_line['airportOneId']
                Line_list[each_line['id']].ID_lineTwo = each_line['airportTwoId']

            self.print_console("Extracting datas from : jsonAircraftList" , 6 )

            #Extraction des données des avions et remplissage de la classe Avion et de l'offre de chaque ligne
            parsed_json_aircraft = json.loads(json_aircraft)
            i=0
            temp_departure =[]

            for each_plane in parsed_json_aircraft:
                Plane_List[each_plane['id']]=New_Plane(each_plane['id'])
                Plane_List[each_plane['id']].name=each_plane['name']
                Plane_List[each_plane['id']].categorie=each_plane['category']
                #Plane_List[each_plane['id']].range=each_plane['range']
                Plane_List[each_plane['id']].isRental=each_plane['isRental']
                Plane_List[each_plane['id']].isCargo=each_plane['isCargo']
                Plane_List[each_plane['id']].seats=np.array([each_plane['seatsEco'],each_plane['seatsBus'],each_plane['seatsFirst'],each_plane['payloadUsed']])
                #Plane_List[each_plane['id']].consumption=each_plane['consumption']
                Plane_List[each_plane['id']].utilizationPercentage=each_plane['utilizationPercentage']
                Plane_List[each_plane['id']].type=each_plane['aircraftListName']
                #Plane_List[each_plane['id']].speed=each_plane['speed']
                Plane_List[each_plane['id']].hub=each_plane['hubId']

                #ici on s'occupe de l'offre par jour
                for each_flight in each_plane['planningList']:
                    numLine = each_flight['lineId']
                    Plane_List[each_plane['id']].destination.append(numLine)
                    day = floor(each_flight['takeOffTime']/86400)
                    Offre[numLine][day] = np.array(Offre[numLine][day]) + (2*Plane_List[each_plane['id']].seats)
                    temp_departure.append(Departure(i, each_flight['takeOffTime'], each_flight['aircraftId'], each_flight['lineId']))
                    i=i+1

            global Departure_List
            Departure_List = sorted(temp_departure, key=lambda Departure: Departure.takeofftime, reverse=False)

            #maintenant on determine l'offre maximale pour le tarifs optimal
            for each_line2 in PaxAtt:
                Line_list[each_line2].Opti_Pax = [max(Offre[each_line2][i][j] for i in range(6)) for j in range(4)]

            self.print_console('Extracting datas for each lines', 10)

            step = 40 / len(Line_list)
            pourcent = 10

            pattern1 = re.compile('<div class="price">(.+?)</div>')
            pattern2 = re.compile('<div class="demand">(.+?)</div>')
            pattern3 = re.compile('href="#">(.+?)<span class="caracTooltip">')

            #pour chacunes des lignes, on request les données prix et pax de l'audit et de l'offre actuelle
            for line in Line_list:
                xhr = opener.open("http://www.airlines-manager.com/marketing/pricing/"+str(Line_list[line].id))
                response = xhr.read().decode("utf-8")
                pourcent = pourcent + step

                self.print_console("Extracting data from line : " + Line_list[line].name , pourcent)

                price = re.findall(pattern1,response)
                demande = re.findall(pattern2,response)
                etat_audit = re.findall(pattern3,response)

                del price[8:]
                del demande[8:]

                for i in range(8):
                    price[i] = price[i].replace(u'\xa0',u'')
                    price[i] = int(re.sub(u'[^0-9]','',price[i],flags=0))
                    demande[i] = demande[i].replace(u'\xa0',u'')
                    demande[i] = int(re.sub(u'[^0-9]','', demande[i] ,flags=0))

                #On remplis l'objet ligne plus completement
                Line_list[line].Audit_Price = price[:4]
                Line_list[line].Audit_Pax = demande[:4]
                Line_list[line].Current_Price = price[4:8]
                Line_list[line].Current_Pax = demande[4:8]
                Line_list[line].Fiability_Audit= etat_audit[0]

                xhr = opener.open("http://www.airlines-manager.com/network/showLine/"+str(Line_list[line].id))
                response = xhr.read().decode("utf-8")

                R_aux=[]
                pattern6 = re.compile('<td class="tableNumeric">(.+?)</td>')
                Regexp_aux = re.findall(pattern6,response)

                pattern_finish = re.compile('([A-Z]{3}) - <i>(.+?)</i> - ([^_/]+)\n')
                pattern_start = re.compile('([A-Z]{3}) - <i>(.+?)</i> - ([^_]+) /\n')
                Line_list[line].arrive = re.findall(pattern_finish, response)[0]
                Line_list[line].depart = re.findall(pattern_start, response)[0]

                R_aux.append(int(re.sub(u'[^0-9]','', Regexp_aux[24] ,flags=0)))
                R_aux.append(int(re.sub(u'[^0-9]','', Regexp_aux[25] ,flags=0)))
                R_aux.append(int(re.sub(u'[^0-9]','', Regexp_aux[26] ,flags=0)))
                R_aux.append(int(re.sub(u'[^0-9]','', Regexp_aux[27] ,flags=0)))
                Line_list[line].Revenus_Aux = R_aux

                pattern8 = re.compile('<li>Nombre de vols hebdomadaires : <strong>(.+?)</strong></li>')
                Nb_vol = int(re.findall(pattern8,response)[0])
                Line_list[line].rotation = Nb_vol

                if (Nb_vol!=0):
                    pattern7 = re.compile('<span class="redBonus">(.+?)</span>')
                    Frais = re.findall(pattern7,response)

                    Frais[0] = int(re.sub(u'[^0-9]','', Frais[0] ,flags=0))/Nb_vol
                    Frais[1] = int(re.sub(u'[^0-9]','', Frais[1] ,flags=0))/Nb_vol
                    Frais[2] = int(re.sub(u'[^0-9]','', Frais[2] ,flags=0))/Nb_vol
                    Line_list[line].Frais = Frais

                    #On execute pour chaque ligne ses méthodes pour compléter la classe
                    Line_list[line].calcul_price()
                    Line_list[line].place_restantes()
                    Line_list[line].ca_max()
                    Line_list[line].ca_current()
                    Line_list[line].ca_opti()
                    Line_list[line].efficiency_current()
                    Line_list[line].efficiency_opti()
                    Line_list[line].getHub()
                    Line_list[line].pax_to_opti()

            pattern15 = ("<span><b>(.+?)</b></span>")

            self.print_console('Extracting datas for each plane', 50)

            step = 50 / len(Plane_List)
            pourcent = 50

            #Pour chaque avions, on lance la méthode pour supprimer les doublons
            for every_plane in Plane_List:
                Plane_List[every_plane].remove_double()

                xhr = opener.open("http://www.airlines-manager.com/aircraft/show/"+str(Plane_List[every_plane].id))
                response = xhr.read().decode("utf-8")
                pourcent = pourcent + step

                self.print_console("Extracting data from plane : " + Plane_List[every_plane].name , pourcent)

                data = re.findall(pattern15,response)

                Plane_List[every_plane].dist_piste=data[0]
                Plane_List[every_plane].range = data[1]
                Plane_List[every_plane].consumption = data[2]
                Plane_List[every_plane].speed = data[3]
                Plane_List[every_plane].buy_date=data[5]
                Plane_List[every_plane].buy_price=data[6]
                Plane_List[every_plane].resultat=data[7]
                Plane_List[every_plane].nb_vol=data[8]
                Plane_List[every_plane].h_de_vol=data[9]
                Plane_List[every_plane].age=data[10]
                Plane_List[every_plane].calc_renta()

            self.save_objects()
            self.print_console("Success !", 100)

            #Update des listes pour l'utilisateur
            self.generate_lists()
            self.display_departure()

        except:
            sys.exit("Error ... Something went wrong")

    def load_objects(self):
        global Line_list, Plane_List, Name_Hub_List, Name_Line_List, Container, Departure_List
        try:
            Container= pickle.load( open( "save.p", "rb" ) )
            Line_list=Container[0]
            Plane_List=Container[1]
            Name_Hub_List=Container[2]
            Name_Line_List=Container[3]
            Departure_List=Container[4]
            self.generate_lists()
            self.display_departure()
            self.print_console("Datas Loaded", 100)
        except:
            self.print_console("Error, no file found", 100)

    def save_objects(self):
        global Container
        Container = [Line_list, Plane_List, Name_Hub_List, Name_Line_List, Departure_List]
        pickle.dump(Container, open( "save.p", "wb" ))
        self.print_console("Datas Saved", 100)

    def updates_finances(self):
        self.open_conn()

        xhr = opener.open("http://www.airlines-manager.com/finances/accounting")
        response = xhr.read().decode("utf-8")

        self.print_console("Downloading accounting of today (1/2)" , 10)

        auj = date.today()
        pattern8 = re.compile('<span class="bold">(.+?)</span>')
        span = re.findall(pattern8,response)
        pattern9 = re.compile('<span class="bold" title="Montant total">(.+?)</span>')
        span2 = re.findall(pattern9,response)
        pattern10 = re.compile('<span class="bold" title="Montant restant à rembourser">(.+?)</span>')
        span3 = re.findall(pattern10,response)

        day = substr_day(auj, 1).strftime("%Y-%m-%d")
        Financial_List[day] = New_Financial(day)
        Financial_List[day].valorisation = span[0]
        Financial_List[day].resultat = span[1]
        Financial_List[day].ts = span2[0]
        Financial_List[day].salaire = span3[-7]

        xhr = opener.open("http://www.airlines-manager.com/home")
        response = xhr.read().decode("utf-8")

        self.print_console("Downloading accounting of today (2/2)" , 50)

        pattern11 = re.compile('<div class="line">(.+?)<span>(.+?)</span></div>')
        res = re.findall(pattern11, response)
        pattern12 = re.compile('<div class="companyRanking"><(.+?)>(.+?)</div>')
        rank = re.findall(pattern12, response)

        Financial_List[day].frais_day = res[1][1]
        Financial_List[day].CA = res[0][1]
        Financial_List[day].rank = rank[0][1]

        Financial_List[day].to_int()

        pickle.dump(Financial_List, open( "finance.p", "wb" ))

        self.print_console("Success !" , 100)

    def plot_finances(self):
        X_value=[]
        Y_value=[]
        Y2_value=[]
        Y3_value=[]
        Y4_value=[]
        Y5_value=[]
        Y6_value=[]
        Y7_value=[]

        array_to_sort =[]

        for eachdate in Financial_List:
            array_to_sort.append(Financial_List[eachdate])
            array_to_sort[-1].date = time.mktime(array_to_sort[-1].date)

        sorted_array = sorted(array_to_sort, key=lambda x:x.date)

        for eachobj in sorted_array:
            try:
                X_value.append(eachobj.date)
                Y_value.append(eachobj.valorisation)
                Y2_value.append(eachobj.resultat)
                Y3_value.append(eachobj.salaire)
                Y4_value.append(eachobj.frais_day)
                Y5_value.append(eachobj.ts)
                Y6_value.append(eachobj.rank)
                Y7_value.append(eachobj.CA)
            except:
                pass


        dts = map(datetime.datetime.fromtimestamp, X_value)
        fds = dates.date2num(dts) # converted
        hfmt = dates.DateFormatter('%d/%m/%Y')

        fig = plt.figure()

        ax = fig.add_subplot(411)
        ax.plot(fds, Y_value, 'ro')
        ax.plot(fds, Y_value, 'r', label = "Valorisation")
        ax.xaxis.set_major_formatter(hfmt)
        ax.xaxis.set_major_locator(dates.DayLocator())
        #ax.set_ylim(bottom = 0)
        #ax.set_xlabel('Date')
        #ax.set_ylabel('Valorisation')
        #ax.set_title('Evolution la valorisation de votre compagnie')
        ax.legend()
        major_formatter = plt.FormatStrFormatter('%2.0f')
        plt.gca().yaxis.set_major_formatter(major_formatter)

        bx = fig.add_subplot(412)
        bx.plot(fds, Y2_value, 'r', label="Résultat")
        bx.plot(fds, Y2_value, 'ro')
        bx.plot(fds, Y7_value, 'b', label="C.A")
        bx.plot(fds, Y7_value, 'bo')
        bx.plot(fds, Y5_value, 'g', label ="T.S")
        bx.plot(fds, Y5_value, 'go')
        bx.xaxis.set_major_formatter(hfmt)
        bx.xaxis.set_major_locator(dates.DayLocator())
        #bx.set_ylim(bottom = 0)
        #bx.set_xlabel('Date')
        #bx.set_ylabel('Valeur en $')
        #bx.set_title('Evolution de votre CA, TS et résultat')
        bx.legend()
        major_formatter = plt.FormatStrFormatter('%2.0f')
        plt.gca().yaxis.set_major_formatter(major_formatter)

        cx = fig.add_subplot(413)
        cx.plot(fds, Y6_value, 'b', label="Classement")
        cx.plot(fds, Y6_value, 'bo')
        cx.xaxis.set_major_formatter(hfmt)
        cx.xaxis.set_major_locator(dates.DayLocator())
        #cx.set_ylim(bottom = 0)
        #cx.set_xlabel('Date')
        #cx.set_ylabel('Classement')
        #cx.set_title('Evolution de votre classement')
        cx.legend()
        major_formatter = plt.FormatStrFormatter('%2.0f')
        plt.gca().yaxis.set_major_formatter(major_formatter)

        dx = fig.add_subplot(414)
        dx.plot(fds, Y3_value, 'r', label="Masse Salariale")
        dx.plot(fds, Y3_value, 'ro')
        dx.plot(fds, Y4_value, 'b', label="Frais de vols")
        dx.plot(fds, Y4_value, 'bo')
        dx.xaxis.set_major_formatter(hfmt)
        dx.xaxis.set_major_locator(dates.DayLocator())
        #dx.set_ylim(bottom = 0)
        #dx.set_xlabel('Date')
        #dx.set_ylabel('Frais en $')
        #dx.set_title('Evolution de vos frais de fonctionnement')
        dx.legend()
        major_formatter = plt.FormatStrFormatter('%2.0f')
        plt.gca().yaxis.set_major_formatter(major_formatter)

        #plt.xticks(rotation='vertical')
        plt.subplots_adjust(bottom=0.05, top=0.95, left=0.07, right=0.98)
        plt.get_current_fig_manager().window.showMaximized()
        plt.show()

    def plot_all_line(self):

        data = []
        label = []

        for each_line in Line_list:
            data.append([Line_list[each_line].CA_Current_G,Line_list[each_line].CA_Opti_G,Line_list[each_line].CA_Audit_G])
            label.append(Line_list[each_line].name)

        pylab.xlabel("Lignes")
        pylab.ylabel("Chiffre d'Affaires")
        pylab.title("Chiffre d'affaires par ligne")

        dim = len(data[0])
        w = 0.75
        dimw = w / dim

        color=['r','g','y']
        titre=['CA actuelle','CA optimal','CA audit']

        x = pylab.arange(len(data))
        for i in range(len(data[0])) :
            y = [d[i] for d in data]
            pylab.bar(x + i * dimw, y, dimw, bottom=0.001, color=color[i%3], label=titre[i%3])

        pylab.legend()
        pylab.gca().set_xticks(x + w / 2)
        pylab.gca().set_xticklabels(label, rotation=90)
        pylab.subplots_adjust(bottom=0.1, top=0.96, right=0.98, left = 0.05)
        major_formatter = pylab.FormatStrFormatter('%2.0f')
        pylab.gca().yaxis.set_major_formatter(major_formatter)
        pylab.get_current_fig_manager().window.showMaximized()
        pylab.show()

    def plot_single_line(self):

        def f1(a,b,x):
            "calcul de la demande en fonction de l'audit (a,b) et de l'offre (c) suivant pente douce"
            return -(b*x)/(3*a)+(4*b/3)

        def f2(a,b,x):
            "calcul de la demande en fonction de l'audit (a,b) et de l'offre (c) suivant pente forte"
            return -(3*b*x)/(a)+(4*b)

        def f3(a,b,x):
            "calcul de l'air de la courbe sous la petite pente = Benefice"
            return x*f1(a,b,x)

        def f4(a,b,x):
            "calcul de l'air de la courbe sous la pente forte = Benefice"
            return x*f2(a,b,x)

        def plot(a,b,c,d, color, text):
            "tracage des courbes en fonction de l'audit (a,b) et de l'offre (c,d)"

            t1 = np.arange(0, a, 15)
            t2 = np.arange(a, 4*a/3, 15)

            ax.plot(t1,f1(a,b,t1), color, label=text)
            ax.plot(t2,f2(a,b,t2), color)
            ax.plot(a, b, 'ro')
            ax.plot(d, c, 'b*')

            bx.plot(t1, f3(a,b,t1), color, label=text)
            bx.plot(t2, f4(a,b,t2) , color)
            bx.plot(a, a*b, 'ro')
            bx.plot(d, c*d, 'b*')

        selectedID = int(self.id_line.text())

        #Initialisation des graphs
        fig = plt.figure()

        ax = fig.add_subplot(211)
        ax.set_xlabel('Prix du billet en $')
        ax.set_ylabel('Demande en Pax/T')
        ax.set_title('Evolution de la demande en fonction du prix du billet')
        #ax.yaxis.get_major_formatter().set_useOffset(False)

        bx = fig.add_subplot(212)
        bx.set_xlabel('Prix du billet en $')
        bx.set_ylabel('C.A des classes')
        bx.set_title('Evolution du C.A en fonction du prix du billet')
        #ax.yaxis.get_major_formatter().set_useOffset(False)

        color = ['blue','red','green','yellow']
        titre = ['Economique', 'Affaire', 'Première', 'Cargo']

        for i in range(4):
            #recuperation des valeur pour les tracés
            a = Line_list[selectedID].Audit_Price[i]
            b = Line_list[selectedID].Audit_Pax[i]
            c = Line_list[selectedID].Current_Pax[i]
            d = Line_list[selectedID].Current_Price[i]

            plot(a,b,c,d, color[i], titre[i])

        ax.legend()
        bx.legend()
        plt.subplots_adjust(bottom=0.05, top=0.95, right=0.98, left = 0.05)
        major_formatter = plt.FormatStrFormatter('%2.0f')
        plt.gca().yaxis.set_major_formatter(major_formatter)
        plt.get_current_fig_manager().window.showMaximized()
        plt.show()

Container = []
Line_list={}
Plane_List={}
Departure_List=[]
Name_Hub_List={}
Name_Line_List={}
Financial_List = {}

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Mon_IHM(MainWindow)
    MainWindow.show()
    MainWindow.setWindowTitle('AM2 - Tool')
    sys.exit(app.exec_())
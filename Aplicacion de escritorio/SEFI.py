from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker, relationship
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QCompleter, QTableView,QHeaderView,QMessageBox, QMdiSubWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from os import path

from Model import Cliente
from Model import Usuario
from Model import Venta

import pymysql
import pandas as pd

engine = create_engine('mysql+pymysql://root:@localhost/sefi')
Session = sessionmaker(bind=engine)
session = Session()


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 530)
        MainWindow.setMinimumSize(QtCore.QSize(1124, 530))
        MainWindow.setMaximumSize(QtCore.QSize(1124, 530))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 90, 1111, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.enviarFactura = QtWidgets.QPushButton(self.tab_4)
        self.enviarFactura.setGeometry(QtCore.QRect(450, 310, 211, 23))
        self.enviarFactura.setObjectName("enviarFactura")
        self.factura1 = QtWidgets.QLineEdit(self.tab_4)
        self.factura1.setGeometry(QtCore.QRect(280, 90, 591, 20))
        self.factura1.setObjectName("factura1")
        self.factura2 = QtWidgets.QLineEdit(self.tab_4)
        self.factura2.setGeometry(QtCore.QRect(280, 130, 591, 20))
        self.factura2.setObjectName("factura2")
        self.factura3 = QtWidgets.QLineEdit(self.tab_4)
        self.factura3.setGeometry(QtCore.QRect(280, 170, 591, 20))
        self.factura3.setObjectName("factura3")
        self.factura4 = QtWidgets.QLineEdit(self.tab_4)
        self.factura4.setGeometry(QtCore.QRect(280, 210, 591, 20))
        self.factura4.setObjectName("factura4")
        self.comboBox1 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox1.setGeometry(QtCore.QRect(280, 250, 591, 22))
        self.comboBox1.setObjectName("comboBox1")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(90, 90, 161, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(90, 130, 161, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(90, 170, 161, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(90, 210, 161, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(90, 250, 161, 20))
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidgetVerFacturas = QtWidgets.QTableWidget(self.tab)
        self.tableWidgetVerFacturas.setGeometry(QtCore.QRect(50, 30, 1011, 301))
        self.tableWidgetVerFacturas.setObjectName("tableWidgetVerFacturas")
        self.tableWidgetVerFacturas.setColumnCount(5)
        self.tableWidgetVerFacturas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetVerFacturas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetVerFacturas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetVerFacturas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetVerFacturas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetVerFacturas.setHorizontalHeaderItem(4, item)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setGeometry(QtCore.QRect(240, 70, 621, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 110, 621, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 150, 621, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 190, 621, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(90, 70, 101, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(90, 110, 101, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(90, 150, 101, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(90, 190, 101, 16))
        self.label_11.setObjectName("label_11")
        self.btnaddClientes = QtWidgets.QPushButton(self.tab_3)
        self.btnaddClientes.setGeometry(QtCore.QRect(420, 280, 221, 23))
        self.btnaddClientes.setObjectName("btnaddClientes")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidgetVerFacturas_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidgetVerFacturas_2.setGeometry(QtCore.QRect(50, 30, 1011, 301))
        self.tableWidgetVerFacturas_2.setObjectName("tableWidgetVerFacturas_2")
        self.tableWidgetVerFacturas_2.setColumnCount(4)
        self.tableWidgetVerFacturas_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetVerFacturas_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetVerFacturas_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetVerFacturas_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetVerFacturas_2.setHorizontalHeaderItem(3, item)
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 171, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(870, 10, 231, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("sefi.PNG"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.tabWidget.setCurrentIndex(0)
        clientes = session.query(Cliente.nombre_cliente).all()
        print(clientes)
        self.tableWidgetVerFacturas.horizontalHeader().setSectionResizeMode( QtWidgets.QHeaderView.Stretch)
        self.tableWidgetVerFacturas_2.horizontalHeader().setSectionResizeMode( QtWidgets.QHeaderView.Stretch)
        for dato in clientes:
            self.comboBox1.addItem(str(dato))
        
        self.enviarFactura.clicked.connect(self.sendFactura)

        self.btnaddClientes.clicked.connect(self.sendCliente)

        self.tabWidget.currentChanged.connect(self.consulta1)

    def consulta1(self):
        
        miConexion = pymysql.connect( host='localhost', user= 'root', password='', db='sefi' )
        cur = miConexion.cursor()
        sql="select * from Venta"
        count=cur.execute(sql)
        self.tableWidgetVerFacturas.setRowCount(count) 
        for carlos in range(count): 
            miConexion = pymysql.connect( host='localhost', user= 'root', password='', db='sefi' )
            cur = miConexion.cursor()
            sql="select nombre_producto,nombre_servicio,cantidad_producto,precio_pu,fk_cliente from venta where id_venta=%s "
            cur.execute(sql,carlos+1)
            id_con=cur.fetchone()
            #print(cur.execute(sql,j+1))
            self.tableWidgetVerFacturas.setItem(carlos,0,QTableWidgetItem(str(id_con[0])))
            self.tableWidgetVerFacturas.setItem(carlos,1,QTableWidgetItem(str(id_con[1])))
            self.tableWidgetVerFacturas.setItem(carlos,2,QTableWidgetItem(str(id_con[2])))
            self.tableWidgetVerFacturas.setItem(carlos,3,QTableWidgetItem(str(id_con[3]))) 
            self.tableWidgetVerFacturas.setItem(carlos,4,QTableWidgetItem(str(id_con[4]))) 


        #################################
        miConexion = pymysql.connect( host='localhost', user= 'root', password='', db='sefi' )
        cur = miConexion.cursor()
        sql="select * from Cliente"
        count=cur.execute(sql)
        self.tableWidgetVerFacturas_2.setRowCount(count) 
        for carlos in range(count): 
            miConexion = pymysql.connect( host='localhost', user= 'root', password='', db='sefi' )
            cur = miConexion.cursor()
            sql="select nombre_cliente,rfc,domicilio,telefono from cliente where id_cliente=%s "
            cur.execute(sql,carlos+1)
            id_con=cur.fetchone()
            #print(cur.execute(sql,j+1))
            self.tableWidgetVerFacturas_2.setItem(carlos,0,QTableWidgetItem(str(id_con[0])))
            self.tableWidgetVerFacturas_2.setItem(carlos,1,QTableWidgetItem(str(id_con[1])))
            self.tableWidgetVerFacturas_2.setItem(carlos,2,QTableWidgetItem(str(id_con[2])))
            self.tableWidgetVerFacturas_2.setItem(carlos,3,QTableWidgetItem(str(id_con[3]))) 
             
            




        miConexion.close()
    def sendCliente(self):
        nombre_cliente = self.lineEdit.text()
        RFC = self.lineEdit_2.text()
        domicilio = self.lineEdit_3.text()
        telefono = self.lineEdit_4.text()
        NewClient = Cliente(nombre_cliente=nombre_cliente,rfc=RFC,domicilio=domicilio,telefono=telefono)
        session.add(NewClient)
        session.commit()
        
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
    def sendFactura(self):
        
        nombre_producto = self.factura1.text()
        nombre_servicio = self.factura2.text()
        cantidad = self.factura3.text()
        precio = self.factura4.text()
        nombre_cliente = self.comboBox1.currentText()
        NewFactura = Venta(nombre_producto=nombre_producto,nombre_servicio=nombre_servicio,cantidad_producto=cantidad,precio_pu=precio,fk_usuario=1,fk_cliente=1)
        session.add(NewFactura)
        session.commit()

        self.factura1.setText('')
        self.factura2.setText('')
        self.factura3.setText('')
        self.factura4.setText('')

    

        

        









    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.enviarFactura.setText(_translate("MainWindow", "Enviar"))
        self.label_3.setText(_translate("MainWindow", "Nombre del producto"))
        self.label_4.setText(_translate("MainWindow", "Nombre del servicio"))
        self.label_5.setText(_translate("MainWindow", "Cantidad"))
        self.label_6.setText(_translate("MainWindow", "Precio"))
        self.label_7.setText(_translate("MainWindow", "Nombre del cliente"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Agregar facturas"))
        item = self.tableWidgetVerFacturas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre del producto"))
        item = self.tableWidgetVerFacturas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre del servicio"))
        item = self.tableWidgetVerFacturas.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cantidad"))
        item = self.tableWidgetVerFacturas.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Precio"))
        item = self.tableWidgetVerFacturas.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ID del Cliente"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Ver facturas"))
        self.label_8.setText(_translate("MainWindow", "Nombre del cliente"))
        self.label_9.setText(_translate("MainWindow", "RFC"))
        self.label_10.setText(_translate("MainWindow", "Domicilio"))
        self.label_11.setText(_translate("MainWindow", "Telefono"))
        self.btnaddClientes.setText(_translate("MainWindow", "Enviar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Agregar clientes"))
        item = self.tableWidgetVerFacturas_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre del cliente"))
        item = self.tableWidgetVerFacturas_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "RFC"))
        item = self.tableWidgetVerFacturas_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Domicilio"))
        item = self.tableWidgetVerFacturas_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Telefono"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "ver clientes"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">SEFI</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

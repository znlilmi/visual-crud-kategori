# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kategoriview.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import mysql.connector as mc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 485)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelId = QtWidgets.QLabel(Form)
        self.labelId.setObjectName("labelId")
        self.verticalLayout.addWidget(self.labelId)
        self.labelName = QtWidgets.QLabel(Form)
        self.labelName.setObjectName("labelName")
        self.verticalLayout.addWidget(self.labelName)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditId = QtWidgets.QLineEdit(Form)
        self.lineEditId.setObjectName("lineEditId")
        self.verticalLayout_2.addWidget(self.lineEditId)
        self.lineEditName = QtWidgets.QLineEdit(Form)
        self.lineEditName.setObjectName("lineEditName")
        self.verticalLayout_2.addWidget(self.lineEditName)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonInsert = QtWidgets.QPushButton(Form)
        self.pushButtonInsert.setObjectName("pushButtonInsert")
        self.horizontalLayout.addWidget(self.pushButtonInsert)
        self.updateButton = QtWidgets.QPushButton(Form)
        self.updateButton.setObjectName("updateButton")
        self.horizontalLayout.addWidget(self.updateButton)
        self.deleteButton = QtWidgets.QPushButton(Form)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.pushButtonLoad = QtWidgets.QPushButton(Form)
        self.pushButtonLoad.setObjectName("pushButtonLoad")
        self.horizontalLayout.addWidget(self.pushButtonLoad)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.searchButton = QtWidgets.QPushButton(Form)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 2)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 2)
        self.labelResult = QtWidgets.QLabel(Form)
        self.labelResult.setObjectName("labelResult")
        self.gridLayout.addWidget(self.labelResult, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.pushButtonInsert.clicked.connect(self.insertkategori)
        self.pushButtonLoad.clicked.connect(self.loadkategori)
        self.updateButton.clicked.connect(self.updatekategori)
        self.deleteButton.clicked.connect(self.deletekategori)
        self.tableWidget.cellClicked.connect(self.getById)
        self.searchButton.clicked.connect(self.searchkategori)
        
    def insertkategori(self):
        try:
            mydb = mc.connect(
                host ="localhost",
                port="3306",
                user="root",
                password="",
                database ="penjualan_visual"
            )
            cursor = mydb.cursor()
            idkat = self.lineEditId.text()
            namekat = self.lineEditName.text()

            sql = "INSERT INTO kategori (id,name) VALUES (%s,%s)"
            val = (idkat,namekat)
            cursor.execute(sql,val)
            mydb.commit()
            self.labelResult.setText("Data Kategori Berhasil Disimpan")

            self.lineEditId.setText("")
            self.lineEditName.setText("")
        except mc.Error as e:
            self.labelResult.setText("Data Kategori Gagal Disimpan")
            
    def loadkategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                port="3306",
                user="root",
                password="",
                database="penjualan_visual"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM kategori ORDER BY ID ASC")
            result = mycursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.labelResult.setText("Data Kategori Berhasil Ditampilkan")
        except mc.Error as err:
            self.labelResult.setText("Data Kategori Gagal DiLoad")
            
    def updatekategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                port="3306",
                user="root",
                password="",
                database="penjualan_visual"
            )
            cursor = mydb.cursor()
            idkat = self.lineEditId.text()
            namekat = self.lineEditName.text()

            sql = "UPDATE kategori SET name = %s WHERE id = %s"
            val = (namekat, idkat)
            cursor.execute(sql, val)
            mydb.commit()
            self.labelResult.setText("Data Kategori Berhasil Diupdate")

            self.lineEditId.setText("")
            self.lineEditName.setText("")
        except mc.Error as e:
            self.labelResult.setText("Data Kategori Gagal Diupdate")
            
    def deletekategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                port="3306",
                user="root",
                password="",
                database="penjualan_visual"
            )
            cursor = mydb.cursor()
            idkat = self.lineEditId.text()

            sql = "DELETE FROM kategori WHERE id = %s"
            val = (idkat,)
            cursor.execute(sql, val)
            mydb.commit()
            self.labelResult.setText("Data Kategori Berhasil Dihapus")

            self.lineEditId.setText("")
            self.lineEditName.setText("")
        except mc.Error as e:
            self.labelResult.setText("Data Kategori Gagal Dihapus")
            
    def getById(self, row, column):
        idkat = self.tableWidget.item(row, 0).text()
        namekat = self.tableWidget.item(row, 1).text()
        self.lineEditId.setText(idkat)
        self.lineEditName.setText(namekat)
        
    def searchkategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                port="3306",
                user="root",
                password="",
                database="penjualan_visual"
            )
            mycursor = mydb.cursor()
            search_value = self.lineEdit.text()
            query = "SELECT * FROM kategori WHERE id LIKE %s OR name LIKE %s ORDER BY ID ASC"
            mycursor.execute(query, ('%' + search_value + '%', '%' + search_value + '%'))
            result = mycursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.labelResult.setText("Data Kategori Berhasil Dicari")
        except mc.Error as err:
            self.labelResult.setText("Data Kategori Gagal Dicari")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelId.setText(_translate("Form", "ID Kategori"))
        self.labelName.setText(_translate("Form", "Nama Karegori"))
        self.pushButtonInsert.setText(_translate("Form", "INSERT DATA"))
        self.updateButton.setText(_translate("Form", "UPDATE"))
        self.deleteButton.setText(_translate("Form", "DELETE"))
        self.pushButtonLoad.setText(_translate("Form", "LOAD DATA"))
        self.searchButton.setText(_translate("Form", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Kategori"))
        self.labelResult.setText(_translate("Form", "TextLabel"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
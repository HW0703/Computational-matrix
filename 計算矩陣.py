# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import sympy as sp
import re

class Ui_MainWindow(object):
    
    def Main_Window(self, MainWindow):
        ##### 主視窗 #####
        MainWindow.setFixedSize(1280, 800)     
        MainWindow.setWindowTitle("Matrix")     #主視窗標題
        self.font()
        self.matrix_page_1_object()
        
        
    def matrix_page_1_object(self):           
        ##### 第一頁 #####
        self.page1 = QtWidgets.QWidget(MainWindow)
        self.page1.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        
        ##### 標題 ######
        self.title = QtWidgets.QLabel('輸入矩陣大小',self.page1)       #在第一頁創立標題
        self.title.setGeometry(QtCore.QRect(0, 50, 1280, 200))
        self.title.setFont(self.font_72)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        
        ##### 行 ######
        self.matrix_row = QtWidgets.QLineEdit(self.page1)
        self.matrix_row.setGeometry(QtCore.QRect(420, 350, 125, 125))
        self.matrix_row.setFont(self.font_48)
        self.matrix_row.setAlignment(QtCore.Qt.AlignCenter)
        
        ##### 中間的X #####
        self.matrix_x_text = QtWidgets.QLabel('X',self.page1)
        self.matrix_x_text.setGeometry(QtCore.QRect(570, 350, 125, 125))
        self.matrix_x_text.setFont(self.font_48)
        self.matrix_x_text.setAlignment(QtCore.Qt.AlignCenter)
        
        ##### 列 #####
        self.matrix_column = QtWidgets.QLineEdit(self.page1)
        self.matrix_column.setGeometry(QtCore.QRect(720, 350, 125, 125))
        self.matrix_column.setFont(self.font_48)
        self.matrix_column.setAlignment(QtCore.Qt.AlignCenter)
        
        ##### 確定按鍵 #####
        self.chick_page1_button = QtWidgets.QPushButton('確定',self.page1)
        self.chick_page1_button.setFont(self.font_48)
        self.chick_page1_button.setGeometry(QtCore.QRect(550, 600, 175, 90))
        self.chick_page1_button.clicked.connect(self.page1_to_page2)
    
        
    def page1_to_page2(self):
        self.matrix_i = self.matrix_row.text()
        self.matrix_j = self.matrix_column.text()
        if (self.matrix_i.isdigit() and self.matrix_j.isdigit()):    #判斷是否為純數字組成之字串
            self.get_matrix_row = int(self.matrix_i)
            self.get_matrix_column = int(self.matrix_j)
            self.matrix_page_2_object()
            if (self.get_matrix_row <= 0 or self.get_matrix_column <= 0): #判斷行列是否為大於0
                QtWidgets.QMessageBox.information(self.page1, "Message", "輸入錯誤")
            else:
                self.page1.close()
                self.page2.show()
        else:
            QtWidgets.QMessageBox.information(self.page1, "Message", "請輸入數字")
            

    def matrix_page_2_object(self):            #第二頁
        self.page2 = QtWidgets.QWidget(MainWindow)
        self.page2.setGeometry(QtCore.QRect(0, 0, 1280, 800))

        ##### 標題 #####
        self.title = QtWidgets.QLabel('輸入矩陣數字',self.page2)
        self.title.setGeometry(QtCore.QRect(0, 0, 1280, 200))
        self.title.setFont(self.font_72) 
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        
        ##### 格子間隔 #####
        self.matrix_grid = QtWidgets.QGridLayout(self.page2)
        self.matrix_grid.setContentsMargins(200, 200, 200, 200)
        
        ##### 產生 行X列 個格子 #####
        self.matrix_dic = dict()
        num = 0
        self.matrix_position = [(i, j) for i in range(self.get_matrix_row) for j in range(self.get_matrix_column)]
        for self.matrix_position in self.matrix_position:
            self.matrix_dic["matrix_line_edit_%d" % num]= QtWidgets.QLineEdit(self.page2)
            self.matrix_dic["matrix_line_edit_%d" % num].setFont(self.font_48)
            self.matrix_dic["matrix_line_edit_%d" % num].setAlignment(QtCore.Qt.AlignCenter)
            self.matrix_dic["matrix_line_edit_%d" % num].setMaximumSize(QtCore.QSize(125, 125))
            self.matrix_grid.addWidget(self.matrix_dic["matrix_line_edit_%d" % num], *self.matrix_position)
            num += 1
        
        ##### 確任和返回按鈕 #####
        self.chick_page2_button = QtWidgets.QPushButton('確定',self.page2)
        self.chick_page2_button.setFont(self.font_48)
        self.chick_page2_button.setGeometry(QtCore.QRect(450, 650, 175, 100))
        self.chick_page2_button.clicked.connect(self.page2_to_page3)
        
        self.back_page2_button = QtWidgets.QPushButton('返回',self.page2)
        self.back_page2_button.setFont(self.font_48)
        self.back_page2_button.setGeometry(QtCore.QRect(650, 650, 175, 100))
        self.back_page2_button.clicked.connect(self.page2_to_page1)
        
        
    def page2_to_page1 (self):
        self.matrix_page_1_object()
        self.page1.show()
        self.page2.close()
    
        
    def page2_to_page3 (self):
        self.matrix_test = []
        have_str = 0
        for num in range(len(self.matrix_dic)):
            self.matrix_test.append(self.matrix_dic["matrix_line_edit_%d" % num].text())
            ##### 有根號 #####
            if ("√" in self.matrix_test[num]):
                matrix_root = self.matrix_test[num].split('√')
                if (matrix_root[0]=='' and matrix_root[1].isdigit()):
                    have_str += 0
                    self.matrix_test[num] = sp.sqrt(int(matrix_root[1]))
                elif (matrix_root[0].isdigit() and matrix_root[1].isdigit()):
                    have_str += 0
                    self.matrix_test[num] = int(matrix_root[0])*sp.sqrt(int(matrix_root[1]))
                else:
                    have_str +=1
            ##### 有分數 #####
            elif ("/" in self.matrix_test[num]):
                fraction_root = self.matrix_test[num].split('/')
                if (fraction_root[0].isdigit() and fraction_root[1].isdigit()):
                    have_str += 0
                    self.matrix_test[num] = sp.Rational(fraction_root[0],fraction_root[1])
                else:
                    have_str +=1
            ##### 無根號、無分數 #####
            else:
                if (self.matrix_test[num].isdigit()):
                    have_str += 0
                    self.matrix_test[num] = int(self.matrix_test[num])
                else:
                    have_str +=1
        if (have_str == 0):
            self.matrix_total = np.reshape(self.matrix_test,(self.get_matrix_row,self.get_matrix_column))   #輸入的矩陣
            self.matrix_page_3_object()
            self.display_matrix()
            self.page2.hide()
            self.page3.show()
        else:
            QtWidgets.QMessageBox.information(self.page2, "Message", "輸入錯誤")
            
        
    def matrix_page_3_object(self):            #第三頁
        self.page3 = QtWidgets.QWidget(MainWindow)
        self.page3.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.select_column_one()
        self.select_column_two()
        
    
        ##### 顯示輸入的矩陣 #####
        self.matrix_display = QtWidgets.QTextBrowser(self.page3)
        self.matrix_display.setGeometry(QtCore.QRect(130, 50, 320, 200))
        self.matrix_display.setFont(self.font_22)
        self.matrix_display.setAlignment(QtCore.Qt.AlignCenter)
        
        

        ##### 運算選項 #####
        self.column_operation = QtWidgets.QRadioButton('單列運算',self.page3)   #單列運算選項
        self.column_operation.setGeometry(QtCore.QRect(600, 45, 225, 50))
        self.column_operation.setFont(self.font_24)
        self.column_operation.clicked.connect(self.select_two.hide)
        self.column_operation.clicked.connect(self.select_one.show)
        
        ##### 列與列 #####
        self.column_and_column = QtWidgets.QRadioButton('列與列運算',self.page3) #列與列運算選項
        self.column_and_column.setGeometry(QtCore.QRect(840, 45, 225, 50))
        self.column_and_column.setFont(self.font_24)
        self.column_and_column.clicked.connect(self.select_one.hide)
        self.column_and_column.clicked.connect(self.select_two.show)
        
        ##### 返回按鈕 #####
        self.back_page3_button = QtWidgets.QPushButton('返回',self.page3)     #返回按鈕
        self.back_page3_button.setFont(self.font_32)
        self.back_page3_button.setGeometry(QtCore.QRect(1050, 250, 120, 70))
        self.back_page3_button.clicked.connect(self.page3_to_page2)
        
        ##### 計算結果顯示 #####
        self.calculation_results_title = QtWidgets.QLabel("計算結果",self.page3)      #顯示的標題
        self.calculation_results_title.setGeometry(QtCore.QRect(530, 450, 220, 100))
        self.calculation_results_title.setFont(self.font_32_setbold)
        self.calculation_results_title.setAlignment(QtCore.Qt.AlignCenter)
        
        self.calculation_results_show = QtWidgets.QTextBrowser(self.page3)     #顯示的視窗
        self.calculation_results_show.setGeometry(QtCore.QRect(480, 550, 320, 200))
        self.calculation_results_show.setFont(self.font_22)
        self.calculation_results_show.setAlignment(QtCore.Qt.AlignCenter)
        
        
        ##### 第三頁單列運算選項 #####
    def select_column_one (self):
        self.select_one = QtWidgets.QFrame(self.page3)             
        self.select_one.setGeometry(QtCore.QRect(550, 140, 620, 70))
        self.select_one.close()
        self.one_matrix_final = self.matrix_total.astype(object)
        

        ##### 單列:選擇哪一列 #####
        self.one_choose_comboBox = QtWidgets.QComboBox(self.select_one)
        self.one_choose_comboBox.setGeometry(QtCore.QRect(0, 0, 120, 70))
        self.one_choose_comboBox.setFont(self.font_22)
        self.one_choose_comboBox.addItems(["第%d列" % i for i in range (1,self.get_matrix_row+1)])
        self.one_choose_comboBox.setMaxVisibleItems(5)
        
        
         
        ##### 單列:選擇×÷ #####
        self.multiply_and_divide_comboBox = QtWidgets.QComboBox(self.select_one)
        self.multiply_and_divide_comboBox.setGeometry(QtCore.QRect(200, 0, 70, 70))
        self.multiply_and_divide_comboBox.addItems(["×","÷"])
        self.multiply_and_divide_comboBox.setFont(self.font_22)
        
        ##### 單列:輸入計算 #####
        self.operation_num = QtWidgets.QLineEdit(self.select_one)
        self.operation_num.setGeometry(QtCore.QRect(350, 0, 70, 70))
        self.operation_num.setFont(self.font_22)
        self.operation_num.setAlignment(QtCore.Qt.AlignCenter)
        
        ##### 單列: 計算按鈕 #####
        self.operation_button = QtWidgets.QPushButton('計算',self.select_one)
        self.operation_button.setFont(self.font_32)
        self.operation_button.setGeometry(QtCore.QRect(500, 0, 120, 70))
        self.operation_button.clicked.connect(self.select_one_calculate)
        

        ##### 第三頁列與列運算選項 #####
    def select_column_two (self):
        self.select_two = QtWidgets.QWidget(self.page3)
        self.select_two.setGeometry(QtCore.QRect(550, 140, 620, 70))
        self.select_two.close()
        self.two_matrix_final = self.matrix_total.astype(object)
        
        
        ##### 列與列:第一格選擇哪一列 #####
        self.two_choose_comboBox = QtWidgets.QComboBox(self.select_two)
        self.two_choose_comboBox.setGeometry(QtCore.QRect(0, 0, 120, 70))
        self.two_choose_comboBox.setFont(self.font_22)
        self.two_choose_comboBox.addItems(["第%d列" % i for i in range (1,self.get_matrix_row+1)])
        self.two_choose_comboBox.setMaxVisibleItems(5)
        
        ##### 中間的X和÷ #####
        self.multiply_divide = QtWidgets.QComboBox(self.select_two)
        self.multiply_divide.setGeometry(QtCore.QRect(130, 0, 70, 70))
        self.multiply_divide.addItems(["×","÷"])
        self.multiply_divide.setFont(self.font_22)
        
        ##### 倍數輸入#####
        self.multiple = QtWidgets.QLineEdit(self.select_two)
        self.multiple.setGeometry(QtCore.QRect(210, 0, 70, 70))
        self.multiple.setFont(self.font_22)
        self.multiple.setAlignment(QtCore.Qt.AlignCenter)
        
        ##### 列與列:選擇+- #####
        self.addition_and_subtraction_comboBox = QtWidgets.QComboBox(self.select_two)
        self.addition_and_subtraction_comboBox.setGeometry(QtCore.QRect(290, 0, 70, 70))
        self.addition_and_subtraction_comboBox.addItems(["+","-"])
        self.addition_and_subtraction_comboBox.setFont(self.font_22)
        
        ##### 列與列:第三格選擇哪一列 #####
        self.final_choose_comboBox = QtWidgets.QComboBox(self.select_two)
        self.final_choose_comboBox.setGeometry(QtCore.QRect(370, 0, 120, 70))
        self.final_choose_comboBox.setFont(self.font_22)
        self.final_choose_comboBox.addItems(["第%d列" % i for i in range (1,self.get_matrix_row+1)])
        self.final_choose_comboBox.setMaxVisibleItems(5)
        
        ##### 列與列: 計算按鈕 #####
        self.operation_button = QtWidgets.QPushButton('計算',self.select_two)
        self.operation_button.setFont(self.font_32)
        self.operation_button.setGeometry(QtCore.QRect(500, 0, 120, 70))
        self.operation_button.clicked.connect(self.select_two_calculate)
        
    def display_matrix (self):
        for i in range (self.get_matrix_row):
            matrix_str = ''
            for j in range (self.get_matrix_column):
                if ('sqrt' in str(self.matrix_total[i][j])):
                    sqrt_text = re.sub(u'\*?sqrt\((\d+)\)', u'√\\1', str(self.matrix_total[i][j]))
                    if j == (self.get_matrix_column-1):
                        matrix_str = matrix_str + str(sqrt_text)
                    else:
                        matrix_str = matrix_str + str(sqrt_text) + '     '
                else:
                    if j == (self.get_matrix_column-1):
                        matrix_str = matrix_str + str(self.matrix_total[i][j])
                    else:
                        matrix_str = matrix_str + str(self.matrix_total[i][j]) + '    '
            self.matrix_display.append(matrix_str)
            self.matrix_display.setAlignment(QtCore.Qt.AlignCenter)
        
        
    def page3_to_page2 (self):
        self.matrix_page_2_object()
        self.page3.close()
        self.page2.show()
        
        
    def select_one_calculate(self):    #單行矩陣計算
        select_row = self.one_choose_comboBox.currentIndex()
        multiply_and_divide = self.multiply_and_divide_comboBox.currentText()
        num = self.operation_num.text()
        ##### 有根號 #####
        if ("√" in num):
            num_root = num.split('√')
            if (num_root[0] == '' and num_root[1].isdigit()):
                if (multiply_and_divide == "×"):
                    self.one_matrix_final[select_row] = self.one_matrix_final[select_row]*sp.sqrt(int(num_root[1]))
                else:
                    self.one_matrix_final[select_row] = self.one_matrix_final[select_row]/sp.sqrt(int(num_root[1]))
                self.select_one_final_show()
            elif(num_root[0].isdigit() and num_root[1].isdigit()):
                if (multiply_and_divide == "×"):
                    self.one_matrix_final[select_row] = self.one_matrix_final[select_row]*(int(num_root[0])*sp.sqrt(int(num_root[1])))
                else:
                    self.one_matrix_final[select_row] = self.one_matrix_final[select_row]/(int(num_root[0])*sp.sqrt(int(num_root[1])))
                self.select_one_final_show()           
            else:
                QtWidgets.QMessageBox.information(self.page3, "Message", "輸入錯誤")
        ##### 有分數 #####
        elif ("/" in num):
            num_fraction = num.split('/')
            if (num_fraction[0].isdigit() and num_fraction[1].isdigit()):
                if (multiply_and_divide == "×"):
                    self.one_matrix_final[select_row] = self.one_matrix_final[select_row]*sp.Rational(num_fraction[0],num_fraction[1])
                else:
                    self.one_matrix_final[select_row] = self.one_matrix_final[select_row]/sp.Rational(num_fraction[0],num_fraction[1])
                self.select_one_final_show()
            else:
                QtWidgets.QMessageBox.information(self.page3, "Message", "輸入錯誤")
        ##### 無根號、無分數 #####
        else:
            if (num.isdigit()):
                num = int(self.operation_num.text())
                if (multiply_and_divide == "×"):
                    self.one_matrix_final[select_row] = self.one_matrix_final[select_row]*num
                else:
                    self.one_matrix_final[select_row] = self.one_matrix_final[select_row]/num
                self.select_one_final_show()
            else:
                QtWidgets.QMessageBox.information(self.page3, "Message", "輸入錯誤")
        
        
    def select_one_final_show (self):
        self.calculation_results_show.clear()
        for i in range (self.get_matrix_row):
            matrix_str = ''
            for j in range (self.get_matrix_column):
                if ('sqrt' in str(self.one_matrix_final[i][j])):
                    root_text = re.sub(u'\*?sqrt\((\d+)\)', u'√\\1', str(self.one_matrix_final[i][j]))
                    if j == (self.get_matrix_column-1):
                        matrix_str = matrix_str + str(root_text)
                    else:
                        matrix_str = matrix_str + str(root_text) + '     '
                else:
                    if j == (self.get_matrix_column-1):
                        matrix_str = matrix_str + str(self.one_matrix_final[i][j])
                    else:
                        matrix_str = matrix_str + str(self.one_matrix_final[i][j]) + '     '
            self.calculation_results_show.append(matrix_str)
            self.calculation_results_show.setAlignment(QtCore.Qt.AlignCenter)
    
    def select_two_calculate(self):
        select_row = self.two_choose_comboBox.currentIndex()
        multiply_and_divide = self.multiply_divide.currentText()
        num = self.multiple.text()
        addition_and_subtraction = self.addition_and_subtraction_comboBox.currentText()
        calculate_row = self.final_choose_comboBox.currentIndex()
        two_matrix = self.matrix_total.astype(object)
        if (select_row != calculate_row):
            if ("√" in num):
                num_root = num.split('√')
                if (num_root[0] == '' and num_root[1].isdigit()):
                    if (multiply_and_divide == "×"):
                        if (addition_and_subtraction == '+'):
                            self.two_matrix_final[calculate_row] = self.two_matrix_final[calculate_row] + two_matrix[select_row]*sp.sqrt(int(num_root[1]))
                        else:
                            self.two_matrix_final[calculate_row] = self.two_matrix_final[calculate_row] - two_matrix[select_row]*sp.sqrt(int(num_root[1]))
                    else:
                        if (addition_and_subtraction == '+'):
                            self.two_matrix_final[calculate_row] = self.two_matrix_final[calculate_row] + two_matrix[select_row]/sp.sqrt(int(num_root[1]))
                        else:
                            self.two_matrix_final[calculate_row] = self.two_matrix_final[calculate_row] - two_matrix[select_row]/sp.sqrt(int(num_root[1]))
                    self.select_two_final_show()
                elif(num_root[0].isdigit() and num_root[1].isdigit()):
                    if (multiply_and_divide == "×"):
                        if (addition_and_subtraction == '+'):
                            self.two_matrix_final[calculate_row] = self.two_matrix_final[calculate_row] + two_matrix[select_row]*sp.sqrt(int(num_root[1]))
                        else:
                            self.two_matrix_final[calculate_row] = self.two_matrix_final[calculate_row] - two_matrix[select_row]*sp.sqrt(int(num_root[1]))
                    else:
                        if (addition_and_subtraction == '+'):
                            self.two_matrix_final[calculate_row] = self.two_matrix_final[calculate_row] + two_matrix[select_row]/sp.sqrt(int(num_root[1]))
                        else:
                            self.two_matrix_final[calculate_row] = self.two_matrix_final[calculate_row] - two_matrix[select_row]/sp.sqrt(int(num_root[1]))
                    self.select_two_final_show()
            elif ("/" in num):
                num_fraction = num.split('/')
                if (num_fraction[0].isdigit() and num_fraction[1].isdigit()):
                    if (multiply_and_divide == "×"):
                        if (addition_and_subtraction == '+'):
                            self.two_matrix_final[calculate_row] = self.two_matrix_final[calculate_row] + two_matrix[select_row]*sp.Rational(num_fraction[0],num_fraction[1])
                        else:
                            self.two_matrix_final[calculate_row] = self.two_matrix_final[calculate_row] - two_matrix[select_row]*sp.Rational(num_fraction[0],num_fraction[1])
                    else:
                        if (addition_and_subtraction == '+'):
                            self.two_matrix_final[calculate_row] = self.two_matrix_final[calculate_row] + two_matrix[select_row]/sp.Rational(num_fraction[0],num_fraction[1])
                        else:
                            self.two_matrix_final[calculate_row] = self.two_matrix_final[calculate_row] - two_matrix[select_row]/sp.Rational(num_fraction[0],num_fraction[1])
                    self.select_two_final_show()
            else:
                if(num.isdigit()):
                    num = int(self.multiple.text())
                    if (multiply_and_divide == "×"):
                        if (addition_and_subtraction == '+'):
                            self.two_matrix_final[calculate_row] = self.two_matrix_final[calculate_row] + two_matrix[select_row]*num
                        else:
                            self.two_matrix_final[calculate_row] = self.two_matrix_final[calculate_row] - two_matrix[select_row]*num
                    else:
                        if (addition_and_subtraction == '+'):
                            self.two_matrix_final[calculate_row] = self.two_matrix_final[calculate_row] + two_matrix[select_row]/num
                        else:
                            self.two_matrix_final[calculate_row] = self.two_matrix_final[calculate_row] - two_matrix[select_row]/num
                        self.select_two_final_show()
                else:
                    QtWidgets.QMessageBox.information(self.page3, "Message", "輸入錯誤")
        else:
            QtWidgets.QMessageBox.information(self.page3, "Message", "錯誤")
            
    def select_two_final_show (self):
        self.calculation_results_show.clear()
        for i in range (self.get_matrix_row):
            matrix_str = ''
            for j in range (self.get_matrix_column):
                if ('sqrt' in str(self.two_matrix_final[i][j])):
                    root_text = re.sub(u'\*?sqrt\((\d+)\)', u'√\\1', str(self.two_matrix_final[i][j]))
                    if j == (self.get_matrix_column-1):
                        matrix_str = matrix_str + root_text
                    else:
                        matrix_str = matrix_str + root_text + '     '
                else:
                    if j == (self.get_matrix_column-1):
                        matrix_str = matrix_str + str(self.two_matrix_final[i][j])
                    else:
                        matrix_str = matrix_str + str(self.two_matrix_final[i][j]) + '     '
            self.calculation_results_show.append(matrix_str)
            self.calculation_results_show.setAlignment(QtCore.Qt.AlignCenter)
        
    def font (self):
        ##### 第三頁:下拉選單、顯示輸入矩陣、計算結果顯示、倍數輸入、中間的X和÷#####
        self.font_22 = QtGui.QFont()
        self.font_22.setFamily("微軟正黑體")
        self.font_22.setPointSize(22)
        
        ##### 第二頁:運算選項 #####
        self.font_24 = QtGui.QFont()
        self.font_24.setFamily("微軟正黑體")
        self.font_24.setPointSize(24)
        
        ##### 第三頁:計算結果標題、計算和返回按鈕 #####
        self.font_32_setbold = QtGui.QFont()
        self.font_32_setbold.setFamily("微軟正黑體")
        self.font_32_setbold.setPointSize(32)
        self.font_32_setbold.setBold(True)
        
        self.font_32 = QtGui.QFont()
        self.font_32.setFamily("微軟正黑體")
        self.font_32.setPointSize(32)
        ##### 第一頁:行X列、確定按鈕、#####
        ##### 第二頁:輸入格、確定和返回按鈕 #####
        self.font_48 = QtGui.QFont()
        self.font_48.setFamily("微軟正黑體")
        self.font_48.setPointSize(48)
        
        ##### 第一頁:大標題 #####
        ##### 第二頁:標題 #####
        self.font_72 = QtGui.QFont()
        self.font_72.setFamily("微軟正黑體")
        self.font_72.setPointSize(72)
        self.font_72.setBold(True)
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.Main_Window(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    


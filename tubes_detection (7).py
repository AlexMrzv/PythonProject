# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tubes_detection2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import cv2
import pytesseract
from tkinter.messagebox import showerror, showinfo
from tkinter import filedialog
import winapps
import tensorflow as tf
import numpy as np
import pandas as pd
import openpyxl
import sys
import matplotlib
import matplotlib.pyplot as plt




class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1460, 830)
        MainWindow.setMinimumSize(QtCore.QSize(1460, 830))
        MainWindow.setMaximumSize(QtCore.QSize(1460, 830))
        font = QtGui.QFont()
        font.setFamily("inherit")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:#323437")
        MainWindow.setWindowIcon(QtGui.QIcon('icons/NeuroSEM.PNG'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.uploadImage = QtWidgets.QPushButton(self.centralwidget)
        self.uploadImage.setGeometry(QtCore.QRect(1070, 700, 161, 71))
        self.inside_conf = QtWidgets.QLineEdit(self.centralwidget)
        self.inside_conf.setGeometry(QtCore.QRect(1300, 601, 140, 30))
        self.inside_conf.setObjectName("inside_conf_line_edit")
        validator = QtGui.QRegExpValidator(QtCore.QRegExp('^(0)(\\.|,)[0-9]{2}'))
        self.inside_conf.setValidator(validator)
        font.setPointSize(10)
        self.inside_conf.setFont(font)
        self.inside_conf.setText('0.6')
        self.inside_conf.setStyleSheet('color: white;')
        self.outside_conf = QtWidgets.QLineEdit(self.centralwidget)
        self.outside_conf.setGeometry(QtCore.QRect(1300, 671, 140, 30))
        self.outside_conf.setObjectName("inside_conf_line_edit")
        self.outside_conf.setValidator(validator)
        self.outside_conf.setFont(font)
        self.outside_conf.setText('0.6')
        self.outside_conf.setStyleSheet('color: white;')
        self.scale_conf = QtWidgets.QLineEdit(self.centralwidget)
        self.scale_conf.setGeometry(QtCore.QRect(1300, 741, 140, 30))
        self.scale_conf.setObjectName("inside_conf_line_edit")
        self.scale_conf.setValidator(validator)
        self.scale_conf.setFont(font)
        self.scale_conf.setText('0.8')
        self.scale_conf.setStyleSheet('color: white;')
        font = QtGui.QFont()
        font.setFamily("inherit")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.uploadImage.setFont(font)
        self.uploadImage.setStyleSheet("QPushButton#uploadImage {\n"
                                       "    background-color:#e2b714;\n"
                                       "    border-radius: 10px;\n"
                                       "    font:  18px;\n"
                                       "    padding: 5px;\n"
                                       "    font-family: inherit;\n"
                                       "    \n"
                                       " \n"
                                       "}\n"
                                       "QPushButton#uploadImage:hover {\n"
                                       "  background-color:#d1d0c5;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#uploadImage:pressed {\n"
                                       "background-color:#646669;\n"
                                       "border: 1px solid #d1d0c5;\n"
                                       "}")
        self.uploadImage.setObjectName("uploadImage")
        self.inside_label = QtWidgets.QLabel(self.centralwidget)
        self.inside_label.setGeometry(QtCore.QRect(1304, 571, 140, 20))
        self.outside_label = QtWidgets.QLabel(self.centralwidget)
        self.outside_label.setGeometry(QtCore.QRect(1304, 641, 140, 20))
        self.scale_label = QtWidgets.QLabel(self.centralwidget)
        self.scale_label.setGeometry(QtCore.QRect(1304, 711, 140, 20))
        font.setPointSize(10)
        self.inside_label.setFont(font)
        self.inside_label.setStyleSheet('color: white;')
        self.inside_label.setText("Inside confidence")
        self.outside_label.setFont(font)
        self.outside_label.setStyleSheet('color: white;')
        self.outside_label.setText("Outside confidence")
        self.scale_label.setFont(font)
        self.scale_label.setStyleSheet('color: white;')
        self.scale_label.setText("Scale confidence")
        self.downloadExcel = QtWidgets.QPushButton(self.centralwidget)
        self.downloadExcel.setGeometry(QtCore.QRect(1070, 600, 161, 71))
        font = QtGui.QFont()
        font.setFamily("inherit")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.downloadExcel.setFont(font)
        self.downloadExcel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.downloadExcel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.downloadExcel.setStyleSheet("QPushButton#downloadExcel {\n"
                                         "    font: 75 8pt \"MS Shell Dlg 2\";\n"
                                         "    background-color:#e2b714;\n"
                                         "    border-radius: 10px;\n"
                                         "    font:  18px;\n"
                                         "    padding: 5px;\n"
                                         "    font-family: inherit;\n"
                                         "    \n"
                                         " \n"
                                         "}\n"
                                         "QPushButton#downloadExcel:hover {\n"
                                         "  background-color:#d1d0c5;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton#downloadExcel:pressed {\n"
                                         "background-color:#646669;\n"
                                         "border: 1px solid #d1d0c5;\n"
                                         "}")
        self.downloadExcel.setObjectName("downloadExcel")

        self.PlotButton = QtWidgets.QPushButton(self.centralwidget)
        self.PlotButton.setGeometry(QtCore.QRect(1070, 540, 45, 45))
        self.PlotButton.setIcon(QtGui.QIcon('icons/PlotButton.PNG'))
        self.PlotButton.setIconSize(QtCore.QSize(45, 45))
        self.PlotButton.setFont(font)
        self.PlotButton.setStyleSheet("QPushButton#PlotButton {\n"
                                       "    background-color:#e2b714;\n"
                                       "    border-radius: 10px;\n"
                                       "    font:  18px;\n"
                                       "    padding: 5px;\n"
                                       "    font-family: inherit;\n"
                                       "    \n"
                                       " \n"
                                       "}\n"
                                       "QPushButton#PlotButton:hover {\n"
                                       "  background-color:#d1d0c5;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#PlotButton:pressed {\n"
                                       "background-color:#646669;\n"
                                       "border: 1px solid #d1d0c5;\n"
                                       "}")
        self.PlotButton.setObjectName("PlotButton")

        self.insidePlot = QtWidgets.QLabel(self.centralwidget)
        self.insidePlot.setScaledContents(True)
        self.insidePlot.setGeometry(1130, 30, 250, 150)
        self.insidePlot.setMinimumSize(QtCore.QSize(30, 0))
        self.insidePlot.setObjectName('insideWidget')
        self.insidePlot.setStyleSheet("QLabel#insideWidget {\n"
                                      "display: box;\n"
                                      "}")
        self.outsidePlot = QtWidgets.QLabel(self.centralwidget)
        self.outsidePlot.setScaledContents(True)
        self.outsidePlot.setGeometry(1130, 200, 250, 150)
        self.outsidePlot.setMinimumSize(QtCore.QSize(30, 0))
        self.outsidePlot.setObjectName('outsideWidget')
        self.outsidePlot.setStyleSheet("QWidget#outsideWidget {\n"
                                       "display: box;\n"
                                       "}")
        self.wallPlot = QtWidgets.QLabel(self.centralwidget)
        self.wallPlot.setScaledContents(True)
        self.wallPlot.setGeometry(1130, 370, 250, 150)
        self.wallPlot.setMinimumSize(QtCore.QSize(30, 0))
        self.wallPlot.setObjectName('wallWidget')
        self.wallPlot.setStyleSheet("QWidget#wallWidget {\n"
                                    "display: box;\n"
                                    "}")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 10, 1024, 798))
        self.stackedWidget.setMinimumSize(QtCore.QSize(256, 0))
        self.stackedWidget.setStyleSheet("QstackedWidget#stackedWidget {\n"
                                         "display: box;\n"
                                         "background-color: red;\n"
                                         "border: 2px solid green;\n"
                                         "}")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.stackedWidget.setObjectName("stackedWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1263, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.values = pd.DataFrame
        self.outside = pd.DataFrame
        self.inside = pd.DataFrame
        self.scalewidth = pd.DataFrame
        self.imgs = {}
        self.label = {}
        self.removed_items = pd.DataFrame({
            'filename': [],
            'x_outside': [],
            'y_outside': [],
            'width_outside': [],
            'height_outside': [],
            'x_inside': [],
            'y_inside': [],
            'width_inside': [],
            'height_inside': [],
            'diameter_outside': [],
            'diameter_inside': [],
            'wall_thickness': [],
        })
        self.downloadExcel.hide()
        self.PlotButton.hide()
        self.stackedWidget.hide()
        self.plot_inside = {}
        self.plot_outside = {}
        self.plot_wall = {}

    def add_plots(self, filename):
        try:
            plt.clf()
            only_for_filename = self.values.loc[(self.values['filename'] == filename.split('.')[0] + '.txt')]
            plt.hist(only_for_filename['diameter_inside'], color='blue', edgecolor='black',
                     bins=int((only_for_filename['diameter_inside'].max() - only_for_filename['diameter_inside'].min())/2))
            plt.xlabel('inside diameter', fontsize=16)
            plt.savefig(f'plots/inside_{filename}')
            plt.clf()
            plt.hist(only_for_filename['diameter_outside'], color='blue', edgecolor='black',
                     bins=int((only_for_filename['diameter_outside'].max() - only_for_filename['diameter_outside'].min())/2))
            plt.xlabel('outside diameter', fontsize=16)
            plt.savefig(f'plots/outside_{filename}')
            plt.clf()
            plt.hist(only_for_filename['wall_thickness'], color='blue', edgecolor='black',
                     bins=int((only_for_filename['wall_thickness'].max() - only_for_filename['wall_thickness'].min())/2))
            plt.xlabel('wall thickness', fontsize=16)
            plt.savefig(f'plots/wall_{filename}')
            plt.clf()
            self.plot_inside[filename] = QtGui.QPixmap(f"plots/inside_{filename}")
            self.plot_outside[filename] = QtGui.QPixmap(f"plots/outside_{filename}")
            self.plot_wall[filename] = QtGui.QPixmap(f"plots/wall_{filename}")

        except Exception as E:
            print(E)

    def add_general_plot(self):
        plt.clf()
        plt.subplot(2, 2, 1)
        plt.hist(self.values['diameter_inside'], color='blue', edgecolor='black',
                     bins=int((self.values['diameter_inside'].max() - self.values['diameter_inside'].min())/2))
        plt.title('inside diameter', fontsize=18)

        plt.subplot(2, 2, 2)
        plt.hist(self.values['diameter_outside'], color='blue', edgecolor='black',
                 bins=int((self.values['diameter_outside'].max() - self.values['diameter_outside'].min())/2))
        plt.title('outside diameter', fontsize=18)

        plt.subplot(2, 2, 3)
        plt.hist(self.values['wall_thickness'], color='blue', edgecolor='black',
                 bins=int((self.values['wall_thickness'].max() - self.values['wall_thickness'].min())/2))
        plt.title('wall thickness', fontsize=18)
        plt.show()




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NeuroSEM"))
        self.uploadImage.setText(_translate("MainWindow", "upload image"))
        self.downloadExcel.setText(_translate("MainWindow", "download excel"))
        self.uploadImageButtonClick()
        self.downloadExcelFile()
        plt.rcParams['figure.figsize'] = [12, 7]
        self.PlotButtonClick()


    def uploadImageButtonClick(self):
        self.uploadImage.clicked.connect(self.get_image)

    def PlotButtonClick(self):
        self.PlotButton.clicked.connect(self.add_general_plot)

    def downloadExcelFile(self):
        self.downloadExcel.clicked.connect(self.download)

    def download(self):
        res = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Escel', '.xlsx')],
                                           initialfile='result')
        if not res == '':
            with pd.ExcelWriter(res) as writer:
                for i in os.listdir('outside/outside/labels'):
                    output = self.values.loc[(self.values['filename'] == i)]
                    output.to_excel(writer, sheet_name=i.split('.')[0], index=False)
                self.scalewidth.to_excel(writer, sheet_name='scale width', index=False)
                self.values.to_excel(writer, sheet_name='all', index=False)

    def add_pages(self):
        class ClickableLabel(QtWidgets.QLabel):
            clicked = QtCore.pyqtSignal()

            def mousePressEvent(self, QMouseEvent):
                self.clicked.emit()

        pages = self.stackedWidget.count()
        for i in range(pages):
            widget = self.stackedWidget.widget(0)
            self.stackedWidget.removeWidget(widget)
        for ind, i in enumerate(os.listdir('img')):
            self.new_page = QtWidgets.QWidget()
            self.new_page.setObjectName(i)
            self.label[i] = ClickableLabel(self.new_page)
            self.label[i].setGeometry(QtCore.QRect(0, 0, 1024, 768))
            self.show_button = QtWidgets.QPushButton(self.new_page)
            self.show_button.setText('Show')
            self.show_button.setGeometry(452, 768, 60, 30)
            self.hide_button = QtWidgets.QPushButton(self.new_page)
            self.hide_button.setText('Hide')
            self.hide_button.setGeometry(512, 768, 60, 30)
            self.next_button = QtWidgets.QPushButton(self.new_page)
            self.next_button.setText('Next')
            self.next_button.setGeometry(964, 768, 60, 30)
            self.previos_button = QtWidgets.QPushButton(self.new_page)
            self.previos_button.setText('Previous')
            self.previos_button.setGeometry(0, 768, 60, 30)
            self.stackedWidget.addWidget(self.new_page)
            self.label[i].setPixmap(QtGui.QPixmap(f"img/{i}"))
            self.label[i].setScaledContents(True)
            self.next_button.setStyleSheet('color: white; \n'
                                           'border-style: none;')
            self.previos_button.setStyleSheet('color: white; \n'
                                              'border-style: none;')
            self.show_button.setStyleSheet('color: white; \n'
                                           'border-style: none;')
            self.hide_button.setStyleSheet('color: white; \n'
                                           'border-style: none;')
            self.next_button.clicked.connect(self.next_page)
            self.previos_button.clicked.connect(self.previous_page)
            self.show_button.clicked.connect(self.show_image)
            self.hide_button.clicked.connect(self.hide_image)
            self.imgs[ind] = i
            self.label[i].clicked.connect(lambda i=i: self.actions(i))
            self.add_plots(i)


    def actions(self, i):
        x = QtGui.QCursor.pos().x() - MainWindow.pos().x() - self.stackedWidget.geometry().x()
        y = QtGui.QCursor.pos().y() - MainWindow.pos().y() - self.stackedWidget.geometry().y() - 40
        a = self.values.index[((abs(self.values['x_outside'] - self.values['width_outside'] / 2) <= x) &
                               (abs(self.values['x_outside'] + self.values['width_outside'] / 2) >= x) &
                               (abs(self.values['y_outside'] - self.values['height_outside'] / 2) <= y) &
                               (abs(self.values['y_outside'] + self.values['height_outside'] / 2) >= y) &
                               (self.values['filename'] == i.split('.')[0] + '.txt')
                               )].tolist()
        if not a:
            b = self.removed_items.index[
                ((abs(self.removed_items['x_outside'] - self.removed_items['width_outside'] / 2) <= x) &
                 (abs(self.removed_items['x_outside'] + self.removed_items['width_outside'] / 2) >= x) &
                 (abs(self.removed_items['y_outside'] - self.removed_items['height_outside'] / 2) <= y) &
                 (abs(self.removed_items['y_outside'] + self.removed_items['height_outside'] / 2) >= y) &
                 (self.removed_items['filename'] == i.split('.')[0] + '.txt')
                 )].tolist()
            if b:
                self.values = pd.concat([self.values, self.removed_items.loc[[b[0]]]])
                self.removed_items = self.removed_items.drop(index=b[0])
                self.add_plots(i)
                self.insidePlot.setPixmap(self.plot_inside[i])
                self.outsidePlot.setPixmap(self.plot_outside[i])
                self.wallPlot.setPixmap(self.plot_wall[i])
                self.save_results(i)
                self.label[i].setPixmap(QtGui.QPixmap(f"result/{i}"))
        else:
            self.removed_items = pd.concat([self.removed_items, self.values.loc[[a[0]]]])
            self.values = self.values.drop(index=a[0])
            self.add_plots(i)
            self.insidePlot.setPixmap(self.plot_inside[i])
            self.outsidePlot.setPixmap(self.plot_outside[i])
            self.wallPlot.setPixmap(self.plot_wall[i])
            self.save_results(i)
            self.label[i].setPixmap(QtGui.QPixmap(f"result/{i}"))

    def show_image(self):
        self.label[self.imgs[self.stackedWidget.currentIndex()]].setPixmap(
            QtGui.QPixmap(f"result/{self.imgs[self.stackedWidget.currentIndex()]}"))

    def hide_image(self):
        self.label[self.imgs[self.stackedWidget.currentIndex()]].setPixmap(
            QtGui.QPixmap(f"img/{self.imgs[self.stackedWidget.currentIndex()]}"))

    def next_page(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)
        self.insidePlot.setPixmap(self.plot_inside[os.listdir('img')[self.stackedWidget.currentIndex()]])
        self.outsidePlot.setPixmap(self.plot_outside[os.listdir('img')[self.stackedWidget.currentIndex()]])
        self.wallPlot.setPixmap(self.plot_wall[os.listdir('img')[self.stackedWidget.currentIndex()]])

    def previous_page(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1)
        self.insidePlot.setPixmap(self.plot_inside[os.listdir('img')[self.stackedWidget.currentIndex()]])
        self.outsidePlot.setPixmap(self.plot_outside[os.listdir('img')[self.stackedWidget.currentIndex()]])
        self.wallPlot.setPixmap(self.plot_wall[os.listdir('img')[self.stackedWidget.currentIndex()]])

    def check_laters(self, filepath):
        laters = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        return laters.intersection(filepath.lower()) != set()

    def predobrabotka(self, input_image):
        image = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)
        image = cv2.GaussianBlur(image, (3, 3), 0)
        image = np.asarray(image)
        image = np.expand_dims(image, axis=0)
        image = tf.image.adjust_contrast(image, 3.)
        filename = input_image.split('/')[-1]
        cv2.imwrite(f'img/{filename}', (image.numpy()[0]))

    def getnums(self, input_value):
        result = ''
        for i in input_value:
            if i.isdigit():
                result += i
        return result

    def relative_to_absolute(self, width, height, xList, yList, widthList, filename, heightList):
        output = pd.DataFrame(
            {
                'filename': [filename for i in range(len(xList))],
                'x': xList,
                'y': yList,
                'width': widthList,
                'height': heightList
            }
        )
        output['x'] = round(output['x'] * width)
        output['y'] = round(output['y'] * height)
        output['width'] = round(output['width'] * width)
        output['height'] = round(output['height'] * height)
        return output

    def scale_len(self):
        result = []
        filenames = []
        for filename in os.listdir('scale/scale/crops/polosochka'):
            image = cv2.imread(f'scale/scale/crops/polosochka/{filename}', cv2.IMREAD_GRAYSCALE)
            thresh = 200
            image = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]
            width = []
            for ind, i in enumerate(image[round(len(image) / 2)]):
                if i == 0:
                    width.append(ind)
            if (max(width) - min(width) + 1) > len(width) / 2:
                result.append(max(width) - min(width) + 1)
            else:
                showinfo('Attention', f'Scale width may not be accurately detected in file {filename}')
                result.append(len(image[0]))
            filenames.append(filename)
        return pd.DataFrame({
            'filename': filenames,
            'scale_width': result
        })

    def accordance(self, outside, inside):
        result = pd.DataFrame({
            'filename': [],
            'x_outside': [],
            'y_outside': [],
            'width_outside': [],
            'height_outside': [],
            'x_inside': [],
            'y_inside': [],
            'width_inside': [],
            'height_inside': []
        })
        for i in range(len(outside)):
            x = int(outside['x'][i])
            y = int(outside['y'][i])
            width = int(outside['width'][i])
            height = int(outside['height'][i])
            filename = str(outside['filename'][i])
            sort = pd.DataFrame()
            if x - width / 2 > 5 and y - height / 2 > 5 and x + width / 2 < 1020 and y + height / 2 < 764:
                sort = inside.loc[(
                        (abs(inside['x'] - x) < round(width / 2)) & (abs(inside['y'] - y) < round(width / 2)) & (
                        inside['width'] - width < 0) & (
                                inside['filename'] == filename))]
            if not sort.empty:
                fx = sort.iloc[0]['x']
                fy = sort.iloc[0]['y']
                fwidth = sort.iloc[0]['width']
                fheight = sort.iloc[0]['height']
                result.loc[len(result.index)] = [filename, x, y, width, height, fx, fy, fwidth, fheight]
        return result

    def diameter_and_wall_thickness(self, scale_width, values, words_in_picture):
        output = pd.DataFrame({
            'filename': [],
            'x_outside': [],
            'y_outside': [],
            'width_outside': [],
            'height_outside': [],
            'x_inside': [],
            'y_inside': [],
            'width_inside': [],
            'height_inside': [],
            'diameter_outside': [],
            'diameter_inside': [],
            'wall_thickness': [],
        })
        for i in range(len(scale_width)):
            scale_len = int(scale_width.iloc[i]['scale_width'])
            filename = scale_width.iloc[i]['filename'].split('.')[0] + '.txt'
            sort = values.loc[(values['filename'] == filename)]
            for ind, word in words_in_picture.items():
                if filename.split('.')[0] in ind:
                    scale_num = word
                    break
            sort['diameter_outside'] = sort['width_outside'] / scale_len * scale_num
            sort['diameter_inside'] = sort['width_inside'] / scale_len * scale_num
            sort['wall_thickness'] = (sort['width_outside'] - sort['width_inside']) / scale_len * scale_num / 2
            output = pd.concat([output, sort], ignore_index=True)
        return output

    def prediction(self):
        os.system(
            'python yolov5/detect.py '
            '--weights scale.pt '
            '--img 1024 '
            f'--conf {self.scale_conf.text()} '
            '--source img '
            '--save-crop '
            '--nosave '
            '--name scale '
            '--project ./scale'
        )
        os.system(
            'python yolov5/detect.py '
            '--weights inside.pt '
            '--img 1024 '
            f'--conf {self.inside_conf.text()} '
            '--source img '
            '--save-txt '
            '--nosave '
            '--name inside '
            '--project ./inside'
        )
        os.system(
            'python yolov5/detect.py '
            '--weights outside.pt '
            '--img 1024 '
            f'--conf {self.outside_conf.text()} '
            '--source img '
            '--save-txt '
            '--nosave '
            '--name outside '
            '--project ./outside'
        )
        resultDict = {}
        found_scale = os.listdir('scale/scale/crops/polosochka')
        if found_scale:
            for filename in os.listdir('scale/scale/crops/polosochka'):
                scaleimage = cv2.imread(f'scale/scale/crops/polosochka/{filename}', cv2.IMREAD_GRAYSCALE)
                thresh = 200
                bwimage = cv2.threshold(scaleimage, thresh, 255, cv2.THRESH_BINARY)[1]
                cv2.imwrite(f'scale/scale/crops/polosochka/{filename}', bwimage)
                pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
                resultDict[filename] = pytesseract.image_to_string(bwimage)
            return resultDict
        else:
            return False

    def save_results(self, ind):
        if ind == '':
            shutil.rmtree('result', True)
            os.mkdir('result')
            for filename in os.listdir('img'):
                image = cv2.imread(f'img/{filename}')
                data = self.values.loc[(filename.split('.')[0] + '.txt' == self.values['filename'])]
                for i in range(len(data)):
                    p1x = int(data.iloc[i]['x_outside'] - round(data.iloc[i]['width_outside'] / 2))
                    p1y = int(data.iloc[i]['y_outside'] - round(data.iloc[i]['height_outside'] / 2))
                    p2x = int(data.iloc[i]['x_outside'] + round(data.iloc[i]['width_outside'] / 2))
                    p2y = int(data.iloc[i]['y_outside'] + round(data.iloc[i]['height_outside'] / 2))
                    cv2.rectangle(image, (p1x, p1y), (p2x, p2y), (0, 255, 0), 2)
                    p1x = int(data.iloc[i]['x_inside'] - round(data.iloc[i]['width_inside'] / 2))
                    p1y = int(data.iloc[i]['y_inside'] - round(data.iloc[i]['height_inside'] / 2))
                    p2x = int(data.iloc[i]['x_inside'] + round(data.iloc[i]['width_inside'] / 2))
                    p2y = int(data.iloc[i]['y_inside'] + round(data.iloc[i]['height_inside'] / 2))
                    cv2.rectangle(image, (p1x, p1y), (p2x, p2y), (242, 245, 66), 2)
                cv2.imwrite(f'result/{filename}', image)
        else:
            image = cv2.imread(f'img/{ind}')
            data = self.values.loc[(ind.split('.')[0] + '.txt' == self.values['filename'])]
            for i in range(len(data)):
                p1x = int(data.iloc[i]['x_outside'] - round(data.iloc[i]['width_outside'] / 2))
                p1y = int(data.iloc[i]['y_outside'] - round(data.iloc[i]['height_outside'] / 2))
                p2x = int(data.iloc[i]['x_outside'] + round(data.iloc[i]['width_outside'] / 2))
                p2y = int(data.iloc[i]['y_outside'] + round(data.iloc[i]['height_outside'] / 2))
                cv2.rectangle(image, (p1x, p1y), (p2x, p2y), (0, 255, 0), 2)
                p1x = int(data.iloc[i]['x_inside'] - round(data.iloc[i]['width_inside'] / 2))
                p1y = int(data.iloc[i]['y_inside'] - round(data.iloc[i]['height_inside'] / 2))
                p2x = int(data.iloc[i]['x_inside'] + round(data.iloc[i]['width_inside'] / 2))
                p2y = int(data.iloc[i]['y_inside'] + round(data.iloc[i]['height_inside'] / 2))
                cv2.rectangle(image, (p1x, p1y), (p2x, p2y), (242, 245, 66), 2)
            cv2.imwrite(f'result/{ind}', image)

    def get_image(self):
        self.values = pd.DataFrame
        self.outside = pd.DataFrame
        self.inside = pd.DataFrame
        self.scalewidth = pd.DataFrame
        shutil.rmtree('img', True)
        shutil.rmtree('inside', True)
        shutil.rmtree('outside', True)
        shutil.rmtree('scale', True)
        input_images = filedialog.askopenfilenames(initialdir="main",
                                                   title="Select an Images",
                                                   filetypes=[
                                                       ('Image file', '.png .jpg .jpeg'),
                                                       ('All files', '*')
                                                   ]
                                                       )
        if input_images == '':
            self.downloadExcel.hide()
            self.PlotButton.hide()
            self.stackedWidget.hide()
            self.wallPlot.hide()
            self.insidePlot.hide()
            self.outsidePlot.hide()
            return None
        if 'img' not in os.listdir():
            os.mkdir('img')
        if 'plots' in os.listdir():
            shutil.rmtree('plots', True)
        os.mkdir('plots')

        for i in input_images:
            if self.check_laters(i):
                showerror('Error', 'There are invalid letters in the file path')
                self.get_image()
                return None
        for i in input_images:
            self.predobrabotka(i)
        words_in_picture = self.prediction()
        if words_in_picture:
            for ind, i in words_in_picture.items():
                words_in_picture[ind] = int(self.getnums(i))
            for filename in os.listdir('inside/inside/labels'):
                nothing = os.listdir('img')
                for i in nothing:
                    if filename.split(".")[0] in i:
                        width = i
                        break
                height = len(cv2.imread(f'img/{width}'))
                width = len(cv2.imread(f'img/{width}')[0])
                inside_file = open(f'inside/inside/labels/{filename}', 'r')
                raw_text = inside_file.read().split('\n')
                xList = []
                yList = []
                widthList = []
                heightList = []
                for i in raw_text:
                    bList = i.split(' ')
                    if bList != ['']:
                        xList.append(float(bList[1]))
                        yList.append(float(bList[2]))
                        widthList.append(float(bList[3]))
                        heightList.append(float(bList[4]))
                if self.inside.empty:
                    self.inside = self.relative_to_absolute(width, height, xList, yList, widthList, filename,
                                                            heightList)
                else:
                    self.inside = pd.concat([self.inside,
                                             self.relative_to_absolute(width, height, xList, yList, widthList, filename,
                                                                       heightList)],
                                            ignore_index=True)
                outside_file = open(f'outside/outside/labels/{filename}', 'r')
                raw_text = outside_file.read().split('\n')
                xList = []
                yList = []
                widthList = []
                heightList = []
                for i in raw_text:
                    bList = i.split(' ')
                    if bList != ['']:
                        xList.append(float(bList[1]))
                        yList.append(float(bList[2]))
                        widthList.append(float(bList[3]))
                        heightList.append(float(bList[4]))
                if self.outside.empty:
                    self.outside = self.relative_to_absolute(width, height, xList, yList, widthList, filename,
                                                             heightList)
                else:
                    self.outside = pd.concat(
                        [self.outside,
                         self.relative_to_absolute(width, height, xList, yList, widthList, filename, heightList)],
                        ignore_index=True)
            self.scalewidth = self.scale_len()
            self.values = self.accordance(self.outside, self.inside)
            self.values = self.diameter_and_wall_thickness(self.scalewidth, self.values, words_in_picture)
            self.add_pages()
            self.insidePlot.setPixmap(self.plot_inside[os.listdir('img')[0]])
            self.outsidePlot.setPixmap(self.plot_outside[os.listdir('img')[0]])
            self.wallPlot.setPixmap(self.plot_wall[os.listdir('img')[0]])
            self.save_results('')
            self.downloadExcel.show()
            self.PlotButton.show()
            self.stackedWidget.show()
            self.wallPlot.show()
            self.insidePlot.show()
            self.outsidePlot.show()
        else:
            showerror("Scale not found", 'Try to reduce the conf')


if __name__ == "__main__":

    teserct_is_installed = winapps.search_installed('Tesseract-OCR')
    while not teserct_is_installed:
        showerror('Error', 'Tesseract-OCR is not installed. Please visit https://github.com/UB-Mannheim/tesseract/wiki')
    if 'yolov5' not in os.listdir():
        os.system('git clone https://github.com/ultralytics/yolov5')
    res = os.popen('pip freeze').read()
    if 'Pillow' not in res:
        os.system('pip install -qr yolov5/requirements.txt')
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

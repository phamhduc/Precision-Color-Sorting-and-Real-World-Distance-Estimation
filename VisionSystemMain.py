from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel,QMessageBox
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon


import numpy as np 
from time import sleep
from datetime import datetime

import cv2
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap


OnlyFloat = QtGui.QDoubleValidator(
                -1200.0, # bottom
                1200.0, # top
                2, # decimals 
                notation=QtGui.QDoubleValidator.StandardNotation)

class Ui_Widget(QWidget):
    def setupUi(self, Widget):
        # config interface
        Widget.setObjectName("Widget")

        # Value to process vision System
        self.CamID = 0
        self.OS_TL_X = 50
        self.OS_TL_Y = 50

        self.OS_TR_X = 50
        self.OS_TR_Y = 50

        self.OS_BL_X = 50
        self.OS_BL_Y = 50

        self.OS_BR_X = 50
        self.OS_BR_Y = 50

        self.Xdim = 0
        self.Ydim = 0
        # HSV value for 3 Color Set

        # Default Value For Red Green Blue
        self.HSV_L1 = [164,70,90]
        self.HSV_U1 = [180,255,255]

        self.HSV_U2 = [92, 255, 255]
        self.HSV_L2 = [37, 94, 77]

        self.HSV_U3 = [132, 219, 229]
        self.HSV_L3 = [101, 84, 84]



        self.Color1_pos = [0.0,0.0,0.0] 
        self.Color2_pos = [0.0,0.0,0.0] 
        self.Color3_pos = [0.0,0.0,0.0] 

        self.Execute = 0
        self.ChosenSet = 0
        self.Transform = 0

        self.IsTracking = 0
        self.Is_SetFram = 0
  
        Widget.resize(940, 560)
        Widget.setFixedSize(940, 560)
        
  
        icon = QtGui.QIcon("DPack/ro.png")
        Widget.setWindowIcon(icon)
        #--------------# config widget 
        self.tabWidget = QtWidgets.QTabWidget(Widget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 941, 570))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        #Background
        #timer

        #TAB2
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
    
        # Set up vision system
        self.video_label = QtWidgets.QLabel(self.tab_2)
        
        
        # Layout for the tab
        layout = QtWidgets.QVBoxLayout(self.tab_2)
        layout.setGeometry(QtCore.QRect(15, 20, 720, 480))
        layout.addWidget(self.video_label)
        
        # Enable/Disable button
        self.EN_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.EN_pushButton.setGeometry(QtCore.QRect(660, 505, 100, 25))
        self.EN_pushButton.setObjectName("EN_pushButton")

        #Clear message tab2 
        self.CLearM_VS_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.CLearM_VS_pushButton.setGeometry(QtCore.QRect(810, 505, 120, 25))
        self.CLearM_VS_pushButton.setObjectName("CLearM_VS_pushButton")
        

        #Label  
        self.label_1_t2 = QtWidgets.QLabel(self.tab_2)
        self.label_1_t2.setGeometry(QtCore.QRect(10, 0, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_1_t2.setFont(font)
        self.label_1_t2.setObjectName("label_1_t2")

        ##
        self.label_2_t2 = QtWidgets.QLabel(self.tab_2)
        self.label_2_t2.setGeometry(QtCore.QRect(680, 250, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_2_t2.setFont(font)
        self.label_2_t2.setObjectName("label_1_t2")

        

        ########
        self.label_3_t2 = QtWidgets.QLabel(self.tab_2)
        self.label_3_t2.setGeometry(QtCore.QRect(680, 0, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_3_t2.setFont(font)
        self.label_3_t2.setObjectName("label_1_t2")

        self.label_4_t2 = QtWidgets.QLabel(self.tab_2)
        self.label_4_t2.setGeometry(QtCore.QRect(665, 20, 270, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4_t2.setFont(font)
        self.label_4_t2.setObjectName("label_1_t2")


        self.CamID_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.CamID_pushButton.setGeometry(QtCore.QRect(130, 5, 80, 20))
        self.CamID_pushButton.setFont(font)
        self.CamID_pushButton.setObjectName("CamID_pushButton")



        self.CamID_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.CamID_lineEdit.setGeometry(QtCore.QRect(220, 5, 20, 20))
        self.CamID_lineEdit.setObjectName("Actual_X_lineEdit")
        self.CamID_lineEdit.setValidator(QtGui.QIntValidator())
        self.CamID_lineEdit.setText(str(self.CamID))

        ##
        self.OffsetBox_comboBox = QtWidgets.QComboBox(self.tab_2)
        self.OffsetBox_comboBox.setGeometry(QtCore.QRect(660, 50, 80, 30))
        self.OffsetBox_comboBox.setObjectName("Baudrate_comboBox")
        self.OffsetBox_comboBox.addItem("")
        self.OffsetBox_comboBox.addItem("")
        self.OffsetBox_comboBox.addItem("")
        self.OffsetBox_comboBox.addItem("")



        # Button to adjust ofset box
        self.Right_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.Right_pushButton.setGeometry(QtCore.QRect(810, 50, 30, 30))
        self.Right_pushButton.setObjectName("EN_pushButton")
        font = QtGui.QFont("Arial", 14)
        font.setBold(True) 
        self.Right_pushButton.setFont(font)
        
        

        self.Left_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.Left_pushButton.setGeometry(QtCore.QRect(780, 50, 30, 30))
        self.Left_pushButton.setObjectName("EN_pushButton")
        font = QtGui.QFont("Arial", 14)
        font.setBold(True) 
        self.Left_pushButton.setFont(font)

        self.Up_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.Up_pushButton.setGeometry(QtCore.QRect(840, 50, 30, 30))
        self.Up_pushButton.setObjectName("EN_pushButton")
        font = QtGui.QFont("Arial", 12)
        font.setBold(True) 
        self.Up_pushButton.setFont(font)

        self.Down_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.Down_pushButton.setGeometry(QtCore.QRect(870, 50, 30, 30))
        self.Down_pushButton.setObjectName("EN_pushButton")
        font = QtGui.QFont("Arial", 12)
        font.setBold(True) 
        self.Down_pushButton.setFont(font)

        #Edit X and Y value 

        self.label_5_t2 = QtWidgets.QLabel(self.tab_2)
        self.label_5_t2.setGeometry(QtCore.QRect(665, 90, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True) 
        self.label_5_t2.setFont(font)
        self.label_5_t2.setObjectName("label_1_t2")

        self.label_6_t2 = QtWidgets.QLabel(self.tab_2)
        self.label_6_t2.setGeometry(QtCore.QRect(750, 90, 100, 20))
        font = QtGui.QFont()
        font.setBold(True) 
        font.setPointSize(8)
        self.label_6_t2.setFont(font)
        self.label_6_t2.setObjectName("label_6_t2")



        self.Actual_X_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.Actual_X_lineEdit.setGeometry(QtCore.QRect(710, 90, 30, 20))
        self.Actual_X_lineEdit.setObjectName("Actual_X_lineEdit")
        self.Actual_X_lineEdit.setText("0.00")
        self.Actual_X_lineEdit.setValidator(OnlyFloat)

        self.Actual_Y_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.Actual_Y_lineEdit.setGeometry(QtCore.QRect(800, 90, 30, 20))
        self.Actual_Y_lineEdit.setObjectName("Actual_X_lineEdit")
        self.Actual_Y_lineEdit.setText("0.00")
        self.Actual_Y_lineEdit.setValidator(OnlyFloat)


        self.ColorSet_comboBox = QtWidgets.QComboBox(self.tab_2)
        self.ColorSet_comboBox.setGeometry(QtCore.QRect(660, 120, 50, 20))
        font = QtGui.QFont()

        font.setPointSize(7)
        self.ColorSet_comboBox.setFont(font)
        self.ColorSet_comboBox.setObjectName("ColorSet_comboBox")
        self.ColorSet_comboBox.addItem("")
        self.ColorSet_comboBox.addItem("")
        self.ColorSet_comboBox.addItem("")
        self.ColorSet_comboBox.addItem("")


        self.ColorPos_label = QtWidgets.QLabel(self.tab_2)
        self.ColorPos_label.setGeometry(QtCore.QRect(720, 120,200, 20))
        font = QtGui.QFont()

        font.setPointSize(7)
        self.ColorPos_label.setFont(font)
        self.ColorPos_label.setObjectName("ColorPos_label")
        self.ColorPosText = "Pos:[X: "+str(self.Color1_pos[0])+"]"+ "[Y: "+str(self.Color1_pos[1])+"]"
        self.ColorPos_label.setText(self.ColorPosText)


        self.UpperHSV_label = QtWidgets.QLabel(self.tab_2)
        self.UpperHSV_label.setGeometry(QtCore.QRect(660, 180, 200, 20))
        font = QtGui.QFont()
        font.setBold(True) 
        font.setPointSize(8)
        self.UpperHSV_label.setFont(font)
        self.UpperHSV_label.setObjectName("UpperHSV_label")
        self.UpperHSV_label.setText("Upper HSV:")

        self.UpperH_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.UpperH_lineEdit.setGeometry(QtCore.QRect(740, 180, 30, 20))
        self.UpperH_lineEdit.setObjectName("Actual_X_lineEdit")
        self.UpperH_lineEdit.setText(str(self.HSV_U1[0]))
        self.UpperH_lineEdit.setValidator(QtGui.QIntValidator())

        self.UpperS_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.UpperS_lineEdit.setGeometry(QtCore.QRect(780, 180, 30, 20))
        self.UpperS_lineEdit.setObjectName("Actual_X_lineEdit")
        self.UpperS_lineEdit.setText(str(self.HSV_U1[1]))
        self.UpperS_lineEdit.setValidator(QtGui.QIntValidator())

        self.UpperV_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.UpperV_lineEdit.setGeometry(QtCore.QRect(820, 180, 30, 20))
        self.UpperV_lineEdit.setObjectName("Actual_X_lineEdit")
        self.UpperV_lineEdit.setText(str(self.HSV_U1[2]))
        self.UpperV_lineEdit.setValidator(QtGui.QIntValidator())


        self.LowerHSV_label = QtWidgets.QLabel(self.tab_2)
        self.LowerHSV_label.setGeometry(QtCore.QRect(660, 150, 200, 20))
        font = QtGui.QFont()
        font.setBold(True) 
        font.setPointSize(8)
        self.LowerHSV_label.setFont(font)
        self.LowerHSV_label.setObjectName("LowerHSV_label")
        self.LowerHSV_label.setText("Lower HSV:")

        self.LowerH_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.LowerH_lineEdit.setGeometry(QtCore.QRect(740, 150, 30, 20))
        self.LowerH_lineEdit.setObjectName("Actual_X_lineEdit")
        self.LowerH_lineEdit.setText(str(self.HSV_L1[0]))
        self.LowerH_lineEdit.setValidator(QtGui.QIntValidator())

        self.LowerS_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.LowerS_lineEdit.setGeometry(QtCore.QRect(780, 150, 30, 20))
        self.LowerS_lineEdit.setObjectName("Actual_X_lineEdit")
        self.LowerS_lineEdit.setText(str(self.HSV_L1[1]))
        self.LowerS_lineEdit.setValidator(QtGui.QIntValidator())

        self.LowerV_lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.LowerV_lineEdit.setGeometry(QtCore.QRect(820, 150, 30, 20))
        self.LowerV_lineEdit.setObjectName("Actual_X_lineEdit")
        self.LowerV_lineEdit.setText(str(self.HSV_L1[2]))
        self.LowerV_lineEdit.setValidator(QtGui.QIntValidator())

        self.SaveColor_label = QtWidgets.QLabel(self.tab_2)
        self.SaveColor_label.setGeometry(QtCore.QRect(660, 210, 180, 50))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.SaveColor_label.setFont(font)
        self.SaveColor_label.setWordWrap(True)
        self.SaveColor_label.setObjectName("SaveColor_label")

        self.SaveColorSet_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.SaveColorSet_pushButton.setGeometry(QtCore.QRect(860, 210, 60, 50))
        self.SaveColorSet_pushButton.setObjectName("SaveColorSet_pushButton")
        self.SaveColorSet_pushButton.setText("Save")


        self.TestColorSet_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.TestColorSet_pushButton.setGeometry(QtCore.QRect(860, 150, 60, 20))
        self.TestColorSet_pushButton.setObjectName("TestColorSet_pushButton")
        self.TestColorSet_pushButton.setText("Test")

        self.Cv_window_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.Cv_window_pushButton.setGeometry(QtCore.QRect(860, 180, 60, 20))
        self.Cv_window_pushButton.setObjectName("Cv_window_pushButton")
        self.Cv_window_pushButton.setText("Track")




        #Save Tab2 button 
        self.SaveT2_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.SaveT2_pushButton.setGeometry(QtCore.QRect(840, 90, 50, 20))
        self.SaveT2_pushButton.setObjectName("SaveT2_pushButton")
     

        
        
        
        #Message for Vision system
        self.Vision_textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.Vision_textBrowser.setGeometry(QtCore.QRect(660, 280, 275, 225))
        self.Vision_textBrowser.setObjectName("Vision_textBrowser")

        # Add tab 2 to tab widget
        self.tabWidget.addTab(self.tab_2, "")
        self.playing = False
        QtCore.QMetaObject.connectSlotsByName(Widget)

        #Draw bounding box 
        self.rectangular_box = QtWidgets.QFrame(self.tab_2)

        self.rectangular_box.setGeometry(QtCore.QRect(5, 30, 650, 500))
        self.rectangular_box.setFrameShape(QtWidgets.QFrame.Box)
        self.rectangular_box.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.rectangular_box.setObjectName("rectangular_box")

        #TAB3
        
        self.Activate_Function_Tab2()
        self.retranslateUi(Widget)

    #Toggle play vision system 
    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Sorting Object By Color"))

        #TAB2 ------------ VISION SYSTEM---------------------------
        self.EN_pushButton.setText(_translate("Widget", "Enable"))
        self.CLearM_VS_pushButton.setText(_translate("Widget", "Clear Message"))
        self.label_1_t2.setText(_translate("Widget", "Vision System"))
        self.label_2_t2.setText(_translate("Widget", "Vision System Message"))
        self.label_3_t2.setText(_translate("Widget", "Vision System Configuration"))
        self.label_4_t2.setText(_translate("Widget", "Edit position of red box to fit your actual frame"))
        self.label_5_t2.setText(_translate("Widget", "XDim:"))
        self.label_6_t2.setText(_translate("Widget", "YDim:"))
        self.SaveT2_pushButton.setText(_translate("Widget", "Set"))
        self.OffsetBox_comboBox.setItemText(0, _translate("Widget", "Top Left"))
        self.OffsetBox_comboBox.setItemText(1, _translate("Widget", "Top Right"))
        self.OffsetBox_comboBox.setItemText(2, _translate("Widget", "Bottom Left"))
        self.OffsetBox_comboBox.setItemText(3, _translate("Widget", "Bottom Right"))

        self.ColorSet_comboBox.setItemText(0, _translate("Widget", "S1"))
        self.ColorSet_comboBox.setItemText(1, _translate("Widget", "S2"))
        self.ColorSet_comboBox.setItemText(2, _translate("Widget", "S3"))
        self.ColorSet_comboBox.setItemText(3, _translate("Widget", "All"))

        self.Right_pushButton.setText(_translate("Widget", "→"))

        self.Left_pushButton.setText(_translate("Widget", "←"))

        self.Up_pushButton.setText(_translate("Widget", "↑"))
        self.CamID_pushButton.setText(_translate("Widget", "Cam Index"))

        self.Down_pushButton.setText(_translate("Widget", "↓"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Widget", "Vision System"))
  

       

    

    def toggle_play(self):

        if not self.playing:
            #print("Camera Enable")
            self.playing = True
            self.timer = QtCore.QTimer(self.tab_2)  
            #timer to update the fram periodi
            try:
                self.video_capture = cv2.VideoCapture(self.CamID)
                # Check if the camera opened successfully
                if not self.video_capture.isOpened():
                    self.EN_pushButton.setText("Enable")
                    raise RuntimeError("Error: Unable to open camera.")
                else:
                    self.timer.timeout.connect(self.update_frame)
                    self.timer.start(25)  # Start timer
                    self.EN_pushButton.setText("Disable")
                    self.Vision_textBrowser.append(datetime.now().strftime("[%H:%M:%S]: ") +"Connect to camera successfuly")
            except Exception as e:
                print("Exception occurred while setting up video capture:", e)
                self.EN_pushButton.setText("Enable")
                self.ChosenSet = 0
                self.Execute = 0
                self.playing = False
                Text = "Exception occurred while setting up video capture, invalid index"
                self.Vision_textBrowser.append(datetime.now().strftime("[%H:%M:%S]: ") +Text)
                self.video_label.clear()
        else:
            self.EN_pushButton.setText("Enable")
            self.ChosenSet = 0
            self.Execute = 0
            self.playing = False
            self.timer.stop()  # Stop timer
            self.Vision_textBrowser.append(datetime.now().strftime("[%H:%M:%S]: ") +"Camera Disable")
            self.video_label.clear()
            
    def update_frame(self):
        ret, frame = self.video_capture.read()
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Draw small square boxes in the four corners
        box_size = 50  # Adjust size as needed
        thickness = 2  # Adjust thickness as needed
        color = (255, 255, 0)  # Adjust color as needed
        #Color to detect 

        h, w, ch = frame.shape
        Copy_Fram = frame.copy() 
        tl_x_center = self.OS_TL_X + box_size // 2
        tl_y_center = self.OS_TL_Y + box_size // 2
        top_left = (tl_x_center,tl_y_center)
        cv2.rectangle(frame, (self.OS_TL_X, self.OS_TL_Y), (box_size + self.OS_TL_X, box_size + self.OS_TL_Y), color, thickness)
        cv2.circle(frame, (tl_x_center, tl_y_center), radius=3, color=(0, 0, 255), thickness=-1)

        # Top-right corner
        tr_x_center = w - self.OS_TR_X - box_size // 2
        tr_y_center = self.OS_TR_Y + box_size // 2
        top_right = (tr_x_center,tr_y_center)
        cv2.rectangle(frame, (w - box_size - self.OS_TR_X, self.OS_TR_Y), (w - self.OS_TR_X, box_size + self.OS_TR_Y), color, thickness)
        cv2.circle(frame, (tr_x_center, tr_y_center), radius=3, color=(0, 0, 255), thickness=-1)

        # Bottom-left corner
        bl_x_center = self.OS_BL_X + box_size // 2
        bl_y_center = h - self.OS_BL_Y - box_size // 2
        bottom_left = (bl_x_center,bl_y_center)
        cv2.rectangle(frame, (self.OS_BL_X, h - box_size - self.OS_BL_Y), (box_size + self.OS_BL_X, h - self.OS_BL_Y), color, thickness)
        cv2.circle(frame, (bl_x_center, bl_y_center), radius=3, color=(0, 0, 255), thickness=-1)

        # Bottom-right corner
        br_x_center = w - self.OS_BR_X - box_size // 2
        br_y_center = h - self.OS_BR_Y - box_size // 2
        bottom_right = (br_x_center,br_y_center)
        cv2.rectangle(frame, (w - box_size - self.OS_BR_X, h - box_size - self.OS_BR_Y), (w - self.OS_BR_X, h - self.OS_BR_Y), color, thickness)
        cv2.circle(frame, (br_x_center, br_y_center), radius=3, color=(0, 0, 255), thickness=-1)

        # Connecting lines
        cv2.line(frame, (tl_x_center, tl_y_center), (tr_x_center, tr_y_center), color, 1)
        cv2.line(frame, (tl_x_center, tl_y_center), (bl_x_center, bl_y_center), color, 1)
        cv2.line(frame, (tr_x_center, tr_y_center), (br_x_center, br_y_center), color, 1)
        cv2.line(frame, (bl_x_center, bl_y_center), (br_x_center, br_y_center), color, 1)
        cv2.putText(frame, f'Xdim: {self.Xdim}', ((tl_x_center + tr_x_center)//2, (tl_y_center + tr_y_center)//2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        cv2.putText(frame, f'Ydim: {self.Ydim}', ((tl_x_center + bl_x_center)//2,(tl_y_center + bl_y_center)//2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        #region_polygon = np.array([top_left, top_right, bottom_right, bottom_left])


        if self.Is_SetFram == 1:
            if self.IsMoving == 0:
                pts1 = np.float32([top_left, top_right, bottom_left, bottom_right])
                pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
                matrix = cv2.getPerspectiveTransform(pts1, pts2)
                frame_1 = cv2.warpPerspective(Copy_Fram, matrix, (w, h))
                fram_hsv = cv2.cvtColor(frame_1, cv2.COLOR_BGR2HSV) 
                Upper_mask_1 = np.array(self.HSV_U1, np.uint8) 
                Lower_mask_1 = np.array(self.HSV_L1, np.uint8) 
                Mask_1 = cv2.inRange(fram_hsv,Lower_mask_1,Upper_mask_1)
                kernel = np.ones((5, 5), np.uint8) 
                Mask_1 = cv2.dilate(Mask_1, kernel) 
                Mask_1_Res = cv2.bitwise_and(frame_1, frame_1, mask = Mask_1) 

                Upper_mask_2 = np.array(self.HSV_U2, np.uint8) 
                Lower_mask_2 = np.array(self.HSV_L2, np.uint8) 
                Mask_2 = cv2.inRange(fram_hsv,Lower_mask_2,Upper_mask_2)
                kernel = np.ones((5, 5), np.uint8) 
                Mask_2 = cv2.dilate(Mask_2, kernel) 
                Mask_2_Res = cv2.bitwise_and(frame_1, frame_1, mask = Mask_2) 

                Upper_mask_3 = np.array(self.HSV_U3, np.uint8) 
                Lower_mask_3 = np.array(self.HSV_L3, np.uint8) 
                Mask_3 = cv2.inRange(fram_hsv,Lower_mask_3,Upper_mask_3)
                kernel = np.ones((5, 5), np.uint8) 
                Mask_3 = cv2.dilate(Mask_3, kernel) 
                Mask_3_Res = cv2.bitwise_and(frame_1, frame_1, mask = Mask_3) 
                if self.Xdim == 0:
                    self.Xdim = w
                if self.Ydim == 0:
                    self.Ydim = h

                P2_mm_Ratio_x = self.Xdim/w
                P2_mm_Ratio_y = self.Ydim/h

                if self.ChosenSet == 1 or self.ChosenSet == 4:  
                    contours, hierarchy = cv2.findContours(Mask_1, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
                    for pic, contour in enumerate(contours): 
                        area = cv2.contourArea(contour) 
                        if(area > 300): 
                            M = cv2.moments(contour)
                            # Calculate the centroid of the contour
                            if M["m00"] != 0:
                                cx = int(M["m10"] / M["m00"])
                                cy = int(M["m01"] / M["m00"])
                                #if cv2.pointPolygonTest(region_polygon, (cx, cy), False) >= 0:
                                cv2.circle(frame_1, (cx, cy), 5, (255, 255, 0), -1)
                                text = f"(X:{(cx) * P2_mm_Ratio_x:.1f}mm|Y:{(h-cy) * P2_mm_Ratio_y:.1f}mm)"
                                cv2.putText(frame_1, "Set 1:" + text, (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

                                # Draw a circle at the centroid
                
                                # Draw a text near the centroid
                        
                            #cv2.drawContours(frame, [contour], 0, (255, 255, 0), 2)
                            #frame = cv2.rectangle(frame, (x, y),(x + w, y + h),(255, 255, 0), 2) 
                            #cv2.putText(frame, "Set 2", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0))  


                if self.ChosenSet == 2 or self.ChosenSet == 4:            
                    contours, hierarchy = cv2.findContours(Mask_2, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
                    for pic, contour in enumerate(contours): 
                        area = cv2.contourArea(contour) 
                        if(area > 300): 
                            M = cv2.moments(contour)
                            # Calculate the centroid of the contour
                            if M["m00"] != 0:
                                cx = int(M["m10"] / M["m00"])
                                cy = int(M["m01"] / M["m00"])
                               
                                cv2.circle(frame_1, (cx, cy), 5, (255, 255, 0), -1)
                                text = f"(X:{(cx) * P2_mm_Ratio_x:.1f}mm|Y:{(h-cy) * P2_mm_Ratio_y:.1f}mm)"
                                cv2.putText(frame_1, "Set 2:" + text, (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
                                    
                                # Draw a circle at the centroid
                                #cv2.circle(frame, (cx, cy), 5, (255, 255, 0), -1)
                                # Draw a text near the centroid
                                #cv2.putText(frame, "Set 2", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
                            #cv2.drawContours(frame, [contour], 0, (255, 255, 0), 2)
                            #frame = cv2.rectangle(frame, (x, y),(x + w, y + h),(255, 255, 0), 2) 
                            #cv2.putText(frame, "Set 2", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0))    

                if self.ChosenSet == 3 or self.ChosenSet == 4:
                    contours, hierarchy = cv2.findContours(Mask_3, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
                    for pic, contour in enumerate(contours): 
                        area = cv2.contourArea(contour) 
                        if(area > 300): 
                            M = cv2.moments(contour)
                            # Calculate the centroid of the contour
                            if M["m00"] != 0:
                                cx = int(M["m10"] / M["m00"])
                                cy = int(M["m01"] / M["m00"])
                                # Draw a circle at the centroid
                                #cv2.circle(frame, (cx, cy), 5, (255, 255, 0), -1)
                                #if cv2.pointPolygonTest(region_polygon, (cx, cy), False) >= 0:
                                cv2.circle(frame_1, (cx, cy), 5, (255, 255, 0), -1)
                                text = f"(X:{(cx) * P2_mm_Ratio_x:.1f}mm|Y:{(h-cy) * P2_mm_Ratio_y:.1f}mm)"
                                cv2.putText(frame_1, "Set 3:" + text, (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
                                
                                # Draw a text near the centroid
                            # cv2.putText(frame, "Set 3", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
                            #cv2.drawContours(frame, [contour], 0, (255, 255, 0), 2)
                            #frame = cv2.rectangle(frame, (x, y),(x + w, y + h),(255, 255, 0), 2) 
                            #cv2.putText(frame, "Set 2", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0))    

            #q_img = QtGui.QImage(Mask_3_Res.data, w, h, bytes_per_line, QtGui.QImage.Format_Indexed8)
            bytes_per_line = ch * w
            q_img = QtGui.QImage(frame_1.data, w, h, bytes_per_line, QtGui.QImage.Format_BGR888)

        else:
          
            bytes_per_line = ch * w
            q_img = QtGui.QImage(frame.data, w, h, bytes_per_line, QtGui.QImage.Format_BGR888)


        self.video_label.setPixmap(QtGui.QPixmap.fromImage(q_img))
        self.video_label.repaint()

        

    
        

    #TAB2
    def Activate_Function_Tab2(self):
        self.CLearM_VS_pushButton.clicked.connect(self.Vision_textBrowser.clear)
        self.EN_pushButton.pressed.connect(self.toggle_play)
        self.Left_pushButton.pressed.connect(self.Left_Button)
        self.Right_pushButton.pressed.connect(self.Right_Button)
        self.Up_pushButton.pressed.connect(self.Up_Button)
        self.Down_pushButton.pressed.connect(self.Down_Button)
        self.SaveT2_pushButton.clicked.connect(self.Save_Dim)
        self.CamID_pushButton.clicked.connect(self.CamID_Change)
        self.ColorSet_comboBox.currentIndexChanged.connect(self.Change_CSet)
        self.TestColorSet_pushButton.clicked.connect(self.Test_Color_Range)
        self.Cv_window_pushButton.clicked.connect(self.OpenCv_trackColor)
    #Tab2 Config

    def Left_Button(self):
        if self.EN_pushButton.text() == 'Disable':
            if self.OffsetBox_comboBox.currentIndex() == 0: 
                self.OS_TL_X  =  self.OS_TL_X - 2
            elif self.OffsetBox_comboBox.currentIndex() == 1: 
                self.OS_TR_X = self.OS_TR_X + 2
            elif self.OffsetBox_comboBox.currentIndex() == 2: 
                self.OS_BL_X = self.OS_BL_X -2
            elif self.OffsetBox_comboBox.currentIndex() == 3: 
                self.OS_BR_X = self.OS_BR_X + 2
        else:
            self.Vision_textBrowser.append(datetime.now().strftime("[%H:%M:%S]: ") +"Please enable camera before adjusting Box position")
            return
        
    def Right_Button(self):
        if self.EN_pushButton.text() == 'Disable':
            if self.OffsetBox_comboBox.currentIndex() == 0: 
                self.OS_TL_X  =  self.OS_TL_X + 2
            elif self.OffsetBox_comboBox.currentIndex() == 1: 
                self.OS_TR_X = self.OS_TR_X - 2
            elif self.OffsetBox_comboBox.currentIndex() == 2: 
                self.OS_BL_X = self.OS_BL_X + 2
            elif self.OffsetBox_comboBox.currentIndex() == 3: 
                self.OS_BR_X = self.OS_BR_X - 2
        else:
            self.Vision_textBrowser.append(datetime.now().strftime("[%H:%M:%S]: ") +"Please enable camera before adjusting Box position")
            return
        
    def Up_Button(self):
        if self.EN_pushButton.text() == 'Disable':
            if self.OffsetBox_comboBox.currentIndex() == 0: 
                self.OS_TL_Y  =  self.OS_TL_Y - 2
            elif self.OffsetBox_comboBox.currentIndex() == 1: 
                self.OS_TR_Y = self.OS_TR_Y - 2
            elif self.OffsetBox_comboBox.currentIndex() == 2: 
                self.OS_BL_Y = self.OS_BL_Y +2
            elif self.OffsetBox_comboBox.currentIndex() == 3: 
                self.OS_BR_Y = self.OS_BR_Y + 2
        else:
            self.Vision_textBrowser.append(datetime.now().strftime("[%H:%M:%S]: ") +"Please enable camera before adjusting Box position")
            return
    
    def Down_Button(self):
        if self.EN_pushButton.text() == 'Disable':
            if self.OffsetBox_comboBox.currentIndex() == 0: 
                self.OS_TL_Y  =  self.OS_TL_Y + 2
            elif self.OffsetBox_comboBox.currentIndex() == 1: 
                self.OS_TR_Y = self.OS_TR_Y + 2
            elif self.OffsetBox_comboBox.currentIndex() == 2: 
                self.OS_BL_Y = self.OS_BL_Y -2
            elif self.OffsetBox_comboBox.currentIndex() == 3: 
                self.OS_BR_Y = self.OS_BR_Y - 2
        else:
            self.Vision_textBrowser.append(datetime.now().strftime("[%H:%M:%S]: ") +"Please enable camera before adjusting Box position")
            return

    def Save_Dim(self):
        if self.EN_pushButton.text() == 'Disable':
            if self.SaveT2_pushButton.text() == 'Set':
                self.SaveT2_pushButton.setText("Reset")
                self.Xdim = float(self.Actual_X_lineEdit.text())
                self.Ydim = float(self.Actual_Y_lineEdit.text())
                self.Vision_textBrowser.append(datetime.now().strftime("[%H:%M:%S]: ") +"Saved your actual XY dimension")
                self.Is_SetFram = 1
            else:
                self.SaveT2_pushButton.setText("Set")
                self.Is_SetFram = 0
        else:
            self.Vision_textBrowser.append(datetime.now().strftime("[%H:%M:%S]: ") +"Please enable camera before saving value")
            return
    def CamID_Change(self):
        if self.EN_pushButton.text() == 'Disable':
            self.Vision_textBrowser.append(datetime.now().strftime("[%H:%M:%S]: ") +"Disable camera before changing value")
        else:
            if not self.CamID_lineEdit.text():
                self.CamID = 0
            else:
                self.CamID = int(self.CamID_lineEdit.text())
            Mes = "Cam index change to "+ str(self.CamID)
            self.Vision_textBrowser.append(datetime.now().strftime("[%H:%M:%S]: ")+Mes)   

            return
    

    def Change_CSet(self):
        if self.ColorSet_comboBox.currentIndex() < 3:
            SetPos = getattr(self, f"Color{self.ColorSet_comboBox.currentIndex()+ 1 }_pos")
            HSVU = getattr(self, f"HSV_U{self.ColorSet_comboBox.currentIndex()+1}")
            HSVL= getattr(self, f"HSV_L{self.ColorSet_comboBox.currentIndex()+1}")
            Text = "Pos: [X: "+f"{SetPos[0]:.2f}"+"]"+ "[Y: "+f"{SetPos[1]:.2f}"+"]"
            self.ColorPos_label.setText(Text)
            self.UpperH_lineEdit.setText(str(HSVU[0]))
            self.UpperS_lineEdit.setText(str(HSVU[1]))
            self.UpperV_lineEdit.setText(str(HSVU[2]))
            self.LowerH_lineEdit.setText(str(HSVL[0]))
            self.LowerS_lineEdit.setText(str(HSVL[1]))
            self.LowerV_lineEdit.setText(str(HSVL[2]))
            self.Vision_textBrowser.append(datetime.now().strftime("[%H:%M:%S]: ") +"Change to Set" + str(self.ColorSet_comboBox.currentIndex()+1))
        self.ChosenSet = self.ColorSet_comboBox.currentIndex()+ 1
    
    def Test_Color_Range(self):

        HSVU = getattr(self, f"HSV_U{self.ColorSet_comboBox.currentIndex()+1}")
        HSVL = getattr(self, f"HSV_L{self.ColorSet_comboBox.currentIndex()+1}")
        HSVL[0] = int(self.LowerH_lineEdit.text())
        HSVL[1] =  int(self.LowerS_lineEdit.text())
        HSVL[2] = int(self.LowerV_lineEdit.text())
        HSVU[0] = int(self.UpperH_lineEdit.text())
        HSVU[1] = int(self.UpperS_lineEdit.text())
        HSVU[2] = int(self.UpperV_lineEdit.text())
        self.ChosenSet = self.ColorSet_comboBox.currentIndex() + 1
        self.Vision_textBrowser.append(datetime.now().strftime("[%H:%M:%S]: ") +"Test Color Range "+str(self.ColorSet_comboBox.currentIndex()+1))
        

    def OpenCv_trackColor(self):
        if self.EN_pushButton.text() == 'Enable':
            if self.Cv_window_pushButton.text() == 'Track':
                try:
                    self.EN_pushButton.setEnabled(False)
                    cap = cv2.VideoCapture(self.CamID)
                    #creating frame for Vision track
                    cap.set(3,1280)
                    cap.set(4,720)
                    if not cap.isOpened():
                        self.Vision_textBrowser.append(datetime.now().strftime("[%H:%M:%S]: ") +"Can not open camera, invalid camera index")
                        self.EN_pushButton.setEnabled(True)
                        raise Exception("Error: Unable to open video capture device.")
                        return
                    self.Cv_window_pushButton.setText("Save")
                    self.IsTracking = 1
    
                    #Creating trackbar for detecting color
                    cv2.namedWindow("Track Color")
                    cv2.createTrackbar("L - H", "Track Color", 0, 179, nothing)
                    cv2.createTrackbar("L - S", "Track Color", 0, 255, nothing)
                    cv2.createTrackbar("L - V", "Track Color", 0, 255, nothing)
                    cv2.createTrackbar("U - H", "Track Color", 179, 179, nothing)
                    cv2.createTrackbar("U - S", "Track Color", 255, 255, nothing)
                    cv2.createTrackbar("U - V", "Track Color", 255, 255, nothing)

                    #Show the frame
                    while True:
                        ret, frame = cap.read()
                        if not ret:
                            break

                        #Convert the BGR image to HSV image
                        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  
                        l_h = cv2.getTrackbarPos("L - H", "Track Color")
                        l_s = cv2.getTrackbarPos("L - S", "Track Color")
                        l_v = cv2.getTrackbarPos("L - V", "Track Color")
                        u_h = cv2.getTrackbarPos("U - H", "Track Color")
                        u_s = cv2.getTrackbarPos("U - S", "Track Color")
                        u_v = cv2.getTrackbarPos("U - V", "Track Color")

                        #Take upper and Lower HSV value
                        lower_range = np.array([l_h, l_s, l_v])
                        upper_range = np.array([u_h, u_s, u_v])

                        #Creata a mask for color
                        mask = cv2.inRange(hsv, lower_range, upper_range)
                        kernel = np.ones((5, 5), np.uint8) 
                        mask = cv2.dilate(mask, kernel) 
                        res = cv2.bitwise_and(frame, frame, mask=mask)
                        mask_3 = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
                        stacked = np.hstack((mask_3,frame,res))


                        cv2.imshow('Track Color',cv2.resize(stacked,None,fx=0.3,fy=0.3))

                        key = cv2.waitKey(1)
                        if key == 27:
                            break
                        #Press track button to save color set value
                        if self.IsTracking == 0:
                            if self.ColorSet_comboBox.currentIndex() < 3:
                                HSVU = getattr(self, f"HSV_U{self.ColorSet_comboBox.currentIndex()+1}")
                                HSVL= getattr(self, f"HSV_L{self.ColorSet_comboBox.currentIndex()+1}")
                                HSVL[0] = l_h
                                HSVL[1] = l_s
                                HSVL[2] = l_v
                                HSVU[0] = u_h
                                HSVU[1] = u_s
                                HSVU[2] = u_v
                                self.UpperH_lineEdit.setText(str(HSVU[0]))
                                self.UpperS_lineEdit.setText(str(HSVU[1]))
                                self.UpperV_lineEdit.setText(str(HSVU[2]))

                                self.LowerH_lineEdit.setText(str(HSVL[0]))
                                self.LowerS_lineEdit.setText(str(HSVL[1]))
                                self.LowerV_lineEdit.setText(str(HSVL[2]))
                                self.Cv_window_pushButton.setText("Track")
                                self.Vision_textBrowser.append(datetime.now().strftime("[%H:%M:%S]: ") +"Save Color for Set "+str(self.ColorSet_comboBox.currentIndex()+1))

                            break

                    cap.release()
                    self.EN_pushButton.setEnabled(True)
                    cv2.destroyAllWindows()
                except Exception as e:
                    self.EN_pushButton.setEnabled(True) 
                    print("An error occurred:", e)
            else:
                self.IsTracking = 0
        else:
            self.Vision_textBrowser.append(datetime.now().strftime("[%H:%M:%S]: ") +"Please disable Camera before tracking color")  





    #TAB3 FUNCTION
    def Save_Robot_Congfig(self):
        if self.AD_D1_lineEdit.text():
            RK.D0 = float(self.AD_D1_lineEdit.text())
      
        if self.AD_D2_lineEdit.text():
            RK.D1 = float(self.AD_D2_lineEdit.text())
 

        if self.AD_D3_lineEdit.text():
            RK.D2 = float(self.AD_D3_lineEdit.text())
        

        if self.AD_L1_lineEdit.text():
            RK.L1= float(self.AD_L1_lineEdit.text())

        if self.AD_L2_lineEdit.text():
            RK.L2 = float(self.AD_L2_lineEdit.text())

        if self.AD_L3_lineEdit.text():
            RK.L3 = float(self.AD_L3_lineEdit.text())

        #Update Upper Limit
        for i in range(1, 6):
            line_edit = getattr(self, f"Lim_U_J{i}lineEdit")
            if line_edit.text():
                self.DOF_Max_UpperLim[i - 1] = float(line_edit.text())

        #Update Upper Limit
        for i in range(1, 6):
            line_edit = getattr(self, f"Lim_L_J{i}lineEdit")
            if line_edit.text():
                self.DOF_Max_LowerLim[i - 1] = float(line_edit.text())

        #Update Upper Limit
        for i in range(1, 6):

            line_edit = getattr(self, f"RR_J{i}_lineEdit")
            if line_edit.text():
                self.Gear_Ratio[i - 1] = float(line_edit.text())
        self.Update_Pose_LineEdit()
    
def nothing(x):
    pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
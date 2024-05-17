## Precision-Color-Sorting-and-Real-World-Distance-Estimation
# About this application
This project is built for sorting colored object, estimate it's realworld distance base on the frame taken on the camera
The GUI is developed base on PyQt5 library in python, combined with opencv to implement application with Vision system
This application can detect a several color base on your HSV value that you input to the app.
It can detect 3 color set simultaneously, for more color set you can config the code base on my tutorial.
# How to use
1. Set frame references.
   
![image](https://github.com/phamhduc/Precision-Color-Sorting-and-Real-World-Distance-Estimation/assets/101264143/03350ee5-1e6d-43a5-af2a-3a7993a243fc)

+ Click Enable button to show the camera frame, make use your computer has aldready connected to webcam and choose the suitable camera index value(default 0).
+ Choose the box in combobox (topleft, topright, bottom ....) and use direction button on the right side to adjust the working cordinate base on the realworld cordinate
+ This application can only work with the square or rectangle realworld coordinate, adjust the coordinate of 4 box to fit your realworld working area(in my example, i used the working area with dimension (180*200)mm
+ Input your actual Xdim and YDim (in my example, X = 180mm and Y = 200mm)
+ Click 'Set' button to set the working frame.
  
![image](https://github.com/phamhduc/Precision-Color-Sorting-and-Real-World-Distance-Estimation/assets/101264143/b74876dd-d494-4b3b-b5d8-adf55245fc49)

After clicking 'Set', the application will warp the frame to fit your realworld coordinate.

![image](https://github.com/phamhduc/Precision-Color-Sorting-and-Real-World-Distance-Estimation/assets/101264143/1a97167a-a741-4362-bab6-fd3cd943baab)

2. Create your Color Set.
  
![image](https://github.com/phamhduc/Precision-Color-Sorting-and-Real-World-Distance-Estimation/assets/101264143/f1087690-1aa1-450a-ac87-1df69d0a7559)
  
+ Choose your set in 'S1' Combobox. This application provides you 3 detection set.
  
![image](https://github.com/phamhduc/Precision-Color-Sorting-and-Real-World-Distance-Estimation/assets/101264143/e2951ce7-c742-4a43-902f-5e1942be37d0)

+ You can edit the HSV value directly in line edit for lower and upper HSV value.
+ You can also track for your expectated color. Please disable the camera before tracking.
  


+ Put all of your object in the frame and use the trackbar to find the best HSV value.

![image](https://github.com/phamhduc/Precision-Color-Sorting-and-Real-World-Distance-Estimation/assets/101264143/eacfa0cb-82de-42d2-abe5-ac88f7b43a40)

+ After obtaining the correct HSV value, choose the set in the 's1' combobox and press save, it will automatically update new value for your set.
+ Do the same to get HSV value for Set 2 and Set 3, for more set, your can config in the project file.


As a result, you can detect the colorset base on your HSV value and get the estimation in distance.

![image](https://github.com/phamhduc/Precision-Color-Sorting-and-Real-World-Distance-Estimation/assets/101264143/26b7e880-34b2-42d7-82d5-68a70c4d7280)


# How this app can estimate distance in realworld coordinate?

+ By obtaining the four corners of a square or rectangle within the real-world frame, I utilize the perspective warp function to transform and display the working frame in a top view. Subsequently, I extract the pixel values of X and Y coordinates.

+ After obtaining the pixel values for X and Y coordinates, I calculate the pixel-to-millimeter ratio separately for each axis base on the actual X and Y dimension inputed by user. as the warping process may result in different scaling factors for X and Y, so the pixel-to-millimeter ratio must be calculated separately.

+ Once the pixel-to-millimeter ratios for both X and Y are determined, I multiply these values by the Cx and Cy coordinates of the object to estimate the real-world distance."

# How to add color set?

+ To add color set, you have to config a bit in the code file
+ First add HSV set for new color set
![image](https://github.com/phamhduc/Precision-Color-Sorting-and-Real-World-Distance-Estimation/assets/101264143/3c3a51c1-868c-4b91-899b-09f0968bae74)

+ Add item for this combo_box.

  ![image](https://github.com/phamhduc/Precision-Color-Sorting-and-Real-World-Distance-Estimation/assets/101264143/2298c4a4-6795-424c-9210-eef2c9b4653f)

+ Additionally, you need to update the control index numbers for the combobox throughout the entire codebase.

  ![image](https://github.com/phamhduc/Precision-Color-Sorting-and-Real-World-Distance-Estimation/assets/101264143/0b009102-3a5e-491e-b8a6-e5cb5a71e4d7)

+ For example, replace all instances of '3' with the number of color sets in your code. There are several lines similar to this that need to be edited accordingly

# Importance Note!!!

+ This code is extracted from my 6-DOF robot arm control project, so it may contain some irrelevant lines. Please disregard those and focus primarily on the relevant parts for your needs

+ For any question about this project, feel free to contact me through email "phamhduc111@gmail.com"





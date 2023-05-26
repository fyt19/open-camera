# Camera Application

This application opens the camera and shows the image on the screen.

## How Does It Work?

The application uses the cv2 library to access the camera and display the image. It uses the VideoCapture function to open the camera and the imshow function to show the image. It also uses the waitKey function to wait for a key press and the destroyAllWindows function to close the window.

## Required Libraries

You need the cv2 library to run the application. You can install this library with pip:

```
pip install opencv-python
```

You also need the numpy library to work with arrays. You can also install this library with pip:
```
pip install numpy
```

## Installation and Usage

After downloading the application, open a terminal in the directory where the application is located and run the following command:
```
python camera.py
```
When the application starts running, you will see a window with the camera image. You can press "q" key to quit the application.

You can change the camera source by changing the argument of the VideoCapture function. If it is 0, it uses the computer's camera. If it is 1, it opens the camera plugged in from usb. If it is 2, it

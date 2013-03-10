snap-nxt v1.0
========

A block module and local server for Snap! to interface with the Mindstorms NXT.

#Requirements
* A Mindstorms NXT
* Python 2.6+
* The `nxt-python` module for Python.

#Getting Started
* Load Snap! in your browser window.
* Import the nxt.xml file.
* Connect your NXT to your computer via USB cable.
* In a command line, navigate to the directory where you are storing these files.
* As a root user, type `python snap.py`.
* The program should print something like `Now serving on port 1330.`
* **Enjoy!**

#NXT stuff
If you connect the sensors, connect them in the following configuration:
* Port 1 - Touch
* Port 2 - Sound
* Port 3 - Light
* Port 4 - Ultrasonic

#Credits
* Based heavily upon the Python CORS server here: https://gist.github.com/2904124
* Thanks to the Snap! team for making this fairly easy to do

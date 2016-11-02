import sys
import subprocess

subprocess.call(["conda", "install", "-c", "anaconda", "pyside", "-y"])

from PySide import QtGui

# Create a Qt application
app = QtGui.QApplication(sys.argv)
# Create a Label and show it
label = QtGui.QLabel("Hello World")
label.show()
# Enter Qt application main loop
app.exec_()
sys.exit()

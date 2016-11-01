import sys
import subprocess

subprocess.call(["pip", "install", "PySide"])

from PySide import QtCore, QtGui

# Create a Qt application
app = QtCore.QApplication(sys.argv)
# Create a Label and show it
label = QtGui.QLabel("Hello World")
label.show()
# Enter Qt application main loop
app.exec_()
sys.exit()

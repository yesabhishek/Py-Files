# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:37:54 2020

@author: RDX
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys
from PyQt4.QtGui import *
a = QApplication(sys.argv)

# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QWidget()

# Show a message box
result = QMessageBox.question(w, 'Message', "Do you like Python?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

if result == QMessageBox.Yes:
    print('Yes.')
else:
    print('No.')

# Show window
w.show()
sys.exit(a.exec_())

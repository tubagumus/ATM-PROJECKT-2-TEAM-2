from PyQt5.QtWidgets import QApplication
from account import LoginPage
from Query_db import ATM_Table_Create,Query_open
import os
import sys

app =QApplication([])

pencere = LoginPage()
pencere.show()
app.exec_()


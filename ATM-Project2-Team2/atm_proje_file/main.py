from PyQt5.QtWidgets import QApplication
from account import LoginPage

#It is imported to create tables with 'ATM_Table_Create' and perform query operations  with 'Query_open 'i n the database.
from Query_db import ATM_Table_Create,Query_open 
import os
import sys

app =QApplication([])

pencere = LoginPage()
pencere.show()
app.exec_()


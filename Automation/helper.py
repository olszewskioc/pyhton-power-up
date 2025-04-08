'''
======================================================================================================================

Run this code to take the position in the screen.
5 seconds between the moment the code runs and the print of position.

Thiago Olszewski de Carvalho - Computer Engineering

======================================================================================================================
'''

import time
import pyautogui as pag
import pandas as pd

table = pd.read_csv('Automation/produtos.csv')
print(table)

time.sleep(5)
x, y = pag.position()
print(f"x={x}, y={y}")

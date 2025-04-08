'''
======================================================================================================================

This code consists in an automation test for register new products in an system from a CSV file.
The test will read the CSV file, create a new product for each row and then stop.
The code is extracted from a class of hashtag programming in Python Power Up.

Thiago Olszewski de Carvalho - Computer Engineering

======================================================================================================================
'''

import time
import pyautogui as pag
import pandas as pd
import os


# Configurations
pag.PAUSE = 0.5
url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
login = ("thiago@gmail.com", "olszewski1234")   # (Login, Password)
checkpoint_file = "Automation/progress.txt"

# Step 1 - Open Web Browser
pag.press("win")
pag.write("edge")
pag.press("enter")

# Step 2 - Acces the system
time.sleep(2)
pag.write(url)
pag.press("enter")

# Step 3 - Login in system
time.sleep(2)
pag.press("tab")
pag.write(login[0]) # Login

pag.press("tab")
pag.write(login[1]) # Password

pag.press("tab")
pag.press("enter")

# Step 4 - Read the data
table = pd.read_csv('Automation/produtos.csv')
print(table)

# Step 5 - Register the products
start_index = 0
if os.path.exists(checkpoint_file):
    with open(checkpoint_file, "r") as f:
        last_line = f.read()
        if last_line.isdigit():
            start_index = int(last_line)

for line in table.index[start_index:]:
    try:
        pag.press("home")
        pag.click(x=758, y=279)

        for column in table.columns:
            print(f"{line} | {column}: {table.loc[line, column]}")

            if str(table.loc[line, column]) != "nan":
                pag.write(str(table.loc[line, column]))

            pag.press("tab")

        pag.press("enter")
        pag.press("end")
        time.sleep(1)

        # save the progress
        with open(checkpoint_file, "w") as f:
            f.write(str(line + 1))

    except Exception as e:
        print(f"Error in line {line}: {e}")
        break

"""A simple template""" 

# Copyright (c) MClavier (mathieu.clavier@outlook.com - https://github.com/claviermathieu).
# Distributed for personnal use

# -----------------------------------------------------------------------------
# Packages
# -----------------------------------------------------------------------------

import os
import pandas as pd
import importlib.util
MODULE_PATH = "C:\\Users\\mathi\\OneDrive\\PROFESSIONNEL\\____cours____\\__travaux__\\Projets\\datary\\src\\datary\\generic_interface.py"
MODULE_NAME = "generic_interface"
spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
gi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gi)

# -----------------------------------------------------------------------------
# Start program
# -----------------------------------------------------------------------------

gi.title('Mon programme')

gi.describe([
    "Etape 1 : assurez-vous que le fichier :", 
    "\t- input.csv"
    ])

input_folder = input("# Indiquer le dossier de données ? > ")

# -----------------------------------------------------------------------------
# Read data
# -----------------------------------------------------------------------------

t = gi.start("Lecture des données")

db = pd.read_csv(f"{input_folder}/monfichier.csv")

gi.end(t)

# -----------------------------------------------------------------------------
# Treatment
# -----------------------------------------------------------------------------

# Treatment 1
# Treatment 2
# Treatment 3

# -----------------------------------------------------------------------------
# Exportation
# -----------------------------------------------------------------------------

# Create folder


df.to_csv("")

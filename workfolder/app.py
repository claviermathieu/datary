"""A template for datascience app

This file is a test file of datary modules
"""

# Copyright (c) MClavier (mathieu.clavier@outlook.com - https://github.com/claviermathieu).
# Part of the datary package : data for actuary
# Distributed for personnal use

# Packages
import os
import pandas as pd

# ------------- import datary ---------------
# import datary.interface as gi
# from datary.excel import ExcelFile
# ------------- specific import during devlpt ---------------
from importlib.machinery import SourceFileLoader
gi = SourceFileLoader("gi", "../src/datary/interface.py").load_module()
excel = SourceFileLoader("excel", "../src/datary/excel.py").load_module()


# -----------------------------------------------------------------------------
# Overwrite presentation function
# -----------------------------------------------------------------------------

def presentation():
    gi.title("A propos")
    gi.describe([
        "# Titre :\t Template de programme de transformation de données",
        "# Crédentials :\t MClavier (mathieu.clavier@outlook.com)",
        "\n\n# Objectifs : Définir l'objectif\n\n",
        "---------------------------------------------------------------------------------------------------------",
        "* Input :",
        "\tBase de données issues de CGI",
        "\t- file1.csv",
        "\t- file2.csv",
        "\t- file3.csv",

        "* Output :",
        "\t- output.csv \t fichier contenant tous les contrats du scope",
        "---------------------------------------------------------------------------------------------------------",
        ""
    ])
    gi.pause()

# -----------------------------------------------------------------------------
# Execution script
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    presentation()


gi.presentation = presentation

def other():
    DEV_MODE = 1
    INPUT_FOLDER = "delits 2022-06-22"
    if not DEV_MODE:
        # Get input folder
        input_folder = os.listdir('input')[-1]
        # gs.presentation give the possibility to change the input and output folder
        input_folder = presentation(input_folder)
    else:
        input_folder = INPUT_FOLDER

    # Create output folder if not existing
    gu.create_folder('output', input_folder)
    gu.create_folder('output/' + input_folder, 'intermediate')
    gu.create_folder('output/' + input_folder, 'figures')
    gu.create_folder('output/' + input_folder, 'controls')

    # # Complete path
    output_folder = 'output/' + input_folder + '/'
    input_folder = 'input/' + input_folder + '/'

    # -----------------------------------------------------------------------------
    # Read data
    # -----------------------------------------------------------------------------

    gi.title("Programme principal")

    # Read data
    t = gi.start("Lecture des données")
    df = pd.read_csv(input_folder + 'donnee-dep-corr.csv', sep = ";")
    gi.end(t)

    # First visualisation : use pandas profiling -> specify the file
    DATA_EXPLORATION = 0
    if DATA_EXPLORATION:
        profile = pp.ProfileReport(df, title = input_folder + 'donnee-dep-corr.csv')
        profile.to_file(output_folder + '/intermediate/donnee-dep-corr.html')

    # -----------------------------------------------------------------------------
    # Main program
    # -----------------------------------------------------------------------------

    gi.sub_title("Etape 1 : choisir les paramètre")


    from rich.theme import Theme
    custom_theme = Theme({
        "info": "dim cyan",
        "warning": "magenta",
        "danger": "bold red"
    })


    print("[warning]test[/warning]")





    gi.describe([
        "[bold u dim cyan]OUTILS[/bold /u dim cyan]!"
    ])









    print("Hello, [bold u dim cyan]World[/bold /u di]!", ":vampire:")









    # -----------------------------------------------------------------------------
    # Program end
    # -----------------------------------------------------------------------------
    if not DEV_MODE:
        os.startfile('output')
        input("\n\n# Fermeture du programme. Entrer pour continuer > ")

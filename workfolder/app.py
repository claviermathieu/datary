"""A template for datascience app

This file is a test file of datary modules
"""

# Copyright (c) MClavier (mathieu.clavier@outlook.com - https://github.com/claviermathieu).
# Distributed for personnal use
# Test template for datary package

# Packages
import os
import pandas as pd

# ------------- import datary ---------------
# import datary.interface as gi
# import datary.excel as excel

# ------------- specific import during devlpt ---------------
import importlib.util
MODULE_PATH = "C:\\Users\\mathi\\OneDrive\\PROFESSIONNEL\\____cours____\\__travaux__\\Projets\\datary\\src\\datary\\interface.py"
MODULE_NAME = "interface"
spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
gi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gi)
MODULE_PATH = "C:\\Users\\mathi\\OneDrive\\PROFESSIONNEL\\____cours____\\__travaux__\\Projets\\datary\\src\\datary\\excel.py"
MODULE_NAME = "excel"
spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
excel = importlib.util.module_from_spec(spec)
spec.loader.exec_module(excel)
MODULE_PATH = "C:\\Users\\mathi\\OneDrive\\PROFESSIONNEL\\____cours____\\__travaux__\\Projets\\datary\\src\\datary\\utils.py"
MODULE_NAME = "utils"
spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(utils)


# -----------------------------------------------------------------------------
# Overwrite presentation function
# -----------------------------------------------------------------------------

def presentation(input_folder="Non initialisé"):
    gi.title("A propos")
    gi.describe([
        "# TITRE \t Template data application from datary",
        "# CREDENTIALS \t MClavier (https://github.com/claviermathieu)",
        
        "\n\n# OBJECTIF",
        "\tCe fichier fourni un fichier template permettant de plus rapidement se mettre au travail tout",
        "\ten ne négligeant pas la forme lors de projet professionnel.\n\n",
        
        "# OUTILS INTERMEDIAIRES",
        "\tCe paragraphe peut être utile pour expliciter les autres outils utilisés dans la dataline :",
        "\t- 01. Convertisseur xlsx to csv",
        "\t- 02. Contrôle ...\n\n\n",

        "---------------------------------------------------------------------------------------------------------",
        "* Inputs :",
        "\tLe dossier input doit contenir uniquement des dossiers contenant eux les données. Chaque",
        "\tsous-dossier représente une version du jeu de données, par exemple par date...",
        "\t* sous-dossier ",
        "\t\t- data.csv \t\t base de données initiale",

        "\n* Outputs :",
        "\t- data_clean.xlsx \t mon fichier output",
        "---------------------------------------------------------------------------------------------------------",
        ""
    ])
    gi.pause()
    return input_folder

# -----------------------------------------------------------------------------
# Execution script
# -----------------------------------------------------------------------------


if __name__ == "__main__":
    ivars = {'input_folder': gi.get_input_folder()}
    print("test", ivars)
    # Overwrite presentation function for specific comment
    gi.presentation = presentation
    gi.menu_principal(ivars)
    # gi.presentation()
    # Start specific code for the project
    # main()

    # gi.presentation("test")

    # gi.presentation = presentation


# -----------------------------------------------------------------------------
# Execution script
# -----------------------------------------------------------------------------


# def main():


ivars = {"test":123}

def test():
    global ivars
    ivars["test"] = 999
    print(ivars)

test()
ivars


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


def test():
    print("test")
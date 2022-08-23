""" Generic FR interface

This file implement some useful functions for interactive Python terminal interface.
"""

# Copyright (c) MClavier (mathieu.clavier@outlook.com - https://github.com/claviermathieu).
# Distributed for personnal use

import os
from time import perf_counter


def ma():
    print("putain c'est le feu")


def ouiii(nom: str, *args, **kwargs):
    print(f"Bonjour {nom}")
    print(f"Bonjour {args}")
    print(f"Bonjour {kwargs}")


def ouiii2(nom: str, *args, **kwargs):
    print(f"Bonjour {nom}")
    print(f"Bonjour {args}")
    print(f"Bonjour {kwargs}")


# -----------------------------------------------------------------------------
# Inputs
# -----------------------------------------------------------------------------

def get_input_folder():
    """
    Get automatic input_folder to skip the input manager step.
    """
    if 'input' in os.listdir():
        folders = os.listdir('input')
        if folders:
            input_folder = folders[-1]
    else:
        input_folder = "N/A"
    return input_folder


# -----------------------------------------------------------------------------
# Inputs
# -----------------------------------------------------------------------------


def input_menu(n_choices):
    """
    Select input number between 1 and n_choices.
    """
    # Possible values
    choices = [str(i) for i in range(1, n_choices+1)] + [str(7), str(8), str(9)]
    # Ask the input
    choice = input("\n# Votre choix ? > ")
    # Control
    if choice not in choices:
        print("> Erreur de saisie : veuillez saisir un nombre entre 1 -", n_choices, "ou 7-9\n")
        choice = input_menu(n_choices=n_choices)
    return int(choice)


def input_int():
    select = input("> ")
    try:
        select = int(select)
    except ValueError():
        print("> Erreur de saisie : veuillez saisir un nombre entier.\n")
        input_int()

    return select


def input_float(lb, ub):
    """
    Select a float number between lb and ub.
    """
    select = input("> ")
    # Type control
    try:
        select = float(select)
    except ValueError():
        print("\n /!\\ --- Veuillez saisir un nombre entre", lb, "et", ub, " --- /!\\ \n")
        select = input_float(lb, ub)
    # Value control
    if not ((select >= lb) & (select <= ub)):
        print("> Erreur de saisie : veuillez saisir un nombre entre", lb, "et", ub, "\n")
        select = input_float(lb, ub)
    return float(select)


def input_confirm():
    """
    Confirm input
    """
    possibilities = ['o', 'n']
    choice = input("Confirmer (o/n) ? > ")
    # Vérification de la validité de l'input
    if choice not in possibilities:
        print("\n /!\\ --- Veuillez saisir un 'o' ou 'n' --- /!\\ ")
        choice = input_confirm()
    if choice == 'o':
        choice = 1
    else:
        choice = 0
    return choice

# -----------------------------------------------------------------------------
# Titles
# -----------------------------------------------------------------------------


def title(monTitre):
    """
    Formatage : nettoyage du terminal plus ajout du titre au format standard.
    """
    os.system("cls")
    n = len(monTitre)
    print("-"*(n+12))
    print("##### "+monTitre+" #####")
    print("-"*(n+12)+"\n")


def sub_title(monTitre):
    """
    Formatage : nettoyage du terminal plus ajout du titre au format standard.
    """
    print("\n#"+"-"*50)
    print("# " + monTitre + "\n")


def describe(my_list):
    # console = Console(theme=custom_theme)
    for i in range(len(my_list)):
        print(my_list[i])


# -----------------------------------------------------------------------------
# Menu
# -----------------------------------------------------------------------------


def menu_principal(ivars):
    title("Menu principal")
    describe([
        "Que souhaitez-vous faire ?",
        "\n\t1. Gestion des inputs (actuellement : " + ivars.get('input_folder') + ")",
        "\t2. Exécuter le programme",
        "\n\t7. Menu principal",
        "\t8. A propos",
        "\t9. Quitter\n\n"
    ])
    # Get choice
    choice = input_menu(2)

    if choice == 1:
        ivars = menu_input(ivars)
    elif choice == 2:
        pass
    elif choice == 7:
        ivars = menu_principal(ivars)
    elif choice == 8:
        pass
        # si.presentation(input_folder)
    elif choice == 9:
        quit()
    else:
        raise ValueError("Normally it cannot go here. Check code !")

    return ivars


def menu_input(ivars):
    # os.system('cls')
    title("Gestion des inputs")
    describe([
        "Que souhaitez-vous faire ?",
        "\n\t1. Visualiser les dossiers diponibles",
        "\t2. Modifier le dossier d'input sélectionné",
        "\t3. Visualiser les fichiers présents",
        "\t4. Ouvrir le dossier 'input'",
        "\t5. Ouvrir le dossier 'input/" + ivars['input_folder'] + "'",
        "\n\t7. Retour au menu principal",
        "\t8. A propos",
        "\t9. Quitter\n"
    ])
    print("#----------------------------------------------------------------------")
    print("# Dossier actuellement sélectionné :", ivars.get('input_folder'))
    print("#----------------------------------------------------------------------\n")
    # Get choice
    choice = input_menu(5)

    # Modify input folder
    if choice == 1:
        print("\nLes dossiers présents :", os.listdir('input'))
        temp_input = input("\nRenseignez le dossier d'inputs > ")
        if temp_input not in ["", ivars['input_folder']]:
            while temp_input not in os.listdir('input'):
                temp_input = input("\nRenseignez un dossier existant > ")
            ivars['input_folder'] = temp_input
        menu_input(ivars)
    # Visualize all files in input_folder
    elif choice == 3:
        files = os.listdir('input/' + ivars.get('input_folder'))
        print("\n--------------------------------------")
        print("Les fichiers présents sont:")
        for file in files:
            print("\t-", file)
        print("--------------------------------------")
        pause()
        menu_input(ivars)
    # Open input folder
    elif choice == 4:
        os.startfile('input')
        pause()
        menu_input(ivars)
    # Open sub-input folder
    elif choice == 5:
        os.startfile('input\\' + ivars.get('input_folder'))
        pause()
        menu_input(ivars)
    # Main menu
    elif choice == 7:
        menu_principal(ivars)
    # Program description
    elif choice == 8:
        presentation(ivars)
    # Quit
    elif choice == 9:
        if input_confirm():
            exit(0)
        else:
            menu_input(ivars)
    else:
        raise ValueError("Normally it cannot go here. Check code !")

    return ivars

# -----------------------------------------------------------------------------
# Others
# -----------------------------------------------------------------------------


def quit(ivars):
    if input_confirm():
        exit(0)
    else:
        menu_principal(ivars)


def pause():
    input("\n# Entrer pour continuer > ")
    print('')


def start(my_str):
    n = len(my_str)
    # Count number of '.' to add
    add_points = 50 - n
    print(my_str + '.'*add_points, end='')

    return perf_counter()


def end(t):
    print("OK/", (perf_counter() - t).seconds, "secondes")


def presentation(input_folder="Non initialisé"):
    title("A propos")
    describe([
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
    pause()
    return input_folder

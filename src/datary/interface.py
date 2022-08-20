""" Genereic FR interface

This file implement some useful functions for interactive Python terminal interface.
"""


def ouiii(nom: str, *args, **kwargs):
    print(f"Bonjour {nom}")
    print(f"Bonjour {args}")
    print(f"Bonjour {kwargs}")


def ouiii2(nom: str, *args, **kwargs):
    print(f"Bonjour {nom}")
    print(f"Bonjour {args}")
    print(f"Bonjour {kwargs}")


# Copyright (c) MClavier (mathieu.clavier@outlook.com - https://github.com/claviermathieu).
# Distributed for personnal use

ouiii(nom="Mathieu")

# ------------------------------------------------------------------------------------------------
# Principal module
# ------------------------------------------------------------------------------------------------

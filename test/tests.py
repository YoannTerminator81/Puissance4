'''
Tests Jeu Puissance4
'''
from app.main import *

def test_unitaire_1():
    assert(grille_valide()) == True

def test_unitaire_2():
    assert(jouer("A","2C")) == True
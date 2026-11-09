from app.livraison import frais_livraison
import pytest

def test_livraison_panier_ordinaire():
    # Arrange
    montant = 120
    # Act
    resultat = frais_livraison(montant)
    # Assert
    assert resultat == 25

def test_livraison_299():
    resultat = frais_livraison(299)
    assert resultat == 25


def test_livraison_300():
    resultat = frais_livraison(300)
    assert resultat == 0


def test_livraison_301():
    resultat = frais_livraison(301)
    assert resultat == 0

def test_livraison_zero():
    resultat = frais_livraison(0)
    assert resultat == 25


# corriger branche non converte
def test_livraison_montant_negatif():
    with pytest.raises(ValueError):
        frais_livraison(-10)
import pytest
from app.texte import nettoyer_texte
# Test paramétré
@pytest.mark.parametrize("entree, attendu", [
    ("  BONJOUR    monde  ", "bonjour monde"),
    (" déjà propre ", "déjà propre"),
    ("", ""),
    ("     ", ""),
    ("PYTHON", "python")
])
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu

def test_nettoyer_texte_nombre():
    with pytest.raises(TypeError):
        nettoyer_texte(123)

def test_nettoyer_texte_none():
    with pytest.raises(TypeError):
        nettoyer_texte(None)


def test_nettoyer_texte_deja_nettoye_ne_change_pas():
    texte = "  BONJOUR    monde  "

    premier = nettoyer_texte(texte)
    deuxieme = nettoyer_texte(premier)

    assert premier == deuxieme


    
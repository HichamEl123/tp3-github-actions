from unittest.mock import patch
from app.surveillance import surveiller
from app.notifications import envoyer_notification
import pytest

def test_surveillance_alerte():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.15)

        assert resultat == "alerte"
        notifier.assert_called_once_with("Taux eleve")

def test_surveillance_sans_alerte():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.05)

        assert resultat == "ok"
        notifier.assert_not_called()

def test_surveillance_seuil_exact():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.10)

        assert resultat == "ok"
        notifier.assert_not_called()

def test_surveillance_propage_erreur():
    with patch(
        "app.surveillance.envoyer_notification",
        side_effect=RuntimeError("Service non configure")
    ):
        with pytest.raises(RuntimeError):
            surveiller(0.15)


# corriger branche non converte
def test_envoyer_notification_non_configuree():
    with pytest.raises(RuntimeError):
        envoyer_notification("Bonjour")
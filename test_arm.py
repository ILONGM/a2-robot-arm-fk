import numpy as np
import pytest
from arm import Arm

def test_bras_valide():
    # construire Arm([1.0, 0.8]) et vérifier que .n == 2
    arm = Arm([1.0, 0.8])
    assert arm.n == 2

def test_longueur_negative():
    # with pytest.raises(ValueError): construire Arm([1.0, -0.5])
    with pytest.raises(ValueError):
        Arm([1.0, -0.5])

def test_bras_vide():
    # pareil avec Arm([])
    with pytest.raises(ValueError):
        Arm([])
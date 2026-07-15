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


def test_fk():
    # construire Arm([1.0, 0.1])
    arm = Arm([1.0, 1])
    # appeler fk([0.0, 0.0]) et vérifier que la liste retournée contient les bonnes poses
    poses = arm.fk([0.0, 0.0])
    print("Poses:", poses)
    assert len(poses) == 3
    assert np.allclose(poses[0].x, 0.0)
    assert np.allclose(poses[0].y, 0.0)
    assert np.allclose(poses[1].x, 1.0)
    assert np.allclose(poses[1].y, 0.0)
    assert np.allclose(poses[2].x, 2.0)
    assert np.allclose(poses[2].y, 0.0)
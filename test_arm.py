import numpy as np
import pytest
from arm import Arm
from transforms2d import normalize_angle

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


def test_bras_tendu():
    arm = Arm([1.0, 1])
    poses = arm.fk([0.0, 0.0])
    assert len(poses) == 3
    assert np.allclose(poses[0].x, 0.0)
    assert np.allclose(poses[0].y, 0.0)
    assert np.allclose(poses[1].x, 1.0)
    assert np.allclose(poses[1].y, 0.0)
    assert np.allclose(poses[2].x, 2.0)
    assert np.allclose(poses[2].y, 0.0)

def test_bras_plie():
    poses = Arm([1.0, 1.0]).fk([np.pi/2, np.pi/2])
    assert len(poses) == 3
    assert_pose_at(poses[1], 0.0, 1.0)
    assert_pose_at(poses[2], -1.0, 1.0, theta=np.pi)


def test_mauvais_nombre_angles():
    with pytest.raises(ValueError):
        Arm([1.0, 1.0]).fk([0.1])

def assert_pose_at(pose, x, y, theta=None):
    """Vérifie la position (et optionnellement l'orientation) d'une pose."""
    assert np.isclose(pose.x, x), f"x: attendu {x}, obtenu {pose.x}"
    assert np.isclose(pose.y, y), f"y: attendu {y}, obtenu {pose.y}"
    if theta is not None:
        diff = normalize_angle(pose.theta - theta)
        assert np.isclose(diff, 0.0), f"theta: attendu {theta}, obtenu {pose.theta}"

def test_end_effector_cablage():
    arm = Arm([1.0, 0.8])
    angles = [0.3, -0.7]
    assert np.allclose(arm.end_effector(angles).matrix, arm.fk(angles)[-1].matrix)
import numpy as np
from transforms2d import Pose2D


class Arm :
    def __init__(self,lengths):
        
        self.lengths = np.asarray(lengths, dtype=float)
        if self.lengths.ndim != 1:
            raise ValueError("lengths must be a flat sequence of numbers")
        if self.lengths.size == 0:
            raise ValueError("arm must have at least one segment")
        if not np.all(self.lengths > 0):
            raise ValueError("all lengths must be strictly positive")
        self.n = len(self.lengths)



    def fk(self, angles):
        """Cinématique directe.

        angles : séquence de self.n angles articulaires (rad).
        Retourne la liste des Pose2D de chaque articulation dans le
        repère monde : [base, articulation_1, ..., effecteur] — n+1 poses.
        """
        # 1. conversion + validation : asarray, puis vérifier len == self.n
        angles = np.asarray(angles, dtype=float)
        if len(angles) != self.n:
            raise ValueError("incompatible number of angles")
        # 2. pose courante = Pose2D identité (la base, à l'origine du monde)
        pose_courante = Pose2D(0.0, 0.0, 0.0)
        # 3. liste résultat, initialisée avec la base
        poses = [pose_courante]
        # 4. boucle sur (L, theta) appariés :
        #        pose courante = pose courante composée avec l'articulation (candidat B)
        #        ajouter à la liste
        for L, theta in zip(self.lengths, angles):
            pose_courante = poses[-1].compose(Pose2D(0.0, 0.0, theta)).compose(Pose2D(L, 0.0, 0.0))
            poses.append(pose_courante)
        # 5. return la liste
        return poses

    def end_effector(self, angles):
        return self.fk(angles)[-1]
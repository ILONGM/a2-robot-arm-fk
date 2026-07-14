import numpy as np


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



    #def fk(self, angles):
        # PROCHAINE ÉTAPE : valider len(angles) == self.n,
        # puis composer la chaîne de Pose2D et retourner la liste des poses


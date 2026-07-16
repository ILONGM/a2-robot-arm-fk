import numpy as np
import matplotlib.pyplot as plt
from arm import Arm        
ARM = Arm([1.0, 0.8])

xs = []
ys = []
for t1 in np.linspace(-np.pi, np.pi, 100):
    for t2 in np.linspace(-np.pi, np.pi, 100):
        end_effector_pose = ARM.end_effector([t1, t2])
        xs.append(end_effector_pose.x)
        ys.append(end_effector_pose.y)

plt.scatter(xs, ys, s=1)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Workspace of the 2-DOF Arm")
plt.axis("equal")
plt.show()
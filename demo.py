import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from arm import Arm

ARM = Arm([1.0, 0.8])

def draw_arms(ax, poses):
    xs = [pose.x for pose in poses]
    ys = [pose.y for pose in poses]
    ax.plot(xs, ys, "-o", linewidth=3, markersize=8)    

def update_graph(_):
    angles = [s1.val, s2.val]
    poses = ARM.fk(angles)
    ax.clear()
    ax.set_aspect('equal')
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.2, 2.2)
    ax.grid()
    draw_arms(ax, poses)     
    fig.canvas.draw_idle()


if __name__ == "__main__":
   
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.3, 0.8, 0.6])  
    s1_ax = fig.add_axes([0.1, 0.2, 0.8, 0.03])  
    s2_ax = fig.add_axes([0.1, 0.1, 0.8, 0.03]) 
    s1 = Slider(s1_ax, "theta1", -np.pi, np.pi, valinit=0.0)
    s2 = Slider(s2_ax, "theta2", -np.pi, np.pi, valinit=0.0)
    s1.on_changed(update_graph)
    s2.on_changed(update_graph)   
    
    update_graph(None)     
    plt.show()
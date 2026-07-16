# 2-DOF Planar Robot Arm — Forward Kinematics

Second project of a self-directed, project-based robotics curriculum (Project A2).
Builds directly on the `Pose2D` transform library from [Project A1](LIEN_VERS_REPO_A1).

![demo](demo.gif)

An interactive 2-link planar arm: drag the sliders to command joint angles and
watch the arm follow in real time. Forward kinematics is computed as a chain of
rigid transforms — each joint is "rotate by θᵢ, then translate along the link" —
composed with the `Pose2D` library built from scratch in A1.

## Workspace

![workspace](workspace.png)

Sampling all joint-angle combinations reveals the reachable workspace: an
annulus with outer radius L₁+L₂ and inner radius |L₁−L₂|. The white hole at
the center is physically unreachable — a real concept found on any industrial
arm datasheet, and the reason inverse kinematics (next project) must handle
unreachable targets gracefully.

## Concepts covered

- Forward kinematics (FK) of serial manipulators
- Joint space vs Cartesian space
- Joints as composed rigid transforms (rotate-then-translate ordering)
- Reachable workspace and its geometry
- Interactive Matplotlib widgets (sliders + callbacks)

## Code structure

- `arm.py` — `Arm` class: geometry stored at construction (immutable),
  joint angles passed per call, poses always derived — never cached.
  `fk(angles)` returns the full pose chain; `end_effector(angles)` the tip.
- `transforms2d.py` — the `Pose2D` library from Project A1 (vendored).
- `demo.py` — interactive slider demo.
- `workspace.py` — workspace sampling and plot.
- `test_arm.py` — pytest suite (construction guards, straight/bent-arm FK
  against hand-computed poses, angle-aware comparisons, wiring tests).

## Run it

```bash
pip3 install numpy matplotlib pytest
python3 demo.py         # interactive arm
python3 workspace.py    # workspace plot
pytest                  # tests
```

## What I learned

[2-3 sentences in your own words — strong candidates from this project:
the rotate-then-translate vs translate-then-rotate trap (candidate A vs B),
the class-vs-instance confusion (calling fk on the mold instead of a built arm),
and comparing angles via normalized difference rather than raw equality.]

## Roadmap context

Part of a progressive robotics learning path (simulation-first).
Next: [A3 — inverse kinematics: making the arm follow the mouse.]
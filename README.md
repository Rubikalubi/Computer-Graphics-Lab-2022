# Computer-Graphics-Lab-2022

Accompanying Repository for the Computer Graphics Lab at University of Bonn / Summer Term 2022

The goal of the Lab is to improve the runtime of this paper
https://4dqv.mpi-inf.mpg.de/phi-SfT/

Therefore we are implementing a solution in taichi.

### Run the cloth simulation

install dependencies:

```py
pip install - r requirements.txt
```

Make sure you have taichi version 0.9.2 installed, since there is a
segfault when running this under 1.0.0
I will open a github issues if i have time

to run the simulation just type

```py
python3 simulator.py
```

# L System Visualizer
Foundations of Computer Science Final Project: Visualizer of L-system fractals

## Usage
1. Clone the repository or download `lsystem.py` and `examples.py`.
2. In `main.py` of the clone repo, or in another `.py` file in the same directory as the downloaded files, import `examples.py` with:
```python
from examples import *
```
3. Choose a fractal, and display it with `[fractal].visualize(#)`, where `#` is the iteration number of the fractal. Fractals with nice step numbers are shown below. Available fractals are:
    - `Dragon` for the [dragon curve](https://en.wikipedia.org/wiki/Dragon_curve)
    - `Sierpinski` for the [Sierpiński triangle](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle)
    - `Koch` for the [Koch snowflake](https://en.wikipedia.org/wiki/Koch_snowflake)
    - `Plant` for a [fractal plant](https://en.wikipedia.org/wiki/L-system#Example_7:_fractal_plant)
    

### Dragon Curve
```python
Dragon().visualize(13)
```
![Dragon curve gif](/img/dragon.gif)
### Sierpiński triangle
```python
Sierpinski().visualize(7)
```
![Sierpiński triangle gif](/img/sierpinski.gif)
### Koch snowflake
```python
Koch().visualize(4)
```
![Koch snowflake gif](/img/koch.gif)
### Fractal plant
```python
Plant().visualize(6)
```
![Fractal plant gif](/img/plant.gif)
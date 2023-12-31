# L-system Visualizer

Foundations of Computer Science Final Project: Visualizer of L-system fractals

## Overview of L-systems

An [L-system, or Lindenmayer system](https://en.wikipedia.org/wiki/L-system) is a type of [rewrite system](https://en.wikipedia.org/wiki/Rewriting), that applies all rewrite rules simultaneously. As such, while standard rewrite systems could rewrite a symbol into multiple different strings, L-systems only rewrite a given symbol into a single specific string. As an example, an L-system with the following production rules:

``` math
A \rightarrow AB, B \rightarrow A
```

would rewrite `ABA` to `ABAAB`:

``` math
\begin{align*}
&A          & &B          & &A \\
&\downarrow & &\downarrow & &\downarrow \\
&AB         & &A          & &AB \\
\end{align*}
```

## L-systems for Generating Fractals

The string generated by an L-system can be used as the instructions for drawing a fractal. Take the [dragon curve](https://en.wikipedia.org/wiki/Dragon_curve) as an example. The L-system for the dragon curve has the following properties: - Start string: $F$ - Rewrite rules: $F \rightarrow F+G$, $G \rightarrow F-G$

Note that $+$ and $-$ are constant symbols, and rewrite to themselves.

Now, read through a generated string. When a given symbol is read, perform the listed action: - $F$: draw forward - $G$: draw forward - $+$: turn left 90° - $-$: turn right 90°

Each fractal has its own set of L-system rules and corresponding drawing rules that can be seen [here](https://en.wikipedia.org/wiki/L-system#Examples_of_L-systems).

## Usage

1.  Clone the repository or download `lsystem.py` and `examples.py`.
2.  In `main.py` of the clone repo, or in another `.py` file in the same directory as the downloaded files, import `examples.py` with:

``` python
from examples import *
```

3.  Choose a fractal, and display it with `[fractal].visualize(#)`, where `#` is the iteration number of the fractal. Fractals with nice step numbers are shown below. Available fractals are:
    -   `Dragon` for the [dragon curve](https://en.wikipedia.org/wiki/Dragon_curve)
    -   `Sierpinski` for the [Sierpiński triangle](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle)
    -   `Koch` for the [Koch snowflake](https://en.wikipedia.org/wiki/Koch_snowflake)
    -   `Plant` for a [fractal plant](https://en.wikipedia.org/wiki/L-system#Example_7:_fractal_plant)

### Dragon Curve

``` python
Dragon().visualize(13)
```

![Dragon curve gif](/img/dragon.gif) \### Sierpiński triangle

``` python
Sierpinski().visualize(7)
```

![Sierpiński triangle gif](/img/sierpinski.gif) \### Koch snowflake

``` python
Koch().visualize(4)
```

![Koch snowflake gif](/img/koch.gif) \### Fractal plant

``` python
Plant().visualize(6)
```

![Fractal plant gif](/img/plant.gif) \### Quadratic gosper

``` python
QuadGosper().visualize(3)
```

![Quadratic Gosper gif](/img/quadgosper.gif) \### Fractal plant - Weed Vairant

``` python
Weed().visualize(7)
```

![Weed gif](/img/weed.gif)
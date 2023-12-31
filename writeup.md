# L-system Visualizer

By Ben Kim and Ian Lum

## Table of Contents

-   [Overview](#overview)
-   [How do L-systems Work?](#how-do-l-systems-work)
    -   [How do L-systems Draw Fractals](#how-do-l-systems-draw-fractals)
    -   [Other Fractals](#other-fractals)
        -   [Sierpiński Triangle](#sierpiński-triangle)
        -   [Koch Snowflake](#koch-snowflake)
        -   [Fractal Plant](#fractal-plant)
-   [Code Overview](#code-overview)
    -   [About `lsystem.py`](#about-lsystempy)
        -   [The `Lsystem` Class](#the-lsystem-class)
        -   [The `VisualLSystem` Class](#the-visuallsystem-class)
    -   [About `examples.py`](#about-examplespy)

## Overview {#overview}

An [L-system, or Lindenmayer system](https://en.wikipedia.org/wiki/L-system) is a type of [rewrite system](https://en.wikipedia.org/wiki/Rewriting), that applies all rewrite rules simultaneously. The strings generated by L-systems can be used to draw fractals, with each character in the string encoding an instruction: draw forward, turn left, turn right, and more. The recursive nature of L-systems makes them a good pairing with fractals, with each iteration of an L-system representing a greater depth fractal.

## How do L-systems Work? {#how-do-l-systems-work}

As mentioned above, L-systems apply all rewrite rules simultaneously. As such, while standard rewrite systems could rewrite a symbol into multiple different strings, L-systems only rewrite a given symbol into a single specific string. As an example, an L-system with the following production rules: - A → AB - B → A

would rewrite ABA to ABAAB:

| A   | B   | A   |
|-----|-----|-----|
| AB  | A   | AB  |

### How do L-systems Draw Fractals? {#how-do-l-systems-draw-fractals}

The string generated by an L-system can be used as the instructions for drawing a fractal. Take the [dragon curve](https://en.wikipedia.org/wiki/Dragon_curve) as an example. The L-system for the dragon curve has the following properties: - Start string: F - Rewrite rules: - F → F+G - G → F-G

Note that + and - are constant symbols, and rewrite to themselves.

Now, read through a generated string. When a given symbol is read, perform the listed action: - F: draw forward - G: draw forward - +: turn left 90° - -: turn right 90°

### Other Fractals {#other-fractals}

#### [Sierpiński Triangle](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle) {#sierpiński-triangle}

The curve approximation of the Sierpiński triangle can be drawn with the following L-system: - Start string: A - Rewrite rules: - A → B−A−B - B → A+B+A

Drawing rules: - A: draw forward - B: draw forward - +: turn left 60° - -: turn right 60°

#### [Koch snowflake](https://en.wikipedia.org/wiki/Koch_snowflake) {#koch-snowflake}

The Koch snowflake can be drawn with the following L-system: - Start string: F++F++F - Rewrite rule: F → F-F++F-F

Drawing rules: - F: draw forward - +: turn left 60° - -: turn right 60°

#### [Fractal Plant](https://en.wikipedia.org/wiki/L-system#Example_7:_fractal_plant) {#fractal-plant}

A fractal plant can be drawn with the following L-system: - Start string: X - Rewrite rules: - X → F+\[\[X\]-X\]-F\[-FX\]+X - F → FF

Drawing rules: - F: draw forward - X: do nothing - +: turn left 25° - -: turn right 25° - \[ : log the current position and angle - \] : set position and angle to the last logged values, then delete those values (in otherwords, treat the log as a stack and pop the stack)

This fractal introduces a new idea of logging position and angle, then returning to the logged position and angle. Most literature will refer to this as the stack of positions and angles. As such, popping the stack means to return to the position and angle at the top of the stack, then deleting said values.

## Code Overview {#code-overview}

Our codebase is split into two main files: `lystem.py` where we defined L-system abstract base classes, and `examples.py` where we implemented various fractals.

### About `lsystem.py`

#### The `Lsystem` class {#the-lsystem-class}

As mentioned above, this file defines the abstract base class `Lsystem`. `Lsystem` has two attributes: - `Lsystem.start`: A string representing the initial state of the system. - `Lsystem.productions`: A dictionary representing the production rules, mapping a character to the output string.

`Lsystem` has one method: `Lsystem.generate`. `Lsystem.generate` takes an integer `steps` as input and outputs the string generated by the L-system after `steps` iterations.

`Lsystem.generate` is a recursive function where the base case is `steps == 0`, in which case it returns `Lsystem.start`. The recursive case applies all rules from `Lsystem.productions` to the result from `Lsystem.generate(steps - 1)`.

Example implementation of the [algae L-system](https://en.wikipedia.org/wiki/L-system#Example_1:_algae):

``` python
class Algae(Lsystem):
    start = "A"
    productions = {"A": "AB", "B": "A"}

print(Algae().generate(3))
```

Output:

```         
>>> ABAAB
```

#### The `VisualLSystem` class {#the-visuallsystem-class}

The `VisualLsystem` class is a child class of `Lsystem`, and is used to visualize L-system fractals. `VisualLsystem` has two methods that `Lsystem` doesn't have: - `init_turtle`: A method that initializes the Python Turtle library, which is used to create the drawings. The argument `show_drawing` is a boolean that controls whether the turtle will play the drawing animation or just have the drawing appaear immediately. `speed_multiplier` is an optional argument that can be used to speed up particularly complex fractals, e.g. fractal plant. - `visualize`: An abstract method that will be implemented on a case by case basis for children of the class, but is meant to use Turtle to draw the fractal after the number of steps defined by an argument.

Example implementation of the [dragon curve L-system](https://en.wikipedia.org/wiki/L-system#Example_6:_dragon_curve):

``` python
class Dragon(VisualLSystem):
    start = "F"
    productions = {"F": "F+G", "G": "F-G"}

    def visualize(self, steps, size=3, show_drawing=True):
        turt = self.init_turtle(show_drawing)

        for char in self.generate(steps):
            match char:
                case "F" | "G":
                    turt.forward(size)
                case "+":
                    turt.left(90)
                case "-":
                    turt.right(90)

        turtle.mainloop()
        turtle.update()

Dragon().visualize(13)
```

Output:

![dragon curve gif](/img/dragon.gif)

Looking at the implementation of `Dragon.visualize`, it takes three arguments (other than `self`): - `steps`: An integer representing the number of steps to generate, an then visualize. - `size`: An optional integer, representing the size of each "forward" segment in the drawing, defaults to `3`. - `show_drawing`: An optional boolean, representing whether the drawing animation is shown or not, defaults to `true`.

The function starts by instantiating Turtle with:

``` python
turt = self.init_turtle(show_drawing)
```

Then, it loops character by character through the generated string, matching different characters to different turtle actions, as defined by the L-system's drawing rules:

``` python
for char in self.generate(steps):
    match char:
        case "F" | "G":
            turt.forward(size)
        case "+":
            turt.left(90)
        case "-":
            turt.right(90)
```

The function ends by calling the following Turtle functions, which keep the drawing window displayed and shows the final fractal if `show_drawing` was set to `True`.

``` python
turtle.mainloop()
turtle.update()
```

### About `examples.py`

In `examples.py`, we've implemented various fractals as L-systems, following the construction and drawing rules listed in the [Other Fractals](#other-fractals) section. Below are the lines of code to draw the various fractals.

``` python
Dragon().visualize(13)
```

Output:

![dragon curve gif](/img/dragon.gif)

``` python
Sierpinski().visualize(7)
```

Output:

![sierpinski gif](/img/sierpinski.gif)

``` python
Koch().visualize(4)
```

Output:

![koch gif](/img/koch.gif)

``` python
Plant().visualize(6)
```

Output:

![plant gif](/img/plant.gif)

``` python
QuadGosper().visualize(3)
```

Output:

![quadratic gosper gif](/img/quadgosper.gif){width="487"}

``` python
Weed().visualize(7)
```

Output:

![weed gif](/img/weed.gif){width="107"}
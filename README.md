Approximates the value of pi using Monte Carlo Simulation.

**What is Monte Carlo Simulation?**
Monte Carlo Simulations work by modeling probability of different outcomes, by using random sampling to calculate multiple outcomes. Random sampling means chosing selecting subsets of data in which every selection has a equally likely chance of occuring. In short, 'brute-forces' an estimate through tons of simulations.

**How does it estimate pi?**
Suppose you draw a square centered around unit circle, with length 2r. Let O be the area of the circle and S the area of the square. Such that the ratio between O and S is pi/4. So in fact pi = ( 4 * O ) / 4. We use this ratio to help us estimate pi. By simulating random points in our square, the ratio of points in the circle to the total points should be equally pi/4. So in running however many simulations of points we want, we estimate pi to be 4 * Points In the circle / Total Points.

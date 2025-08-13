# uq-edx-test
### This repository contains code for the UQ EdX course on fractals.

## Chaos Game Implementation
1.Define a polygon and determine its vertices.

2.Randomly choose an initial point inside the polygon.

3.In each iteration, randomly select one vertex of the polygon.

4.Move the current point to the midpoint between the current point and the selected vertex.

5.Repeat 

After many iterations, the points will converge to a fractal pattern.

### Using PyTorch in the Chaos Game

* **Vectorized processing**: The code does not use a for loop to compute each point individually; instead, it processes a tensor containing NUM_POINTS points all at once.

* **Tensor operations**: The core computation points = (points + chosen_vertices) / 2.0 is a vectorized operation, which PyTorch can distribute across multiple GPU cores for parallel execution.

* **GPU acceleration**: All computations are performed on the GPU, significantly reducing computation time.

**Analysis**: 
The code uses PyTorch's tensor operations to efficiently compute the points of the fractal, leveraging GPU acceleration for performance.
The fractal dimension of the Sierpinski triangle is log(3)/log(2), approximately 1.585. By analyzing the generated pattern, we can see that it has a self-similar structure, where each smaller triangle resembles the overall shape.
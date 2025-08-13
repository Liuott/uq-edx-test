#chans game
import torch
import matplotlib.pyplot as plt
import numpy as np

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def chaos_game_pytorch(vertices, num_points, iterations):

    #on the device
    vertices = vertices.to(device)
    #initialize random points
    points = torch.rand(num_points, 2, device=device)

    #initialize storage for all points
    all_points = torch.zeros(num_points * iterations, 2, device=device)

    #perform the chaos game iterations
    for i in range(iterations):

        random_indices = torch.randint(0, len(vertices), (num_points,), device=device)
        chosen_vertices = vertices[random_indices]

        #update points by averaging with chosen vertices
        points = (points + chosen_vertices) / 2.0

        #store the points
        all_points[i*num_points:(i+1)*num_points] = points

    return all_points.cpu()

#define the vertices of the Sierpinski triangle
triangle_vertices = torch.tensor([
    [0.0, 1.0],
    [-1.0, -1.0],
    [1.0, -1.0]
], dtype=torch.float32)

#parameters
NUM_POINTS = 1000  
ITERATIONS = 100  

#run the chaos game
fractal_points = chaos_game_pytorch(triangle_vertices, NUM_POINTS, ITERATIONS)

#plot the  fractal
fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(fractal_points[:, 0], fractal_points[:, 1], s=0.1, color='blue')
ax.set_title('Sierpinski Triangle (Chaos Game)')
ax.set_aspect('equal', adjustable='box')
plt.show()
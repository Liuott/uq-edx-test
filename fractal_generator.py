#chans game
import torch
import matplotlib.pyplot as plt
import numpy as np

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def chaos_game_pytorch(vertices, num_points, iterations):


    vertices = vertices.to(device)

    points = torch.rand(num_points, 2, device=device)

    all_points = torch.zeros(num_points * iterations, 2, device=device)

    for i in range(iterations):

        random_indices = torch.randint(0, len(vertices), (num_points,), device=device)
        chosen_vertices = vertices[random_indices]

        points = (points + chosen_vertices) / 2.0

        all_points[i*num_points:(i+1)*num_points] = points

    return all_points.cpu()

triangle_vertices = torch.tensor([
    [0.0, 1.0],
    [-1.0, -1.0],
    [1.0, -1.0]
], dtype=torch.float32)


NUM_POINTS = 1000  
ITERATIONS = 100  


fractal_points = chaos_game_pytorch(triangle_vertices, NUM_POINTS, ITERATIONS)


fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(fractal_points[:, 0], fractal_points[:, 1], s=0.1, color='blue')
ax.set_title('Sierpinski Triangle (Chaos Game)')
ax.set_aspect('equal', adjustable='box')
plt.savefig('sierpinski.png')
@@ -2,6 +2,7 @@
import matplotlib.patches as patches
from constraint import Problem    

problem = Problem()
# 1. Setup the Regions and Adjacency
regions = ['WA', 'NA', 'SA', 'QLD', 'NSW']
neighbors = {
@@ -13,32 +14,40 @@
}
#Contsraint Satisfaction Logic :
colors_map = {'Blue': '#3498db', 'Red': '#e74c3c', 'Green': '#2ecc71'}
assignment = {}
colors_list = list(colors_map.keys())
problem.addVariables(regions, colors_list)

for region, adj_list in neighbours.items():
    for neighbour in adj_list:
        problem.addConstraint(lambda c1, c2: c1 != c2, (region,neighbour))

sloution = problem.getSolution()

if solution is None:
    raise RuntimeError("No Ssolution found - Check constraints !")

assignment = {region: colors_map[color_name] for region, color_name in solution.items()}

for region in regions:
    for name, hex_code in colors_map.items():
        if all(assignment.get(n) != hex_code for n in neighbors[region]):
            assignment[region] = hex_code
            break

#Plotting the oval map
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-1.5, 1.5)

#Creating the reigions
#Labelling the reigions
pos = {'WA': (-1.3, 0), 'NA': (0, 0.6), 'SA': (0, -0.4), 'QLD': (1.3, 0.5), 'NSW': (1.3, -0.6)}

# Creating a clipping path for the oval shape
oval = patches.Ellipse((0, 0), 4, 2.2, color='none')
ax.add_patch(oval)

# Plotting the regions with assigned colors
for reg, p in pos.items():
    color = assignment[reg]
    rect_coords = {'WA': [-2, -1.1, 1.2, 2.2], 'NA': [-0.8, 0.1, 1.6, 1], 
rect_coords = {'WA': [-2, -1.1, 1.2, 2.2], 'NA': [-0.8, 0.1, 1.6, 1], 
                   'SA': [-0.8, -1.1, 1.6, 1.2], 'QLD': [0.8, 0, 1.2, 1.1], 
                   'NSW': [0.8, -1.1, 1.2, 1.1]}
    

for reg, p in pos.items():
    color = assigment[reg]
    r = rect_coords[reg]
    patch = patches.Rectangle((r[0], r[1]), r[2], r[3], facecolor=color, edgecolor='white', clip_path=oval, clip_on=True)
    ax.add_patch(patch)
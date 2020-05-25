import numpy as np
import paraconsistent

# Classes de dados
classes = np.array([
    [[0.87, 0.27, 0.88, 0.75], [0.39, 0.24, 0.19, 0.55], [0.18, 0.79, 0.04, 0.35], [0.94, 0.61, 0.03, 0.06]],
    [[0.74, 0.78, 0.25, 0.27], [0.17, 0.94, 0.89, 0.09], [0.45, 0.29, 0.27, 0.21], [0.32, 0.91, 0.68, 0.78]],
    [[0.17, 0.02, 0.76, 0.90], [0.06, 0.02, 0.47, 0.38], [0.32, 0.13, 0.51, 0.96], [0.28, 0.24, 0.44, 0.17]]
])

alpha = paraconsistent.alpha(classes)
beta = paraconsistent.beta(classes)

# Ponto G1
assurance = paraconsistent.assurance(alpha, beta)
# Ponto G1
contradiction = paraconsistent.contradiction(alpha, beta)

falsehood = paraconsistent.falsehood(assurance, contradiction)
truth = paraconsistent.truth(assurance, contradiction)
indefinition = paraconsistent.indefinition(assurance, contradiction)
ambiguity = paraconsistent.ambiguity(assurance, contradiction)

print(f'Alfa: {alpha:.3f}')
print(f'Beta: {beta:.3f}\n')

print(f'P=(G1, G2) = ({assurance:.3f}, {contradiction:.3f})\n')

print(f'Distância de P para o ponto (-1, 0) = {falsehood:.3f}')
print(f'Distância de P para o ponto (1, 0) = {truth:.3f}')
print(f'Distância de P para o ponto (0, -1) = {indefinition:.3f}')
print(f'Distância de P para o ponto (0, 1) = {ambiguity:.3f}')

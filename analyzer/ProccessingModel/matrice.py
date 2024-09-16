import matplotlib.pyplot as plt
import numpy as np

# Données de la matrice de risques
risques = [
    "Charge excessive du navigateur",
    "Temps de téléchargement long",
    "Problèmes de compatibilité avec les systèmes d'exploitation plus anciens",
    "Exposition des données",
    "Adoption par les utilisateurs",
    "Interruption des services lors du déploiement",
    "Collecte incomplète des besoins",
    "Limites technologiques des solutions OCR",
    "Résistance des utilisateurs",
    "Dépassement des coûts",
    "Non-respect des délais",
    "Failles de sécurité"
]

probabilites = ["Très faible", "Faible", "Moyenne", "Élevée", "Très élevée"]
impacts = ["Très faible", "Faible", "Moyen", "Élevé", "Très élevé"]

# Scores de probabilité et d'impact
probabilite_scores = [3, 4, 2, 1, 3, 2, 3, 4, 3, 2, 3, 2]
impact_scores = [3, 2, 3, 5, 4, 4, 4, 5, 3, 4, 4, 4]

# Création de la matrice de risques
matrice = np.zeros((5, 5))
for i in range(len(risques)):
    matrice[5 - probabilite_scores[i], impact_scores[i] - 1] += 1

# Création de la figure
fig, ax = plt.subplots()

# Ajout de couleurs pour chaque niveau de risque
cmap = plt.cm.RdYlGn_r
heatmap = ax.imshow(matrice, cmap=cmap, vmin=0, vmax=5)

# Ajout des étiquettes de texte
for i in range(5):
    for j in range(5):
        ax.text(j, i, int(matrice[i, j]), ha='center', va='center', color='black')

# Configuration des axes
ax.set_xticks(np.arange(len(impacts)))
ax.set_yticks(np.arange(len(probabilites)))
ax.set_xticklabels(impacts)
ax.set_yticklabels(probabilites[::-1])
plt.xlabel('Gravité')
plt.ylabel('Probabilité')
plt.title('Matrice de Risques')

# Ajout de la légende
cbar = ax.figure.colorbar(heatmap, ax=ax, cmap=cmap)
cbar.set_label('Nombre de Risques')

# Affichage de la figure
plt.show()

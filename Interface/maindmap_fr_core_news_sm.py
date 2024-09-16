import spacy
import graphviz

# Cargar el modelo en francés de Spacy
nlp = spacy.load('fr_core_news_sm')

# Texto de ejemplo
text = "Je suis contente de t'avoir choisi"

# Procesar el texto
doc = nlp(text)

# Crear un nuevo grafo
dot = graphviz.Digraph(comment='Funcionamiento del Modelo fr_core_news_sm')

# Nodo principal
dot.node('A', 'Texto Original')
dot.node('B', text)

dot.edge('A', 'B')

# Tokenización
tokens = [token.text for token in doc]
dot.node('C', 'Tokenización')
for i, token in enumerate(tokens):
    dot.node(f'C{i}', token)
    dot.edge('C', f'C{i}')

# Etiquetas POS
pos_tags = [(token.text, token.pos_) for token in doc]
dot.node('D', 'Etiquetas POS')
for i, (token_text, pos) in enumerate(pos_tags):
    dot.node(f'D{i}', f'{token_text} ({pos})')
    dot.edge('D', f'D{i}')

# Entidades nombradas
entities = [(ent.text, ent.label_) for ent in doc.ents]
dot.node('E', 'Entidades Nombradas')
for i, (ent_text, label) in enumerate(entities):
    dot.node(f'E{i}', f'{ent_text} ({label})')
    dot.edge('E', f'E{i}')

# Lematización
lemmas = [token.lemma_ for token in doc]
dot.node('F', 'Lematización')
for i, lemma in enumerate(lemmas):
    dot.node(f'F{i}', lemma)
    dot.edge('F', f'F{i}')

# Stopwords eliminadas
filtered_tokens = [token.text for token in doc if not token.is_stop]
dot.node('G', 'Stopwords Eliminadas')
for i, token in enumerate(filtered_tokens):
    dot.node(f'G{i}', token)
    dot.edge('G', f'G{i}')

# Conectar nodos de cada fase al texto original
dot.edge('B', 'C')
dot.edge('B', 'D')
dot.edge('B', 'E')
dot.edge('B', 'F')
dot.edge('B', 'G')

# Renderizar el grafo en formato PNG
output_path = dot.render('funcionamiento_modelo_fr_core_news_sm', format='png')

print(f"Mapa mental guardado en: {output_path}")
print(dot.source)

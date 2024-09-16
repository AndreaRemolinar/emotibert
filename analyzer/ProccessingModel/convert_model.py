import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Directorio base del modelo
model_base_dir = 'D:/Python Code/Project/analyzer/models'
pt_model_path = f'{model_base_dir}/my_t5_style_transfer_best_model.pt'
hf_model_dir = f'{model_base_dir}/my_t5_style_transfer_model'

# Cargar el modelo de PyTorch
pt_model = torch.load(pt_model_path)

# Inicializar el modelo de Hugging Face
hf_model = T5ForConditionalGeneration.from_pretrained('t5-base')  # Asegúrate de ajustar esto según tu variante de T5

# Cargar los pesos del modelo de PyTorch en el modelo de Hugging Face
hf_model.load_state_dict(pt_model)

# Guardar el modelo en el formato de Hugging Face
hf_model.save_pretrained(hf_model_dir)

# Guardar el tokenizador en el formato de Hugging Face
tokenizer = T5Tokenizer.from_pretrained('t5-base')  # Asegúrate de usar el tokenizer correspondiente
tokenizer.save_pretrained(hf_model_dir)

print(f'Model and tokenizer saved to {hf_model_dir}')

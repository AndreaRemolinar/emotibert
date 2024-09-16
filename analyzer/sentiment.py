import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer, CamembertTokenizer, CamembertForSequenceClassification
import os

import torch
from transformers import CamembertForSequenceClassification, CamembertTokenizer

# Directorio base del modelo
model_base_dir = 'D:/Python Code/Project/analyzer/models'
model_path = f'{model_base_dir}/path_to_save_model'

def predict_sentiment(text):
    try:
        # Cargar el modelo de Camembert desde los pesos de TensorFlow
        model = CamembertForSequenceClassification.from_pretrained(model_path, from_tf=True)
        tokenizer = CamembertTokenizer.from_pretrained(model_path)

        inputs = tokenizer(text, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = logits.argmax().item()

        # Mapear la clase predicha a la etiqueta correspondiente
        labels = ["😤 frustration", "😞 tristesse", "😡 colere", "😄 joie", "😑 neutre"]
        predicted_label = labels[predicted_class]
        return predicted_label
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# Código para convertir y guardar el modelo T5
def convert_and_save_t5_model():
    # Directorio base del modelo
    model_base_dir = 'D:/Python Code/Project/analyzer/models'
    pt_model_path = f'{model_base_dir}/my_t5_style_transfer_best_model.pt'
    hf_model_dir = f'{model_base_dir}/my_t5_style_transfer_model'

    # Cargar el state_dict del modelo de PyTorch
    pt_state_dict = torch.load(pt_model_path)

    # Inicializar el modelo de PyTorch
    pt_model = T5ForConditionalGeneration.from_pretrained('t5-base')

    # Cargar los pesos del state_dict en el modelo de PyTorch
    pt_model.load_state_dict(pt_state_dict)

    # Guardar el modelo en el formato de Hugging Face
    pt_model.save_pretrained(hf_model_dir)

    # Guardar el tokenizador en el formato de Hugging Face
    tokenizer = T5Tokenizer.from_pretrained('t5-base')
    tokenizer.save_pretrained(hf_model_dir)

    print(f'Model and tokenizer saved to {hf_model_dir}')

# Ejecutar la conversión del modelo si este archivo se ejecuta directamente
if __name__ == "__main__":
    convert_and_save_t5_model()

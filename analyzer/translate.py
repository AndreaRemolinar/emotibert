from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def translate_sentiment(input_text, target_sentiment):
    logger.info(f"Translating sentiment: '{input_text.strip()}' to '{target_sentiment}'")
    
    try:
        # directorio del modelo
        model_base_dir = 'D:/Python Code/Project/analyzer/models'
        model_dir = os.path.join(model_base_dir, 'my_t5_style_transfer_model')

        # Cargar el modelo y el tokenizador
        tokenizer = T5Tokenizer.from_pretrained(model_dir)
        model = T5ForConditionalGeneration.from_pretrained(model_dir)

        # Preparar la entrada del modelo
        input_text = f'translate sentiment to {target_sentiment}: {input_text.strip()}'
        inputs = tokenizer.encode_plus(input_text, return_tensors='pt')

        # Generar la salida con beam search para mejorar la calidad de la traducción
        with torch.no_grad():
            outputs = model.generate(inputs['input_ids'], max_length=50, num_beams=5, early_stopping=True)

        # Decodificar la salida
        output_text = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        logger.info(f"Translated output: '{output_text}'")
        return output_text

    except Exception as e:
        logger.error(f"Error translating sentiment: {e}")
        return False

if __name__ == "__main__":
    input_text = "ravi de mon cadeau"
    target_sentiment = "neutre"
    result = translate_sentiment(input_text, target_sentiment)
    print(result)

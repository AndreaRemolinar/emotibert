from transformers import TFCamembertForSequenceClassification, CamembertTokenizer, CamembertConfig

model_name_or_path = "path_to_save_model"
model = TFCamembertForSequenceClassification.from_pretrained(model_name_or_path)
config = CamembertConfig.from_pretrained(model_name_or_path)

# Acceder a la ubicación del archivo config.json
config_path = config.config_file
print("Ruta del archivo config.json:", config_path)

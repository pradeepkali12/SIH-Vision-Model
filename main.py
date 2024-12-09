# from doctr.io import DocumentFile
# from doctr.models import kie_predictor

# # Model
# model = kie_predictor(det_arch='fast_base', reco_arch='crnn_vgg16_bn', pretrained=True)
# # PDF
# doc = DocumentFile.from_images("asserts/img.jpeg")
# # Analyze
# result = model(doc)

# predictions = result.pages[0].predictions
# for class_name in predictions.keys():
#     list_predictions = predictions[class_name]
#     for prediction in list_predictions:
#         print(f"Prediction for {class_name}: {prediction}")


import os
from groq import Groq
import base64
from dotenv import load_dotenv

load_dotenv()

GORQ_API_KEY = os.environ.get("GORQ_API_KEY")

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "./asserts/img.jpeg"

# Getting the base64 string
base64_image = encode_image(image_path)

client = Groq(api_key=GORQ_API_KEY)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Extract all details in the document image"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
    model="llama-3.2-11b-vision-preview",
)

print(chat_completion.choices[0].message.content)
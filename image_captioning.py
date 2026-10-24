from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load the processor and model
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

# Open the image
image = Image.open("test image 3.jpg")

# Process image
inputs = processor(image, return_tensors="pt")

# Generate caption
output = model.generate(**inputs)

# Convert output to text
caption = processor.decode(output[0], skip_special_tokens=True)

print("Caption:", caption)
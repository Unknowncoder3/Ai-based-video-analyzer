import torch
from transformers import BlipProcessor, BlipForConditionalGeneration


def load_blip(model_name: str, device: str):
    processor = BlipProcessor.from_pretrained(model_name)
    model = BlipForConditionalGeneration.from_pretrained(model_name).to(device)
    return processor, model


def caption_image(processor, model, image, device: str, max_length: int = 32) -> str:
    inputs = processor(images=image, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=max_length)
    return processor.decode(outputs[0], skip_special_tokens=True)

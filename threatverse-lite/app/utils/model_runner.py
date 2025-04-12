from transformers import AutoTokenizer, AutoModelForSeq2SeqLM,AutoModelForCausalLM
import torch
import json

# Load flan-t5-base model (small, CPU-friendly)
# model_name = "google/flan-t5-base"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

model_name = "NousResearch/DeepHermes-3-Llama-3-3B-Preview"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def extract_cti_entities(text_chunk: str) -> dict:
    prompt = f"""
Extract the following threat intelligence elements from the TEXT:
  TEXT: {text_chunk}

           after sucessful extraction produce
           the output **ONLY IN JSON format** with keys: ttps, cves, iocs, actors

"""
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=200)

    raw_output = tokenizer.decode(outputs[0], skip_special_tokens=True)

    try:
        result = json.loads(raw_output)
    except json.JSONDecodeError:
        result = {"error": "Model response not in valid JSON format", "raw_output": raw_output}
    return result,model_name

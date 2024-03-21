from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "google/gemma-2b"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

input_text = "Tell me about yourself?"
input_ids = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(**input_ids, max_new_tokens=50)
print(tokenizer.decode(outputs[0]))

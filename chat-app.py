import time
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "google/gemma-2b"

tokenizer = []
model = []


def load_model_and_tokenizer():
	global tokenizer, model
	tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
	model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)


def prompt():
	input_text = input(">> ")
	return input_text


def get_input_tokens(input_text):
	input_ids = tokenizer(input_text, return_tensors="pt")
	return input_ids


def generate_output(input_ids):
	outputs = model.generate(**input_ids, max_new_tokens=50)
	return outputs


def get_decoded_output(model_outputs):
	output_text = tokenizer.decode(model_outputs[0])
	return output_text


def run():
	load_model_and_tokenizer()
	while True:
		input_text = prompt()
		start_pipeline_ts = time.process_time()
		input_ids = get_input_tokens(input_text)
		model_outputs = generate_output(input_ids)
		output_text = get_decoded_output(model_outputs)
		end_pipeline_ts = time.process_time()
		print(f'Elapsed time: {end_pipeline_ts - start_pipeline_ts}')
		print(output_text)


run()

# All things Gemma, on a CPU!

## Setup
1. Sign up on Kaggle for [access to Gemma-2b](https://www.kaggle.com/models/google/gemma)
2. Get [Hugging Face Access Token](https://huggingface.co/google/gemma-2b#usage) and store it on local `$huggingface-cli login`
3. Install HF Transformers library and [PyTorch library](https://pytorch.org/get-started/locally/)
4. If using `WSL2`, add a `.wslconfig` file at `C:\\Users\\username\` with below config to ensure sufficient resources (below is for my system with total 16GB RAM and 8 processors)
```sh
[wsl2]
memory=12GB
processors=8
```
5. You are all set! Clone this repo and run `$python gemma-1.py` to see the first output of Gemma model on your local machine!

## Comments
1. Gemma takes up to 9GB for the prompt in `gemma-1.py` file.

## References
1. [Setting `max_new_tokens` for longer completions](https://discuss.huggingface.co/t/confused-about-max-length-and-max-new-tokens/30892/6)



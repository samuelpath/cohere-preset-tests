import cohere
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from presets import presets_data
from config import api_key, minimum_cosine_similarity

co = cohere.Client(api_key)

class Preset:
    def __init__(self, name, max_tokens, temperature, stop_sequences, prompt, expected_output):
        self.name = name
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.stop_sequences = stop_sequences
        self.prompt = prompt
        self.expected_output = expected_output

def get_current_output(prompt, max_tokens, temperature, stop_sequences):
    """
    Generate text using the Cohere API.
    """
    try:
        response = co.generate(
            model='command',
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            k=0,
            stop_sequences=stop_sequences,
            return_likelihoods='NONE')
        return response.generations[0].text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def calculate_similarity(text1, text2):
    """
    Calculate cosine similarity between embeddings of two texts.
    """
    text1_embeddings = np.array(co.embed([text1]).embeddings)
    text2_embeddings = np.array(co.embed([text2]).embeddings)
    return cosine_similarity(text1_embeddings, text2_embeddings)[0][0]

presets_data = [Preset(**preset) for preset in presets_data]

for preset in presets_data:
    current_output = get_current_output(preset.prompt, preset.max_tokens, preset.temperature, preset.stop_sequences)

    if current_output is not None:
        similarity = calculate_similarity(preset.expected_output, current_output)
        is_pass = similarity >= minimum_cosine_similarity
        print(f"{'✅' if is_pass else '❌'}, Preset Name: {preset.name}, Coside Similarity: {similarity:.2f}")

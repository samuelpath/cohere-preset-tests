import cohere
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from presets import presets_data
from config import api_key, minimum_cosine_similarity

co = cohere.Client(api_key)

def get_current_output(input_text, max_tokens, temperature, stop_sequences):
    """
    Generate text using the Cohere API.
    """
    try:
        response = co.generate(
            model='command',
            prompt=input_text,
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

for preset in presets_data:
    preset_name = preset["preset_name"]
    max_tokens = preset["max_tokens"]
    temperature = preset["temperature"]
    stop_sequences = preset["stop_sequences"]
    input_value = preset["input"]
    expected_output = preset["expected_output"]
    current_output = get_current_output(input_value, max_tokens, temperature, stop_sequences)

    if current_output is not None:
        similarity = calculate_similarity(expected_output, current_output)
        is_pass = similarity >= minimum_cosine_similarity
        print(f"{'✅' if is_pass else '❌'}, Preset Name: {preset_name}, Coside Similarity: {similarity:.2f}")

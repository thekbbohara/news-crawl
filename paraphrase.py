import google.generativeai as genai
from system import paraphrase_instruction


async def paraphrase_content(news_json_str, api_key):
    """
    Paraphrases the content of news articles from a given JSON string.

    Parameters:
    - json_str (str): A string containing a JSON list of articles with "title" and "content".
    - api_key (str): The API key for Google Generative AI.

    Returns:
    - str: A JSON string containing the paraphrased list of articles.
    """

    # Configure the AI model
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=paraphrase_instruction,
        generation_config={
            "temperature": 0.8,
            "top_p": 0.5,
            "top_k": 1,
            "max_output_tokens": 8189,
            "response_mime_type": "application/json",
        },
    )

    # Generate the response
    response = model.generate_content(news_json_str)

    # Return the paraphrased JSON as a string
    print(response.text)
    return response.text


# Example usage:
# json_data = """[{"title": "Some Article", "content": "Original content here..."}]"""
# result = paraphrase_content(json_data, "your-api-key-here")
# print(result)

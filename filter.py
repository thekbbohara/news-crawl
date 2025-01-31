import google.generativeai as genai
from system import stock_filter_instruction


async def filter_financial_news(recent_news_str: str, api_key: str):
    """
    Filters financial news from a given JSON string.

    Parameters:
    - json_str (str): A string containing a JSON list of news articles.
    - api_key (str): The API key for Google Generative AI.

    Returns:
    - str: A JSON string containing the filtered list of articles.
    """

    # Configure the AI model
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=stock_filter_instruction,
        generation_config={
            "temperature": 0.0,  # Lower temperature reduces randomness
            "top_p": 0.1,  # Focuses on high-probability outputs (lowers variability)
            "top_k": 1,  # Chooses the single most probable response
            "max_output_tokens": 8189,  # Ensures full response
            "response_mime_type": "application/json",  # Forces structured JSON response
        },
    )

    # Generate the response
    response = model.generate_content(recent_news_str)

    # Return the filtered JSON as a string
    return response.text


# Example usage:
# recent_news = """[{"title": "Some Financial News", "url": "/news1", "date": "Jan 29, 2025"}]"""
# result = filter_financial_news(recent_news, "your-api-key-here")
# print(result)

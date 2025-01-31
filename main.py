import asyncio
from recent import get_recent_news
from filter import filter_financial_news
from paraphrase import paraphrase_content
from news import crawl_news
import json
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


async def main(site):
    recent_news = await get_recent_news(site)
    if not recent_news:  # Ensure we got news
        print("No recent news found.")
        return

    # Convert the list to a JSON string before passing it to the function
    recent_news_str = json.dumps(recent_news, ensure_ascii=False)
    print("recent_news", recent_news_str)
    filtered_news_res = await filter_financial_news(
        f"{recent_news_str}", GEMINI_API_KEY
    )
    print("filtered_news", filtered_news_res)
    # Convert JSON string to Python list
    filtered_news = json.loads(filtered_news_res)

    # Step 3: Crawl full news articles concurrently
    crawl_tasks = [crawl_news(site, news["url"]) for news in filtered_news]
    crawled_news = await asyncio.gather(*crawl_tasks)
    print("crawled_news", crawled_news)

    # Step 4: Paraphrase the crawled news concurrently
    paraphrase_tasks = [
        paraphrase_content(article, GEMINI_API_KEY) for article in crawled_news
    ]
    paraphrased_results = await asyncio.gather(*paraphrase_tasks)

    # Print results
    for result in paraphrased_results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main("merolagani.com"))

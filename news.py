import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
from schema_config import news_schema


async def crawl_news(site: str, news_url: str):
    """
    Fetches and extracts news content from a given website asynchronously.

    Parameters:
    - site (str): The website domain (e.g., "merolagani.com").
    - news_url (str): The specific news article URL path.

    Returns:
    - dict: Extracted content from the news article.
    """

    extraction_strategy = JsonCssExtractionStrategy(news_schema[site], verbose=True)

    config = CrawlerRunConfig(
        exclude_external_images=True,
        extraction_strategy=extraction_strategy,
        cache_mode=CacheMode.BYPASS,
    )

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=f"https://{site}{news_url}",
            config=config,
        )
        return result.extracted_content  # Return extracted data


# Example: Running directly
if __name__ == "__main__":
    extracted_content = asyncio.run(crawl_news("merolagani.com", "/some-news-url"))
    print(extracted_content)

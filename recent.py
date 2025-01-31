import asyncio
from datetime import datetime
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
from schema_config import recent_schema
import json

last_post_dates = {"merolagani.com": "Jan 29, 2025 12:56 PM"}


def getLastPost(site: str) -> str:
    return last_post_dates.get(
        site, "Jan 01, 2000 12:00 AM"
    )  # Default to a very old date


def updateLastPost(site: str, date: str):
    last_post_dates[site] = date


async def get_recent_news(site):
    # print(recent_schema)
    extraction_strategy = JsonCssExtractionStrategy(recent_schema[site], verbose=True)

    last_post_date_str = getLastPost("merolagani.com")
    date_format = "%b %d, %Y %I:%M %p"

    try:
        last_post_date = datetime.strptime(last_post_date_str, date_format)
    except ValueError as e:
        print(f"Error parsing last post date: {e}")
        return

    config = CrawlerRunConfig(
        css_selector="div.container",
        exclude_external_images=True,
        extraction_strategy=extraction_strategy,
        cache_mode=CacheMode.BYPASS,
    )

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=f"https://{site}",
            config=config,
        )

        recent_posts = result.extracted_content
        # print("extracted_content", recent_posts)
        try:
            parsed_data = json.loads(result.extracted_content)  # Attempt to parse JSON
            # print("Successfully parsed JSON:", parsed_data)
            recent_posts = parsed_data
        except json.JSONDecodeError:
            print("❌ Error: Extracted content is not valid JSON.")
        # Ensure the extracted content is a list
        if not isinstance(recent_posts, list):
            print(
                "❌ Error: Extracted content is not a list. Instead, got:",
                type(recent_posts),
            )
            return

        # Filter posts that are newer than the last recorded post
        filtered_posts = []
        for post in recent_posts:
            if not isinstance(post, dict):
                print(f"Skipping unexpected data format: {post}")
                continue
            if "date" not in post:
                print(f"Skipping post with missing date: {post}")
                continue

            try:
                post_date = datetime.strptime(post["date"], date_format)
                if post_date > last_post_date:
                    # print("new post found", post_date, last_post_date)
                    filtered_posts.append(post)

            except ValueError as e:
                print(f"Error parsing date {post['date']}: {e}")

        # If new posts exist, update the last post date
        if filtered_posts:
            newest_post_date = max(
                datetime.strptime(post["date"], date_format) for post in filtered_posts
            )
            updateLastPost(site, newest_post_date.strftime(date_format))
        # print(filtered_posts)
        return filtered_posts


if __name__ == "__main__":
    asyncio.run(get_recent_news("merolagani.com"))

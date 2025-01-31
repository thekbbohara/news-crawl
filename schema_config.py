news_schema = {
    "merolagani.com": {
        "name": "Articles",
        "baseSelector": "div.container",
        "fields": [
            {"name": "title", "selector": "h4", "type": "text"},
            {
                "name": "content",
                "selector": "#aspnetForm > div.container > div.row > div:nth-child(7) > div.media-news.media-news-lg.alt",
                "type": "text",
            },
        ],
    }
}
recent_schema = {
    "merolagani.com": {
        "name": "Recent News",
        "baseSelector": "table#ctl00_ContentPlaceHolder1_tblRecentNews > tbody > tr",
        "fields": [
            {
                "name": "title",
                "selector": "h4.headlineTitle a",
                "type": "text",
            },
            {
                "name": "url",
                "selector": "h4.headlineTitle a",
                "type": "attribute",
                "attribute": "href",
            },
            {
                "name": "date",
                "selector": "h4.headlineTitle span.media-label-recent-news",
                "type": "text",
            },
        ],
    }
}

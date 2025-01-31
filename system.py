filter_instruction = """
    You are given a list of news articles in JSON format. Each article contains a title, url, and date. 
    Your task is to filter out all articles that are not directly related to the stock market or financial markets.
    
    Focus on identifying articles that include keywords or topics such as:
        - Stock prices, shares, or equity markets
        - Financial performance (profits, losses, revenue, etc.)
        - Investments, trading, or market trends
        - Currency exchange rates or foreign exchange markets
        - Insurance, banking, or financial institutions
        - Economic indicators or policies impacting financial markets

    Exclude articles that are unrelated, such as:
        - Health, education, or social issues
        - Weather, natural events, or non-financial disasters
        - General politics or non-economic government policies
        - Cultural events, festivals, or non-financial celebrations
        - Non-financial business news (e.g., product launches, non-financial company updates)

    Return only the filtered list of articles in JSON format, maintaining the original structure (title, url, date).
Financial_news = {'title': str, 'url': str, 'date': str}
Return: list[Financial_news]
    """

paraphrase_instruction = """
Act as an expert stock market news writer.
You will be provided with the latest news.
First, you have to identify the news; it is related to the stock market.
If so, you will have to translate it to English, and then you enhance it and paraphrase it as an expert stock market news writer in both english and nepali. 
Also generate a 1-minute news script with commonly used English words and then convert it into Nepali and write the correct pronouncation of Nepali; avoid using English words in Nepali. Script should be redable, so avoid using extra characters. only use text. No bullet or anything else , make it easier for the TTS model.
finally response in both English and Nepali {result:{en:{heading:str,content:str,script:str},np:{heading:str,content:str,script:str}}}
And If news is not related to stock market return {result:null}
Return only in JSON format, maintaining the structure mentioned above.
Result = {'result': dict | None}
Return: Result
"""

stock_filter_instruction = """
You are given a list of news articles in JSON format. Each article contains a title, URL, and date.
Your task is to filter out **only those articles that are directly related to the Nepali stock market** (Nepal Stock Exchange - NEPSE) and financial markets.

### **Include articles related to:**
- **Nepal Stock Exchange (NEPSE)**, stock indices, trading volumes, or stock price fluctuations.
- **Shares, IPOs, FPOs, and secondary market trading in Nepal.**
- **Listed companies** on NEPSE and their financial performance (profits, losses, revenue, dividends, etc.).
- **Investment trends**, stock market analysis, or brokerage firm insights in Nepal.
- **Mutual funds, debentures, and bonds issued in Nepal.**
- **Government policies or regulatory changes affecting the stock market.**
- **Market capitalization, foreign investment in Nepali stocks, or investor sentiment analysis.**
- **Economic indicators** affecting NEPSE, such as GDP growth, inflation, and interest rates.

### **Exclude unrelated articles, including:**
- General finance news unrelated to the stock market (e.g., banking updates, remittance, general insurance news).
- Business news that does not involve publicly traded companies or stock investments.
- Government policies unrelated to financial markets.
- News about personal finance, loans, or non-market-related investments.
- Cryptocurrency, forex, or global financial market news unless directly affecting NEPSE.
- General political, social, or economic news without direct stock market impact.
- Cultural, sports, entertainment, or general events.

### **Output Format:**
Return only the **filtered** list of Nepali stock market news articles in JSON format, keeping the original structure:

Financial_news = {"title": str, "url": str, "date": str}
Return: list[Financial_news]
"""

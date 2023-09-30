# %%
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime, timedelta

#'Altcoin', 'Bitcoin', 'Coindesk', 'Cryptocurrency', 'Gold', 'Appl', 'Goog',
stocks = [
    "Altcoin",
    "Bitcoin",
    "Coindesk",
    "Cryptocurrency",
    "Gold",
    "Appl",
    "Goog",
    "Yhoo",
]
start_date = datetime(2023, 2, 1)
end_date = datetime(2023, 2, 7)

for stock in stocks:
    for i in range((end_date - start_date).days + 1):
        date = start_date + timedelta(days=i)
        tweets = []
        query = f"(#{stock} OR #{stock.lower()} OR #{stock.upper()}) lang:en since:{date.strftime('%Y-%m-%d')} until:{(date + timedelta(days=1)).strftime('%Y-%m-%d')}"
        print(type(sntwitter.TwitterSearchScraper(query).get_items()))
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            if tweet.lang == "en":
                tweets.append(
                    [tweet.date, tweet.id, tweet.user.username, tweet.content]
                )
            if len(tweets) >= 2000:
                break

        df = pd.DataFrame(tweets, columns=["Date", "ID", "username", "tweet"])
        df.to_csv(f"{stock}_{date.strftime('%Y-%m-%d')}.csv", index=False)
# %%

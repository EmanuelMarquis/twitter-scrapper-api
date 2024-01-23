import json, os, asyncio
from enum import Enum
from scrapfly import ScrapeConfig, ScrapflyClient

__SCRAPFLY = ScrapflyClient(key=os.getenv("SCRAPFLY_API_KEY"))

__ScrapeType = Enum("ScrapeType", ["Undefined", "UserProfile", "UserTweet"])

# TODO: finish data filtering function

def __filterData(data: dict, keysToFilter: tuple, keysToSubFilter: dict = None):

    filtered: dict = data.fromkeys(keysToFilter)
    for key, val in filtered.items():
        if keysToSubFilter and key in keysToSubFilter.keys():
            filtered[key] = __filterData(data[key], keysToSubFilter[key])
            continue
        filtered[key] = data[key]
    return filtered

def __setScrapeTypeConfig(SCRAPE_TYPE) -> dict:
    if SCRAPE_TYPE == __ScrapeType.UserProfile:
        return {
            "searchFor" : "UserBy", 
            "waitForSelector" : "[data-testid='primaryColumn']",
            "data" : "user"
        }
    elif SCRAPE_TYPE == __ScrapeType.UserTweet:
        return {
            "searchFor" : "TweetResultByRestId",
            "waitForSelector" : "[data-testid='tweet']",
            "data" : "tweetResult"
        }

    elif SCRAPE_TYPE == None or SCRAPE_TYPE == __ScrapeType.Undefined:
        raise Exception("SCRAPE_TYPE undefined!")
    else:
        raise Exception("SCRAPE_TYPE invalid value!")

async def __scrape(URL: str, SCRAPE_TYPE):
    
    SCRAPE_TYPE_CONFIG = __setScrapeTypeConfig(SCRAPE_TYPE)

    res = await __SCRAPFLY.async_scrape(ScrapeConfig(
            URL,
            asp=True,
            render_js=True, # headless browser
            wait_for_selector=SCRAPE_TYPE_CONFIG["waitForSelector"] # wait page loading
        ))
        
    xhrCalls = res.scrape_result["browser_data"]["xhr_call"]
    call = [f for f in xhrCalls if SCRAPE_TYPE_CONFIG["searchFor"] in f["url"]]

    for xhr in call:
        if not xhr["response"]:
            continue
        data = json.loads(xhr["response"]["body"])
        scrappedData : dict = data["data"][SCRAPE_TYPE_CONFIG["data"]]["result"]

        filteredData = {
            "legacy": __filterData(
                scrappedData.get("legacy"),
                ("name", "screen_name","description",
                 "profile_image_url_https","profile_banner_url","pinned_tweet_ids_str",
                 "location", "followers_count", "favourites_count", "entities")
            ),
            "professional": __filterData(
                scrappedData.get("professional"),
                ("category", "professional_type"),
                # {"category": ("name")}
            )
        }

        return filteredData

def scrape_profile(username):
    URL = "https://twitter.com/" + username
    return asyncio.run(__scrape(URL, __ScrapeType.UserProfile))

def scrape_tweet_from(username, tweetID):
    URL = "https://twitter.com/" + username + "/status/" + tweetID
    return asyncio.run(__scrape(URL, __ScrapeType.UserTweet))
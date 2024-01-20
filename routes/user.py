import flask, json, asyncio, os
from scrapfly import ScrapeConfig, ScrapflyClient
def init(app: flask.app.Flask, ):
    SCRAPFLY = ScrapflyClient(key=os.getenv("SCRAPFLY_API_KEY"))
    async def scrape_profile(username):
        URL = "https://twitter.com/" + username
        res = await SCRAPFLY.async_scrape(ScrapeConfig(
            URL,
            asp=True,
            render_js=True, # headless browser
            wait_for_selector="[data-testid='primaryColumn']" # wait page loading
        ))

        xhrCalls = res.scrape_result["browser_data"]["xhr_call"]
        call = [f for f in xhrCalls if "UserBy" in f["url"]]

        for xhr in call:
            if not xhr["response"]:
                continue
            data = json.loads(xhr["response"]["body"])
            return data["data"]["user"]["result"]
    @app.route("/user/<string:username>")
    def user(username):
        return asyncio.run(scrape_profile(username))
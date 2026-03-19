import scrapy
import hashlib
import os

class AppSpider(scrapy.Spider):
    name = "app_spider"
    allowed_domains = ["f-droid.org"]
    start_urls = ["https://f-droid.org/packages/"]

    def parse(self, response):
        apps = response.xpath("//a[contains(@href, '/packages/')]/@href").getall()

        print("Found apps:", len(apps))

        for link in apps[:10]:
            yield response.follow(link, self.parse_app)

    def parse_app(self, response):
        app_name = response.css("h3::text").get().strip()

        print("Visiting app:", app_name)

        apk_link = response.xpath(
    "//a[contains(@href, '/repo/') and contains(@href, '.apk')]/@href").get()

        print("APK LINK:", apk_link)

        if apk_link:
            yield response.follow(
                apk_link,
                self.download_apk,
                meta={"app_name": app_name}
            )

    def download_apk(self, response):
        app_name = response.meta.get("app_name", "unknown_app")

        os.makedirs("apk_files", exist_ok=True)

        safe_name = app_name.replace(" ", "_").replace("/", "_").replace("\n", "").strip()
        file_name = f"{safe_name}.apk"
        path = f"apk_files/{file_name}"

        print("Saving APK:", path)

        with open(path, "wb") as f:
            f.write(response.body)

        app_hash = hashlib.sha256(response.body).hexdigest()

        yield {
            "app_name": app_name,
            "apk_path": path,
            "app_hash": app_hash
        }
import asyncio

from kwork import Kwork


async def main() -> None:
    async with Kwork(login="login", password="password") as api:
        await api.web_login(url_to_redirect="/exchange")

        result = await api.web.create_exchange_offer(
            want_id=2920487,
            offer_type="custom",
            description="Добрый день! Готов предложить услугу.",
            kwork_duration=1,
            kwork_price=500,
            kwork_name="Мое предложение",
            user_agent=(
                "Mozilla/5.0 (iPhone; CPU iPhone OS 18_6_2 like Mac OS X) "
                "AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 "
                "KworkMobileAppWebView AppBundleVersion/4.5.0"
            ),
        )

        print("HTTP:", result["status"])
        if result["json"] is not None:
            print("JSON:", result["json"])
        else:
            print("TEXT:", result["text"][:500])


if __name__ == "__main__":
    asyncio.run(main())


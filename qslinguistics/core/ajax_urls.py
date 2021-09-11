import json
import aiohttp
from typing import Awaitable
from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass
class AJAXURL:
    """
    The AJAXURL object finds the AJAX URL that stores data.
    """

    year: int

    def find_ajax_url(self, soup: BeautifulSoup) -> str:
        """The find_url method finds the AJAX URL.

        Args:
            soup (BeautifulSoup): the BeautifulSoup object

        Returns:
            a string (i.e. the URL)
        """
        jsonified_ajax = json.loads(
            soup.find("script", {"type": "application/json"}).string
        )
        return jsonified_ajax["qs_rankings_datatables"]["rank_url"]

    async def get_ajax_url(self) -> Awaitable[str]:
        """The get_ajax_url method gets the AJAX URL.

        Returns:
            a str (i.e. the URL)
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://www.topuniversities.com/university-rankings/university-subject-rankings/{self.year}/linguistics"
            ) as response:
                html = await response.text()
                soup = BeautifulSoup(html, "lxml")
                url = self.find_ajax_url(soup)
                return url

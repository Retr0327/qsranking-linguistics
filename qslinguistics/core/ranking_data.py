import json
import asyncio
import aiohttp
from typing import Awaitable
from .ajax_urls import AJAXURL
from dataclasses import dataclass


@dataclass
class QSRankingData:
    """
    The QSRankingData object downloads the data from the AJAX URL.
    """

    year: int

    def __post_init__(self) -> None:
        self.url = asyncio.run(AJAXURL(self.year).get_ajax_url())

    async def download_data(self) -> Awaitable[list[dict[str, str]]]:
        """The download_data method downloads the data.

        Returns:
            a list: [
                {
                    'core_id': '410',
                    'country': 'United States',
                    'city': 'Cambridge',
                    'guide': '',
                    'nid': '294850',
                    'title': '<div class="td-wrap"><a href="/universities/massachusetts-institute-technology-mit" class="uni-link">Massachusetts Institute of Technology (MIT) </a></div>',
                    'logo': '/sites/default/files/massachusetts-institute-of-technology-mit_410_small.jpg',
                    'score': '97.9',
                    'rank_display': '1',
                    'region': 'North America',
                    'stars': '',
                    'recm': '0--'
                },
                ...
            ]
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                html = await response.read()

            data = json.loads(html)
            institute_info_list = data.get("data")
            return institute_info_list

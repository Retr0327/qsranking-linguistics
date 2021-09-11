import asyncio
import numpy as np
import pandas as pd
from dataclasses import dataclass
from .core import QSRankingData


# --------------------------------------------------------------------
# helper functions


def convert_file(conversion_type: str, table: pd.DataFrame, year: int):
    """The convert_file method converts the table frame to different serialization formats (here, csv and pickle).
    Args:
        conversion_type (str): format name
        table (pd.DataFrame): the Dataframe
        year (int): the year that the user wants to check
    Returns:
        a csv or pickle file based on the parameter `conversion_type`
    """
    factories = {
        "csv": table.to_csv(
            f"./{year}_linguistics_ranking.csv", index=False, encoding="utf_8_sig"
        ),
        "pickle": table.to_pickle(f"./{year}_linguistics_ranking.pkl"),
    }

    return factories[conversion_type]


# --------------------------------------------------------------------
# public interface


@dataclass
class LinguisticsRanking:
    """
    The LinguisticsRanking object downloads the universities or institutes of linguistics ranking data as a table.
    """
    year: int

    def __post_init__(self) -> None:
        self.ranking_data = asyncio.run(QSRankingData(self.year).download_data())

    def download_table(self) -> pd.DataFrame:
        """The download_table method downloads the table from `ranking_data`.

        Returns:
            a DataFrame 
        """
        df = pd.DataFrame(self.ranking_data)
        df.title = df.title.str.replace("<[^<]+?>", "", regex=True)
        df["year"] = self.year
        df["actual_rank"] = np.arange(1, len(df) + 1)
        df = df.drop(["core_id", "guide", "nid", "logo", "stars", "recm"], axis=1)
        df = df[
            [
                "year",
                "rank_display",
                "title",
                "score",
                "city",
                "country",
                "region",
                "actual_rank",
            ]
        ]
        return df

    def to_csv(self):
        return convert_file(
            conversion_type="csv",
            table=self.download_table(),
            year=self.year,
        )

    def to_pickle(self):
        return convert_file(
            conversion_type="pickle",
            table=self.download_table(),
            year=self.year,
        )

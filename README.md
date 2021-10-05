# **QS Rankings for Linguisticse**
Downloading the ranking data as a table from the website [QS World University Rankings for Linguistics](https://www.topuniversities.com/university-rankings/university-subject-rankings/2021/linguistics). 

> The website does not have information before 2013, so please search from 2013 onwards. 

## **Documentation**

### 1. Import the package.

``` python
from qslinguistics import LinguisticsRanking
```
If you are working on Jupyter Notebook, you need to add two additional code lines (before or after importing the `LinguisticsRanking` package):

``` python
import nest_asyncio
nest_asyncio.apply()
```
Since `LinguisticsRanking` is built with Python asynchronous frameworks, it cannot run properly on Jupyter Notebook due to the fact that Jupyter [(IPython ≥ 7.0)](https://blog.jupyter.org/ipython-7-0-async-repl-a35ce050f7f7) is already running an event loop. Visit [this question](https://stackoverflow.com/questions/56154176/runtimeerror-asyncio-run-cannot-be-called-from-a-running-event-loop) asked in StackOverflow for further details.

 
### 2. Fill in and instantiate `LinguisticsRanking` class: 
* `year`: the year that you want to find

``` python
qs_ling = LinguisticsRanking(2021)
```

### 3. Download the table: 
Download the table by using the `.download_table()` method:
```python
qs_ling.download_table()
```
This prints:
| year |  rank_display |title | score | city | country | region  | actual_rank |
|----|----|----|----|----|----|----|----|
| 2021 | 1 | Massachusetts Institute of Technology (MIT) | 97.9 | Cambridge | United States | North America	 | 1 | 
| ... | ...| ...| ...| ...| ...| ...| ...| ... | ... |

### 4. Download the table as CSV: 
Download the table as a CSV file by calling the `.to_csv()` method:
```python
qs_ling.to_csv()
```

### 5. Download the table as Pickle: 
Download the table as a CSV file by calling the `.to_pickle()` method:
```python
qs_ling.to_pickle()
```
---
## **Tidbit: Generating tables for multiple years**

### 1. in .py file:
```python
import asyncio 
from qslinguistics import LinguisticsRanking


async def main(year):
    return LinguisticsRanking(year).download_table()


async def download_multiple():      # download table from 2013 to 2021
    return await asyncio.gather(*[main(year) for year in range(2013, 2022)])


asyncio.run(download_multiple())

```
### 2. in .ipynb file:
```python
import asyncio
import nest_asyncio
from qslinguistics import LinguisticsRanking


nest_asyncio.apply()


async def main(year):
    return LinguisticsRanking(year).download_table()


async def download_multiple():      # download table from 2013 to 2021
    return await asyncio.gather(*[main(year) for year in range(2013, 2022)])


asyncio.run(download_multiple())

```

## Contact Me
If you have any suggestion or question, please do not hesitate to email me at r07142010@g.ntu.edu.tw

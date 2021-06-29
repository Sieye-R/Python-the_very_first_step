import pandas as pd
import numpy as np
import requests
from logger import logger

def popular_movie():
    html_url = "https://www.the-numbers.com/market/2021/top-grossing-movies"
    r = requests.get(html_url)
    logger.debug(f"get the web address {html_url}")
    top_movie = pd.read_html(r.text, header=0)
    movie = top_movie[0]
    logger.debug(f"get the data")
    movie.set_index('Rank', inplace=True)
    logger.debug("data is cleaned to be read")
    return movie.drop(['Total Gross of All Movies', 'Total Tickets Sold'], axis = 0)
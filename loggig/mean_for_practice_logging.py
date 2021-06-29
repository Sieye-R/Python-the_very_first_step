import pandas
from fetch_for_practice_logging import popular_movie
from logger import logger

def get_mean(ticker):
    logger.warning("about to download data.")
    movie = popular_movie()  
    logger.warning("data is downloaded.")
    return movie[ticker].mean()
import pandas as pd
from fetch_for_practice_logging import popular_movie
from logger import logger

def refinement(genre):
    logger.debug("is about to download data.")
    movie = popular_movie()
    logger.debug("data is downloaded.")
    genre = movie[(movie['Genre'] == genre)]
    logger.warning("will show the data of the requested genre.")
    return pd.DataFrame(genre['Movie'])
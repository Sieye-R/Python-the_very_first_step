import sys
from logger import logger

from mean_for_practice_logging import get_mean

if __name__ == "__main__":
    try:
        ticker = sys.argv[1]
        logger.warning("ready to show the average.")
        print(f"The average {sys.argv[1]} for movie in 2021 is {get_mean(sys.argv[1])}.")
    
    except BaseException:
        logger.error("Error happened!", exc_info=True)
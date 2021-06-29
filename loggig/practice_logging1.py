import sys
from logger import logger

from refinement_for_practice_logging import refinement

if __name__ == "__main__":
    genre = sys.argv[1]
    logger.warning("Everything is going well.")
    print(f"Popular {sys.argv[1]} movie in 2021 with the total ranks are {refinement(sys.argv[1])}.")
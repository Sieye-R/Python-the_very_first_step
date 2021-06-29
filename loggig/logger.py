import logging

logger = logging.getLogger(__name__)

# handlers to determine the destination of log messages
stream_handler = logging.StreamHandler() # command line interpreter
file_handler = logging.FileHandler("debug_genre.log") # file

# set levels
logger.setLevel(logging.DEBUG) # all levels
stream_handler.setLevel(logging.WARNING) # only serious three levels on command line interpreter
file_handler.setLevel(logging.DEBUG) # details in the file

# formatters to determine the layouts of log messages
fmt_stream = '%(levelname)s %(asctime)s %(message)s'
fmt_file = '%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s'

stream_formatter = logging.Formatter(fmt_stream)
file_formatter = logging.Formatter(fmt_file)

# here we hook everything together
stream_handler.setFormatter(stream_formatter)
file_handler.setFormatter(file_formatter)

# add handlers from the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
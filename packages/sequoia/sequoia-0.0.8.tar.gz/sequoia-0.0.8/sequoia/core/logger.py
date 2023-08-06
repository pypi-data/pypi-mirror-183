import logging

logger = logging.getLogger('worker')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

yellow = '\x1b[38;5;226m'
blue = '\x1b[38;5;39m'
reset = '\x1b[0m'

formatter = logging.Formatter(
    f'{blue}%(asctime)s - %(name)s - %(levelname)s: {yellow} %(message)s{reset}'
)
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

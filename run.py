from modules.isrunning import isrunning
from time import sleep
from modules.input import accept_match
import logging
from modules.gui import rendergui

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S', level=logging.DEBUG)


while False:
    if accept_match() == -1:
        logging.debug('Match accepting failed, retrying...')
        sleep(3)
        continue

rendergui()
from modules.isrunning import isrunning
from time import sleep
from modules.input import accept_match
import logging
from modules.gui import rendergui

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S', level=logging.DEBUG)

rendergui()
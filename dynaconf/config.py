'''
Created on 25.09.2024

@author: sholzhauer
'''

import logging

logger = logging.getLogger("dynconf.custom")

class AHIDConfig:
    '''
    classdocs
    '''
    
    evaluate = True


    def __init__(self, params):
        '''
        Constructor
        '''
        logger.warning("Use AHIDConfig...")
        
        
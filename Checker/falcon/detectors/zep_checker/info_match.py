
from falcon.detectors.zep_checker.configs import model, infothreshold
import logging.config
def preprocess(doc):
    return doc.lower().split()
def similarity(s1,s2):


    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'loggers': {
            'gensim': {
                'level': 'ERROR',
            },
            'Falcon':{
                'level': 'INFO',
            },
            'Detectors':{
                'level': 'INFO',
            },
            'Printers':{
                'level': 'INFO',
            }
            }
        }

    logging.config.dictConfig(logging_config)

    distance = model.wmdistance(preprocess(s1), preprocess(s2))
    # return False
    if 1-distance >= infothreshold:
        return True
    else:
        return False

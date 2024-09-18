from mapper import *
import pandas as pd
import os

def get_output(labels, task: str):
    if task == 'triplet':
        pass
    elif task == 'quadruplet':
        return get_quadruplet_output(labels)
    elif task == 'pair':
        return labels

def get_triplet_io(triplet):
    pass

def get_quadruplet_output(labels):

    def get_quadruplet(quad):
        ac, at, sp, ot = quad.split(',')

        if (at == 'null') and (ot == 'null'):
            completion = f"{mapping_category(os.environ['domain'], ac)} thì {sp}"
        else:
            at = 'nó' if at == 'null' else at
            ot = f'#{SENTIMENT_ENG2VIET[sp]}' if ot == 'null' else ot

            completion = f"{mapping_category(os.environ['domain'], ac)} thì {sp} bởi vì {at} thì {ot}"
        
        return completion
    
    quads = labels.strip().strip('{}')
    quadruplets = [] 
    for quad in quads:
        quadruplet = get_quadruplet(quad)
        quadruplets.append(quadruplet)
        output_text = ' và '.join(quadruplets)
    
        return output_text


def read_data(domain, task):
    if task == 'pair':
        df_train = pd.read_csv(f'../data/Pair/{domain}/Train.csv')
        df_test = pd.read_csv(f'../data/Pair/{domain}/Test.csv')
    elif task == 'triplet':
        pass
    elif task == 'quadruplet':
        df_train = pd.read_csv(f'../data/Quadruplet/{domain}/Train.csv')
        df_test = pd.read_csv(f'../data/Quadruplet/{domain}/Test.csv')
    
    return df_train, df_test


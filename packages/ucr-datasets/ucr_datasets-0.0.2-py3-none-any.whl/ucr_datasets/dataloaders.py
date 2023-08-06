import pandas as pd
from importlib import resources
from romaniya_menim.utils import read_all_datasets

def DataLoader(dataset_names):
    return read_all_datasets(dataset_names)

import sys
import os
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class Datalngestionconfig:
    train_data_path: str=os.path.join( 'artifacts' , "train.csv")
    test_data_path: str=os.path.join( 'artifacts' , "test.csv")
    raw_data_path: str=os.path.join( 'artifacts' , "data.csv")

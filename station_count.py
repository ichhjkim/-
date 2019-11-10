import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from numpy import nan as NA
import matplotlib.pyplot as plt

station_df = pd.read_csv('서울특별시 공공자전거 외국인 대여정보(월별).csv')
station_df.index.name = ['대여소번호']
station_df.index = []
for i in range()


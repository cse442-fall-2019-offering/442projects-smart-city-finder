#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
import uuid
from random import choice


def retrieve_dummy_data():
    # use the same random seed every time so we get repeatable results
    random_seed = 20192310
    random = np.random.RandomState(random_seed)

    # generate random values
    names = np.array([str(uuid.uuid4()) for _ in range(1000)])
    ages = random.randint(18, 31, (1000, ))
    cities = np.array([random.choice(['NYC', 'Buffalo', 'SF', 'LA', 'Seattle', 'San Jose']) for _ in range(1000)])
    transport = np.array([random.choice(['car', 'bike', 'bus', 'train']) for _ in range(1000)])
    salary = random.randint(500, 15000, (1000, ))
    height_cm = random.randint(100, 200, (1000, ))
    weight_lb = random.randint(60, 400, (1000, ))
    Job_Title = np.array([random.choice(['Software Enginner', 'Actor', 'Doctor', 'Teacher', 'Other']) for _ in range(1000)])
    Shift_Hours = random.randint(20, 40, (1000, ))

    df = pd.DataFrame()
    df['id'] = names
    df['age'] = ages
    df['city'] = cities
    df['transport'] = transport
    df['salary'] = salary
    df['height'] = height_cm
    df['weight'] = weight_lb
    df['job'] = Job_Title
    df['shift hours'] = Shift_Hours

    return df

if __name__ == '__main__':
    df = retrieve_dummy_data()
    #print(df)
    print(df.head())


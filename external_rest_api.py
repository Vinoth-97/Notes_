# -*- coding: utf-8 -*-
"""External-rest-api.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lh_N8myLkmN9wDwNOcInECN4KkBl0nuf
"""

import requests

import json

import pprint

url = "http://api.tvmaze.com/singlesearch/shows"

show = input("Please input a show name.  ")

params = {"q":show}



response = requests.get(url, params)



if response.status_code == 200:

    data = json.loads(response.text)

    # pprint.pprint(data)

    

    name = data['name']

    premiered = data['premiered']

    summary = data['summary']

    

    print(f"{name} premiered on {premiered}.")

    print(summary)

    

else:

    print(f"Error: {response.status_code}")
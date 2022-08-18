"""
File of configs
"""
import os


class Config:
    token = open('TOKEN', 'r').read()  # Token from virtual environment variable
    admins = [5412434521, 1264066850, 5339365196]
    data_path = os.path.dirname(__file__)
    data_path = data_path[:data_path.rfind('/')]

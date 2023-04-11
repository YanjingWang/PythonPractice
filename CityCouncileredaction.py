import os,glob,shutil
import base64
import requests
import datetime
import time
from datetime import date
from ms_graph import generate_access_token
import win32com.client as win32
import subprocess
import pandas as pd
# from rpy2 import robjects

df = pd.read_excel (r'R:\SEO Analytics\Reporting\City Council SY22\City Council QC\Annual Special Education Data Report SY22.xlsx') #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
print (df)
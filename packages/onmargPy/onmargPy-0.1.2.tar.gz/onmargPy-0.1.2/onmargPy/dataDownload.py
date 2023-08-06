import pandas as pd
# needs xlrd
# needs openpyxl

import geopandas as gpd

import os

import re

import zipfile
import tempfile

from urllib.request import urlopen
from io import BytesIO

def om_data(year, level):
    
    year = str(year)
    
    # Ensure year is valid and get url
    if year == "2001":
        raise Exception("This year has not yet been implemented")
    elif year == "2006":
        raise Exception("This year has not yet been implemented")
    elif year == "2011":
        url = "https://www.publichealthontario.ca/-/media/Data-Files/index-on-marg-2011.xlsx?la=en&sc_lang=en&hash=88EFEB83D1A1DFC5A90517AE2E71C855"
    elif year == "2016":
        url = "https://www.publichealthontario.ca/-/media/Data-Files/index-on-marg.xls?sc_lang=en"
    else:
        raise Exception("There is no record for year: " + year)
    
    
    # Ensure level is valid
    valid_levels = ["DAUID", "CTUID", "CSDUID", "CCSUID", "CDUID", "CMAUID", "PHUUID", "LHINUID", "LHIN_SRUID"]
    
    if level not in valid_levels:
        raise Exception("There is no level: " + level)
    
    # Determine page format depending on year and level
    if level == "DAUID":
        prefix = "DA"
    else:
        prefix = level
        
    if year == "2011" or level == "DAUID":
        page = prefix + "_" + year
    else:
        page = year + "_" + prefix
    
    
    # Read and return data
    df = pd.read_excel(url, sheet_name=page)
    
    return df


def om_geo(year, level, style):
    
    # Get On-Marg data
    dat = om_data(year, level)
    
    year = str(year)
    
    # Ensure year is valid and get url
    if year == "2001":
        raise Exception("This year has not yet been implemented")
    elif year == "2006":
        raise Exception("This year has not yet been implemented")
    elif year == "2011":
        stat_url = "https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/gda_000a11a_e.zip"
    elif year == "2016":
        stat_url = "https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/2016/lda_000b16a_e.zip"
    else:
        raise Exception("There is no record for year: " + year)
    
    
    # Read zip file
    resp = urlopen(stat_url)
    stat_zip = zipfile.ZipFile(BytesIO(resp.read()))
    
    
    # Get the name of the shapefile in the directory
    def getFileName(filenames):
        for name in filenames:
            if re.search(".shp$", name):
                return name
        raise Exception("Error: Shapefile not found in download")
        
    
    # Create temporary directory
    with tempfile.TemporaryDirectory() as tempdir:
        stat_zip.extractall(tempdir)
        filenames = os.listdir(tempdir)
        filename = getFileName(filenames)
        filepath = tempdir + "\\" + filename
        geo_dat = gpd.read_file(filepath)
    
    
    # Join geographic file with data file
    total_dat = pd.concat([dat, geo_dat], axis=1, join="inner")
    
    return total_dat
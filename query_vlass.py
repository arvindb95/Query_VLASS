import argparse
import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord
from astroquery.cadc import Cadc
import os

parser = argparse.ArgumentParser(prefix_chars='@')
parser.add_argument("ra",help="RA of the source in 00h00m00.00s format",type=str)
parser.add_argument("dec",help="DEC of the source in +00d00m00.00s format",type=str)
parser.add_argument("radius",help="radius around ra dec center",type=str,default="3 arcmin")
args = parser.parse_args()

ra = args.ra
dec = args.dec
radius = args.radius

cadc = Cadc()
coords = ra + " " + dec
results = cadc.query_region(coords, radius, collection='VLASS')
image_list = cadc.get_image_list(results, coords, radius)

if (len(image_list) > 1):
    print("The coordinates entered are present in more than one field!")
    for i in range(len(image_list)):
        print(i," : ",image_list[i])
    field_id = input("Enter field you would like to download : ")
    field_id = int(field_id)
    sel_image = image_list[field_id]
    filename = sel_image.split("/")[-1].split("&")[0][21:]
    print(filename)
    print("Downloading VLASS image : ",filename)
    os.system("wget -O "+filename+" "+sel_image)
else :
    sel_image = image_list[0]
    filename = sel_image.split("/")[-1].split("&")[0][21:]
    print(filename)
    print("Downloading VLASS image : ",filename)
    os.system("wget -O "+filename+" "+sel_image)


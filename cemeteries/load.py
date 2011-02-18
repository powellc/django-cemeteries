import os
from models import Cemetery, Monument
from django.template.defaultfilters import slugify

cem_data = os.path.abspath('data/castine-cemetery.csv')

import csv
reader = csv.reader(open(cem_data), dialect='excel')
CEMETERY=Cemetery.objects.get(pk=1)

for row in reader:
    LAST=row[0]
    FULL=row[1]
    DOD=row[2]
    DOB=row[3]
    GRAVE_LOT=row[4]
    GRAVE_SEC=row[5]
    GRAVE_NAME=row[6]
    if row[7]=='Yes':
        STONE=True
    else:
        STONE=False
    STONE_NAME=row[8]
    STONE_LOT=row[9]
    STONE_SECTION=row[10]
    STONE_PHOTO=row[11]
    STONE_SURFACE=row[12]
    STONE_TRANS=row[13] 
    Monument.objects.get_or_create(last_name=LAST, full_name=FULL, dob=DOB, dod=DOD, grave_lot=GRAVE_LOT,
                 grave_section=GRAVE_SEC, grave_display_name=GRAVE_NAME, stone=STONE, stone_name=STONE_NAME,
                 stone_lot=STONE_LOT, stone_section=STONE_SECTION, stone_photo=STONE_PHOTO, 
                 stone_surface_content = STONE_SURFACE, stone_surface_transcription=STONE_TRANS, cemetery=CEMETERY, slug=slugify(LAST))

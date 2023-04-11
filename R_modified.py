import os
import glob
import shutil
import base64
import requests
import datetime
import time
from datetime import date
from ms_graph import generate_access_token
import win32com.client as win32
import subprocess
# from rpy2 import robjects


def copyonefile(src, dst):
    shutil.copy(src, dst)
    print('copying one file from {0} to {1} is compelte'.format(src, dst))


def copyallfiles(srcdir, dstdir):
    # shutil.copytree(srcdir,dstdir)
    files = os.listdir(srcdir)

    # iterating over all the files in
    # the source directory
    for fname in files:
        # copying the files to the destination directory
        shutil.copy2(os.path.join(srcdir, fname), dstdir)
        print(fname)


def R_Process():
    # Process 2 : Create XLS Files for Charter and CSD schools
    MDSY22_23 = "\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Processing\Data Mart Files\Mandate_Distribution_SY22-23"
    int_pdfpath = 'C:\PA_Distribution_PDF'
    int_xlspath = 'C:\PA_Distribution_XLS'  # never been used
    int_charterpdf = 'C:\PA_DISTRIBUTION_PDF_Charter'
    int_charterxls = 'C:\PA_DISTRIBUTION_XLS_Charter'  # never been used
    CSD_Archive = 'R:\SEO Analytics\Processing\Data Mart Files\Archives\Backup_{0}'.format(
        date.today().strftime("%Y-%m-%d"))
    Charter_Archive = 'R:\SEO Analytics\Reporting\CharterArchive\{0}'.format(
        date.today().strftime("%Y%m%d"))
    dst_CSD_PDF = 'R:\All Central Offices\Special Ed Data\PA_Distribution_PDF'
    dst_CSD_XLS = 'C:\Template'
    shareCharter = 'R:\SEO Analytics\Share\Charter\{0}'.format(
        date.today().strftime("%Y%m%d"))
    mylocalXLSfolder = 'C:\Template'
    RSCompliance = 'R:\SEO Analytics\Share\Related Services\{0}'.format(
        date.today().strftime("%Y%m%d"))
    RSDashboardSharepoint = 'https://nycdoe.sharepoint.com/:f:/r/sites/RelatedServicesDashboard/Shared%20Documents/RS%20Compliance?csf=1&web=1&e=52Kaaq'

    file1 = os.path.join(MDSY22_23, 'RS_Reports_2022_2023_modified.R')
    copyonefile(file1, mylocalXLSfolder)
    file2 = os.path.join(MDSY22_23, 'RS_Reports_2022_2023_Charter.R')
    copyonefile(file2, mylocalXLSfolder)
    newfile2 = os.path.join(mylocalXLSfolder, 'RS_Reports_2022_2023_Charter.R')
    file3 = os.path.join(MDSY22_23, 'RS_Template_new.xlsx')
    copyonefile(file3, mylocalXLSfolder)
    newfile3 = os.path.join(mylocalXLSfolder, 'RS_Template_new.xlsx')
    file4 = os.path.join(MDSY22_23, 'RS_Compliance_new.xlsx')
    copyonefile(file4, mylocalXLSfolder)
    newfile4 = os.path.join(mylocalXLSfolder, 'RS_Compliance_new.xlsx')
    src_CSD = '\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Reporting\Related Services\Output Files\SY 22-23\MandatedServices_{0}'.format(
        date.today().strftime("%Y%m%d"))
    src_Charter = '\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Reporting\Related Services\Output Files\SY 22-23 Charter\MandatedServicesCharter_{0}'.format(
        date.today().strftime("%Y%m%d"))

    file1 = os.path.join(mylocalXLSfolder, 'RS_Reports_2022_2023.R')
    os.startfile(file1)
    print('Click Run and it takes 10 mins')
    time.sleep(10*60)

    copyallfiles(src_CSD, dst_CSD_XLS)

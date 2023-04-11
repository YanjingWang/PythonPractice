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


def createdir(path):
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)
    else:
        return  # 'folder is created'


def rmfilesfromdir(dir):
    for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)


def rmonefile(path):
    isExist = os.path.exists(path)
    if isExist:
        os.remove(path)
    else:
        return


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


def copyfiles(srcdir, dstdir):
    # shutil.copytree(srcdir,dstdir)
    files = os.listdir(srcdir)

    # iterating over all the files in
    # the source directory
    for fname in files:
        # copying the files to the destination directory
        shutil.copyfile(os.path.join(srcdir, fname), dstdir)
        print(fname)


def openfiles(srcdir):
    # shutil.copytree(srcdir,dstdir)
    files = os.listdir(srcdir)
    for fname in files:
        if fname in ['Access Schools.xlsx', 'Bronx.xlsx', 'Brooklyn North.xlsx', 'Brooklyn South.xlsx', 'D75.xlsx', 'Manhattan.xlsx', 'Queens North.xlsx', 'Queens South.xlsx', 'Stanten Island.xlsx']:
            fname = os.path.join(srcdir, fname)
            os.startfile(fname)
            print(fname)
        else:
            return


def countfiles(srcdir):
    files = os.listdir(srcdir)
    count = 0
    for fname in files:
        count += 1
    print(count)
    return count


def printfiles(olddir, newdir):
    file_0822 = []
    files = os.listdir(olddir)
    for fname in files:
        file_0822.append(fname)
    file_0829 = []
    newfiles = os.listdir(newdir)
    for newfile in newfiles:
        file_0829.append(newfile)
    list_difference = []
    for element in file_0822:
        if element not in file_0829:
            list_difference.append(element)
    print(list_difference)


def copy_files_byfilename(src_folder, dest_folder, file_names):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    for file in os.listdir(src_folder):
        if file in file_names:
            src_file_path = os.path.join(src_folder, file)
            dest_file_path = os.path.join(dest_folder, file)
            shutil.copy2(src_file_path, dest_file_path)
            print(f"Copied {file} from {src_folder} to {dest_folder}")


def extract_first_six_chars(folder_path):
    file_prefixes = []
    for file in os.listdir(folder_path):
        file_prefixes.append(file[:6])
    return file_prefixes


def RelatedServices():
    # Process 1 : Created PDFs for CSD and Charter schools
    # os.startfile(r'R:\All Central Offices\Special Ed Data\PA_Distribution_PDF')
    # os.startfile(r'R:\SEO Analytics\Reporting\Critical Processes\Related Services\SY22-23')
    # 1). create folders we need
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
    dst_CSD_XLS = 'R:\All Central Offices\Special Ed Data\PA_Distribution_XLS'
    shareCharter = 'R:\SEO Analytics\Share\Charter\{0}'.format(
        date.today().strftime("%Y%m%d"))
    mylocalXLSfolder = 'C:\Template'
    RSCompliance = 'R:\SEO Analytics\Share\Related Services\{0}'.format(
        date.today().strftime("%Y%m%d"))
    RSDashboardSharepoint = 'https://nycdoe.sharepoint.com/:f:/r/sites/RelatedServicesDashboard/Shared%20Documents/RS%20Compliance?csf=1&web=1&e=52Kaaq'

    createdir(int_pdfpath)
    createdir(int_xlspath)
    createdir(int_charterpdf)
    createdir(int_charterxls)
    createdir(CSD_Archive)
    createdir(Charter_Archive)  # really created?
    createdir(shareCharter)  # really created?
    createdir(mylocalXLSfolder)

    # 2.1): delete previous week XLS and PDF files
    for f in os.listdir(dst_CSD_PDF):
        os.remove(os.path.join(dst_CSD_PDF, f))
        print(f)

    for file in os.scandir(dst_CSD_XLS):
        os.remove(file.path)
        print(file)
    rmfilesfromdir(dst_CSD_PDF)
    rmfilesfromdir(dst_CSD_XLS)
    rmfilesfromdir(int_pdfpath)
    rmfilesfromdir(int_xlspath)
    rmfilesfromdir(int_charterpdf)  # add to run guidance
    rmfilesfromdir(int_charterxls)  # add to run guidance
    rmfilesfromdir(mylocalXLSfolder)

    # 2.2) copy Mandate_Distribution_SY22-23 to your local C or D
    copyonefile('\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Processing\Data Mart Files\Mandate_Distribution_SY22-23\Mandate_Distribution_SY22-23.accdb', mylocalXLSfolder)
    os.startfile('C:\Template\Mandate_Distribution_SY22-23.accdb')
    time.sleep(60)
    now = datetime.datetime.now()
    print('Click Run and wait for 50 mins, start time: {0}'.format(
        now.strftime("%d/%B/%Y %H:%M:%S")))
    time.sleep(55*60)
    print('1598 files should be saved in C:\PA_Distribution_PDF and 271 files should saved in C:\PA_DISTRIBUTION_PDF_Charter.')
    print('End time: {0}'.format(now.strftime("%d/%B/%Y %H:%M:%S")))

    print('Close Access file')
    time.sleep(60)
    # rmonefile('C:\Template\Mandate_Distribution_SY22-23.accdb')
    time.sleep(10)
    # copy 1601 CSD files
    copyallfiles(int_pdfpath, dst_CSD_PDF)
    copyallfiles(int_pdfpath, CSD_Archive)
    print('copy pdf CSD files complete')

    # copy 275 chater files
    copyallfiles(int_charterpdf, shareCharter)
    copyallfiles(int_charterpdf, Charter_Archive)
    print('copy pdf charter files compelte')


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
    dst_CSD_XLS = 'R:\All Central Offices\Special Ed Data\PA_Distribution_XLS'
    shareCharter = 'R:\SEO Analytics\Share\Charter\{0}'.format(
        date.today().strftime("%Y%m%d"))
    mylocalXLSfolder = 'C:\Template'
    RSCompliance = 'R:\SEO Analytics\Share\Related Services\{0}'.format(
        date.today().strftime("%Y%m%d"))
    RSDashboardSharepoint = 'https://nycdoe.sharepoint.com/:f:/r/sites/RelatedServicesDashboard/Shared%20Documents/RS%20Compliance?csf=1&web=1&e=52Kaaq'

    file1 = os.path.join(MDSY22_23, 'RS_Reports_2022_2023.R')
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
    print('Click Run and it takes 35 mins')
    time.sleep(40*60)

    copyallfiles(src_CSD, dst_CSD_XLS)
    # copy PA_Distribution_XLS to archive?
    copyallfiles(dst_CSD_XLS, int_xlspath)
    copyallfiles(int_xlspath, CSD_Archive)
    # copyallfiles(RSCompliance,RSDashboardSharepoint)

    file2 = os.path.join(mylocalXLSfolder, 'RS_Reports_2022_2023_Charter.R')
    os.startfile(file2)
    print('Click Run and it takes 5 mins')
    time.sleep(5*60)
    createdir(Charter_Archive)  # really created?
    createdir(shareCharter)  # really created?
    copyallfiles(src_Charter, shareCharter)
    copyallfiles(src_Charter, Charter_Archive)


def rerun_R():
    pdf_count = countfiles(
        'R:\All Central Offices\Special Ed Data\PA_Distribution_PDF')
    xls_count = countfiles(
        'R:\All Central Offices\Special Ed Data\PA_Distribution_XLS')
    src_CSD = '\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Reporting\Related Services\Output Files\SY 22-23\MandatedServices_{0}'.format(
        date.today().strftime("%Y%m%d"))
    dst_CSD_XLS = 'R:\All Central Offices\Special Ed Data\PA_Distribution_XLS'
    int_xlspath = 'C:\PA_Distribution_XLS'
    CSD_Archive = 'R:\SEO Analytics\Processing\Data Mart Files\Archives\Backup_{0}'.format(
        date.today().strftime("%Y-%m-%d"))
    Charter_Archive = 'R:\SEO Analytics\Reporting\CharterArchive\{0}'.format(
        date.today().strftime("%Y%m%d"))
    CSD_Archive_count = countfiles(CSD_Archive)
    Charter_Archive_count = countfiles(Charter_Archive)
    # find the missing files
    folder1_path = 'R:\All Central Offices\Special Ed Data\PA_Distribution_PDF'
    folder2_path = 'R:\All Central Offices\Special Ed Data\PA_Distribution_XLS'
    folder1_prefixes = extract_first_six_chars(folder1_path)
    folder2_prefixes = extract_first_six_chars(folder2_path)
    # Find the different elements in the two lists
    folder1_unique_prefixes = list(
        set(folder1_prefixes) - set(folder2_prefixes))
    folder2_unique_prefixes = list(
        set(folder2_prefixes) - set(folder1_prefixes))
    print("Unique elements in folder PDF:", folder1_unique_prefixes)
    print("Unique elements in folder XLS:", folder2_unique_prefixes)
    if pdf_count > xls_count:
        print('PDF count is more than XLS count')
        print(CSD_Archive_count)
        print(Charter_Archive_count)
        # #clear R drive
        # rmfilesfromdir(src_CSD)
        # rmfilesfromdir(dst_CSD_XLS)
        # rmfilesfromdir(int_xlspath)
        # rmfilesfromdir(CSD_Archive)
        # R_Process()
    elif pdf_count == xls_count:
        print('PDF counts is equal to XLS Count')
        print(CSD_Archive_count)
        print(Charter_Archive_count)
    else:
        print('PDF has less files than XLS')
        print(CSD_Archive_count)
        print(Charter_Archive_count)


def MandatedServices():
    os.startfile(
        r'R:\SEO Analytics\Reporting\Critical Processes\Related Services\SY22-23')
    file = 'R:\SEO Analytics\Processing\Data Mart Files\Templates\SESIS Mandated Services Report\SESIS Mandated Services Report - AUTOMATED - SY22-23.xlsm'
    os.popen(file, 'r')
    print("Click Enable Enable in the ribbon-->Developer tab: Click Macros button-->Click Run-->Wait for 4 mins")
    time.sleep(5*60)


def ms_send_outlook_email():
    # construct Outlook application instance
    olApp = win32.Dispatch('Outlook.Application')
    olNS = olApp.GetNameSpace('MAPI')

    # construct the email item object
    mailItem = olApp.CreateItem(0)
    mailItem.Subject = 'Mandated Services updates for {0}'.format(
        datetime.date.today())
    mailItem.BodyFormat = 1
    mailItem.Body = """Hi  All,\
    Updates at the Borough/City wide office (BCO) level have been updated to R:\Drive (R:\All Central Offices\Special Ed Data\PA SharePoint) and posted to SharePoint. \
    The above link is for sharing student level data.  If you are denied access, please log out of the network and then log back in. \
    * Please do not modify or store any personal files within any of our directories. We use that drive as a staging area to load and distribute student level data to various systems/people within the DOE.\
    Thanks,
    """
    mailItem.To = 'Nobari Kevin KNobari@schools.nyc.gov; Van Biema Michael <MVanBiema@schools.nyc.gov>; Palladino Linette <LPalladino2@schools.nyc.gov>; Kaufman Helen <HKaufma@schools.nyc.gov>; Leo Maria <MLeo2@schools.nyc.gov>; \
    Elkayam Barry <BElkaya@schools.nyc.gov>; Shah Archana <AShah@schools.nyc.gov>; Stamm Charles <CStamm@schools.nyc.gov>; Leong Melanie <MLeong@schools.nyc.gov>; \
    Han Louise <LHan@schools.nyc.gov>; Silverman Joy <JSilverman8@schools.nyc.gov>'
    mailItem.Cc = 'Mayilrajan Rajamanickam <RMayilrajan@schools.nyc.gov>; ywang36@schools.nyc.gov; \
    Nutter Grace <GNutter@schools.nyc.gov>; Powers Alan <APowers3@schools.nyc.gov>'

    # mailItem.Attachments.Add(os.path.join(os.getcwd(), 'fibonacci.py'))
    # mailItem.Attachments.Add(os.path.join(os.getcwd(), 'EmployeeClass.py'))

    mailItem.Display()

    mailItem.Save()
    mailItem.Send()


def rs_charter_send_outlook_email():
    # construct Outlook application instance
    olApp = win32.Dispatch('Outlook.Application')
    olNS = olApp.GetNameSpace('MAPI')

    # construct the email item object
    mailItem = olApp.CreateItem(0)
    mailItem.Subject = 'Weekly Charter Related Services Report {0}'.format(
        datetime.date.today())
    mailItem.BodyFormat = 1
    mailItem.Body = """Hello All, \
    Weekly charter Related Service reports are generated and saved at the following location: R:\SEO Analytics\Share\Charter\{0}
    """.format(date.today().strftime("%Y%m%d"))

    mailItem.To = 'Van Biema Michael <MVanBiema@schools.nyc.gov>; Liu Mei <MLiu2@schools.nyc.gov>; \
    Thompson Karyn <KThompson7@schools.nyc.gov>; Sandi Mariama <MSandi@schools.nyc.gov>;jwallenstein@schools.nyc.gov'
    mailItem.Cc = 'Hammer John <JHammer4@schools.nyc.gov>; Daverin Rebecca <RDaverin2@schools.nyc.gov>; Powers Alan <APowers3@schools.nyc.gov>; \
    Mayilrajan Rajamanickam <RMayilrajan@schools.nyc.gov>; Grace Nutter <gnutter@schools.nyc.gov>; ywang36@schools.nyc.gov'

    # mailItem.Attachments.Add(os.path.join(os.getcwd(), 'fibonacci.py'))
    # mailItem.Attachments.Add(os.path.join(os.getcwd(), 'EmployeeClass.py'))

    mailItem.Display()

    mailItem.Save()
    mailItem.Send()


def archive_rs_borough():
    source_folder = '\\\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Reporting\RS Dashboard\Weekly RS Dashboard'
    destination_folder = 'R:\SEO Analytics\Reporting\RS Dashboard\Weekly RS Dashboard Archive\{0}'.format(
        date.today().strftime("%Y%m%d"))
    file_names_to_copy = ['Access Schools.xlsx', 'Bronx.xlsx', 'Brooklyn North.xlsx', 'Brooklyn South.xlsx', 'Citywide.xlsx',
                          'Citywide RS Powerpoint.pptm', 'D75.xlsx', 'Manhattan.xlsx', 'Queens North.xlsx', 'Queens South.xlsx', 'Stanten Island.xlsx']
    copy_files_byfilename(
        source_folder, destination_folder, file_names_to_copy)


if __name__ == '__main__':
    # RelatedServices()
    # R_Process()
    # rerun_R()
    # rs_charter_send_outlook_email()
    # MandatedServices()
    # ms_send_outlook_email()
    # openfiles('R:\SEO Analytics\Reporting\RS Dashboard\Weekly RS Dashboard')
    # time.sleep(60*60)
    archive_rs_borough()

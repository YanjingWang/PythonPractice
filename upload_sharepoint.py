# pip install shareplum
from shareplum import Site
from shareplum import Office365
from shareplum.site import Version
import os
# # SharePoint and file details
# sharepoint_url = "https://nycdoe.sharepoint.com"
# sharepoint_site = "/sites/yoursite"
# username = "ywang36@schools.nyc.gov"
# password = "WYJiwillbe/519"
# folder_name = "Shared Documents/YourFolder"  # SharePoint destination folder
# local_folder = "/path/to/local/folder"
# file_name = "yourfile.xlsx"  # Local file to upload
# # Authenticate with SharePoint
# authcookie = Office365(sharepoint_url, username=username,
#                        password=password).GetCookies()
# site = Site(sharepoint_url + sharepoint_site,
#             version=Version.v365, authcookie=authcookie)
# # Get SharePoint folder
# sp_folder = site.Folder(folder_name)
# # Upload file to SharePoint
# with open(os.path.join(local_folder, file_name), "rb") as file:
#     sp_folder.upload_file(file, file_name)
#     print(f"Uploaded {file_name} to SharePoint folder: {folder_name}")


# Credentials
username = 'YWang36@schools.nyc.gov'
password = 'WYJiwillbe/519'
site_url = "https://nycdoe.sharepoint.com"

# Connect to SharePoint
authcookie = Office365(site_url, username=username,
                       password=password).GetCookies()
site = Site(site_url, authcookie=authcookie)

# SharePoint folder path
folder_path = "/sites/RelatedServicesDashboard/Shared%20Documents/Forms/AllItems.aspx?csf=1&web=1&e=52Kaaq&cid=0aa4e6f3%2D9bf2%2D4409%2Db358%2D30a2ef4843ef&FolderCTID=0x0120003896AEA985037F478C76713D8238A3C7&id=%2Fsites%2FRelatedServicesDashboard%2FShared%20Documents%2FAccess%20Schools&viewid=a94c67c5%2Dcfe7%2D4a86%2Da884%2D06fa1bc02cad"

# Local folder path
local_folder_path = "\\CENTRAL.NYCED.ORG\DoE$\SEO Analytics\Reporting\RS Dashboard\Weekly RS Dashboard"

# Upload files to SharePoint
for filename in os.listdir(local_folder_path):
    with open(os.path.join(local_folder_path, filename), 'rb') as file:
        file_content = file.read()
    site.Folder(folder_path).upload_file(filename, file_content)

import requests
import os
from hashlib import md5

# Your FlagCounter CGI link
url = "[URL=https://info.flagcounter.com/xn0k][IMG]https://s01.flagcounter.com/count2/xn0k/bg_22C29F/txt_85F2C7/border_CCCCCC/columns_8/maxflags_40/viewers_0/labels_1/pageviews_1/flags_0/percent_0/[/IMG][/URL]"
output_file = "flagcounter.png"
temp_file = "temp_flagcounter.png"

# Download new image to temp file
response = requests.get(url)
if response.status_code == 200:
    with open(temp_file, "wb") as f:
        f.write(response.content)
else:
    print(f"Failed to fetch flagcounter image: {response.status_code}")
    exit(0)

# Compare MD5 hash of existing and new files (if old exists)
def file_md5(filename):
    with open(filename, "rb") as f:
        return md5(f.read()).hexdigest()

if os.path.exists(output_file):
    if file_md5(output_file) == file_md5(temp_file):
        print("No change detected, skipping commit.")
        os.remove(temp_file)
        exit(0)

# Replace old file with new
os.replace(temp_file, output_file)
print("Flagcounter updated.")

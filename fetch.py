import requests

# Your updated custom flag counter image URL
url = "url = "https://s01.flagcounter.com/count2/xn0k/bg_22C29F/txt_85F2C7/border_CCCCCC/columns_8/maxflags_40/viewers_0/labels_1/pageviews_1/flags_0/percent_0/""

# Download the image
response = requests.get(url)
response.raise_for_status()

# Save in repo root
with open("flagcounter.png", "wb") as f:
    f.write(response.content)

print("Flag counter image updated.")

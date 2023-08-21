from bs4 import BeautifulSoup
import time
import requests
import json

file = "/tmp/Arch Linux - Releases.html"
output = "/tmp/releases.json"
release_info = []
releases = []
with open(file, "r") as fp:
    # contents = f.read()
    soup = BeautifulSoup(fp, "html.parser")
table = soup.find("table", id="release-table")
i = 6
for row in table.tbody.find_all("tr"):
    columns = row.find_all("td")
    if columns != []:
        # print(columns)
        path = columns[2].find("a")["href"]
        # release = {
        #     "release_date": columns[1].get_text(strip=True),
        #     "path": path,
        #     "kernel_version": columns[3].get_text(strip=True),
        #     "available": columns[4].get_text(strip=True),
        #     "size": columns[5].get_text(strip=True)
        # }
        response = requests.get(path)
        response_data = BeautifulSoup(response.content, "html.parser")
        release_data = response_data.find(class_="release box").find("ul").find_all("li")
        result = []
        for item in release_data:
            strong_tag = item.find("strong")
            if strong_tag is not None:
                # print(strong_tag.get_text(strip=True))
                key = strong_tag.get_text(strip=True)
                value = item.get_text(strip=True)[len(key):]
                result.append(value)
        ITEM_ = {
            "fields": {
                "kernel_version": result[1] if len(result) >= 2 else None,
                "release_date": result[0] if len(result) >= 1 else None,
                "sha256_sum": result[3] if len(result) >= 4 else None,
                "b2_sum": result[4] if len(result) >= 5 else None,
                "version": result[0] if len(result) >= 1 else None,
                "pgp_key": result[5] if len(result) >= 6 else None,
            },
            "model": "releng.release",
            "pk": i
        }
        print(i, " sent request to: ", path)
        release_info.append(ITEM_)
        time.sleep(5)
        i = i + 1
        # print(result)
        # print(release_info)
        # if i == 8:
        #     break
        # releases.append(release)

# output the release in release.json
# with open(output, 'w') as json_file:
#     json.dump(releases, json_file, indent=2)
with open("data/release_info.json", "w") as json_file:
    json.dump(release_info, json_file, indent=2)
# print(releases)

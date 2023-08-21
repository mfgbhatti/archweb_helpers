from bs4 import BeautifulSoup
import requests
import json

release_file = "release.json"
# with open(release_file, 'r') as data:
#     releases = json.load(data)
# for i in releases:
#     # print(i["path"])
#     url = i["path"]
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     raw_data = soup.find(class_="release box")
#     release_data = raw_data.find("ul").find_all("li")
#     for item in release_data:
#         strong_tag = item.find("strong")
#         if strong_tag is not None:
#             # print(strong_tag.get_text(strip=True))
#             key = strong_tag.get_text(strip=True)
#             value = item.get_text(strip=True)[len(key):]
#             print(key,value)
    # print(raw_data)
    # for raw_lists in raw_data.find_all("ul"):
        # print(raw_lists)
        # print(torrent)
# data.close()
html_data = """
<ul>
<li><strong>Release Date:</strong> 2023-08-01</li>
<li><strong>Kernel Version:</strong> 6.4.7</li>
<li><strong>Available:</strong> Yes</li>
<li><a href="/releng/releases/2023.08.01/torrent/" title="Download torrent for 2023.08.01">
               Download via Torrent <img alt="" height="12" src="/static/download.301a2aacd2a2.png" width="12"/></a></li>
<li><a href="magnet:?xt=urn:btih:7a9c4a72e79fcf5f65f091e462b60e589af3f865&amp;dn=archlinux-2023.08.01-x86_64.iso" title="Get magnet link for 2023.08.01">
               Download via Magnet URI <img alt="" height="12" src="/static/magnet.29ed728b8ae4.png" width="12"/></a></li>
<li><strong>SHA256:</strong> 3bf1287333de5c26663b70a17ce7573f15dc60780b140cbbd1c720338c0abac5</li>
<li><strong>BLAKE2b:</strong> e097be4cbcae19085c55e1f8b52c8e82bf373441abd6411b79ee0d783d7074592d29fe81b5c1984e7d5577cf053cfb4caff4bf4a1f3e16b3d13d6568c85b4825</li>
<li><strong>PGP fingerprint:</strong> <a href="https://keyserver.ubuntu.com/pks/lookup?op=vindex&amp;fingerprint=on&amp;exact=on&amp;search=0x3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C" title="PGP key search for 3E80 CA1A 8B89 F69C BA57  D98A 76A5 EF90 5444 9A5C">0x54449A5C</a></li>
</ul>
"""
"""
<ul>
<li><strong>Comment:</strong> Arch Linux 2023.08.01 &lt;https://archlinux.org&gt;</li>
<li><strong>Creation Date:</strong> 2023-08-01 12:20 UTC</li>
<li><strong>Created By:</strong> mktorrent 1.1</li>
<li><strong>Announce URL:</strong> None</li>
<li><strong>File Name:</strong> archlinux-2023.08.01-x86_64.iso</li>
<li><strong>File Length:</strong> 793.3 MB</li>
<li><strong>Piece Count:</strong> 1587.0 pieces</li>
<li><strong>Piece Length:</strong> 512.0 KB</li>
<li><strong>Info Hash:</strong> 7a9c4a72e79fcf5f65f091e462b60e589af3f865</li>
<li><strong>URL List Length:</strong> 351 URLs</li>
</ul>
"""

soup = BeautifulSoup(html_data, "html.parser")
normal_release = soup.find("ul").find_all("li")
# wip
# torrent_release = normal_release.find_next_sibling("ul")

result = []
for item in normal_release:
    # print(item)
    strong_tag = item.find("strong")
    if strong_tag is not None:
        # print(strong_tag.get_text(strip=True))
        key = strong_tag.get_text(strip=True)
        value = item.get_text(strip=True)[len(key):]
        result.append(value)
        # print(value)
print(result)

    # release_date, kernel, avaible, torrent_link, magnetic_link, sha256, BLAKE2b, fingerprint

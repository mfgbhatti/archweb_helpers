""" Uncomment the following"""
# import os
# import sys
# import django

# sys.path.append(
#     os.path.join(os.path.dirname(__file__), 'archweb')
# )
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# django.setup()

# import json
# from mirrors.models import Mirror, MirrorUrl, MirrorProtocol
# from datetime import datetime, timezone
# import time
#
# f = open("../archweb_helpers/data/mirrors.json")
# mirrors = json.load(f)
# for mirror in mirrors:
#     mirror_instance = Mirror.objects.create(
#         name=mirror["name"],
#         tier=mirror["tier"],
#         public=True,
#         active=True,
#         isos=True,
#         created=datetime.now(timezone.utc),
#         last_modified=datetime.now(timezone.utc)
#     )
#     print("Created new mirror: ", mirror_instance.name)
#     protocols = mirror["protocols"]
#     url_list = [MirrorUrl(url=url) for url in mirror["urls"]]
#     for protocol, url_instance in zip(protocols, url_list):
#         protocol_instance = MirrorProtocol.objects.get(id=protocol)
#         url_instance.protocol = protocol_instance
#         url_instance.mirror = mirror_instance
#         url_instance.country = mirror["code"]
#         url_instance.created = datetime.now(timezone.utc)
#         url_instance.save()
#         print("Created new mirror's url at: ", url_instance.id)
#         print("with protocol", protocol_instance.protocol)
#         time.sleep(3)
# f.close()

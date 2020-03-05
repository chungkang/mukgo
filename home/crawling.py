from bs4 import BeautifulSoup
import urllib.request
import datetime
import sys
import io
import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
import requests
from operator import itemgetter, attrgetter
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



endurl =['https://socialblade.com/youtube/channel/UC_S4C51xOcE7ooD48jZeCKQ','https://socialblade.com/youtube/channel/UC005BPECU5QAR2JVItQOswg','https://socialblade.com/youtube/channel/UC0VR2v4TZeGcOrZHnmwbU_Q','https://socialblade.com/youtube/channel/UC1Wq-BQZblFGbGgDAoCwrmA','https://socialblade.com/youtube/channel/UC1yFIXF66_VVDEdGHZAjAVg','https://socialblade.com/youtube/channel/UC2fsxQr6Hcx1enORxXgKpxQ','https://socialblade.com/youtube/channel/UC2wZJuuD_WA9ps2FORco1EQ','https://socialblade.com/youtube/channel/UC3lLSu0B-JqA-l9o2aVsHLQ','https://socialblade.com/youtube/channel/UC4KBQuY1OqKHEDfzbJsOjvQ','https://socialblade.com/youtube/channel/UC4PpFUrfT2Pou7OwpVF0MUQ','https://socialblade.com/youtube/channel/UC4VljnooZZkRhhb5s5rv1Mw','https://socialblade.com/youtube/channel/UC5Ida86tt8QKa4Myw7idxNg','https://socialblade.com/youtube/channel/UC5oft5dVf43M2cFmhpJLVGQ','https://socialblade.com/youtube/channel/UC5XuQ-xiWAB6f-qu6gJMDBQ','https://socialblade.com/youtube/channel/UC5zak5tqTE3JJFtiIpXyOnA','https://socialblade.com/youtube/channel/UC71gchLWSQsrpy6qv2eNX_A/','https://socialblade.com/youtube/channel/UC7bRo3yLjtrRV9qU_KsE6nA','https://socialblade.com/youtube/channel/UC7LW-JMyKZ2r2zXZS-VwBYQ','https://socialblade.com/youtube/channel/UC81RXTYxQTU2Ti-2Pqz92zA','https://socialblade.com/youtube/channel/UC8kRUGUkq_sTGuKNR1l6Rrw','https://socialblade.com/youtube/channel/UC9Mo-ijXMy7LuGaLHkBxn7Q','https://socialblade.com/youtube/channel/UCa56qkMvVvq1IMn4xbXaKEA','https://socialblade.com/youtube/channel/UCBCY00Ox6Cins0oRwSLqNGA','https://socialblade.com/youtube/channel/UCBIoXzDldCnpbM_7uyG0_Tg','https://socialblade.com/youtube/channel/UC-Bsa2ivAGWq7bsSPrPGFVA','https://socialblade.com/youtube/channel/UCbzI92w5vWa6mEj1dACfy6g','https://socialblade.com/youtube/channel/UCc7v5yYC_mviB1_fLuB-GRw','https://socialblade.com/youtube/channel/UCdfhK0yIMjmhcQ3gP-qpXRw','https://socialblade.com/youtube/channel/UCEBNRLMrhuE9oTmzpS5umiA','https://socialblade.com/youtube/channel/UCeftkDFnfUJ3xMiFzRbmx7Q','https://socialblade.com/youtube/channel/UCf9sl-IcwNXDqWwWwp4vEwg','https://socialblade.com/youtube/channel/UCfpaSruWW3S4dibonKXENjA','https://socialblade.com/youtube/channel/UCftypYUp6boUauNi_P5WdZg','https://socialblade.com/youtube/channel/UCg7xkCKcxA84xSTGgtF9ySA','https://socialblade.com/youtube/channel/UCGISU4yWiEf4lB9RzdY8O4w','https://socialblade.com/youtube/channel/UChdn7vG9Lf3xCCk2srWjmKA','https://socialblade.com/youtube/channel/UChE5nZAIhWS5vYTRjsUgRpQ','https://socialblade.com/youtube/channel/UCHn2-DNS5t4tEXqBK5bHmTQ','https://socialblade.com/youtube/channel/UChYcJLnVxqgO3SkM6vKX9aw','https://socialblade.com/youtube/channel/UC-i2ywiuvjvpTy2zW-tXfkw','https://socialblade.com/youtube/channel/UCI78AdiI6f7VKhqW1i4B3Rw','https://socialblade.com/youtube/channel/UCIb3x85pM9KjSFGbZ_kzEJQ/','https://socialblade.com/youtube/channel/UCIUfR-2qcpWqgAIfZJXOLWA','https://socialblade.com/youtube/channel/UCj7mdvAJCRKvGBmcusOr9Ag','https://socialblade.com/youtube/channel/UCJCdVamkTKKbJzzzT_uuMaw','https://socialblade.com/youtube/channel/UCj-durTg1W7uWsB8oq0u7kA','https://socialblade.com/youtube/channel/UCKDryfi71TjzKFkr9J9wzew','https://socialblade.com/youtube/channel/UCkS6mJ0i2oMdHEdR-Jpw9Ug','https://socialblade.com/youtube/channel/UCLKUMuHePpmRMeRJ_Ldhd3w','https://socialblade.com/youtube/channel/UCMa-5a4Hg3KnbiDOvhdfb3w','https://socialblade.com/youtube/channel/UC--nMcJvSDK9bUiJMZ2ilUw','https://socialblade.com/youtube/channel/UCO61Rl-jslhyeenfjt-NO4w','https://socialblade.com/youtube/channel/UCo9ZZ04kIhN_8xGxvnjaduQ','https://socialblade.com/youtube/channel/UCoLQZ4ZClFqVPCvvjuiUSRA','https://socialblade.com/youtube/channel/UCp4LfMtDfoa29kTlLnqQ5Mg','https://socialblade.com/youtube/channel/UCpak-zDg3JvdIrfVO68QDEg','https://socialblade.com/youtube/channel/UCPKNKldggioffXPkSmjs5lQ','https://socialblade.com/youtube/channel/UCQ_21lZoPVNWiW2_MSzGxcg','https://socialblade.com/youtube/channel/UCq9MDndXc1y3he3uPZLPskQ','https://socialblade.com/youtube/channel/UCQlc9zUsaiBkXyAPKwZxZ1A','https://socialblade.com/youtube/channel/UCRtoqRleHkDQRVgN9OwV6TA','https://socialblade.com/youtube/channel/UCtvKnzSHvW8XUxfwpYkGrvQ','https://socialblade.com/youtube/channel/UCU6619aa_BntZJude5Sbm5A','https://socialblade.com/youtube/channel/UCVFSrUkV0LTzi4bLICZ7SEw','https://socialblade.com/youtube/channel/UCVPkwz7nxd5bbR536ugmiBw','https://socialblade.com/youtube/channel/UCWKmBNqCPnHsxj8fOhvdt4w','https://socialblade.com/youtube/channel/UCWUwriihuQ_ybNrAOqbg3yg','https://socialblade.com/youtube/channel/UCx_7Isnu10jfrlV7m1Fz06A','https://socialblade.com/youtube/channel/UCx_--zZCqTOb8-m-o_r_-_w','https://socialblade.com/youtube/channel/UCXFPRXi5qgvlmwfwOLol7ig','https://socialblade.com/youtube/channel/UCxO1kNtnTxNhhN_R4z4RkIQ','https://socialblade.com/youtube/channel/UCYFRrnIOK_Qrw3uabkZjltQ','https://socialblade.com/youtube/channel/UCYJrfuYXNqb5XSRd22XRwGw','https://socialblade.com/youtube/channel/UCysVk8dzvSydsFklSu96HSg','https://socialblade.com/youtube/channel/UCyT7JoYJl2usoWYhC1lXteQ','https://socialblade.com/youtube/channel/UCYx9lhCw0u2-OoqVtEU0IMg','https://socialblade.com/youtube/user/NikocadoAvocado','https://socialblade.com/youtube/user/OmaDesalasOrlin','https://socialblade.com/youtube/user/Quinsee18','https://socialblade.com/youtube/user/dkzos','https://socialblade.com/youtube/user/BJPaToo','https://socialblade.com/youtube/user/mcbeom','https://socialblade.com/youtube/user/Pdragonfour','https://socialblade.com/youtube/user/kkanddabbiyaa','https://socialblade.com/youtube/user/TogingTV','https://socialblade.com/youtube/user/ch17go','https://socialblade.com/youtube/user/hyeyounga','https://socialblade.com/youtube/user/koreanenglishman']

result4 = []

for url in endurl:


    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req).read()

    soup = BeautifulSoup(response, "html.parser")
    title = soup.find('h1').text
    sub = soup.find(id="youtube-stats-header-subs").text
    if '.' in sub:
        sub2 = sub.replace('.','').replace('M','0000').replace('K','00')
    else:
        sub2 = sub.replace('M','000000').replace('K','000')
    #sub2 = sub.replace('.','').replace('M','0000').replace('K','000')
    sub3 = int(sub2)
    views = soup.find(id="youtube-stats-header-views").text
    views2 = int(views)
    country = soup.find(id="youtube-user-page-country").text
    result4.append([title,sub,sub3,views2,country, url])

    result5 = sorted(result4, key = itemgetter(1), reverse=True)
print(result5)

dt = datetime.datetime.now()
filename = 'MukbangChart' + dt.strftime('%Y-%m-%d')
#f = open(filename + '.csv', 'w')
f = open(f'{filename}.csv', 'w', encoding='utf-8-sig', newline='')
csvWriter = csv.writer(f)

header_list = ['Title','Sub','Sub#','View','Country','URL']
csvWriter.writerow(header_list)

for i in result5:
    csvWriter.writerow(i)

f.close()

print('완료되었음^^')

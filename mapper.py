import sys
import os,json
from datetime import datetime

result = {
    "youtube":[],
    "twitter":[],
    "instagram":[],
    "facebook": [],
}


for line in sys.stdin:
    data = line.strip()
    jsondata = json.loads(data)
    
    if (len(jsondata) != 0):
        for data_point in jsondata:

            if 'crawler_target' in data_point.keys():
                social_media = data_point['crawler_target']['specific_resource_type']
                
                if social_media == "facebook":
                    # Normalisasi tanggal
                    date = data_point['created_time'][:10]
                    print(f"facebook\t{date}\t1")
                    # Setiap data adalah post dalam facebook yang mempunyai beberapa comment
                    for comment in data_point['comments']['data']:
                        print(f"facebook\t{date}\t1")
                elif social_media == "youtube":
                    if 'publishedAt' in data_point['snippet'].keys():
                        date = data_point['snippet']['publishedAt'][:10]
                        print(f"youtube\t{date}\t1")
                elif social_media == "instagram":
                    date = datetime.utcfromtimestamp(int(data_point['created_time'])).strftime('%Y-%m-%d')
                    print(f"instagram\t{date}\t1")
                elif social_media == "twitter":
                    date = datetime.strftime(datetime.strptime(data_point['created_at'],'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d')
                    print(f"twitter\t{date}\t1")
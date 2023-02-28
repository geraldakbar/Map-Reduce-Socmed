import sys
import csv

result = {
    "youtube":{},
    "twitter":{},
    "instagram":{},
    "facebook": {},
}

for line in sys.stdin:

    social_media, date, count = line.split("\t")

    if date in result[social_media].keys():
        result[social_media][date] += int(count)

    else:
        result[social_media][date] = int(count)


csvWriter = csv.writer(sys.stdout)

csvWriter.writerow(['social_media','date','count'])

for key in result:

    socmed_data = result[key]

    for details in socmed_data:

        csvWriter.writerow([key,details,socmed_data[details]])
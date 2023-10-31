import requests
import os
from tqdm import tqdm
from io import BytesIO
import gzip
import argparse

# Set up command-line argument parsing
parser = argparse.ArgumentParser(description="Download weather data")
parser.add_argument("USAF", type=int, help="USAF code")
parser.add_argument("START_YEAR", type=int, help="Start year")
parser.add_argument("END_YEAR", type=int, help="End year")
args = parser.parse_args()

USAF = args.USAF
START_YEAR = args.START_YEAR
END_YEAR = args.END_YEAR

BASE_URL = "https://www1.ncdc.noaa.gov/pub/data/noaa"
TOTAL_FILES = END_YEAR - START_YEAR + 1

# make sure the folder to hold the downloaded files exists
if not os.path.exists("./downloads"):
    os.makedirs("./downloads")

# keep track of the downloaded and skipped files
downloaded = 0
skipped = 0

print("START_Year :",START_YEAR)
# download the files
print("Downloading files...")
for i in tqdm(range(START_YEAR, END_YEAR + 1)):
    print(i)
    file_name = f"{USAF}-99999-{i}.gz"
    file_link = f"{BASE_URL}/{i}/{file_name}"
    print(file_name)
    # if the file already exists, skip
    if os.path.exists(f"./downloads/{file_name}"):
        downloaded += 1
        continue

    try:
        response = requests.get(file_link)
        content = BytesIO(response.content)
        print(content)
    except:
        skipped += 1
        continue

    with gzip.GzipFile(fileobj=content) as f:
        extracted_data = f.read()

    # write to a new file
    with open(f"./downloads/{file_name[:-3]}", "wb") as f:
        f.write(extracted_data)

    downloaded += 1

print(f"Successfully downloaded {downloaded} files out of {TOTAL_FILES}...")
print(f"Skipped {skipped} files out of {TOTAL_FILES}...")


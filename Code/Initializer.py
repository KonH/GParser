import sys
from Logger import Log
from Database import DB

# Args:
# - AppFile
# - DevFile
# - PagesFile
apps_file_name = sys.argv[1]
dev_file_name = sys.argv[2]
page_file_name = sys.argv[3]
Log.log("Init start.")
db = DB()
db.test()

total = 0
apps = 0
devs = 0
pages = 0

apps_file = open(apps_file_name, 'r')
for app in apps_file:
    url = app.rstrip()
    bundle = url.split('=')[1]
    db.insert_app(bundle)
    total += 1
    apps += 1

dev_file = open(dev_file_name, 'r')
for dev in dev_file:
    url = dev.rstrip()
    dev_id = url.split('=')[1]
    db.insert_developer(dev_id)
    total += 1
    devs += 1

page_file = open(page_file_name, 'r')
for page in page_file:
    url = page.rstrip()
    db.insert_page(url)
    total += 1
    pages += 1

Log.log(
    "Insert " +
    str(total) + " rows (" +
    str(apps) + " apps, " +
    str(devs) + " developers, " +
    str(pages) + " pages)")




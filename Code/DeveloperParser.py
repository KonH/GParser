from Database import DB
from Logger import Log
from Parser import Parser
from Common import Common

class DeveloperParser:
    def __init__(self, _db):
        self.db = _db

    def convert_name(self, dev_id):
        return "https://play.google.com/store/apps/developer?id=" + dev_id

    def get_developers(self):
        return self.db.get_developers()

    def process_all(self):
        developers = self.get_developers()
        Log.log("Process " + str(len(developers)) + " developers.")
        count = len(developers)
        index = 0
        new_links = 0
        for dev in developers:
            percent = round((index / count) * 100, 2)
            Log.log("Process progress: " + str(percent) + "% " + str(index) + "/" + str(count))
            new_links += self.process(dev[1])
            Common.Wait()
            index += 1
        Log.log("Process complete (" + str(new_links) + " new links)")

    def process(self, dev_id):
        link = self.convert_name(dev_id)
        Log.log("Current devloper is " + str(dev_id) + "(" + link + ")")
        links = Parser.get_app_links_from_page(link)
        if links != -1:
            new_links = []
            for link in links:
                insert_result = db.insert_app(link)
                if insert_result == 1:
                    new_links.append(link)
            Log.log("Found " + str(len(links)) + " links")
            Log.log("New links: " + str(len(new_links)) + " " + str(new_links))
            return len(new_links)
        else:
            Log.log("Page not found!")
            return 0

db = DB()
dp = DeveloperParser(db)
dp.process_all()
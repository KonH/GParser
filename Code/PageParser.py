from Database import DB
from Logger import Log
from Parser import Parser


class PageParser:

    def __init__(self, _db):
        self.db = _db

    def process(self):
        page = self.db.select_page(24)
        current_link = page[1]
        Log.log("Current link is '" + current_link + "'")
        links = Parser.get_links_from_page(current_link)
        if links != -1:
            new_links = []
            for link in links:
                insert_result = db.insert_app(link)
                if insert_result == 1:
                    new_links.append(link)
            Log.log("Found " + str(len(links)) + " links")
            Log.log("New links: " + str(len(new_links)) + " " + str(new_links))
        else:
            Log.log("Page not found!")

db = DB()
pp = PageParser(db)
pp.process()
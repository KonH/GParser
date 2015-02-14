from Database import DB
from Logger import Log
from Parser import Parser
from Common import Common


class PageParser:

    def __init__(self, _db):
        self.db = _db

    def get_pages(self):
        return self.db.get_pages()

    def process_all(self):
        pages = self.get_pages()
        Log.log("Process " + str(len(pages)) + " pages.")
        new_links = 0
        for page in pages:
            new_links += self.process(page[1])
            Common.Wait()
        Log.log("Process complete (" + str(new_links) + " new links)")

    def process(self, url):
        current_link = url
        Log.log("Current link is '" + current_link + "'")
        links = Parser.get_app_links_from_page(current_link)
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
pp = PageParser(db)
pp.process_all()
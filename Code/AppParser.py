from Database import DB
from Logger import Log
from Parser import Parser
from Common import Common
from htmldom import htmldom

class AppParser:
    def __init__(self, _db):
        self.db = _db

    def get_url(self, bundle):
        return "https://play.google.com/store/apps/details?id=" + bundle

    def get_info(self, bundle):
        page_content = Parser.get_page_content(self.get_url(bundle))

        dom = htmldom.HtmlDom()
        dom.createDom(page_content)
        details_info = dom.find('div[class="details-info"]')
        cover_container = details_info.find('div[class="cover-container"]')
        icon_img = cover_container.find("img")

        # Icon
        icon = icon_img.attr("src")
        print("Icon: " + icon)

        # Name
        info_container = details_info.find('div[class="info-container"]')
        document_title = info_container.find('div[class="document-title"]')
        name_div = document_title.find("div")
        name = name_div.text()
        print("Name: " + name)

        # Category
        # TODO
        #category = info_container.find('div#href')
        #print("Category: " + str(category.html()))
        #<a class="document-subtitle category" href="/store/apps/category/GAME_ACTION"> <span itemprop="genre">Экшен</span> </a>

        # Description
        # TODO: Optimization find
        # TODO: Safe assignment
        description = dom.find('div[class="id-app-orig-desc"]')
        print("Description: " + description.text())

        # Recent changes
        recent_changes = dom.find('div[class="recent-change"]')
        print("Recent changes: " + recent_changes.text())

        # Version


ap = AppParser(DB())
ap.get_info("us.kr.runandfly")

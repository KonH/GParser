from Logger import Log
import urllib.request
import urllib.error
import re

class Parser:
    @staticmethod
    def get_links_from_page(url):
        page_content = Parser.get_page_content(url)
        if page_content == -1:
            return -1
        else:
            return Parser.get_links(page_content)

    @staticmethod
    def get_page_content(url):
        try:
            response = urllib.request.urlopen(url)
            return response.read().decode("utf-8", "strict")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return -1
            else:
                Log.log_ex("get response")
        except:
            Log.log_ex("get response")
        return None

    @staticmethod
    def get_links(page_content):
        try:
            p = re.compile('\"(/store/apps/details\?id=[a-zA-Z.]*)\"|\"(/store/apps/developer\?id=[a-zA-Z.]*)\"')
            result = re.findall(p, page_content)
            raw_idlist = []
            for groups in result:
                for line in groups:
                    if line != "" and line not in raw_idlist:
                        raw_idlist.append(line)
            id_list = []
            for line in raw_idlist:
                if "/apps/developer" not in line:
                    bundle = line
                    bundle = bundle.replace("/store/apps/details?id=", '')
                    id_list.append(bundle)
            return id_list
        except:
            Log.log_ex("get links")
            return []
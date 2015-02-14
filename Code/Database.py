from Logger import Log
import pymysql


class DB:
    use_password = False
    db_host = 'localhost'
    db_port = 3306
    db_name = 'gparser'
    user_name = 'root'
    user_password = 'oJfcrRaMHac4mBsyzdpk'

    def __init__(self):
        try:
            if self.use_password:
                self._connection = \
                    pymysql.connect(
                        host=self.db_host,
                        port=self.db_port,
                        user=self.user_name,
                        db=self.db_name,
                        passwd=self.user_password,
                        charset='utf8')
            else:
                self._connection = \
                    pymysql.connect(
                        host=self.db_host,
                        port=self.db_port,
                        user=self.user_name,
                        db=self.db_name,
                        charset='utf8')
            self._connection.encoding = "utf8"
            self._connection.autocommit(True)
            self._cursor = self._connection.cursor()
        except:
            Log.log_ex("Open connection")

    def test(self):
        try:
            self._cursor.execute("SHOW TABLES;")
            Log.log("Connection is valid.")
            return True
        except:
            Log.log_ex("Test connection")
            return False

    def get_pages(self):
        try:
            self._cursor.execute("SELECT * FROM page")
            result = []
            for val in self._cursor:
                result.append(val)
            return result
        except:
            Log.log_ex("get pages")
            return []

    def select_page(self, id):
        try:
            self._cursor.execute("SELECT * FROM page WHERE page_id = " + pymysql.escape_string(str(id)))
            result = None
            for val in self._cursor:
                result = val
            return result
        except:
            Log.log_ex("select page")


    def get_developers(self):
        try:
            self._cursor.execute("SELECT * FROM developer")
            result = []
            for val in self._cursor:
                result.append(val)
            return result
        except:
            Log.log_ex("get developers")
            return []

    def select_developer(self, id):
        try:
            self._cursor.execute("SELECT * FROM developer WHERE developer_id = " + pymysql.escape_string(str(id)))
            result = None
            for val in self._cursor:
                result = val
            return result
        except:
            Log.log_ex("select developer")

    def insert_app(self, bundle):
        try:
            self._cursor.execute("INSERT INTO app(bundle) VALUES(\"" + pymysql.escape_string(bundle) + "\")")
            Log.log("Insert app complete.")
            return 1
        except pymysql.err.IntegrityError:
            return -1
        except:
            Log.log_ex("insert app")
            return 0

    def insert_developer(self, dev_id):
        Log.log("Insert developer: " + dev_id)
        try:
            self._cursor.execute("INSERT INTO developer(dev_page_id) VALUES(\"" + pymysql.escape_string(dev_id) + "\")")
            Log.log("Insert developer complete.")
            return 1
        except pymysql.err.IntegrityError:
            return -1
        except:
            Log.log_ex("insert developer")
            return 0

    def insert_page(self, url):
        Log.log("Insert page: " + url)
        try:
            self._cursor.execute("INSERT INTO page(page_url) VALUES(\"" + pymysql.escape_string(url) + "\")")
            Log.log("Insert page complete.")
            return 1
        except pymysql.err.IntegrityError:
            return -1
        except:
            Log.log_ex("insert page")
            return 0

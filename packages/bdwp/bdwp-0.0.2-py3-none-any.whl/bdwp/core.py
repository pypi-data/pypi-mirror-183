from cloudscraper import create_scraper
import requests.adapters
import re


class BDWP:
    download_useragent = "LogStatistic"
    
    def _getSignCore(self, surl):
        url = "https://pan.baidu.com/share/tplconfig?surl={}&fields=sign,timestamp&channel=chunlei&web=1&app_id=250528&clienttype=0".format(surl)
        headers = {
            "user-agent": "netdisk",
            "cookie": "BDUSS={}; STOKEN={}".format(self.BDUSS, self.STOKEN)
        }
        return self.s.get(url, headers=headers)

    def getSignCore(self, surl):
        return self._getSignCore(surl).json()

    def _getList(self, code, pw, path):
        url = "https://pan.baidu.com/share/wxlist?channel=weixin&version=2.2.2&clienttype=25&web=1"
        headers = {
            "user-agent": "netdisk",
            "cookie": "BDUSS={}; STOKEN={}".format(self.BDUSS, self.STOKEN)
        }
        return self.s.post(url, data={
            "shorturl": "1"+code,
            "dir": path,
            "root": "0" if path else "1",
            "pwd": pw,
            "page": "1",
            "num": "9999",
            "order": "time",
        }, headers=headers)

    def getList(self, code, pw, path):
        return self._getList(code, pw, path).json()

    def _getDlink(self, fs_id, ts, sign, randsk, share_id, uk, appid=250528):
        url = "https://pan.baidu.com/api/sharedownload?app_id={}&channel=chunlei&clienttype=12&sign={}&timestamp={}&web=1".format(
            appid,
            sign,
            ts
        )
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.514.1919.810 Safari/537.36",
            "Cookie": self.cookies,
            "Referer": "https://pan.baidu.com/disk/home",
        }
        r = self.s.post(url, data={
            "encrypt": "0",
            "extra": '{"sekey":"'+randsk+'"}',
            "fid_list": "[{}]".format(fs_id),
            "primaryid": share_id,
            "uk": uk,
            "product": "share",
            "type": "nolimit",
        }, headers=headers)
        return r

    def getDlink(self, fs_id, ts, sign, randsk, share_id, uk, appid=250528):
        return self._getDlink(fs_id, ts, sign, randsk, share_id, uk, appid=appid).json()

    def getFiles(self, code, pw, path, cb=None):
        lists = self.getList(code, pw, path)
        # print(lists)
        randsk = lists["data"]["seckey"]
        share_id = lists["data"]["shareid"]
        uk = lists["data"]["uk"]
        # print(randsk, share_id, uk)
        for _ in lists["data"]["list"]:
            if int(_["isdir"]) == 1:
                print(_["path"])
                self.getFiles(code, pw, _["path"], cb)
            else:
                r = self.getFile(code, randsk, share_id, uk, _)
                callable(cb) and cb(r)

    def getFile(self, code, randsk, share_id, uk, item):
        signcore = self.getSignCore("1"+code)
        ts = signcore["data"]["timestamp"]
        sign = signcore["data"]["sign"]
        fs_id = item["fs_id"]
        dlink = self.getDlink(fs_id, ts, sign, randsk, share_id, uk)
        # print(dlink)
        r = self.s.head(dlink["list"][0]["dlink"], headers={
            "Cookie": "BDUSS={}".format(self.BDUSS)
        }, allow_redirects=False)
        return {
            "url": r.headers["Location"],
            "path": "/".join(item["path"].split("/")[:-1]),
            "name": item["server_filename"],
            "size": item["size"],
            "md5": item["md5"],
        }

    def __init__(self, cookies, source_address=None):
        self.cookies = cookies
        self.BDUSS = cookies.split("BDUSS=")[1].split(";")[0]
        self.STOKEN = cookies.split("STOKEN=")[1].split(";")[0]
        s = create_scraper()
        if source_address:
            for prefix in ('http://', 'https://'):
                s.get_adapter(prefix).init_poolmanager(
                    connections=requests.adapters.DEFAULT_POOLSIZE,
                    maxsize=requests.adapters.DEFAULT_POOLSIZE,
                    source_address=(source_address, 0),
                )
        self.s = s

    def extract_code_pw(self, url):
        m = re.search(r"/s/1([a-zA-Z0-9\-\_]{22})(?:\?pwd=([a-zA-Z0-9]{4}))?$", url)
        if not m:
            m = re.search(r"/share/init\?surl=([a-zA-Z0-9\-\_]{22})(?:&pwd=([a-zA-Z0-9]{4}))?$", url)
            if not m:
                raise
        return m.groups()



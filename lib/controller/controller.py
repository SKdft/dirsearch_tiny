#
#
from queue import Queue
from thirdparty import requests
from lib.connection.requester import Requester
from lib.dict_parse.dict_parse import Dictparse
from lib.url_path.url_path_extract import Urlextract


class Controller(object):
    def __init__(self):
        self.targets = Queue()
        self.dict_result = []
        self.url_path_num = 0
        self.url_path_result = {}

    def run(self,url):
        # while not self.targets.empty():
        #     url = self.targets.get()
        self.dictparse = Dictparse("1.txt")
        self.urlextract = Urlextract("1.txt")

        self.urlextract.url_path_extract(self.url_path_num)
        self.dict_result = self.dictparse.dict_input()

        self.requester = Requester(
            url
        )

        request = requests.Request(
            "get",
            url=url,
        )

        prepare = request.prepare()
        prepare.url = url

        r = self.requester.send(prepare)
        resp_size = size = sum(len(chunk) for chunk in r.iter_content(8196))
        print(self.dict_result)
        print("[+]{0} {1} {2}".format(url,r.status_code,resp_size))
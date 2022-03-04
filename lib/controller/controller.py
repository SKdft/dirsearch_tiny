#
#
from queue import Queue
from thirdparty import requests
from lib.connection.requester import Requester


class Controller(object):
    def __init__(self):
        self.targets = Queue()
        self.run()

    def run(self):
        # while not self.targets.empty():
        #     url = self.targets.get()
        url = "http://xinwen.eastday.com/a/"
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
        print(r)
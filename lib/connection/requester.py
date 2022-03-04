from collections import OrderedDict
from thirdparty import requests

class Requester(object):
    def __init__(
            self,
            url
    ):
        self.adapters = OrderedDict()
        self.url = url

    def send(self, request, **kwargs):

        adapter = self.get_adapter(url=request.url)
        r = adapter.send(request,**kwargs)
        return r

    def get_adapter(self, url):
        for (prefix, adapter) in self.adapters.items():

            if url.lower().startswith(prefix.lower()):
                return adapter
            return adapter
        #raise InvalidSchema("No connection adapters were found for {!r}".format(url))
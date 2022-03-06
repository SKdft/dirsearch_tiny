from collections import OrderedDict
from thirdparty import requests
from thirdparty.requests.adapters import HTTPAdapter

__attrs__ = [
    'headers', 'cookies', 'auth', 'proxies', 'hooks', 'params', 'verify',
    'cert', 'adapters', 'stream', 'trust_env',
    'max_redirects',
]

class Requester(object):
    def __init__(
            self,
            url
    ):
        self.adapters = OrderedDict()
        self.mount('https://', HTTPAdapter())
        self.mount('http://', HTTPAdapter())
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

    def mount(self, prefix, adapter):
        """Registers a connection adapter to a prefix.

        Adapters are sorted in descending order by prefix length.
        """
        self.adapters[prefix] = adapter
        keys_to_move = [k for k in self.adapters if len(k) < len(prefix)]

        for key in keys_to_move:
            self.adapters[key] = self.adapters.pop(key)

    def __getstate__(self):
        state = {attr: getattr(self, attr, None) for attr in self.__attrs__}
        return state

    def __setstate__(self, state):
        for attr, value in state.items():
            setattr(self, attr, value)

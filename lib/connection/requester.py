from collections import OrderedDict

class Requester(object):
    def __init__(
            self,
            url
    ):
        self.adapters = OrderedDict()



    def get_adapter(self, url):
    """
    Returns the appropriate connection adapter for the given URL.

    :rtype: requests.adapters.BaseAdapter
    """
        for (prefix, adapter) in self.adapters.items():

            if url.lower().startswith(prefix.lower()):
                return adapter
        raise InvalidSchema("No connection adapters were found for {!r}".format(url))
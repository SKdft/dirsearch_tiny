

class Dictparse(object):
    def __init__(
            self,
            dict_route
    ):
        self.dict_route = dict_route,

    def dict_input(self):
        dict_result = []
        dict_route = self.dict_route
        dict_route = r'D:\Tools\pycharm2020\dirsearch_tiny\lib\dict_parse\20220301-tiny.txt'
        f = open(dict_route)
        lines = f.readlines()      #读取全部内容 ，并以列表方式返回
        for line in lines:
            dict_result.append(line.strip('\n'))
            # print(line.strip('\n'))
        return dict_result

import re

class Urlextract(object):
    def __init__(
            self,
            url_route
    ):
        self.url_route = url_route,

    def url_path_extract(self,num):
        url_path_route = r'C:\Users\Admin\Desktop\burp_js_path.txt'
        url_path_url = []
        line_num = num

        f = open(url_path_route)
        lines = f.readlines()
        re_result = re.findall()
        for line in lines[line_num:]:
            line_num = line_num+1
            url_path_url.append(line.strip('\n'))
            print(line.strip('\n'))
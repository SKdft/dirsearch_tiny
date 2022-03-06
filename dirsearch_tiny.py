import sys

if sys.version_info < (3, 7):
    sys.stdout.write("Sorry, dirsearch requires Python 3.7 or higher\n")
    sys.exit(1)

class Program(object):
    def __init__(self,url):
        self.url = url

        from lib.controller.controller import Controller
        con = Controller()
        con.run()


if __name__ == "__main__":
    main = Program("http://180.101.49.11:80/")
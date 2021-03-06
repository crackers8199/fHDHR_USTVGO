import sys
from flask import request
from io import StringIO


class Version_HTML():
    endpoints = ["/version", "/version.html"]
    endpoint_name = "version"

    def __init__(self, fhdhr, page_elements):
        self.fhdhr = fhdhr
        self.page_elements = page_elements

    def __call__(self, *args):
        return self.get(*args)

    def get(self, *args):

        fakefile = StringIO()
        page_elements = self.page_elements.get(request)

        for line in page_elements["top"]:
            fakefile.write(line + "\n")

        fakefile.write("<h4 style=\"text-align: center;\">fHDHR Version Information</h4>")
        fakefile.write("\n")

        fakefile.write("<table class=\"center\" style=\"width:50%\">\n")
        fakefile.write("  <tr>\n")
        fakefile.write("    <th></th>\n")
        fakefile.write("    <th></th>\n")
        fakefile.write("  </tr>\n")

        table_guts = [
                        ["fHDHR", self.fhdhr.version],
                        ["Python", sys.version],
                        ["Operating System", self.fhdhr.config.dict["main"]["opersystem"]],
                        ["Using Docker", self.fhdhr.config.dict["main"]["isdocker"]],
                        ["ffmpeg", self.fhdhr.config.dict["ffmpeg"]["version"]],
                        ["vlc", self.fhdhr.config.dict["vlc"]["version"]]
                    ]

        for item in table_guts:
            fakefile.write("  <tr>\n")
            fakefile.write("    <td>%s</td>\n" % (str(item[0])))
            fakefile.write("    <td>%s</td>\n" % (str(item[1])))
            fakefile.write("  </tr>\n")

        for line in page_elements["end"]:
            fakefile.write(line + "\n")

        return fakefile.getvalue()

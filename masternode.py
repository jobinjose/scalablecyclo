import web
import shelve
import os
import sys

urls = (
    '/(.*)/', 'redirect',
    '/(.*)', 'mainclass'
)

class masterapp(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

class mainclass:
    def GET(self,filename):
        s = shelve.open('dir_db')
        try:
            f_dir = s[filename]
        finally:
            s.close()
        fullpath = os.path.join(f_dir, filename)
        f = open(fullpath,"r")
        return f.read()

class redirect:
    def GET(self, path):
        web.seeother('/' + path)

if __name__ == "__main__":
    app = masterapp(urls, globals())
    app.run(port=8866)

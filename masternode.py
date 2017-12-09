import web
import shelve
import os
import git
import sys

urls = (
    '/(.*)/', 'redirect',
    '/mainclass', 'mainclass'
)

class masterapp(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

class mainclass:
    def GET(self):
        return
    def POST(self):
        return

class redirect:
    def GET(self, path):
        web.seeother('/' + path)

if __name__ == "__main__":
    repo = git.Repo("C:/Users/Jobin/Documents/GitHub/mlframework")
    commitlist = list(repo.iter_commits('master'))
    fileincommit = {}
    for commit in commitlist:
        fileincommit[commit.hexsha] = list(commit.stats.files.keys())

    app = masterapp(urls, globals())
    app.run(port=8080)

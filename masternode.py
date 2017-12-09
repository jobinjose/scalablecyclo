import web
import shelve
import os
import git
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
    def GET(self):
        return
    def POST(self):
        return

class redirect:
    def GET(self, path):
        web.seeother('/' + path)

if __name__ == "__main__":
    repo = git.Repo("C:/Users/Jobin/Documents/GitHub/carousel")
    commits_list = list(repo.iter_commits('master'))
    i=1
    for commit in commits_list:
        for file_key in commit.stats.files.keys():
            web.config.filelist_per_commit[i] = [commit.hexsha,file_key]
            i=i+1
    print(len(web.config.filelist_per_commit))

    app = masterapp(urls, globals())
    app.run(port=8080)

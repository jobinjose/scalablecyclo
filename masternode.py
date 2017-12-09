import web
import os
import git
import sys
import requests

urls = (
    '/(.*)/', 'redirect'
    '/mainclass', 'mainclass'
    '/register','register'
    '/finish','finish'
)

class masterapp(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

class mainclass:
    def GET(self):
        return
    def POST(self):
        workerip = web.input(hostid='',port='')
        jobdesc = fileincommit[workerid]
        workerid = workerid+1
        url = "http://" + str(workerip.hostid) + ":"+ str(workerip.port)+":/worker?id="+str(jobdesc[0])+"&filename="+str(jobdesc[1])
        requests.get(url)
        return "Work alloted..."

class redirect:
    def GET(self, path):
        web.seeother('/' + path)

class register:
    def GET(self):
        return

    def POST(self):
        workernum = workernum + 1
        return "Worker active..."

class finish:
    def GET(self):
        return

    def POST(self):
        cyclomatic_complexity = web.input(cc='')
        finish_count = finish_count+1
        cc_total = cc_total + int(cyclomatic_complexity.cc)
        if finish_count == len(fileincommit):
            cc_average = cc_total/finish_count
        return "Result received..."

if __name__ == "__main__":
    repo = git.Repo("C:/Users/Jobin/Documents/GitHub/mlframework")
    commitlist = list(repo.iter_commits('master'))
    i=1
    fileincommit = {}
    finish_count = 0
    workernum = 0
    workerid=1
    cc_total = 0
    for commit in commitlist:
        for j in commit.stats.files.keys():
            fileincommit[i] = [commit.hexsha,j]
            i=i+1

    app = masterapp(urls, globals())
    app.run(port=8080)

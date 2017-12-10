import web
import os
import git
import threading
import requests

repoURL = "C:/Users/Jobin/Documents/GitHub/distributedFS"

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
        if web.config.workerid <= len(web.config.filelist_per_commit):
            web.config.lock.acquire()
            jobdesc = web.config.fileincommit[web.config.workerid]
            web.config.workerid = web.config.workerid+1
            web.config.lock.release()
            url = "http://" + str(workerip.hostid) + ":"+ str(workerip.port)+":/worker?id="+str(jobdesc[0])+"&filename="+str(jobdesc[1])+"&repoURL="+str(repoURL)
            print(url)
            requests.get(url)
            return "Work alloted..."
        else:
            return "No work now..."

class redirect:
    def GET(self, path):
        web.seeother('/' + path)

class register:
    def GET(self):
        web.config.workernum = web.config.workernum+1
        return "Worker active..."
    def POST(self):
        return

class finish:
    def GET(self):
        return

    def POST(self):
        cyclomatic_complexity = web.input(cc='')
        web.config.lock.acquire()
        web.config.finish_count = web.config.finish_count+1
        web.config.cc_total = web.config.cc_total + float(cyclomatic_complexity.cc)
        web.config.lock.release()
        print("len(web.config.fileincommit)",len(web.config.fileincommit))
        print("Recieved CC",cyclomatic_complexity.cc)
        print("web.config.finish_count",web.config.finish_count)
        if web.config.finish_count >= len(web.config.fileincommit):
            cc_average = web.config.cc_total/web.config.finish_count
            print("Average CC: ",cc_average)
        return "Result received..."


if __name__ == "__main__":
    repo = git.Repo(repoURL)
    commitlist = list(repo.iter_commits('master'))
    i=1
    fileincommit = {}
    finish_count = 0
    workernum = 0
    workerid=1
    cc_total = 0
    web.config.update({"workernum":0, "fileincommit" : {},"workerid":1,"finish_count" : 0,"cc_total" : 0,"lock": threading.Lock()})
    for commit in commitlist:
        for filekey in commit.stats.files.keys():
            if os.path.splitext(filekey)[1] not in [".txt",".md",".pdf",".csv",".pyc",""]:
                web.config.fileincommit[i] = [commit.hexsha,filekey]
                i=i+1
    print(len(web.config.fileincommit))

    app = masterapp(urls, globals())
    app.run(port=8080)

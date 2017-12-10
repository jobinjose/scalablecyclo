import web
import shelve
import os
import git
import sys
import lizard
import requests
import threading

class workerapp(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

class workerappthread(threading.Thread):
    def run (self):
        urls = (
            '/worker','worker'
        )
        app = workerapp(urls, globals())
        app.run(port=port)

class worker:
    def GET(self):
        fileobject = web.input(id='',filename="")
        repo = git.Repo(fileobject.repoURL)
        filecontent = repo.git.show("%s:%s" % (fileobject.id, fileobject.filename))
        with open(fileobject.filename,"w") as tf:
            tf.write(file_content)
        tf.close()
        i = lizard.analyze_file(fileobject.filename)
        os.remove(fileobject.filename)
        print("Average CC",i.average_cyclomatic_complexity)
        url = "http://localhost:8080/finish?cc="+str(i.average_cyclomatic_complexity)
        finish_reply = requests.post(url)

    def POST(self):
        return

if __name__ == "__main__":
    host = sys.argv[1]
    port = int(sys.argv[2])
    workerappthread().start()
    while True:
        resp = requests.get("http://localhost:8080/register/")
        print(resp.text)
        if resp.text == 'Worker active...':
            url = "http://localhost:8080/master?hostid="+str(host)+"&port="+str(port)
            print(url)
            response = requests.post(url)
            if response.text == 'No work now...':
                break;

    print("Standby...")

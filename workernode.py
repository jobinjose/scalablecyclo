import web
import shelve
import os
import git
import sys
import lizard
import requests

urls = (
    '/worker','worker'
)

class workerapp(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

class worker:
    def GET(self):
        print("hey")
        fileobject = web.input(id='',filename="")
        repo = git.Repo("C:/Users/Jobin/Documents/GitHub/mlframework")
        filecontent = repo.git.show("%s:%s" % (fileobject.id, fileobject.filename))
        with open(fileobject.filename,"w") as tf:
            tf.write(file_content)
        tf.close()
        i = lizard.analyze_file(fileobject.filename)
        os.remove(fileobject.filename)
        print(i.average_cyclomatic_complexity)
        url = "http://localhost:8080/finish?cc="+str(i.average_cyclomatic_complexity)
        finish_reply = requests.post(url)

    def POST(self):
        return

if __name__ == "__main__":
    host = sys.argv[1]
    port = int(sys.argv[2])
    app = workerapp(urls, globals())
    app.run(port=port)
    resp = requests.post("http://localhost:8080/register/")
    if register.response == 'Worker active...':
        url = "http://localhost:8080/master?hostid="+str(host)+"&port="+str(port)
        requests.post(url)

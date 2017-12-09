import web
import shelve
import os
import git
import sys
import lizard

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
        print("hey")
        return i.average_cyclomatic_complexity

    def POST(self):
        return

if __name__ == "__main__":
    port = int(sys.argv[1])
    app = workerapp(urls, globals())
    app.run(port=port)

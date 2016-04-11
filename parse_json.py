import tornado.ioloop, tornado.web
import json

with open('mlb.json') as data_file:
    data = json.load(data_file)

class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h3>Simple Parsing</h3><br/><p>This is a simple parsing of a json file using Python with Tornado web server.</p>")
        for team in data['mlb_teams']:
            self.write("<b>Team:</b> " + team["name"] + " <b>City:</b> " + team['city'] + "<br/>")

        data

		
application = tornado.web.Application([ (r"/", Handler) ])

def startTornado():
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

def stopTornado():
    tornado.ioloop.IOLoop.instance().stop()

if __name__ == "__main__":
    import time, threading
    threading.Thread(target=startTornado).start()
    print("Your web server will self destruct in 2 minutes")
    time.sleep(120)
    stopTornado()
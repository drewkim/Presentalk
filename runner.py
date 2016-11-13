import parse
import threading
import time
from flask import Flask, jsonify
import init_imgs
import init_text
 
app = Flask(__name__)

class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """
    d = {'current_slide': 1, 'url': ''}
    # current_slide = 1
    # url = ''

    def __init__(self, interval=0.1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        #self.images = init_imgs.get() # save API calls for now
        self.images = {}
        self.text = init_text.get()
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            current = parse.parse(self.images, self.text)
            if type(current) == str:
                self.d['url'] = current
            else:
                self.d['url'] = ''
                if current != 0:
                    if current == -1:
                	    self.d['current_slide'] = self.d['current_slide'] + 1
                    elif current == -2:
                        self.d['current_slide'] = self.d['current_slide'] - 1
                    else:
                        self.d['current_slide'] = current
                    time.sleep(self.interval)
                print(self.d['current_slide'])


example = ThreadingExample()

@app.route('/display/')
def display():
    return jsonify(example.d)

@app.route('/viewer/')
def viewer():
    return app.send_static_file('viewer.html')

time.sleep(3)
print('Checkpoint')
time.sleep(2)
print('Bye')


if __name__ == '__main__':
  app.run()
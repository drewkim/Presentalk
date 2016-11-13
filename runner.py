import parse
import threading
import time
from flask import Flask, jsonify
import init_imgs
 
app = Flask(__name__)

class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """
    current_slide = 1

    def __init__(self, interval=0.1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        #self.images = init_imgs.get() # save API calls for now
        self.images = None
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            current = parse.parse(self.images)
            if current != 0:
                if current == -1:
            	    self.current_slide = self.current_slide + 1
                elif current == -2:
                    self.current_slide = self.current_slide -1
                else:
                    self.current_slide = current
                time.sleep(self.interval)
            print(self.current_slide)

    

example = ThreadingExample()

@app.route('/display/')
def display():
	return jsonify(example.current_slide)

time.sleep(3)
print('Checkpoint')
time.sleep(2)
print('Bye')


if __name__ == '__main__':
  app.run()
import threading

class SpinBar:
    def __init__(self, value_limit=None):
        self.value = 1
        self.rotation_state = 0 
        self.started = False
        self.seconds = 0
        self.stop_timer = False
        self.value_limit = value_limit
        
    def display(self):
        for v in range(self.value - 1):
            print('-', end='')
        rot_map = {
            0: '-',
            1: '\\',
            2: '|',
            3: '/',
            
            
        }
        c = rot_map[self.rotation_state]
        print(c, end='')
        print('\r', end='')
    def end_timer(self):
        self.stop_timer = False
    def finish(self):
        for v in range(self.value - 1):
            print('-', end='')
        rot_map = {
            0: '-',
            1: '\\',
            2: '|',
            3: '/',
            
            
        }
        c = rot_map[self.rotation_state]
        print(c, end='')
    def next(self):
        if not self.started:
            self.started = True
            self.display()
        self.rotation_state += 1
        if self.rotation_state > 3:
            self.rotation_state = 0
            self.value += 1
        if self.value_limit is not None:
            if self.value > self.value_limit:
                self.value = 1
        self.display()
        
    def start_timer(self, interval):
        while self.seconds < interval and not self.stop_timer:
            timer = threading.Timer(interval, self.next)
            timer.start()
        
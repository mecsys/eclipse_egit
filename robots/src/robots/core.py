class Robot(object):    
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._moves = 0

    
    def walk(self, x, y):
        self._moves += 1  
        self._x += x
        self._y += y

    
    def get_pos(self):
        return self._x, self._y

    
    def print_mood(self):
        if self._moves < 2:
            print 'Brand new'
        else:
            print 'Tired alredy'
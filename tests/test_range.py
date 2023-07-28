from quickbar import Quickbar
from time import sleep

def basic(n: int = 1000):
    it = range(n)
    x = 0
    
    for i in Quickbar.track(it):
        x = 3
        sleep(0.01)        
    assert x == 3
        
        
        
if __name__ == '__main__':
    basic()
from quickbar import Quickbar
from time import sleep

def basic(n: int = 500):
    it = ( i%32 for i in range(n) )
    x = 0
    
    for i in Quickbar.track(it):
        x = 3 / 2032 - 123 + 44
        x = x % 32 + 555 + 3**4
        x = 3
        sleep(0.01) # big compute
        
    assert x == 3
        
        
        
if __name__ == '__main__':
    basic()
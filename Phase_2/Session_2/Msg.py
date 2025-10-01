from time import time
from rich.console import Console
console = Console()
def send_Msg(msg):
    if isinstance(msg, BaseMsg):
        console.print(msg, style=msg.style)
    else:
        print(msg)


class BaseMsg:
    def __init__(self, data: str):
        self._data = data
    
    @property
    def style(self):
        return '' # BaseMsg-specific
        
    @property
    def data(self):
        return self._data
    
    def __str__(self):
        return self.data # BaseMsg-specific
    
    def __len__(self):
        return len(self._data)
    def __eq__(self, other):
        if isinstance(other,self.__class__):
            return self.data== other.data
        else:
            return False
         
    def __add__(self, other):
            return self.__class__(self.data+ other)

class LogMsg(BaseMsg):
    def __init__(self, data):
        super().__init__(data)
        self._timestamp: int = int(time())
    def __str__(self):
        return f"{self._timestamp} {self.data}"
    @property
    def style(self):
        return "on yellow"


class WarnMsg(LogMsg):
    def __init__(self, data):
        super().__init__(data)
    def __str__(self):
        return f"Warn! {self._timestamp} {self.data}"
    @property
    def style(self):
        return "white on red" 

if __name__ == '__main__':
    m1 = BaseMsg('Normal message')
    m2 = LogMsg('Log')
    m3 = WarnMsg('Warning')
    m4=LogMsg('Log')
    send_Msg(m1+" (test)")
    send_Msg(m2+" (test)")
    send_Msg(m3+" (test)")
    print(m1=='Normal message')
    print(m2==m4)

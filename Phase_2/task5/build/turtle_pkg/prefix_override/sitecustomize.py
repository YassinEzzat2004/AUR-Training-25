import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/yassin_ezzat/AUR-Training-25/Phase_2/task5/install/turtle_pkg'

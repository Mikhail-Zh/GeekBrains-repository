import sys
from task_6_6 import read_data

if len(sys.argv) == 1:
    read_data()
elif len(sys.argv) == 2:
    read_data(int(sys.argv[1]))
elif len(sys.argv) == 3:
    read_data(int(sys.argv[1]), int(sys.argv[2]))

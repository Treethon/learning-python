import time, sys
indent = 0 # How many spaces to indent
indent_increasing = True #Whether indentation is increasing or not

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10th of a second

        if indent_increasing:
            # Increase number of spaces
            indent = indent + 1
            if indent == 20:
                indent_increasing = False

        else: 
            # Decrease the number of spaces
            indent = indent - 1
            if indent == 0:
                # Change direction
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()
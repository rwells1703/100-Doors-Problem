import time

def get_doors_iterational():
    step = 1
    num_doors = 100
    doors = [False] * num_doors

    while step <= num_doors:
        current = step - 1
        while current < num_doors:
            doors[current] = not doors[current]
                
            current += step
        step += 1

    return doors

def get_doors_modulo():
    num_doors = 100
    doors = []

    door = 1
    while door <= num_doors:
        state = False
        
        step = 1
        while step <= num_doors:
            if door % step == 0:
                state = not state
                
            step += 1
            
        doors.append(state)
        door += 1

    return doors

def print_doors(doors):
    i = 0
    while i < len(doors):
        if doors[i]:
            print("Door %s is open" % (i + 1))
        i += 1
        
def time_test(iterations, function, label):
    start_time = time.time()
    
    i = 0
    while i < iterations:
        function()
        i += 1
    print("--- %s took %s seconds per iteration ---" % (label, ((time.time() - start_time)/iterations)))

time_test(1000, get_doors_iterational, "iterational")
time_test(1000, get_doors_modulo, "modulo")

def cache(times):
    def mind(func):
        def memory():
            memory.count += 1  # we track how many times the function has been requested
            if memory.count == 1 or memory.count > times + 1:  # start and end
                memory.x = func() #assign this variable the value of the function
                memory.count = 1
                # for reset the counter
            else:
                print(memory.x)

        # defining variables
        memory.x = ''
        memory.count = 0
        return memory

    return mind





def logFile(log):
    with open("log.txt", "a") as f:
        f.write(log + '\n')

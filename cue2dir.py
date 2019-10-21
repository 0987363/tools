import os,sys


def make(file):
    base = os.getcwd()

    print("start:", file)

    name = os.path.splitext(file)[0]


    cmd = 'mv "' + os.path.join(base, name) + '"* "' + os.path.join(base, name) + '"'
    print("cmd: ", cmd)

    if os.path.exists(name) == False:
        os.mkdir(name)

    os.system(cmd)


def artist(dir):
    os.chdir(dir)

    for file in os.listdir(dir):
        if os.path.splitext(file)[1].lower() == ".cue":
            make(file)
        if os.path.splitext(file)[1].lower() == ".ape":
            make(file)
        if os.path.splitext(file)[1].lower() == ".flac":
            make(file)
        if os.path.splitext(file)[1].lower() == ".wav":
            make(file)



def main():
    dir=sys.argv[1]

    base = os.getcwd()
    for file in os.listdir(dir):
        artist(os.path.join(base, file))








if __name__ == '__main__':
    main()



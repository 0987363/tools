import os,sys

def count_em(valid_path):
   x = 0
   for root, dirs, files in os.walk(valid_path):
       for f in files:
            x = x+1
   return x

def run(dir):
    print ("len:", count_em(dir), " dir:", dir)

    os.chdir(dir)

    cue = ""
    flac=""

    for file in os.listdir("."):
        if os.path.splitext(file)[1].lower() == ".cue":
            cue = file
            continue

        if os.path.splitext(file)[1].lower() == ".ape":
            flac = file
            continue
        if os.path.splitext(file)[1].lower() == ".flac":
            flac = file
            continue
        if os.path.splitext(file)[1].lower() == ".wav":
            flac = file
            continue

    if os.path.splitext(cue)[0] == "" or os.path.splitext(flac)[0] == "":
        print("cue and ape are nil:", cue, flac)
        return

    if os.path.splitext(cue)[0] != os.path.splitext(flac)[0]:
        print("cue and ape not equal:", cue, flac)
        return

    if os.path.getsize(flac) < 90000000:
        print("flac size too small:", os.path.getsize(flac))
        return


    cmd = 'shnsplit -f "' + cue + '" -t "%n" -o flac "' + flac + '"'
    print("run:", cmd)
    os.system(cmd)


def artist(dir):
    os.chdir(dir)
    base = os.getcwd()
    print("start: ", dir)

    for file in os.listdir(dir):
        f = os.path.join(base, file)
        
        if os.path.isfile(f):
            continue

        if count_em(f) < 6:
            run(f)


def main():
    dir=sys.argv[1]

    base = os.getcwd()

    for file in os.listdir(dir):
        artist(os.path.join(base, file))


if __name__ == '__main__':
    main()



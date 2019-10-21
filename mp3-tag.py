import eyed3,os,sys


def load(file):
    audiofile = eyed3.load(file)
    return audiofile





def main():
    dir=sys.argv[1]

    for file in os.listdir(dir):
        if os.path.splitext(file)[1] != ".mp3":
            continue

        audiofile = load(file).tag

        audiofile.tag.artist = u"Integrity"
        audiofile.tag.album = u"Humanity Is The Devil"
        audiofile.tag.album_artist = u"Integrity"
        audiofile.tag.title = os.path.basename(file)
        audiofile.tag.track_num = 2

        audiofile.tag.save()








if __name__ == '__main__':
    main()



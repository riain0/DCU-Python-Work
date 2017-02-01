import sys


def get_best(f):
    try:
        with open(f) as filename:
            name = ""
            best_mark = 0
            for line in filename.readlines():
                lines = line.split()
                mark = lines[0]
                try:
                    mark = int(mark)
                except ValueError:
                    print('Invalid mark %s encountered. Skipping.' % mark)
                    continue
                if best_mark < mark:
                    name = " ".join(lines[1:])
                    best_mark = mark
                elif mark == best_mark:
                    name += ", " + " ".join(lines[1:])

            print('Best student(s): %s' % name)
            print('Best mark: %d' % best_mark)
    except (OSError, IOError):
        print("File %s does not exist." % f)


def main():
    get_best(sys.argv[1])


if __name__ == "__main__":
    main()

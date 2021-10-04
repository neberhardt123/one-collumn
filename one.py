import re
import sys
def main():
    file_path = str(sys.argv[1])
    with open(file_path) as f:
        for x in f:
            x = x.strip()
            y = re.sub(' +',' ', x)
            z = y.replace(' ', '\n')
            print(z)
        f.close()


if __name__ == "__main__":
    main()
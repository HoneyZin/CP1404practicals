import os


def main():
    os.chdir("FilesToSort")
    print(os.getcwd())

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')
        file_extension = extension[1]
        try:
            os.mkdir(file_extension)
        except FileExistsError:
            pass
        print(f"{file_extension}/{filename}")
        os.rename(filename, f"{file_extension}/{filename}")


if __name__ == '__main__':
    main()

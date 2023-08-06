import os

from config.reader import config_reader


class bundle():
    def __init__(self) -> None:
        config = config_reader.get_config_data(
            'module/app.json')['compile_bundle']

        if config == True:
            self.sushi_compile()
            return

        return

    def sushi_compile(self) -> None:
        # install cython in pip quiet mode
        print("[sushi] installing required dependencies: cython")
        os.system('python3 -m pip -q install cython')

        # and compile
        print("[sushi] compiling")

        # create output folder only if it doesnt exists
        if not os.path.exists("sushi"):
            os.mkdir('sushi')

        os.system('python3 -m cython module/main.py -o sushi/main.c --embed')
        os.system(
            'gcc -Os -I/usr/include/python3.8/ sushi/main.c -lpython3.8 -o sushi/output')


if __name__ == "__main__":
    bundle()

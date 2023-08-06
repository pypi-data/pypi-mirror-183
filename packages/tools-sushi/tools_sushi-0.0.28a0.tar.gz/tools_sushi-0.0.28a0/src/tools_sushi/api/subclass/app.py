
class SushiApp(object):
    def __init__(self, keep_alive: bool) -> None:
        self.app()

        # if keep_alive is True wait until user will press 'CTRL + C'
        if keep_alive:
            try:
                while True:
                    pass
            except KeyboardInterrupt:
                exit(0)

    def app(self):
        pass

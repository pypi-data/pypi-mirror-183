import webview as web


class RuCodingerWebsite:
    @staticmethod
    def show():
        web.create_window("RuCodinger", "https://rucodinger.github.io/")
        web.start()

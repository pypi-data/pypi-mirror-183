import webview as web


class RuCodingerVkGroup:
    @staticmethod
    def show():
        web.create_window("RuCodinger | Vk", "https://vk.com/rucodinger/")
        web.start()

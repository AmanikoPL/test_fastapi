import dotenv, os

dotenv.load_dotenv(override=True)


class Parser:
    def __init__(self):
        self.driver = ""
        self.URL = os.getenv("AVITO_URL")

        print("FFFFFF:", self.URL)


parser = Parser()

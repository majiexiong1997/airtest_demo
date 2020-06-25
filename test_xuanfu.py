from main import Main



class Testxuanfu:
    def setup(self):
        self.main = Main()

    def test_xuanfu(self):
        self.main = Main()

        self.main.login().xuanfu()



if __name__ == '__main__':
    Testxuanfu().test_xuanfu()
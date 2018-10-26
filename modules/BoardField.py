class BoardField:
    coin = None
    def set_coin(self, coin, y, x):
        self.coin = coin
        self.coin.y = y
        self.coin.x = x

    def unset_coin(self):
        self.coin = None

    def get_html(self):
        return '' if not self.coin else\
            self.coin.html()

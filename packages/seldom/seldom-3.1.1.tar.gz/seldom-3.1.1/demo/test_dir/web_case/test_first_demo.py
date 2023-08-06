import seldom
from seldom import Steps
from seldom import Seldom
from seldom import ChromeConfig


class BingTest(seldom.TestCase):
    """Bing search test case"""

    def test_case(self):
        """a simple test case """
        self.open("https://cn.bing.com")
        self.set_window(wide=1920, high=1080)
        self.screenshots()
        self.type(id_="sb_form_q", text="seldom", enter=True)
        self.assertTitle("seldom - 搜索")

    # def test_case_two(self):
    #     """method chaining """
    #     Steps(url="https://cn.bing.com").open().find("#sb_form_q").type("seldom").submit()
    #     self.assertTitle("seldom - 搜索")


if __name__ == '__main__':
    ChromeConfig.headless = True
    seldom.main(browser="chrome")  # 设置 debug 模式

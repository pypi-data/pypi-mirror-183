from autotest_tools.log_tool.logtest import LogTest

TAG = "ActionWord"
page_obj_map = {}
page_method_map = {}
page_objs = []


class ActionWord(object):

    @staticmethod
    def execute(driver, page: str, method: str, args: dict = None):
        """
        执行测试用例
        :param driver: 浏览器驱动
        :param page: 页面名
        :param method: 方法名
        :param args: 入参
        :return: PO方法
        """

        def _execute(_page: str):
            if _page:
                LogTest.info(TAG, "创建新对象：{}".format(_page))
                _new_page = page_obj_map.get(page)(driver)
                page_objs.append(_new_page)
            return page_objs[-1]

        page_obj = _execute(page) if page and not page == "" else page_objs[-1]
        po_method = getattr(page_obj, page_method_map.get(method))
        return po_method(args) if args and not args == "" else po_method()

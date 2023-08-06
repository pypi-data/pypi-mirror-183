import time

from autotest_tools.log_tool.logtest import LogTest
from autotest_tools.web_tool.driver import DriverCommon

TAG = "WaitTool"


class WaitCommon(DriverCommon):
    def __init__(self, driver):
        super().__init__(driver)

    def wait(self, seconds):
        """
        等待
        :param seconds: 秒数
        :return: None
        """
        LogTest.debug(TAG, "Wait for {} seconds".format(seconds))
        time.sleep(seconds)

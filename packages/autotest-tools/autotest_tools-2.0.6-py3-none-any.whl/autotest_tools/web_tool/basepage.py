from autotest_tools.web_tool.alert import AlertCommon
from autotest_tools.web_tool.ec import EcCommon
from autotest_tools.web_tool.element import ElementCommon
from autotest_tools.web_tool.keyboard import KeyboardCommon
from autotest_tools.web_tool.mouse import MouseCommon
from autotest_tools.web_tool.ui import UiCommon
from autotest_tools.web_tool.wait import WaitCommon


class BasePage(AlertCommon,
               EcCommon,
               ElementCommon,
               KeyboardCommon,
               MouseCommon,
               UiCommon,
               WaitCommon):
    ...

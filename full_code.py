# encoding="utf-8"
from kivy.config import Config
Config.set("widgets", "scroll_timeout", "50")
Config.set('input', 'mouse', 'mouse,disable_multitouch')
from kivy.base import EventLoop
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.scrollview import ScrollView

import logging
import os


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# handle = logging.FileHandler(os.path.join("data", "log.log"))
handle = logging.StreamHandler()
formatter = logging.Formatter(
    '\n\n=start=\n%(asctime)s - %(funcName)s - %(message)s\n=end=')
logger.addHandler(handle)
handle.setFormatter(formatter)

KV = '''
BoxLayout:
    orientation: "vertical"
    NewSectionEntry:
    RTextInput:
    InnerLvlText:
'''


class RTextInput(TextInput):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs,
                         use_bubble=True,
                         padding=(10, 10))

    def on_touch_down(self, touch):

        super().on_touch_down(touch)
        logger.debug(f'any {touch=}, {self=}')

        if touch.button == 'right':
            logger.debug(f'right {touch=}, {self=}')

            pos = super().to_local(
                touch.pos[0], touch.pos[1], relative=False)
            self._show_cut_copy_paste(
                pos, EventLoop.window, mode='paste')

    def _show_cut_copy_paste(self, *args, **kwargs):
        super()._show_cut_copy_paste(*args, **kwargs)
        logger.debug(f'{args=}, \n{kwargs=}')


class InnerLvlText(RTextInput):
    '''TextInput that shows content of section clicked'''

    def __init__(self, *args, **kwargs):
        super().__init__(text="Techsupport helper",
                         size_hint=(1, None)
                         )


class NewSectionEntry(RTextInput):
    '''Module that contains functionalete to add, delete, rename sections'''

    def __init__(self, *args, **kwargs):

        super().__init__(
                         # multiline=False,
                         readonly=False,
                         halign="left")


class NotMainApp(App):
    def __init__(self):
        super().__init__()

    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    NotMainApp().run()

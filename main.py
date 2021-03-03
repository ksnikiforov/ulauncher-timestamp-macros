import json
import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
import datetime

logger = logging.getLogger(__name__)


class DemoExtension(Extension):

    def __init__(self):
        super(DemoExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        logger.info('preferences %s' % json.dumps(extension.preferences))
        
        today = datetime.date.today().strftime("%d %B, %Y")
        time = datetime.datetime.now().strftime("%H:%M")
        
        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name=f'{time} | {today}',
                                         description='',
                                         on_enter=CopyToClipboardAction(
                                             '{0:%Y-%m-%d %H:%M}'.format(datetime.datetime.now()))))
        
        
        return RenderResultListAction(items)


if __name__ == '__main__':
    DemoExtension().run()

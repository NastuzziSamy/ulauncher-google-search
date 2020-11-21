from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction

from src.functions import search_from_google
from src.items import no_input_item, show_suggestion_items

class GoogleSearchExtension(Extension):
    def __init__(self):
        super(GoogleSearchExtension, self).__init__()

        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument() or str()

        if len(query.strip()) == 0:
            return RenderResultListAction(no_input_item())
            
        return RenderResultListAction(show_suggestion_items([query] + search_from_google(query)))


if __name__ == '__main__':
    GoogleSearchExtension().run()

from asphalt.core import Component, Context
from textual.app import ComposeResult
from textual.widgets import Button, Static
from txl.base import Launcher, MainArea
from txl.hooks import register_component


class LauncherMeta(type(Launcher), type(Static)): pass


class _Launcher(Launcher, Static, metaclass=LauncherMeta):

    def __init__(
        self,
        main_area: MainArea,
    ):
        super().__init__()
        self.main_area = main_area
        self.documents = {}
        self.buttons = []

    def register(self, i: str, document):
        self.documents[i] = document

    def compose(self) -> ComposeResult:
        for k in self.documents.keys():
            button = Button(k, id=k)
            self.buttons.append(button)
            yield button

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        for button in self.buttons:
            button.remove()
        document = self.documents[event.button.id]()
        self.main_area.mount(document)
        await document.open()


class LauncherComponent(Component):

    async def start(
        self,
        ctx: Context,
    ) -> None:
        main_area = await ctx.request_resource(MainArea, "main_area")
        launcher = _Launcher(main_area)
        ctx.add_resource(launcher, name="launcher", types=Launcher)


c = register_component("launcher", LauncherComponent)

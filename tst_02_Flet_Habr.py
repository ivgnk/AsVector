"""
05.08.2024
https://habr.com/ru/articles/677734/
"""
import flet
from flet import (
    AppBar,
    Icon,
    IconButton,
    Page,
    PopupMenuButton,
    PopupMenuItem,
    Text,
    colors,
    icons,
)


def tst_01():
    def main(page: Page):
        def check_item_clicked(e):
            e.control.checked = not e.control.checked
            page.update()

        page.appbar = AppBar(
            leading=Icon(icons.PALETTE),
            leading_width=40,
            title=Text("AppBar Example"),
            center_title=False,
            bgcolor=colors.SURFACE_VARIANT,
            actions=[
                IconButton(icons.WB_SUNNY_OUTLINED),
                IconButton(icons.FILTER_3),
                PopupMenuButton(
                    items=[
                        PopupMenuItem(text="Item 1"),
                        PopupMenuItem(),  # divider
                        PopupMenuItem(
                            text="Checked item",
                            checked=False,
                            on_click=check_item_clicked
                        ),
                    ]
                ),
            ],
        )
        page.add(Text("Body!"))

    flet.app(target=main)

from flet import ElevatedButton, Page, Text, TextField, icons
def tst_02():
    def main(page: Page):
        def button_clicked(e):
            t.value = (
                f"Textboxes values are:  "
                f"'{tb1.value}', "
                f"'{tb2.value}', "
                f"'{tb3.value}', "
                f"'{tb4.value}', "
                f"'{tb5.value}'."
            )
            page.update()

        t = Text()
        tb1 = TextField(label="Standard")
        tb2 = TextField(label="Disabled", disabled=True, value="First name")
        tb3 = TextField(label="Read-only", read_only=True, value="Last name")
        tb4 = TextField(label="With placeholder", hint_text="Please enter text here")
        tb5 = TextField(label="With an icon", icon=icons.EMOJI_EMOTIONS)
        b = ElevatedButton(text="Submit", on_click=button_clicked)
        page.add(tb1, tb2, tb3, tb4, tb5, b, t)

    flet.app(target=main)



if __name__ == "__main__":
    tst_02()

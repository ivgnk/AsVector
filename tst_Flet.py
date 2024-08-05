"""
Flet Examples from
26.06.2023 Гайд по Flet: приступая к работе. Создание приложений на Python
https://www.ixbt.com/live/sw/gayd-po-flet-pristua.html
"""

import time
import flet as ft

def tst_00():
    def main(page: ft.Page):
        # add/update controls on Page
        pass

    ft.app(target=main) # , view=ft.WEB_BROWSER

def tst_01():
    def main(page: ft.Page):
        t = ft.Text(value="Hello, world!", color="green")
        page.controls.append(t)
        page.update()

    ft.app(target=main) # , view=ft.WEB_BROWSER

def tst_02():
    def main(page: ft.Page):
        t = ft.Text()
        page.add(t)  # it's a shortcut for page.controls.append(t) and then page.update()

        for i in range(10):
            t.value = f"Step {i}"
            page.update()
            time.sleep(1)

    ft.app(target=main) # , view=ft.WEB_BROWSER

def tst_03():
    def main(page: ft.Page):
        page.add(
            ft.Row(controls=[
                ft.Text("A"),
                ft.Text("B"),
                ft.Text("C")
            ])
        )

        page.add(
            ft.Row(controls=[
                ft.TextField(label="Your name"),
                ft.ElevatedButton(text="Say my name!")
            ])
        )

    ft.app(target=main) # , view=ft.WEB_BROWSER

def tst_03_1():
    def main(page: ft.Page):
        for i in range(10):
            page.controls.append(ft.Text(f"Line {i}"))
            if i > 4:
                page.controls.pop(0)
            page.update()
            time.sleep(0.3)
    ft.app(target=main)  # , view=ft.WEB_BROWSER

def tst_03_2():
    def main(page: ft.Page):
        t = ft.Text()
        page.add(t)  # it's a shortcut for page.controls.append(t) and then page.update()

        def button_clicked(e):
            page.add(ft.Text("Clicked!"))
        page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

        for i in range(10):
            t.value = f"Step {i}"
            page.update()
            time.sleep(1)

    ft.app(target=main)  # , view=ft.WEB_BROWSER


def tst_04():
    def main(page):
        def add_clicked(e):
            page.add(ft.Checkbox(label=new_task.value))
            new_task.value = ""
            new_task.focus()
            new_task.update()

        new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
        page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

    ft.app(target=main) # , view=ft.WEB_BROWSER

def tst_05():
    def main(page: ft.Page):
        # add/update controls on Page
        # first_name = ft.TextField()
        # last_name = ft.TextField()
        # first_name.disabled = True
        # last_name.disabled = True
        # page.add(first_name, last_name)

        first_name = ft.TextField()
        last_name = ft.TextField()
        c = ft.Column(controls=[
            first_name,
            last_name
        ])
        c.disabled = True
        page.add(c)

    ft.app(target=main) # , view=ft.WEB_BROWSER

def tst_06():
    def main(page: ft.Page):
        first_name = ft.TextField(label="First name", autofocus=True)
        last_name = ft.TextField(label="Last name")
        greetings = ft.Column()

        def btn_click(e):
            greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
            first_name.value = ""
            last_name.value = ""
            page.update()
            first_name.focus()

        page.add(
            first_name,
            last_name,
            ft.ElevatedButton("Say hello!", on_click=btn_click),
            greetings,
        )

    ft.app(target=main)

def tst_06_with_ref():
    def main(page):
        first_name = ft.Ref[ft.TextField]()
        last_name = ft.Ref[ft.TextField]()
        greetings = ft.Ref[ft.Column]()

        def btn_click(e):
            greetings.current.controls.append(
                ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}!")
            )
            first_name.current.value = ""
            last_name.current.value = ""
            page.update()
            first_name.current.focus()

        page.add(
            ft.TextField(ref=first_name, label="First name", autofocus=True),
            ft.TextField(ref=last_name, label="Last name"),
            ft.ElevatedButton("Say hello!", on_click=btn_click),
            ft.Column(ref=greetings),
        )

    ft.app(target=main)

if __name__ == "__main__":
    # tst_00() # +
    # tst_01() # +
    # tst_02() # +
    # tst_03() # +
    # tst_03_1() # +
    # tst_03_2()  # +
    # tst_04() # +
    # tst_05() # +
    # tst_06() # +
    tst_06_with_ref()

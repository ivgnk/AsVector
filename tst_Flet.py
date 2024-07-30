"""
Flet Examples
"""

# 26.06.2023 Гайд по Flet: приступая к работе. Создание приложений на Python
# https://www.ixbt.com/live/sw/gayd-po-flet-pristua.html

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


if __name__ == "__main__":
    tst_04()
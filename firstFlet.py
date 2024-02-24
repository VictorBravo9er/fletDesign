import  flet as ft

def app(page: ft.Page) -> None:
    page.title = "Increment Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.SYSTEM

    text_number: ft.TextField = ft.TextField(value="0", text_align=ft.TextAlign.END)

    def decrement(e: ft.ControlEvent) -> None:
        text_number.value = str(int(text_number.value) - 1)
        page.update()

    def increment(e: ft.ControlEvent) -> None:
        text_number.value = str(int(text_number.value) + 1)
        page.update()

    def close(E: ft.ControlEvent) -> None:
        page.clean()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.CLOSE, on_click=close),
            ],
            alignment=ft.MainAxisAlignment.END
        ),
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=decrement),
                text_number,
                ft.IconButton(ft.icons.ADD, on_click=increment)
            ],
            alignment=ft.MainAxisAlignment.CENTER

        ),

    )

def main():
    ft.app(target=app, view=ft.AppView.WEB_BROWSER)

if __name__ == "__main__":
    main()


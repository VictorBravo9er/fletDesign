import flet as ft

def main(page: ft.Page):
    page.title = "Sign Up"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window_height = 400
    page.window_width = 400
    page.window_resizable = False

    text_uname: ft.TextField = ft.TextField(label="UserName", text_align=ft.TextAlign.LEFT, width=200)
    text_paswd: ft.TextField = ft.TextField(label="Password", text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_sign: ft.Checkbox = ft.Checkbox(label="I agree.", value=False)
    button_submit: ft.ElevatedButton = ft.ElevatedButton(text="sign up", width=200, disabled=True)


    def validate(e: ft.ControlEvent) -> None:
        button_submit.disabled = False if all(
            map(lambda x: x.value, (text_uname, text_paswd, checkbox_sign))
        ) else True

        page.update()

    def submit(e: ft.ControlEvent) -> None:
        print(f"UserName: {text_uname.value}", f"PassWD : {text_paswd.value}", sep="\n")
        page.clean()
        page.add(
            ft.Row(
                [
                    ft.Text(value=f"Welcome {text_uname.value}", size = 20)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )


    checkbox_sign.on_change = validate
    text_paswd.on_change = validate
    text_uname.on_change = validate
    button_submit.on_click = submit

    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        text_uname,
                        text_paswd,
                        checkbox_sign,
                        button_submit,
                    ],
                    alignment=ft.VerticalAlignment.CENTER,
                    expand=True
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        )
    )

if __name__ == '__main__':
    ft.app(target=main)

import flet as ft

def main(page: ft.Page):
    page.title = "เครื่องคิดเลข Flet"
    page.window_width = 300
    page.window_height = 400

    expression = ""

    result_display = ft.Text(value="", size=24, text_align="right")

    def update_display(value):
        nonlocal expression
        expression += value
        result_display.value = expression
        page.update()

    def calculate_result(e):
        nonlocal expression
        try:
            expression = str(eval(expression))
        except:
            expression = "ข้อผิดพลาด"
        result_display.value = expression
        page.update()

    def clear_display(e):
        nonlocal expression
        expression = ""
        result_display.value = ""
        page.update()

    # ปุ่มทั้งหมด
    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"],
    ]

    # แสดงผลลัพธ์
    page.add(
        ft.Container(
            content=result_display,
            alignment=ft.alignment.center_right,
            padding=10,
            height=70
        )
    )

    # สร้างปุ่ม
    for row in buttons:
        row_controls = []
        for btn in row:
            if btn == "=":
                action = calculate_result
            elif btn == "C":
                action = clear_display
            else:
                action = lambda e, b=btn: update_display(b)

            row_controls.append(
                ft.Container(
                    content=ft.ElevatedButton(text=btn, on_click=action),
                    expand=True,
                    padding=5
                )
            )
        page.add(ft.Row(controls=row_controls, expand=True))

# รันแอป
ft.app(target=main)

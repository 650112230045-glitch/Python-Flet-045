import flet as ft
import csv
import os

CSV_FILE = "สมัครเข้าร่วม.csv"

def main(page: ft.Page):
    page.title = "แบบฟอร์มการรับสมัคร"
    page.window_width = 400
    page.window_height = 500

    name = ft.TextField(label="ชื่อ - สกุล", width=300)
    phone = ft.TextField(label="หมายเลขโทรศัพท์", width=300)
    team = ft.TextField(label="ชื่อทีม", width=300)

    def save_data(e):
        if name.value and phone.value and team.value:
            file_exists = os.path.exists(CSV_FILE)
            with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(["ชื่อ-สกุล", "หมายเลขโทรศัพท์", "ชื่อทีม"])
                writer.writerow([name.value, phone.value, team.value])
            name.value, phone.value, team.value = "", "", ""
            page.snack_bar = ft.SnackBar(ft.Text("✅ บันทึกสำเร็จ"))
            page.snack_bar.open = True
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("❌ กรุณากรอกให้ครบ"))
            page.snack_bar.open = True
            page.update()

    page.add(
        ft.Column(
            [
                ft.Text("📋 แบบฟอร์มการรับสมัคร", size=24, weight="bold"),
                name,
                phone,
                team,
                ft.ElevatedButton(text="บันทึก", on_click=save_data),
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=20,
        )
    )

ft.app(target=main)
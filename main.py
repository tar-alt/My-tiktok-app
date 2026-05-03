import flet as ft

def main(page: ft.Page):
    page.title = "TT Downloader Test"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # App ပွင့်ကြောင်း သေချာစေရန် စာသားတစ်ခုပဲ အရင်ပြကြည့်မည်
    page.add(
        ft.Icon(ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN, size=50),
        ft.Text("App အလုပ်လုပ်နေပါပြီ!", size=25, weight="bold"),
        ft.Text("ဒီစာသားပေါ်ရင် ကုဒ်ပြန်ပြင်လို့ရပါပြီ။", size=16)
    )

ft.app(target=main)

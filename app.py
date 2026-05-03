import flet as ft
import requests

def main(page: ft.Page):
    page.title = "TikTok Downloader"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    url_input = ft.TextField(label="TikTok Link", width=300)
    status_label = ft.Text()

    def download_click(e):
        if not url_input.value:
            status_label.value = "Link ထည့်ပါ!"
            page.update()
            return
        
        status_label.value = "ခဏစောင့်ပါ... watermark ဖျောက်နေသည်"
        page.update()

        try:
            api_url = f"https://www.tikwm.com/api/?url={url_input.value}"
            response = requests.get(api_url).json()
            video_url = response['data']['play']
            page.add(ft.ElevatedButton("Video သိမ်းရန် နှိပ်ပါ", icon=ft.icons.DOWNLOAD, on_click=lambda _: page.launch_url(video_url)))
            status_label.value = "အောင်မြင်ပါသည်!"
        except:
            status_label.value = "Error! Link ကိုစစ်ပါ။"
        page.update()

    page.add(
        ft.Text("TT Downloader App", size=25, weight="bold"),
        url_input,
        ft.ElevatedButton("Download", on_click=download_click),
        status_label
    )

ft.app(target=main)
          

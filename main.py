import flet as ft
import requests

def main(page: ft.Page):
    page.title = "TikTok Downloader"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 600

    url_input = ft.TextField(
        label="TikTok Link", 
        width=300,
        hint_text="https://vt.tiktok.com/..."
    )
    status_label = ft.Text()
    download_btn_container = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def download_click(e):
        # အဟောင်းတွေကို ရှင်းထုတ်ပါ
        download_btn_container.controls.clear()
        
        if not url_input.value:
            status_label.value = "Link ထည့်ပါ!"
            status_label.color = ft.colors.RED_400
            page.update()
            return
        
        status_label.value = "ခဏစောင့်ပါ... ရှာဖွေနေသည်"
        status_label.color = ft.colors.BLUE_200
        page.update()

        try:
            # API ခေါ်ယူခြင်း
            api_url = f"https://www.tikwm.com/api/?url={url_input.value}"
            response = requests.get(api_url, timeout=10).json()
            
            # API က အောင်မြင်စွာ ပြန်လာသလား စစ်ဆေးခြင်း
            if response.get('code') == 0:
                video_url = response['data']['play']
                title = response['data'].get('title', 'Video Download')

                status_label.value = "ဗီဒီယို ရှာတွေ့ပါပြီ!"
                status_label.color = ft.colors.GREEN_400
                
                # ဒေါင်းလုဒ် ခလုတ်အသစ် ထည့်ခြင်း
                download_btn_container.controls.append(
                    ft.ElevatedButton(
                        "Video သိမ်းရန် နှိပ်ပါ", 
                        icon=ft.icons.FILE_DOWNLOAD,
                        color=ft.colors.WHITE,
                        bgcolor=ft.colors.PINK_600,
                        on_click=lambda _: page.launch_url(video_url)
                    )
                )
            else:
                status_label.value = "Link မှားနေပုံရသည်။ ပြန်စစ်ပေးပါ။"
                status_label.color = ft.colors.ORANGE_400
                
        except Exception as err:
            status_label.value = f"Error: ချိတ်ဆက်မှု မအောင်မြင်ပါ"
            status_label.color = ft.colors.RED_400
            
        page.update()

    page.add(
        ft.Icon(ft.icons.TIKTOK, size=50, color=ft.colors.PINK_Accent),
        ft.Text("TT Downloader App", size=25, weight="bold"),
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
        url_input,
        ft.ElevatedButton(
            "Download Info", 
            icon=ft.icons.SEARCH,
            on_click=download_click,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
        ),
        status_label,
        download_btn_container
    )

if __name__ == "__main__":
    ft.app(target=main)
    

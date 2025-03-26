import ctypes
import io
import requests
import threading
import win32clipboard
import win32gui
import win32con
from PIL import ImageGrab, Image

# 手动定义 WM_CLIPBOARDUPDATE
WM_CLIPBOARDUPDATE = 0x031D

# API 配置
UPLOAD_URL = "https://img.doufei.eu.org/upload"
AUTH_CODE = "dou_upload"
TOKEN = "4B718BBFBC3C84C998EADB5AC58379385C2E478197C1E67AE6D6AB348975AD21A033B274E3F592FAB1881B3C31342A89"

PARAMS = {
    "authCode": AUTH_CODE,
    "serverCompress": "true",
    "uploadChannel": "telegram",
    "uploadNameType": "default",
}

HEADERS = {
    "pragma": "no-cache",
    "priority": "u=1, i",
    "token": TOKEN,
    "User-Agent": "Apifox/1.0.0 (https://apifox.com)",
    "Accept": "*/*",
    "Connection": "keep-alive",
}

def upload_image(image):
    """在后台线程上传图片"""
    def _upload():
        with io.BytesIO() as output:
            image.save(output, format="PNG")
            image_bytes = output.getvalue()
            files = {"file": ("clipboard.png", image_bytes, "image/png")}
            response = requests.post(UPLOAD_URL, headers=HEADERS, params=PARAMS, files=files)
        print(f"图片上传结果: {response.status_code}, {response.text}")

    threading.Thread(target=_upload, daemon=True).start()  # 开启后台线程

def get_clipboard_image():
    """获取剪贴板中的图片"""
    image = ImageGrab.grabclipboard()
    return image if isinstance(image, Image.Image) else None  # 这里正确使用 `Image.Image`

def win_msg_handler(hwnd, msg, wparam, lparam):
    """Windows 消息回调"""
    if msg == WM_CLIPBOARDUPDATE:  # 使用手动定义的 WM_CLIPBOARDUPDATE
        image = get_clipboard_image()
        if image:
            print("检测到剪贴板图片，后台上传中...")
            upload_image(image)
    return 0

def start_clipboard_listener():
    """启动剪贴板监听"""
    print("启动剪贴板监听（异步上传）...")

    wc = win32gui.WNDCLASS()
    wc.lpfnWndProc = win_msg_handler
    wc.lpszClassName = "ClipboardListenerWindow"
    class_atom = win32gui.RegisterClass(wc)

    hwnd = win32gui.CreateWindow(class_atom, "ClipboardListener", 0, 0, 0, 0, 0, 0, 0, 0, None)

    ctypes.windll.user32.AddClipboardFormatListener(hwnd)
    win32gui.PumpMessages()  # 进入 Windows 消息循环

if __name__ == "__main__":
    start_clipboard_listener()

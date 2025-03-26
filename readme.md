# AutoUploadClipboardImg

## 项目简介
**AutoUploadClipboardImg** 是一个基于 Python 的工具，能够监听 Windows 剪贴板的变化，并自动上传剪贴板中的图片到指定的服务器。

## 功能特点
- **自动监听**：后台运行，无需手动操作，自动检测剪贴板中的图片。
- **异步上传**：使用多线程异步上传图片，确保不会影响系统性能。
- **支持自定义 API**：可更改上传地址及认证参数。
- **轻量级**：基于 `pywin32` 和 `Pillow`，无需额外依赖 GUI 库。

## 环境要求
- Windows 10/11
- Python 3.8 及以上

## 安装步骤
1. **克隆项目**
   ```bash
   git clone https://github.com/doulongfei/autoUploadClipboardImg.git
   cd AutoUploadClipboardImg
   ```

2. **创建虚拟环境（可选）**
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

## 运行方式
```bash
python main.py
```

运行后，程序将在后台监听剪贴板内容，一旦检测到图片，将自动上传。

## 配置项
你可以在 `main.py` 中修改以下参数以适配你的 API：
```python
UPLOAD_URL = "https://img.doufei.eu.org/upload"
AUTH_CODE = "dou_upload"
TOKEN = "your_api_token"
PARAMS = {
    "authCode": AUTH_CODE,
    "serverCompress": "true",
    "uploadChannel": "telegram",
    "uploadNameType": "default",
}
```

## 依赖库
- `pywin32`：用于监听剪贴板变化
- `Pillow`：处理图片数据
- `requests`：用于上传图片到服务器

## 可能遇到的问题及解决方案
1. **`pywin32` 安装失败**
   ```bash
   pip install --upgrade pywin32
   python -m pywin32_postinstall
   ```

2. **监听失败，提示 `WM_CLIPBOARDUPDATE` 错误**
   - 确保 `pywin32` 版本正确，并在代码中手动定义 `WM_CLIPBOARDUPDATE = 0x031D`

3. **无法检测剪贴板中的图片**
   - 可能是 `ImageGrab.grabclipboard()` 返回 `None`，请检查是否有图片被复制。

## 贡献
欢迎提交 PR 或 issue 进行改进！

## 许可证
MIT License

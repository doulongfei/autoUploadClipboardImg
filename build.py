# 打包脚本 build.py
import os
import subprocess
import PyInstaller.__main__

def build_exe():
    # 确保安装了所有依赖
    # subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])

    # PyInstaller 配置
    pyinstaller_args = [
        'main.py',
        '--onefile',          # 打包成单个exe
        '--noconsole',        # 不显示控制台窗口
        '--name=ClipboardImgUploader',  # 输出文件名
        '--icon=NONE',        # 不使用图标
        '--clean',            # 清理临时文件
        '--add-data=requirements.txt;.'  # 包含依赖文件
    ]

    # 执行打包
    PyInstaller.__main__.run(pyinstaller_args)

    print("打包完成！输出文件在 dist 目录")

if __name__ == '__main__':
    build_exe()

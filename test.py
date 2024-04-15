import requests
import io
import sys

def main():
    # GitHub 上檔案的 URL
    github_file_url = "https://github.com/ivan17lai/setup-OTA/blob/main/main.py"

    try:
        # 使用 requests 模組下載檔案內容
        response = requests.get(github_file_url)
        response.raise_for_status()  # 確認是否下載成功

        # 將下載的檔案內容讀取為文字
        file_content = response.text

        eval(file_content)


    except requests.exceptions.RequestException as e:
        print("Error downloading file:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()

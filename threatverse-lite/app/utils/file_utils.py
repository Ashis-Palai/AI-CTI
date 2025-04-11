import aiofiles
import requests

async def save_upload_file(upload_file, destination_path):
    async with aiofiles.open(destination_path, "wb") as buffer:
        content = await upload_file.read()
        await buffer.write(content)

def download_html_from_url(url: str, destination_path: str):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination_path, "w", encoding="utf-8") as f:
            f.write(response.text)
    else:
        raise Exception(f"Failed to fetch HTML from {url} (status code: {response.status_code})")
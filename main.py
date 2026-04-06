from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
import yt_dlp

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    # កូដ HTML នេះសម្រាប់បង្កើតរូបរាងវេបសាយ
    return """
    <html>
        <head><title>GodKing Downloader</title></head>
        <body style="text-align: center; font-family: sans-serif; padding-top: 50px;">
            <h1>GodKing Video Downloader</h1>
            <form action="/download" method="get">
                <input type="text" name="url" placeholder="ផាស Link វីដេអូនៅទីនេះ..." style="width: 300px; padding: 10px;">
                <button type="submit" style="padding: 10px; background: #007bff; color: white; border: none; cursor: pointer;">ទាញយក</button>
            </form>
        </body>
    </html>
    """

@app.get("/download")
def download(url: str):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return RedirectResponse(url=info['url'])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

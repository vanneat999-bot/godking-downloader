from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
import yt_dlp

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html lang="km">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>GodKing Downloader</title>
        <style>
            body { font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background: #0f0f0f; color: white; margin: 0; }
            .card { background: #1e1e1e; padding: 30px; border-radius: 15px; width: 100%; max-width: 400px; text-align: center; border: 1px solid #333; box-shadow: 0 4px 8px rgba(0,0,0,0.5); }
            h2 { margin-top: 0; color: #fff; }
            input { width: 100%; padding: 12px; margin: 15px 0; border-radius: 8px; border: 1px solid #555; background: #333; color: white; box-sizing: border-box; font-size: 14px; }
            button { width: 100%; padding: 12px; background: #ff0000; color: white; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 16px; transition: 0.3s; }
            button:hover { background: #cc0000; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>GodKing Downloader</h2>
            <form action="/download" method="get">
                <input type="text" name="url" placeholder="ផាស Link វីដេអូនៅទីនេះ..." required>
                <button type="submit">ទាញយក (Download)</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.get("/download")
def download(url: str):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'cookiefile': 'cookies.txt',  # ទាញយក Cookies មកប្រើដើម្បីកុំឱ្យ YouTube គិតថាជា Bot
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return RedirectResponse(url=info['url'])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

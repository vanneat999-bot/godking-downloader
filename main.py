from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
import yt_dlp

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return "<h1>GodKing Downloader is Running!</h1>"

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

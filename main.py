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
        <title>GodKing Downloader v2</title>
        <style>
            body { font-family: 'Khmer OS Battambang', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background: #0f0f0f; color: white; margin: 0; }
            .card { background: #1e1e1e; padding: 30px; border-radius: 15px; width: 90%; max-width: 450px; text-align: center; border: 1px solid #333; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
            h2 { margin-top: 0; color: #ff0050; text-transform: uppercase; letter-spacing: 2px; }
            p { color: #aaa; font-size: 14px; }
            input { width: 100%; padding: 15px; margin: 20px 0; border-radius: 10px; border: 1px solid #444; background: #2a2a2a; color: white; box-sizing: border-box; font-size: 14px; outline: none; }
            input:focus { border-color: #ff0050; }
            button { width: 100%; padding: 15px; background: #ff0050; color: white; border: none; border-radius: 10px; font-weight: bold; cursor: pointer; font-size: 16px; transition: 0.3s; }
            button:hover { background: #00f2ea; color: black; }
            .footer { margin-top: 20px; font-size: 12px; color: #555; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>GodKing v2</h2>
            <p>ទាញយកវីដេអូ TikTok (No Watermark) & YouTube</p>
            <form action="/download" method="get">
                <input type="text" name="url" placeholder="ផាស Link វីដេអូនៅទីនេះ..." required>
                <button type="submit">ទាញយកឥឡូវនេះ</button>
            </form>
            <div class="footer">Powered by yt-dlp & FastAPI</div>
        </div>
    </body>
    </html>
    """

@app.get("/download")
def download(url: str):
    # ការកំណត់ដើម្បីដោនឡូត TikTok កុំឱ្យជាប់ Watermark និង YouTube កុំឱ្យ Block
    ydl_opts = {
        'format': 'best', # ជ្រើសរើសគុណភាពល្អបំផុតដែលគ្មាន Watermark សម្រាប់ TikTok
        'quiet': True,
        'no_warnings': True,
        'cookiefile': 'cookies.txt', # ប្រើ Cookies ដើម្បីកុំឱ្យ YouTube ចាប់ថាជា Bot
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info.get('url')
            
            if not video_url:
                raise HTTPException(status_code=404, detail="រកមិនឃើញ Link វីដេអូឡើយ")

            # បញ្ជូនអ្នកប្រើទៅកាន់ Link វីដេអូផ្ទាល់ដែលគ្មាន Watermark
            return RedirectResponse(url=video_url)
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

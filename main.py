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
            body { font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background: #000; color: white; margin: 0; }
            .card { background: #111; padding: 30px; border-radius: 20px; width: 90%; max-width: 400px; text-align: center; border: 1px solid #ff0050; }
            h2 { color: #ff0050; margin-bottom: 20px; }
            input { width: 100%; padding: 15px; margin-bottom: 20px; border-radius: 10px; border: none; background: #222; color: white; }
            button { width: 100%; padding: 15px; background: #ff0050; color: white; border: none; border-radius: 10px; font-weight: bold; cursor: pointer; }
            button:hover { background: #00f2ea; color: black; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>GodKing Downloader</h2>
            <form action="/download" method="get">
                <input type="text" name="url" placeholder="ផាស Link TikTok ឬ YouTube..." required>
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
        'no_warnings': True,
        'cookiefile': 'cookies.txt', # ចាំបាច់បំផុតសម្រាប់ YouTube
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            # សម្រាប់ TikTok វានឹងស្វែងរក Link ណាដែលគ្មាន Watermark ឱ្យអូតូ
            video_url = info.get('url')
            
            if not video_url:
                raise HTTPException(status_code=404, detail="រកមិនឃើញវីដេអូទេ")

            return RedirectResponse(url=video_url)
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")

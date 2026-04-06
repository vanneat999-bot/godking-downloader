import streamlit as st
import yt_dlp
import os

# ការកំណត់រូបរាងវេបសាយ
st.set_page_config(page_title="GODKING DOWNLOADER", page_icon="👑", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    h1 { color: #FF4B4B; text-align: center; text-shadow: 2px 2px #000; font-family: 'Arial'; }
    p { color: #FAFAFA; text-align: center; }
    div.stButton > button:first-child {
        width: 100%;
        height: 50px;
        background-color: #262730;
        color: white;
        border: 2px solid #FF4B4B;
        border-radius: 15px;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #FF4B4B;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>👑 GODKING DOWNLOADER 👑</h1>", unsafe_allow_html=True)
st.markdown("<p>Download Video & Music from YouTube, FB, TikTok, IG</p>", unsafe_allow_html=True)

# ប្រអប់ដាក់ Link
url = st.text_input("", placeholder="បិទភ្ជាប់ Link ទីនេះ (YT, FB, TikTok, IG...)", label_visibility="collapsed")

# មុខងារទាញយកមេ
def download_process(link, is_audio=False):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'nocheckcertificate': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }
    }
    
    if is_audio:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'outtmpl': 'godking_music.mp3',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
        file_name = "godking_music.mp3"
    else:
        ydl_opts.update({
            'format': 'best',
            'outtmpl': 'godking_video.mp4',
        })
        file_name = "godking_video.mp4"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    return file_name

col1, col2 = st.columns(2)

with col1:
    if st.button("🎬 DOWNLOAD VIDEO"):
        if url:
            try:
                with st.spinner("⏳ កំពុងទាញយក Video..."):
                    file = download_process(url, is_audio=False)
                    with open(file, "rb") as f:
                        st.download_button("📥 Save Video", f, file, "video/mp4")
                    os.remove(file)
            except:
                st.error("❌ បរាជ័យ! ប្រហែល Link ខុស ឬ IP ត្រូវបាន Block")
        else: st.warning("សូមដាក់ Link!")

with col2:
    if st.button("🎵 DOWNLOAD MP3"):
        if url:
            try:
                with st.spinner("⏳ កំពុងបំប្លែងជា MP3..."):
                    file = download_process(url, is_audio=True)
                    with open(file, "rb") as f:
                        st.download_button("📥 Save MP3", f, file, "audio/mpeg")
                    os.remove(file)
            except:
                st.error("❌ បរាជ័យ! សូមពិនិត្យមើល packages.txt")
        else: st.warning("សូមដាក់ Link!")

st.markdown("---")
st.markdown("<p style='font-size: 12px; color: gray;'>Powered by GODKING • 2026</p>", unsafe_allow_html=True)

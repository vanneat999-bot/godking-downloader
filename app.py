import streamlit as st
import yt_dlp
import os

# ការកំណត់រូបរាង (Ultimate King Style)
st.set_page_config(page_title="GODKING DOWNLOADER", page_icon="👑", layout="centered")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #0f0c29, #302b63, #24243e); color: white; }
    h1 { text-align: center; color: #FF4B4B; text-shadow: 2px 2px 10px #000; font-size: 45px; }
    p { text-align: center; font-size: 18px; color: #ccc; }
    .stButton>button {
        width: 100%; border-radius: 20px; height: 60px;
        background: linear-gradient(45deg, #FF4B4B, #ff8a05);
        color: white; font-weight: bold; font-size: 18px; border: none;
        transition: 0.3s; box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4);
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0px 6px 20px rgba(255, 75, 75, 0.6); }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>👑 GODKING DOWNLOADER 👑</h1>", unsafe_allow_html=True)
st.markdown("<p>Download Video & Music from YouTube, Facebook, TikTok, Instagram</p>", unsafe_allow_html=True)

url = st.text_input("", placeholder="បិទភ្ជាប់ Link នៅទីនេះ (YT, FB, TikTok...)", label_visibility="collapsed")

# មុខងារ Bypass YouTube & Every Platform
def godking_engine(link, type='video'):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'nocheckcertificate': True,
        '#': 'Bypass YouTube IP Block',
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
        }
    }

    if type == 'music':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'outtmpl': 'godking_music.mp3',
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
        })
        return "godking_music.mp3"
    else:
        ydl_opts.update({
            'format': 'best',
            'outtmpl': 'godking_video.mp4',
        })
        return "godking_video.mp4"

col1, col2 = st.columns(2)

with col1:
    if st.button("🎬 DOWNLOAD VIDEO"):
        if url:
            try:
                with st.spinner("⏳ កំពុងទាញយក Video..."):
                    file = godking_engine(url, 'video')
                    with yt_dlp.YoutubeDL({'quiet': True, 'outtmpl': 'godking_video.mp4'}) as ydl:
                        ydl.download([url])
                    with open(file, "rb") as f:
                        st.download_button("📥 Save Video", f, file, "video/mp4")
                    os.remove(file)
            except:
                st.error("❌ YouTube Blocked IP! សូមធ្វើតាមជំហាន 'ប្ដូរផ្ទះថ្មី' ខាងក្រោម!")
        else: st.warning("សូមដាក់ Link!")

with col2:
    if st.button("🎵 DOWNLOAD MP3"):
        if url:
            try:
                with st.spinner("⏳ កំពុងបំប្លែងជា MP3..."):
                    file = godking_engine(url, 'music')
                    with yt_dlp.YoutubeDL({'quiet': True, 'outtmpl': 'godking_music', 'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3'}]}) as ydl:
                        ydl.download([url])
                    with open(file, "rb") as f:
                        st.download_button("📥 Save MP3", f, file, "audio/mpeg")
                    os.remove(file)
            except:
                st.error("❌ បរាជ័យ! សូមពិនិត្យ packages.txt (ffmpeg)")
        else: st.warning("សូមដាក់ Link!")

st.markdown("---")
st.markdown("<p style='font-size: 12px; color: #777;'>Powered by GODKING • 2026</p>", unsafe_allow_html=True)

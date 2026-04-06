import streamlit as st
import yt_dlp
import os

# ការកំណត់រូបរាងវេបសាយ (Full Theme)
st.set_page_config(page_title="GODKING DOWNLOADER", page_icon="👑", layout="centered")

# បន្ថែមស្ទីល CSS ឱ្យស្អាត
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; }
    h1 { color: #FF4B4B; text-align: center; font-family: 'Khmer OS Battambang'; }
    p { color: #FAFAFA; text-align: center; }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 50px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>👑 GODKING DOWNLOADER 👑</h1>", unsafe_allow_html=True)
st.markdown("<p>ទាញយកវីដេអូ ឬចម្រៀង MP3 ពី YouTube & TikTok បានយ៉ាងងាយ</p>", unsafe_allow_html=True)

# ប្រអប់ដាក់ Link
url = st.text_input("", placeholder="បិទភ្ជាប់ Link នៅទីនេះ (YouTube, TikTok, FB...)", label_visibility="collapsed")

col1, col2 = st.columns(2)

# --- ផ្នែកដោនឡូត VIDEO ---
with col1:
    if st.button("🎬 VIDEO"):
        if url:
            try:
                with st.spinner("⏳ កំពុងទាញយក Video..."):
                    ydl_opts = {
                        'format': 'best',
                        'outtmpl': 'godking_video.mp4',
                        'noplaylist': True,
                        'quiet': True,
                        'http_headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
                    }
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    
                    with open("godking_video.mp4", "rb") as f:
                        st.download_button("📥 ចុចត្រង់នេះដើម្បី Save Video", f, "godking_video.mp4", "video/mp4")
                    os.remove("godking_video.mp4")
            except Exception as e:
                st.error("❌ បរាជ័យ! YouTube/TikTok អាចនឹងទប់ស្កាត់ Link នេះ។")
        else:
            st.warning("⚠️ សូមដាក់ Link ជាមុនសិន!")

# --- ផ្នែកដោនឡូត MP3 ---
with col2:
    if st.button("🎵 MP3"):
        if url:
            try:
                with st.spinner("⏳ កំពុងបំប្លែងជា MP3..."):
                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'outtmpl': 'godking_audio',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                        'quiet': True,
                        'http_headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
                    }
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    
                    if os.path.exists("godking_audio.mp3"):
                        with open("godking_audio.mp3", "rb") as f:
                            st.download_button("📥 ចុចត្រង់នេះដើម្បី Save MP3", f, "godking_music.mp3", "audio/mpeg")
                        os.remove("godking_audio.mp3")
                    else:
                        st.error("❌ មិនអាចបំប្លែងបាន! ប្រាកដថាបានថែម ffmpeg ក្នុង packages.txt រួចហើយ។")
            except Exception as e:
                st.error("❌ មានបញ្ហាបច្ចេកទេស! សូមព្យាយាមម្ដងទៀត។")
        else:
            st.warning("⚠️ សូមដាក់ Link ជាមុនសិន!")

st.markdown("---")
st.markdown("<p style='font-size: 12px; color: gray;'>Powered by GODKING • 2026</p>", unsafe_allow_html=True)

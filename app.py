import streamlit as st
import yt_dlp
import os

# ការកំណត់រូបរាង (King Theme)
st.set_page_config(page_title="GODKING DOWNLOADER", page_icon="👑")

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>👑 GODKING DOWNLOADER 👑</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #FAFAFA;'>ទាញយកវីដេអូ ឬចម្រៀង MP3 ពី YouTube & TikTok</p>", unsafe_allow_html=True)

url = st.text_input("", placeholder="បិទភ្ជាប់ Link នៅទីនេះ...")

# បច្ចេកទេស Bypass ពិសេស
ydl_opts_base = {
    'quiet': True,
    'no_warnings': True,
    'nocheckcertificate': True,
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
}

col1, col2 = st.columns(2)

with col1:
    if st.button("🎬 VIDEO"):
        if url:
            try:
                with st.spinner("⏳ កំពុងដោន Video..."):
                    opts = ydl_opts_base.copy()
                    opts.update({'format': 'best', 'outtmpl': 'video.mp4'})
                    with yt_dlp.YoutubeDL(opts) as ydl:
                        ydl.download([url])
                    with open("video.mp4", "rb") as f:
                        st.download_button("📥 Save Video", f, "godking_video.mp4")
                    os.remove("video.mp4")
            except Exception:
                st.error("❌ YouTube បានទប់ស្កាត់! សូមព្យាយាមម្ដងទៀត។")

with col2:
    if st.button("🎵 MP3"):
        if url:
            try:
                with st.spinner("⏳ កំពុងដោន MP3..."):
                    opts = ydl_opts_base.copy()
                    opts.update({
                        'format': 'bestaudio/best',
                        'outtmpl': 'music',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                    })
                    with yt_dlp.YoutubeDL(opts) as ydl:
                        ydl.download([url])
                    with open("music.mp3", "rb") as f:
                        st.download_button("📥 Save MP3", f, "godking_music.mp3")
                    os.remove("music.mp3")
            except Exception:
                st.error("❌ បរាជ័យ! សូមឆែកមើល packages.txt ម្ដងទៀត។")

import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="GODKING DOWNLOADER", page_icon="👑")

st.markdown("<h1 style='text-align: center; color: #FF0000;'>👑 GODKING DOWNLOADER 👑</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>ទាញយកវីដេអូ ឬចម្រៀង MP3 បានយ៉ាងងាយស្រួល</p>", unsafe_allow_html=True)

url = st.text_input("បិទភ្ជាប់ Link នៅទីនេះ៖", placeholder="https://...")

col1, col2 = st.columns(2)

with col1:
    if st.button("🎬 VIDEO"):
        if url:
            try:
                with st.spinner("⏳ កំពុងដោន Video..."):
                    ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4', 'noplaylist': True}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    with open("video.mp4", "rb") as f:
                        st.download_button("📥 Save Video", f, "godking_video.mp4", "video/mp4")
                    os.remove("video.mp4")
            except Exception as e:
                st.error("❌ បរាជ័យ!")
        else: st.warning("សូមដាក់ Link!")

with col2:
    if st.button("🎵 MP3"):
        if url:
            try:
                with st.spinner("⏳ កំពុងដោន MP3..."):
                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'outtmpl': 'music.mp3',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                    }
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    with open("music.mp3", "rb") as f:
                        st.download_button("📥 Save MP3", f, "godking_music.mp3", "audio/mpeg")
                    os.remove("music.mp3")
            except Exception as e:
                st.error("❌ បរាជ័យ!")
        else: st.warning("សូមដាក់ Link!")

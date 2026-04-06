import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="GODKING DOWNLOADER", page_icon="👑")

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>👑 GODKING DOWNLOADER 👑</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>ទាញយក Video & MP3 បានគ្រប់ Platform</p>", unsafe_allow_html=True)

url = st.text_input("", placeholder="បិទភ្ជាប់ Link នៅទីនេះ...")

# មុខងារពិសេសសម្រាប់ Bypass YouTube (២០២៦ Style)
def godking_bypass_engine(link, is_music=False):
    filename = "godking_media"
    
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'nocheckcertificate': True,
        # ក្បាច់បន្លំខ្លួនជា App ផ្លូវការរបស់ YouTube (Android)
        'client_id': 'android', 
        'client_version': '19.05.36',
        'http_headers': {
            'User-Agent': 'com.google.android.youtube/19.05.36 (Linux; U; Android 14; en_US) gzip',
        }
    }

    if is_music:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'outtmpl': f'{filename}.%(ext)s',
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
        })
        final_path = f"{filename}.mp3"
    else:
        ydl_opts.update({
            'format': 'best',
            'outtmpl': f'{filename}.mp4',
        })
        final_path = f"{filename}.mp4"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    return final_path

col1, col2 = st.columns(2)

with col1:
    if st.button("🎬 VIDEO"):
        if url:
            try:
                with st.spinner("⏳ កំពុងទាញយក..."):
                    path = godking_bypass_engine(url, False)
                    with open(path, "rb") as f:
                        st.download_button("📥 Save Video", f, path)
                    os.remove(path)
            except:
                st.error("❌ YouTube Block IP! សូមចុច Reboot App ម្ដងទៀត។")

with col2:
    if st.button("🎵 MP3"):
        if url:
            try:
                with st.spinner("⏳ កំពុងបំប្លែង..."):
                    path = godking_bypass_engine(url, True)
                    with open(path, "rb") as f:
                        st.download_button("📥 Save MP3", f, path)
                    os.remove(path)
            except:
                st.error("❌ បរាជ័យ! សូមឆែកមើល packages.txt")

import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="GODKING DOWNLOADER", page_icon="👑")

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>👑 GODKING DOWNLOADER 👑</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Download Video & MP3 from YT, FB, TikTok, IG</p>", unsafe_allow_html=True)

url = st.text_input("", placeholder="បិទភ្ជាប់ Link នៅទីនេះ...")

# ការកំណត់ជម្រើសដើម្បី Bypass IP Block
def download_media(link, is_audio=False):
    filename = "godking_output"
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'nocheckcertificate': True,
        '#': 'Bypass Protection',
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        }
    }

    if is_audio:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'outtmpl': f'{filename}.%(ext)s',
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
        })
        final_file = f"{filename}.mp3"
    else:
        ydl_opts.update({
            'format': 'best',
            'outtmpl': f'{filename}.mp4',
        })
        final_file = f"{filename}.mp4"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    return final_file

col1, col2 = st.columns(2)

with col1:
    if st.button("🎬 VIDEO"):
        if url:
            try:
                with st.spinner("⏳ កំពុងដោន Video..."):
                    path = download_media(url, is_audio=False)
                    with open(path, "rb") as f:
                        st.download_button("📥 Save Video", f, path)
                    os.remove(path)
            except:
                st.error("❌ បរាជ័យ! IP ត្រូវបាន Block! សូមលុប App ហើយ Deploy ថ្មី។")

with col2:
    if st.button("🎵 MP3"):
        if url:
            try:
                with st.spinner("⏳ កំពុងដោន MP3..."):
                    path = download_media(url, is_audio=True)
                    with open(path, "rb") as f:
                        st.download_button("📥 Save MP3", f, path)
                    os.remove(path)
            except:
                st.error("❌ បរាជ័យ! សូមពិនិត្យ packages.txt")

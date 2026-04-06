import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="GODKING DOWNLOADER", page_icon="👑")

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>👑 GODKING DOWNLOADER 👑</h1>", unsafe_allow_html=True)

url = st.text_input("", placeholder="បិទភ្ជាប់ Link YouTube, Facebook ឬ TikTok...")

# មុខងារ Bypass ជំនាន់ចុងក្រោយ ២០២៦
def godking_super_download(link, is_music=False):
    filename = "godking_output"
    
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'nocheckcertificate': True,
        # បច្ចេកទេសបន្លំខ្លួនជា Web Browser ពិតប្រាកដ
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        },
    }

    if is_music:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'outtmpl': f'{filename}.%(ext)s',
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
        })
        final_file = f"{filename}.mp3"
    else:
        # បង្ខំយក Video ដែលមានរូបភាព និងសំឡេងស្រាប់ (បន្លំ YouTube)
        ydl_opts.update({
            'format': 'best[ext=mp4]/best',
            'outtmpl': f'{filename}.mp4',
        })
        final_file = f"{filename}.mp4"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    return final_file

col1, col2 = st.columns(2)

with col1:
    if st.button("🎬 DOWNLOAD VIDEO"):
        if url:
            try:
                with st.spinner("⏳ កំពុងទម្លុះប្រព័ន្ធ YouTube..."):
                    path = godking_super_download(url, is_music=False)
                    with open(path, "rb") as f:
                        st.download_button("📥 Save Video", f, path)
                    os.remove(path)
            except Exception:
                st.error("❌ YouTube Block IP នេះ! សូមធ្វើតាមជំហាន 'ប្តូរផ្ទះថ្មី' ខាងក្រោម!")
        else: st.warning("សូមដាក់ Link!")

with col2:
    if st.button("🎵 DOWNLOAD MP3"):
        if url:
            try:
                with st.spinner("⏳ កំពុងបំប្លែងជា MP3..."):
                    path = godking_super_download(url, is_music=True)
                    with open(path, "rb") as f:
                        st.download_button("📥 Save MP3", f, path)
                    os.remove(path)
            except Exception:
                st.error("❌ បរាជ័យ! សូមពិនិត្យ packages.txt")
        else: st.warning("សូមដាក់ Link!")

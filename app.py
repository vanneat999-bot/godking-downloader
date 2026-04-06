import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="GODKING DOWNLOADER", page_icon="👑")

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>👑 GODKING DOWNLOADER 👑</h1>", unsafe_allow_html=True)

url = st.text_input("", placeholder="បិទភ្ជាប់ Link YouTube/TikTok នៅទីនេះ...")

# ការកំណត់ពិសេសដើម្បី Bypass YouTube Block
YDL_OPTIONS = {
    'format': 'bestaudio/best',
    'quiet': True,
    'no_warnings': True,
    'nocheckcertificate': True,
    'add_header': [
        'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language: en-us,en;q=0.5',
        'Sec-Fetch-Mode: navigate',
    ],
}

if st.button("🎵 DOWNLOAD MP3"):
    if url:
        try:
            with st.spinner("⏳ កំពុងវាយលុកប្រព័ន្ធ YouTube... សូមរង់ចាំ"):
                # កែសម្រួលសម្រាប់ MP3
                opts = YDL_OPTIONS.copy()
                opts.update({
                    'outtmpl': 'song.mp3',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                })
                
                with yt_dlp.YoutubeDL(opts) as ydl:
                    ydl.download([url])
                
                if os.path.exists("song.mp3"):
                    with open("song.mp3", "rb") as f:
                        st.download_button("📥 ចុចទីនេះដើម្បីរក្សាទុក MP3", f, "godking_music.mp3")
                    os.remove("song.mp3")
                else:
                    st.error("❌ មិនអាចបំប្លែងបាន! សូម Reboot App ក្នុង Streamlit Dashboard")
        except Exception as e:
            st.error("❌ YouTube កំពុងរឹតបន្តឹងខ្លាំង! សូមព្យាយាម Reboot App ឬប្តូរ Link ថ្មី។")
    else:
        st.warning("⚠️ សូមដាក់ Link ជាមុនសិន!")

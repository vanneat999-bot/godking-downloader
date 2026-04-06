import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="GODKING MUSIC", page_icon="🎵")

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🎵 GODKING MUSIC 🎵</h1>", unsafe_allow_html=True)

url = st.text_input("", placeholder="បិទភ្ជាប់ Link YouTube នៅទីនេះ...")

# ការកំណត់ពិសេសដើម្បី Bypass YouTube ជំនាន់ចុងក្រោយ
YDL_OPTIONS = {
    'format': 'bestaudio/best',
    'quiet': True,
    'no_warnings': True,
    'nocheckcertificate': True,
    'extract_flat': False,
    'ext': 'mp3',
    # បន្ថែមបច្ចេកទេសបន្លំខ្លួនជា Android App
    'youtube_include_dash_manifest': False,
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Android 14; Mobile; rv:120.0) Gecko/120.0 Firefox/120.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    },
}

if st.button("🚀 ទាញយក MP3"):
    if url:
        try:
            with st.spinner("⏳ កំពុងទម្លុះប្រព័ន្ធ YouTube... សូមរង់ចាំបន្តិច"):
                output_file = 'song.mp3'
                opts = YDL_OPTIONS.copy()
                opts.update({
                    'outtmpl': 'song',
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
                        st.download_button("📥 រក្សាទុកក្នុងម៉ាស៊ីន (Save MP3)", f, "godking_music.mp3")
                    os.remove("song.mp3")
                    st.success("🎉 រួចរាល់! លោកអធិរាជអាចរក្សាទុកបានហើយ")
                else:
                    st.error("❌ បញ្ហា FFmpeg: សូមចុច Reboot App ក្នុង Streamlit Dashboard ម្ដងទៀត!")
        except Exception as e:
            st.error("❌ YouTube នៅតែទប់ស្កាត់! សូមព្យាយាមប្តូរ Link ផ្សេង ឬ Reboot App ថ្មី។")
    else:
        st.warning("⚠️ សូមដាក់ Link ជាមុនសិន!")

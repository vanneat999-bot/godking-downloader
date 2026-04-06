import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="GODKING DOWNLOADER", page_icon="🎬")

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>👑 GODKING VIDEO DOWNLOADER 👑</h1>", unsafe_allow_html=True)

url = st.text_input("", placeholder="បិទភ្ជាប់ Link វីដេអូ YouTube/TikTok នៅទីនេះ...")

# ការកំណត់ពិសេសសម្រាប់ទាញយកវីដេអូ (Bypass YouTube Block)
YDL_OPTIONS = {
    'format': 'best', # យកកម្រិតវីដេអូដែលល្អបំផុត
    'quiet': True,
    'no_warnings': True,
    'nocheckcertificate': True,
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }
}

if st.button("🎬 ចាប់ផ្ដើមទាញយកវីដេអូ"):
    if url:
        try:
            with st.spinner("⏳ កំពុងទម្លុះប្រព័ន្ធ YouTube... សូមរង់ចាំ"):
                output_file = 'godking_video.mp4'
                opts = YDL_OPTIONS.copy()
                opts.update({'outtmpl': 'godking_video.mp4'})
                
                with yt_dlp.YoutubeDL(opts) as ydl:
                    ydl.download([url])
                
                if os.path.exists("godking_video.mp4"):
                    with open("godking_video.mp4", "rb") as f:
                        st.download_button("📥 ចុចទីនេះដើម្បីរក្សាទុកវីដេអូ (Save Video)", f, "godking_video.mp4", "video/mp4")
                    os.remove("godking_video.mp4")
                    st.success("🎉 រួចរាល់ហើយលោកអធិរាជ!")
                else:
                    st.error("❌ បរាជ័យ! សូមព្យាយាមចុច Reboot App ឡើងវិញ។")
        except Exception as e:
            st.error("❌ YouTube បានទប់ស្កាត់ IP នេះ! សូមលុប App ហើយ Deploy ថ្មីដើម្បីប្ដូរ IP Server។")
    else:
        st.warning("⚠️ សូមដាក់ Link ជាមុនសិន!")

import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="GODKING DOWNLOADER", page_icon="👑")

st.markdown("<h1 style='text-align: center; color: #FF0000;'>👑 GODKING DOWNLOADER 👑</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>ទាញយកវីដេអូ ឬចម្រៀង MP3</p>", unsafe_allow_html=True)

url = st.text_input("បិទភ្ជាប់ Link នៅទីនេះ៖", placeholder="https://...")

col1, col2 = st.columns(2)

# កូដសម្រាប់ Video
with col1:
    if st.button("🎬 VIDEO"):
        if url:
            try:
                with st.spinner("⏳ កំពុងដោន Video..."):
                    ydl_opts = {'format': 'best', 'outtmpl': 'video_temp.mp4', 'noplaylist': True}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    with open("video_temp.mp4", "rb") as f:
                        st.download_button("📥 Save Video", f, "godking_video.mp4", "video/mp4")
                    os.remove("video_temp.mp4")
            except Exception as e:
                st.error("❌ វីដេអូនេះមានប្រព័ន្ធការពារ ឬ Link ខូច")
        else: st.warning("សូមដាក់ Link!")

# កូដសម្រាប់ MP3 (កែសម្រួលថ្មី)
with col2:
    if st.button("🎵 MP3"):
        if url:
            try:
                with st.spinner("⏳ កំពុងបំប្លែងជា MP3..."):
                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'outtmpl': 'audio_temp', # ទុកឱ្យវាដោនសិន
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                    }
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    
                    if os.path.exists("audio_temp.mp3"):
                        with open("audio_temp.mp3", "rb") as f:
                            st.download_button("📥 Save MP3", f, "godking_music.mp3", "audio/mpeg")
                        os.remove("audio_temp.mp3")
                    else:
                        st.error("❌ ប្រព័ន្ធបំប្លែង (FFmpeg) មិនទាន់ដំឡើងរួចរាល់។ សូម Reboot App ក្នុង Streamlit Dashboard!")
            except Exception as e:
                st.error("❌ បរាជ័យ! សូមឆែកមើល File packages.txt ម្តងទៀត")
        else: st.warning("សូមដាក់ Link!")

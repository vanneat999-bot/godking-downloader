import streamlit as st
import yt_dlp
import os
import uuid

st.set_page_config(page_title="GODKING DOWNLOADER", page_icon="👑")

st.markdown("<h1 style='text-align: center; color: #FF0000;'>👑 GODKING DOWNLOADER 👑</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>ទាញយកវីដេអូ ឬចម្រៀង MP3 បានយ៉ាងងាយស្រួល</p>", unsafe_allow_html=True)

url = st.text_input("បិទភ្ជាប់ Link នៅទីនេះ៖", placeholder="https://...")

col1, col2 = st.columns(2)

# បង្កើតឈ្មោះ File ប្លែកៗគ្នាដើម្បីកុំឱ្យជាន់គ្នា
unique_id = str(uuid.uuid4())[:8]
video_file = f"video_{unique_id}.mp4"
audio_file = f"audio_{unique_id}.mp3"

with col1:
    if st.button("🎬 VIDEO"):
        if url:
            try:
                with st.spinner("⏳ កំពុងដោន Video..."):
                    ydl_opts = {'format': 'best', 'outtmpl': video_file, 'noplaylist': True}
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    with open(video_file, "rb") as f:
                        st.download_button("📥 Save Video", f, f"godking_{unique_id}.mp4", "video/mp4")
                    os.remove(video_file) # លុប File ចេញពី Server ភ្លាមក្រោយដោនរួច
            except Exception as e:
                st.error("❌ បរាជ័យ! សូមព្យាយាមម្ដងទៀត។")
        else: st.warning("សូមដាក់ Link!")

with col2:
    if st.button("🎵 MP3"):
        if url:
            try:
                with st.spinner("⏳ កំពុងដោន MP3..."):
                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'outtmpl': audio_file,
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                    }
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    with open(audio_file, "rb") as f:
                        st.download_button("📥 Save MP3", f, f"godking_{unique_id}.mp3", "audio/mpeg")
                    os.remove(audio_file) # លុប File ចេញពី Server ភ្លាមក្រោយដោនរួច
            except Exception as e:
                st.error("❌ បរាជ័យ! ប្រាកដថាបានថែម packages.txt រួចហើយ។")
        else: st.warning("សូមដាក់ Link!")

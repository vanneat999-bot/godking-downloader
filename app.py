import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="GODKING DOWNLOADER", page_icon="👑")

# UI Style (King Version)
st.markdown("<h1 style='text-align: center; color: #FF0000;'>👑 GODKING DOWNLOADER 👑</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>ដោនឡូតវីដេអូបានគ្រប់វេទិកា YT, FB, TikTok, Douyin</p>", unsafe_allow_html=True)

# Input field
url = st.text_input("បិទភ្ជាប់ Link វីដេអូនៅទីនេះ៖", placeholder="https://www.youtube.com/watch?v=...")

if st.button("ចាប់ផ្តើមទាញយកឥឡូវនេះ"):
    if url:
        try:
            with st.spinner("⏳ កំពុងដំណើរការ... សូមរង់ចាំ (Bypassing Protection)"):
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': 'video.mp4',
                    'noplaylist': True,
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                # បង្ហាញវីដេអូ និងប៊ូតុង Save
                with open("video.mp4", "rb") as file:
                    st.video("video.mp4")
                    st.download_button(
                        label="📥 ចុចទីនេះដើម្បីរក្សាទុកវីដេអូ (Save Video)",
                        data=file,
                        file_name="GODKING_VIDEO.mp4",
                        mime="video/mp4"
                    )
                os.remove("video.mp4") 
        except Exception as e:
            st.error(f"❌ បរាជ័យ៖ Link នេះមានប្រព័ន្ធការពារខ្ពស់ ឬមិនគាំទ្រ។")
    else:
        st.warning("សូមបញ្ចូល Link ជាមុនសិន!")

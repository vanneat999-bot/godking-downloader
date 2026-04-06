import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="GODKING DOWNLOADER", page_icon="👑")
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>👑 GODKING DOWNLOADER 👑</h1>", unsafe_allow_html=True)

url = st.text_input("", placeholder="បិទភ្ជាប់ Link YouTube, Facebook ឬ TikTok...")

# ការកំណត់ពិសេសបំផុតដោយប្រើ Cookies
YDL_OPTIONS = {
    'quiet': True,
    'cookiefile': 'cookies.txt',  # សំខាន់បំផុត៖ ប្រើ Cookies ដើម្បីបន្លំជាមនុស្ស
    'no_warnings': True,
    'nocheckcertificate': True,
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

if st.button("🚀 DOWNLOAD NOW"):
    if url:
        try:
            with st.spinner("⏳ កំពុងប្រើ Cookies ដើម្បីទម្លុះ YouTube..."):
                with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
                    ydl.download([url])
                st.success("✅ ជោគជ័យ! YouTube គិតថាលោកជាមនុស្សពិត។")
        except Exception as e:
            st.error("❌ YouTube នៅតែ Block! សូម Update ឯកសារ cookies.txt ថ្មី។")

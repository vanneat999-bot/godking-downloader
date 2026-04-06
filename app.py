import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="GODKING DOWNLOADER", page_icon="👑")

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>👑 GODKING DOWNLOADER 👑</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>សាកល្បងដោនឡូតពី YouTube, Facebook, TikTok</p>", unsafe_allow_html=True)

url = st.text_input("", placeholder="បិទភ្ជាប់ Link ទីនេះ...")

# ការកំណត់មហាសាលសម្រាប់ Bypass គ្រប់ Platform
YDL_OPTIONS = {
    'quiet': True,
    'no_warnings': True,
    'nocheckcertificate': True,
    # បច្ចេកទេសបន្លំជា App ទូរស័ព្ទ (ជួយឱ្យ FB និង YT ដើរ)
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'referer': 'https://www.google.com/',
    'extract_flat': False,
}

def godking_download(link, mode):
    # កូដសម្គាល់ឈ្មោះ File កុំឱ្យជាន់គ្នា
    filename = "godking_media"
    opts = YDL_OPTIONS.copy()
    
    if mode == 'music':
        opts.update({
            'format': 'bestaudio/best',
            'outtmpl': f'{filename}.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        # សម្រាប់ Video យកកម្រិតដែលល្អបំផុតដែលអាចដោនបាន
        opts.update({
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{filename}.mp4',
            'merge_output_format': 'mp4',
        })
    
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([link])
    
    return f"{filename}.mp3" if mode == 'music' else f"{filename}.mp4"

col1, col2 = st.columns(2)

with col1:
    if st.button("🎬 DOWNLOAD VIDEO"):
        if url:
            try:
                with st.spinner("⏳ កំពុងទាញយក Video... (Support FB & YT)"):
                    file_path = godking_download(url, 'video')
                    with open(file_path, "rb") as f:
                        st.download_button("📥 Save Video", f, file_path)
                    os.remove(file_path)
            except Exception as e:
                st.error("❌ YouTube/FB ទប់ស្កាត់! សូមព្យាយាម 'Delete App' រួច 'Deploy ថ្មី'")
        else: st.warning("សូមដាក់ Link!")

with col2:
    if st.button("🎵 DOWNLOAD MP3"):
        if url:
            try:
                with st.spinner("⏳ កំពុងបំប្លែងជា MP3..."):
                    file_path = godking_download(url, 'music')
                    with open(file_path, "rb") as f:
                        st.download_button("📥 Save MP3", f, file_path)
                    os.remove(file_path)
            except Exception as e:
                st.error("❌ បរាជ័យ! សូមឆែកមើល packages.txt")
        else: st.warning("សូមដាក់ Link!")

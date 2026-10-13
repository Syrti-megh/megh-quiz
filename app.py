import streamlit as st
import random

st.set_page_config(page_title="Megh-Quiz Game", page_icon="🧠")

# --- DATA ---
all_questions = [
    {"q": "Meghalaya ki capital kaunsi hai?", "options": ["Shillong", "Tura", "Jowai", "Nongpoh"], "ans": "Shillong"},
    {"q": "Meghalaya ko kya kehte hain?", "options": ["Abode of Clouds", "Land of Rivers", "Hills Queen", "Green Land"], "ans": "Abode of Clouds"},
    {"q": "Cherrapunji ka naya naam?", "options": ["Sohra", "Mawlynnong", "Dawki", "Mawsynram"], "ans": "Sohra"},
    {"q": "Nohkalikai Falls kahan hai?", "options": ["Meghalaya", "Assam", "Nagaland", "Mizoram"], "ans": "Meghalaya"},
    {"q": "Living Root Bridge kahan milta hai?", "options": ["Cherrapunji", "Shillong", "Tura", "Jowai"], "ans": "Cherrapunji"},
    {"q": "Meghalaya ka state animal?", "options": ["Clouded Leopard", "Tiger", "Elephant", "Hoolock Gibbon"], "ans": "Clouded Leopard"},
    {"q": "Meghalaya ka famous festival?", "options": ["Wangala", "Bihu", "Hornbill", "Losar"], "ans": "Wangala"},
    {"q": "Umiam Lake ka dusra naam?", "options": ["Barapani", "Wards Lake", "Thadlaskein", "Umiam hi hai"], "ans": "Barapani"},
    {"q": "Dawki River kyun famous hai?", "options": ["Crystal clear water", "Bada dam", "Boating race", "Gold"], "ans": "Crystal clear water"},
    {"q": "Shillong ka nickname?", "options": ["Scotland of the East", "Paris of East", "Queen of Hills", "Rock Capital"], "ans": "Scotland of the East"},
    {"q": "Khasi me 'Khublei' ka matlab?", "options": ["Thank you", "Hello", "Goodbye", "Welcome"], "ans": "Thank you"},
    {"q": "Meghalaya kab bana tha state?", "options": ["1972", "1947", "1975", "2000"], "ans": "1972"},
]

if "level" not in st.session_state:
    st.session_state.level = 1
    st.session_state.score = 0
    st.session_state.q_index = 0
    st.session_state.level_questions = random.sample(all_questions, 5)

st.title("🧠 Megh-Quiz Game")
st.caption(f"Meghalaya's own quiz - by bahlleh | Level {st.session_state.level} - NEVER ENDING")

progress = st.session_state.q_index / 5
st.progress(progress)

if st.session_state.q_index < 5:
    curr = st.session_state.level_questions[st.session_state.q_index]
    st.subheader(f"Q{st.session_state.q_index+1}: {curr['q']}")
    
    choice = st.radio("Jawab chuno:", curr["options"], index=None)
    
    if st.button("Next"):
        if choice == curr["ans"]:
            st.session_state.score += 1
            st.toast("✅ Sahi Jawab!")
        else:
            st.toast(f"❌ Galat! Sahi tha: {curr['ans']}")
        
        st.session_state.q_index += 1
        st.rerun()
else:
    st.success(f"Level {st.session_state.level} Complete! Score: {st.session_state.score} / 5")
    if st.session_state.score >= 3:
        st.balloons()
        st.write(f"### 🔥 Level {st.session_state.level+1} Unlocked!")
        if st.button("Next Level >>"):
            st.session_state.level += 1
            st.session_state.score = 0
            st.session_state.q_index = 0
            # Difficulty badhao - har level pe random naye 5
            st.session_state.level_questions = random.sample(all_questions, 5)
            random.shuffle(st.session_state.level_questions)
            st.rerun()
    else:
        st.error("3 se kam score! Dobara koshish karo.")
        if st.button("Fir se khelo"):
            st.session_state.score = 0
            st.session_state.q_index = 0
            st.session_state.level_questions = random.sample(all_questions, 5)
            st.rerun()

st.sidebar.write(f"🏆 Current Level: {st.session_state.level}")
st.sidebar.write("Never ending game hai, jitna khel sakta hai khel!")
if st.sidebar.button("Game Reset"):
    st.session_state.level = 1
    st.session_state.score = 0
    st.session_state.q_index = 0
    st.session_state.level_questions = random.sample(all_questions, 5)
    st.rerun()

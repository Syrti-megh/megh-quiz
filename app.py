import streamlit as st
st.set_page_config(page_title="Megh-Quiz", page_icon="🧠")
st.title("🧠 Megh-Quiz Game")
st.caption("Meghalaya's own quiz - by bahlieh")

if "q" not in st.session_state:
    st.session_state.q = 0
    st.session_state.score = 0

questions = [
    {"q": "Meghalaya ki capital kya hai?", "opts": ["Shillong", "Guwahati", "Tura", "Jowai"], "ans": "Shillong"},
    {"q": "Sabse zyada barish kaha hoti hai?", "opts": ["Mawsynram", "Delhi", "Mumbai", "Cherrapunji"], "ans": "Mawsynram"},
    {"q": "Meghalaya ko kya kehte hain?", "opts": ["Abode of Clouds", "Land of Kings", "Desert", "Hills"], "ans": "Abode of Clouds"},
    {"q": "Shillong ki famous lake?", "opts": ["Umiam Lake", "Dal Lake", "Wular", "Loktak"], "ans": "Umiam Lake"},
    {"q": "Meghalaya ka famous orange?", "opts": ["Sohra Orange", "Apple", "Banana", "Mango"], "ans": "Sohra Orange"},
]

if st.session_state.q < len(questions):
    curr = questions[st.session_state.q]
    st.subheader(f"Q{st.session_state.q+1}. {curr['q']}")
    choice = st.radio("Jawab chuno:", curr["opts"], index=None)
    if st.button("Next", use_container_width=True):
        if choice:
            if choice == curr["ans"]:
                st.session_state.score += 1
            st.session_state.q += 1
            st.rerun()
else:
    st.balloons()
    st.success(f"Score: {st.session_state.score} / {len(questions)}")
    if st.button("Fir se khelo"):
        st.session_state.q = 0
        st.session_state.score = 0
        st.rerun()

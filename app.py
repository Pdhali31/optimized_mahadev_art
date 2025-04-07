import streamlit as st
import matplotlib.pyplot as plt
import time

# Page setup
st.set_page_config(page_title="Mahadev Live Drawing", layout="centered", page_icon="🕉️")
st.title("🕉️ Mahadev Turtle Art - Live Drawing (No Video)")

# Create a blank canvas
fig, ax = plt.subplots()
ax.set_facecolor("black")
fig.patch.set_facecolor('black')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis("off")

# Symbolic Mahadev drawing steps (example)
lines = [
    ((20, 50), (80, 50)),     # Horizontal bar (tripund)
    ((50, 20), (50, 80)),     # Vertical trishul
    ((35, 65), (65, 65)),     # Crescent
    ((30, 35), (70, 35)),     # Base
    ((45, 40), (55, 60)),     # Diagonal left
    ((55, 40), (45, 60)),     # Diagonal right
]

# Draw step by step with delay
for i, (start, end) in enumerate(lines):
    ax.plot([start[0], end[0]], [start[1], end[1]], color="deepskyblue", linewidth=3)
    st.pyplot(fig)
    time.sleep(0.6)

# Signature
st.markdown("<p style='text-align:right; color: white;'>Create by pintu_coder</p>", unsafe_allow_html=True)
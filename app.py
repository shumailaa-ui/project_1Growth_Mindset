import streamlit as st

# Title
st.set_page_config(page_title="Growth Mindset App", layout="centered")
st.title("🌱 Growth Mindset Challenge")
st.markdown("---")

# What is a Growth Mindset?
st.header("💡 What is a Growth Mindset?")
st.write("""
A **growth mindset** is the belief that your abilities and intelligence can grow with effort, learning, and persistence. 
Psychologist **Carol Dweck** introduced this idea, showing that success comes from dedication and hard work, not just talent.
""")

# Why Adopt a Growth Mindset?
st.header("🎯 Why Adopt a Growth Mindset?")
st.markdown("""
- **Embrace Challenges**: Treat obstacles as opportunities to learn.
- **Learn from Mistakes**: Mistakes help you grow.
- **Persist Through Difficulties**: Keep going even when it’s hard.
- **Celebrate Effort**: Effort matters more than outcome.
- **Keep an Open Mind**: Stay curious and flexible.
""")

# How to Practice?
st.header("🛠️ How Can You Practice a Growth Mindset?")
st.markdown("""
1. **Set Learning Goals** – Focus on developing skills, not just grades.
2. **Reflect on Learning** – Think about what you've learned from challenges.
3. **Seek Feedback** – Use feedback to improve.
4. **Stay Positive** – Believe in your potential to grow.
""")

# Final Encouragement
st.header("🚀 Final Words")
st.success("""
Your journey in education is not about proving your intelligence—it’s about developing it. 
Every step, forward or backward, is part of growth.

✨ Embrace your potential. Keep learning. Keep growing!
""")

# Interactive Section
st.markdown("---")
st.subheader("📢 Will you adopt a Growth Mindset?")
choice = st.radio("Choose your response:", ["Yes! I'm ready!", "Still thinking...", "Not sure yet"])
if choice == "Yes! I'm ready!":
    st.balloons()
    st.success("That's the spirit! 🌟 Let's grow together!")
elif choice == "Still thinking...":
    st.info("Take your time, but remember, growth starts with belief.")
else:
    st.warning("It's okay to be unsure. Keep exploring and stay open to learning.")


import streamlit as st
import requests
st.set_page_config(page_title="TailorTalk AI", page_icon="📅")


st.title(" TailorTalk")

user_input = st.text_input("What would you like to schedule?")

if st.button("📅 Schedule"):
    if user_input:
        with st.spinner("Booking your event..."):
            try:
                response = requests.post(
                    "https://tailortalk-0v8t.onrender.com/chat",
                    json={"user_input": user_input},
                    timeout=30  # Optional timeout for safety
                )

                # Try decoding JSON safely
                try:
                    data = response.json()
                    result = data.get("response", "⚠️ No 'response' key found.")
                except requests.exceptions.JSONDecodeError:
                    st.error("❌ Error: Server returned non-JSON response.")
                    st.text(response.text)
                    result = None

                if result:
                    if "calendar.google.com" in result:
                        st.success("✅ Event created!")
                        st.markdown(f"📆 [View calendar event]({result})", unsafe_allow_html=True)
                    else:
                        st.info(result)

            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please enter something to schedule.")

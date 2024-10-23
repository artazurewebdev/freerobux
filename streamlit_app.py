import streamlit as st

st.title("Free Robux")
st.write("ABOLISH PAY TO WIN")

st.write("Hieleros Base Code Version")

st.text("Only compatible with Windows Software Devices")

st.text("So far only tested in the US, Canada, and Australia")

message = st.text_area("Enter your Gamertag", "e.g. builderman")

city = st.selectbox("Your Country", ["USA", "Canada", "Australia"])

radio_but = st.radio("Your Selection", ["100,000", "500,000", "1,000,000"])
if radio_but == "100,000":
      st.info("To Install 100K Robux")
elif radio_but == "500,000":
      st.info("To Install 500K Robux")
elif radio_but == "1,000,000":
      st.info("To Install 1M Robux")

if st.button("Prepare Robux"):
      import time
      with st.spinner("Please wait..."):
            time.sleep(10)
      st.error("Unable to prepare with Hieleros. Download with Streamlit as a repository code.")

if st.button("Download with Streamlit"):
      st.error("Download Failed")
      st.text("Unable to retrieve code")

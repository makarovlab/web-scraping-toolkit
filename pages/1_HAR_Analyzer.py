import streamlit as st
import json
from analyzers.constants import CONTENT_TYPES, URL_STOP_WORDS
from analyzers.coordinates import has_coordinates

def info():
    st.markdown("## Analysis of Website HTTP Archive (HAR)")

def filter_requests(entries):
    for request in entries:
        status = request["response"]["status"]

        if status == 200:
            if not any([stop_word in request["request"]["url"] for stop_word in URL_STOP_WORDS]):
                content = request["response"]["content"]

                if content.get("size") > 0 and len(content.get("text", "")) > 0 and content["mimeType"] in CONTENT_TYPES:
                    if has_coordinates(content.get("text")):
                        # yield request["request"]["url"]
                        yield request


def har_upload_widget():
    uploaded_file = st.file_uploader(
        "HAR file", 
        type=['har'],
        accept_multiple_files=False,
        label_visibility="visible"
        )
    
    if uploaded_file is not None:
        har_json = json.loads(uploaded_file.getvalue().decode("utf-8"))
        filtered_requests = list(filter_requests(har_json["log"]["entries"]))
        
        for request in filtered_requests:
            expander = st.expander(request["request"]["url"][:100])

            try:
                content = request["response"]["content"]["text"]
                expander.json(json.loads(content))
            except:
                expander.text(content)
    

def main():
    info()
    har_upload_widget()

if __name__ == "__main__":
    main()
import streamlit as st 
from parser import parse_model
from scrape import scrap_website, split_dom_content, clean_body_content,extract_body_content 
st.title("AI Web Scraper") 
url = st.text_input("Enter the website URL: ")

if st.button("Scrape Site"):
    result = scrap_website(url)
    
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    st.session_state.dom_content = cleaned_content 
    with st.expander("View DOM Content"):
        st.text_area("DOM Content",cleaned_content,height=400)
        

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.spinner("Parsing the content...")
            
            
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_model(dom_chunks, parse_description)
            print(parsed_result)
            st.write(parsed_result) 
            
            #eg: can you please collect of all relevant property information and organize it in a table ?
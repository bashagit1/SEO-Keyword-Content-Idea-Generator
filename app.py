import streamlit as st
import openai
import os
from SimplerLLM.language.llm import LLM, LLMProvider

# Set up OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize LLM instance
llm_instance = LLM.create(provider=LLMProvider.OPENAI, model_name="gpt-3.5-turbo")

# Title and Description
st.set_page_config(page_title="SEO Keyword & Content Idea Generator", page_icon="🔍")

# Title and Description with Icons
st.markdown("<h1 style='text-align: center;'>🔍 SEO Keyword & Content Idea Generator 🔍</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Generate SEO keywords and content ideas for your blog or website.</h4>", unsafe_allow_html=True)

# Sidebar for input options with icons
with st.sidebar:
    st.header("🛠️ Options")
    content_type = st.selectbox("📝 Select Content Type", ["Blog Post", "Article", "Product Description", "Social Media"])
    target_audience = st.text_input("👥 Enter Target Audience", placeholder="e.g., Small Business Owners")

# User Input for topic/theme
user_input = st.text_input("💬 Enter a topic for keyword generation", placeholder="e.g., Digital Marketing")

# Generate and Display Response
if st.button("🚀 Generate Ideas", key="generate"):
    if user_input and target_audience:
        prompt_keywords = f"Generate SEO keywords for {content_type.lower()} about {user_input} targeting {target_audience}."
        prompt_content_ideas = f"Generate content ideas for {content_type.lower()} about {user_input} targeting {target_audience}."

        # Generate responses from LLM
        keywords_response = llm_instance.generate_response(prompt=prompt_keywords)
        content_ideas_response = llm_instance.generate_response(prompt=prompt_content_ideas)
        
        st.subheader("🔑 Generated SEO Keywords")
        st.write(keywords_response)
        
        st.subheader("📝 Content Ideas")
        st.write(content_ideas_response)
    else:
        st.warning("⚠️ Please enter a topic and target audience to generate ideas.")

# Display User Instructions
st.info("""
### How to Use:
1. Enter a topic for keyword generation.
2. Specify your target audience.
3. Select the type of content you are creating.
4. Click 'Generate Ideas' to create keywords and content ideas!
""")

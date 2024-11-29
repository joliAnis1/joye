import streamlit as st
from datetime import datetime

# Title and header
st.title("My Personal Blog")
st.header("Welcome to My Blog!")

# Blog post content
st.sidebar.title("Navigation")
sections = ["Home", "Create a Post", "View Posts", "About"]
choice = st.sidebar.radio("Go to", sections)

# Global storage for blog posts (for simplicity; use a database for production)
if 'posts' not in st.session_state:
    st.session_state['posts'] = []

if choice == "Home":
    st.subheader("Latest Posts")
    if st.session_state['posts']:
        for post in reversed(st.session_state['posts']):
            st.markdown(f"### {post['title']}")
            st.write(post['content'])
            st.write(f"Written by {post['author']} on {post['date']}")
            st.markdown("---")
    else:
        st.write("No posts yet. Start creating!")

elif choice == "Create a Post":
    st.subheader("Create a New Blog Post")
    title = st.text_input("Post Title")
    author = st.text_input("Author Name")
    content = st.text_area("Write your blog content here...")
    submit = st.button("Publish")

    if submit:
        if title and author and content:
            st.session_state['posts'].append({
                "title": title,
                "author": author,
                "content": content,
                "date": datetime.now().strftime("%B %d, %Y %H:%M:%S"),
            })
            st.success("Your post has been published!")
        else:
            st.error("Please fill in all fields.")

elif choice == "View Posts":
    st.subheader("All Blog Posts")
    if st.session_state['posts']:
        for post in reversed(st.session_state['posts']):
            st.markdown(f"### {post['title']}")
            st.write(post['content'])
            st.write(f"Written by {post['author']} on {post['date']}")
            st.markdown("---")
    else:
        st.write("No posts to display.")

elif choice == "About":
    st.subheader("About This Blog")
    st.write("""
    This is a simple blog built using Streamlit.
    You can create, view, and manage posts dynamically.
    Enjoy blogging!
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Built with ❤️ using Streamlit")
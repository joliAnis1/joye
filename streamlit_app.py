import streamlit as st
from datetime import datetime

# Title and Header
st.title("My Personal Blog")
st.header("Welcome to My Blog!")

# Global storage
if 'posts' not in st.session_state:
    st.session_state['posts'] = []

if 'certificates' not in st.session_state:
    st.session_state['certificates'] = []

if 'education' not in st.session_state:
    st.session_state['education'] = []

# Profile Section
st.subheader("Profile")

# Display the image directly from a file path
st.image("profile_image.jpg", caption="Princess Joye Abdula C. Retorta", use_column_width=True)  # Update this to the correct file path

# Personal Info
st.markdown("### Personal Information")
name = "Princess Joye Abdula C. Retorta"
address = "Sitio Bioborjan P-2 Brgy. Rizal, Surigao City"
age = 18
birthday = datetime(2006, 3, 12)

st.markdown(f"""
- **Name**: {name}
- **Address**: {address}
- **Age**: {age}
- **Birthday**: {birthday.strftime('%B %d, %Y')}
""")

# About Me Section
st.subheader("About Me")
about_me = "I love cooking, reading, drawing, watching movies, and writing poems."
st.markdown(f"**About Me**: {about_me}")

# Blog Post Section
sections = ["Create a Post", "View Posts", "Certificates & Educational Attainment"]
choice = st.selectbox("Go to", sections)

if choice == "Create a Post":
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

elif choice == "Certificates & Educational Attainment":
    st.subheader("Certificates and Educational Attainment")

    # Certificates Section
    st.markdown("### Certificates")
    new_certificate = st.text_input("Add a Certificate")
    if st.button("Add Certificate"):
        if new_certificate:
            st.session_state['certificates'].append(new_certificate)
            st.success("Certificate added!")
        else:
            st.error("Please enter a certificate.")

    if st.session_state['certificates']:
        for i, cert in enumerate(st.session_state['certificates']):
            st.write(f"{i + 1}. {cert}")
            if st.button(f"Delete Certificate {i + 1}", key=f"del_cert_{i}"):
                st.session_state['certificates'].pop(i)
                st.success("Certificate deleted!")
                st.experimental_rerun()

    # Educational Attainment Section
    st.markdown("### Educational Attainment")
    new_education = st.text_input("Add Educational Attainment")
    if st.button("Add Educational Attainment"):
        if new_education:
            st.session_state['education'].append(new_education)
            st.success("Educational attainment added!")
        else:
            st.error("Please enter educational attainment.")

    if st.session_state['education']:
        for i, edu in enumerate(st.session_state['education']):
            st.write(f"{i + 1}. {edu}")
            if st.button(f"Delete Educational Attainment {i + 1}", key=f"del_edu_{i}"):
                st.session_state['education'].pop(i)
                st.success("Educational attainment deleted!")
                st.experimental_rerun()

# Footer
st.markdown("---")
st.write("Built with ❤️ using Streamlit")

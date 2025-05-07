import streamlit as st
from googletrans import Translator


# Title
st.title("🎨 Indian Traditional Art Forms & Tourism Guide")
# Language selection
language_options = {
    'English': 'en',
    'Hindi': 'hi',
    'Marathi': 'mr',
    'Bengali': 'bn',
    'Tamil': 'ta',
    'Telugu': 'te'
}
selected_language = st.selectbox("Select Language", list(language_options.keys()))

# Translator setup
translator = Translator()

# Function to translate text
def translate_text(text, lang_code):
    return translator.translate(text, dest=lang_code).text

# List of art forms with tourism info
art_forms = [
    {
        "name": "Madhubani",
        "origin": "Bihar",
        "description": "Madhubani painting is a traditional art form originating from the Mithila region of Bihar. It features intricate patterns, often inspired by nature.",
        "video": "https://www.youtube.com/embed/UvH7xm8JfJ4",
        "tourism": {
            "nearest_city": "Darbhanga",
            "places_to_visit": ["Madhubani Village", "Darbhanga Fort", "Ahilya Sthan"],
            "best_time": "October to March",
            "maps_link": "<iframe src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d57206.311984809945!2d86.03240210897742!3d26.346099427058782!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39edcd30bc1d5d47%3A0x8bbe389999d9c709!2sMadhubani%2C%20Bihar!5e0!3m2!1sen!2sin!4v1746369532330!5m2!1sen!2sin' width='600' height='450' style='border:0;' allowfullscreen='' loading='lazy'></iframe>"
        }
    },
    {
        "name": "Warli",
        "origin": "Maharashtra",
        "description": "Warli art is a tribal art form from Maharashtra, known for its simple geometric shapes like circles, triangles, and squares.",
        "video": "https://www.youtube.com/embed/n_zPi9jiY2g",
        "tourism": {
            "nearest_city": "Mumbai",
            "places_to_visit": ["Warli Villages", "Sanjay Gandhi National Park", "Elephanta Caves"],
            "best_time": "November to February",
            "maps_link": "<iframe src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d60102.8920245379!2d72.72784249218226!3d19.694276912927467!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be71cdea3ddc177%3A0xdb2b913629961d24!2sPalghar%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1746371935614!5m2!1sen!2sin' width='600' height='450' style='border:0;' allowfullscreen='' loading='lazy'></iframe>"
        }
    },
    {
        "name": "Pattachitra",
        "origin": "Odisha",
        "description": "Pattachitra is a traditional painting style from Odisha, known for its intricate patterns and mythological narratives depicted on cloth or dried palm leaves.",
        "video": "https://www.youtube.com/embed/0fbFJVrxDh0",
        "tourism": {
            "nearest_city": "Bhubaneswar",
            "places_to_visit": ["Raghurajpur Village", "Konark Sun Temple", "Jagannath Temple"],
            "best_time": "October to March",
            "maps_link": "<iframe src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d60059.741900660774!2d85.78035079315963!3d19.808877982045875!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a19c4180256e495%3A0x496a9d8b30c1fad7!2sPuri%2C%20Odisha!5e0!3m2!1sen!2sin!4v1746371986523!5m2!1sen!2sin' width='600' height='450' style='border:0;' allowfullscreen='' loading='lazy'></iframe>"
        }
    },
    {
        "name": "Tanjore",
        "origin": "Tamil Nadu",
        "description": "Tanjore painting is a classical South Indian painting style that uses surface decorations with gold foil and vibrant colors, often depicting deities.",
        "video": "https://www.youtube.com/embed/j9Ay6PwWc_M",
        "tourism": {
            "nearest_city": "Thanjavur",
            "places_to_visit": ["Brihadeeswarar Temple", "Thanjavur Palace", "Schwartz Church"],
            "best_time": "November to February",
            "maps_link": "<iframe src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d125432.31724747956!2d79.0490455886108!3d10.752977698418187!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3baab89cea453039%3A0xe113da9b1f632be6!2sThanjavur%2C%20Tamil%20Nadu!5e0!3m2!1sen!2sin!4v1746372031470!5m2!1sen!2sin' width='600' height='450' style='border:0;' allowfullscreen='' loading='lazy'></iframe>"
        }
    },
    {
        "name": "Kalamkari",
        "origin": "Telangana and Andhra Pradesh",
        "description": "Kalamkari is a type of hand-painted or block-printed cotton textile. The art form involves intricate designs and mythological themes.",
        "video": "https://www.youtube.com/embed/v8iwZ2G6hw4",
        "tourism": {
            "nearest_city": "Hyderabad",
            "places_to_visit": ["Kalamkari Village", "Golconda Fort", "Charminar"],
            "best_time": "October to March",
            "maps_link": "<iframe src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d62007.855557737494!2d79.66208450002556!3d13.749239504611046!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a4d3e543dbbc769%3A0xc759d83ecf891652!2sSrikalahasti%2C%20Andhra%20Pradesh!5e0!3m2!1sen!2sin!4v1746372070389!5m2!1sen!2sin' width='600' height='450' style='border:0;' allowfullscreen='' loading='lazy'></iframe>"
        }
    }
]

# Quiz questions
quizzes = {
    "Madhubani": {
        "question": "Madhubani painting originates from which Indian state?",
        "options": ["Rajasthan", "Bihar", "Kerala"],
        "answer": "Bihar"
    },
    "Warli": {
        "question": "Which shapes are commonly used in Warli art?",
        "options": ["Geometric shapes", "Abstract strokes", "Calligraphy"],
        "answer": "Geometric shapes"
    },
    "Pattachitra": {
        "question": "Pattachitra is mostly painted on?",
        "options": ["Canvas", "Palm leaves or cloth", "Stone walls"],
        "answer": "Palm leaves or cloth"
    },
    "Tanjore": {
        "question": "Which material is often used in Tanjore paintings?",
        "options": ["Gold foil", "Silver dust", "Fabric"],
        "answer": "Gold foil"
    },
    "Kalamkari": {
        "question": "What technique is used in Kalamkari art?",
        "options": ["Block printing & hand painting", "Spray painting", "Stencil work"],
        "answer": "Block printing & hand painting"
    }
}

def display_art_form(art_form):
    st.subheader(translate_text(art_form["name"], language_options[selected_language]))
    st.markdown(f"**{translate_text('Origin', language_options[selected_language])}**: {translate_text(art_form['origin'], language_options[selected_language])}")
    st.markdown(f"**{translate_text('Description', language_options[selected_language])}**: {translate_text(art_form['description'], language_options[selected_language])}")
    
    # Display video
    if "video" in art_form:
        st.components.v1.iframe(art_form["video"], height=315)

    # Display tourism info
    tourism = art_form.get("tourism", {})
    st.markdown("### 🧭 Tourism Info")
    st.markdown(f"**Nearest City**: {tourism.get('nearest_city')}")
    st.markdown(f"**Best Time to Visit**: {tourism.get('best_time')}")
    st.markdown("**Places to Visit:**")
    for place in tourism.get("places_to_visit", []):
        st.markdown(f"- {place}")
    
    st.components.v1.html(tourism.get("maps_link", ""), height=450)

    # Quiz
    quiz = quizzes.get(art_form["name"])
    if quiz:
        st.markdown("### 🧠 Quick Quiz")
        selected = st.radio(quiz["question"], quiz["options"])
        if st.button(f"Submit Answer for {art_form['name']}"):
            if selected == quiz["answer"]:
                st.success("Correct! 🎉")
            else:
                st.error(f"Oops! The correct answer is **{quiz['answer']}**.")

# Streamlit interface to select and display art form
selected_art = st.selectbox("Select an Art Form", [art["name"] for art in art_forms])
for art in art_forms:
    if art["name"] == selected_art:
        display_art_form(art)
        break

import streamlit as st
import time

def get_ai_response(question):
    """
    Simulated AI response - Replace this with your actual AI integration.
    """
    # Simulate AI processing
    time.sleep(2)
    
    # Simple keyword-based response
    if "ticket" in question.lower() or "problem" in question.lower() or "issue" in question.lower():
        return "I understand you're experiencing an issue. Let me create a support ticket for you.", True
    else:
        return "I'm here to help with any F1-related questions. What would you like to know?", False

def initialize_session_state():
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'ticket_created' not in st.session_state:
        st.session_state.ticket_created = False

def main():
    initialize_session_state()
    
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #000000;
            color: #FFFFFF;
        }
        .stButton>button {
            width: 30%;
            background-color: #FF1E00;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 5px;
            padding: 10px;
        }
        .stButton>button:hover {
            background-color: #DC0000;
        }
        .stTextInput>div>div>input {
            background-color: #2B2B2B;
            color: white;
        }
        .stMarkdown {
            color: #FFFFFF;
        }
        [data-testid="column"]:first-child {
            background-color: #15151E;
            padding: 20px;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1,2])

    with col1:
        if st.button("Home"):
            st.switch_page("pages/user_landing.py")
        st.markdown("---")
        st.image("https://logodownload.org/wp-content/uploads/2016/11/formula-1-logo-7.png", width=200)

        st.markdown("### Customer Support")
        st.markdown("""
        🎫 **Support Ticket System**
        - AI-powered chat assistance
        - Automatic ticket creation for complex issues
        - Quick resolution for common queries

        📞 **Contact Information**
        - Email: support@f1app.com
        - Phone: +1 (555) 123-4567
        - Hours: 24/7 Support

        📚 **FAQ Section**
        - Troubleshooting common issues
        - Account management help
        - Billing and subscription information

        ---
        """)

    with col2:
        st.title("F1 Customer Support 🏁")
        
        chat_container = st.container()
        
        prompt = st.chat_input("How can we assist you today?")
        
        with chat_container:
            if len(st.session_state.messages) == 0:
                welcome_msg = "Welcome to F1 Customer Support! How can I assist you today?"
                st.session_state.messages.append({"role": "assistant", "content": welcome_msg})
            
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
        
            if prompt:
                with st.chat_message("user"):
                    st.markdown(prompt)
                st.session_state.messages.append({"role": "user", "content": prompt})

                with st.chat_message("assistant"):
                    with st.spinner("Processing your request..."):
                        response, create_ticket_flag = get_ai_response(prompt)
                        st.markdown(response)
                        if create_ticket_flag and not st.session_state.ticket_created:
                            st.success("A support ticket has been created. Our team will get back to you soon.")
                            st.session_state.ticket_created = True
                st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    st.set_page_config(
        page_title="F1 Customer Support",
        page_icon="🏁",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    main()
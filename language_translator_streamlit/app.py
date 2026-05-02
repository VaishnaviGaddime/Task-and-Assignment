import streamlit as st
import pandas as pd
from translator_utils import LANGUAGES, get_language_code, translate_text


st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍",
    layout="centered"
)


if "history" not in st.session_state:
    st.session_state.history = []


st.title("🌍 Language Translator App")
st.write("Translate text between English, Hindi, Marathi, Spanish, French, German and many more languages.")


tab1, tab2, tab3 = st.tabs(["Single Translation", "Batch CSV Translation", "Translation History"])


with tab1:
    st.subheader("Translate Text")

    col1, col2 = st.columns(2)

    with col1:
        source_language_name = st.selectbox(
            "From",
            list(LANGUAGES.keys()),
            index=0
        )

    with col2:
        target_language_name = st.selectbox(
            "To",
            list(LANGUAGES.keys())[1:],
            index=0
        )

    input_text = st.text_area(
        "Enter text",
        height=180,
        placeholder="Example: Hello, how are you?"
    )

    translate_button = st.button("Translate", type="primary")

    if translate_button:
        source_code = get_language_code(source_language_name)
        target_code = get_language_code(target_language_name)

        try:
            with st.spinner("Translating..."):
                translated_text = translate_text(
                    input_text,
                    source_code,
                    target_code
                )

            st.success("Translation completed!")

            st.text_area(
                "Translated text",
                value=translated_text,
                height=180
            )

            st.download_button(
                label="Download Translation",
                data=translated_text,
                file_name="translation.txt",
                mime="text/plain"
            )

            st.session_state.history.append({
                "Source Language": source_language_name,
                "Target Language": target_language_name,
                "Input Text": input_text,
                "Translated Text": translated_text
            })

        except Exception as e:
            st.error(f"Translation failed: {e}")


with tab2:
    st.subheader("Batch Translation Using CSV")

    st.write("Upload a CSV file with a column named `text`.")

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    col3, col4 = st.columns(2)

    with col3:
        batch_source_language_name = st.selectbox(
            "Batch From",
            list(LANGUAGES.keys()),
            index=0,
            key="batch_source"
        )

    with col4:
        batch_target_language_name = st.selectbox(
            "Batch To",
            list(LANGUAGES.keys())[1:],
            index=0,
            key="batch_target"
        )

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)

            st.write("Preview of uploaded file:")
            st.dataframe(df.head())

            if "text" not in df.columns:
                st.error("CSV must contain a column named `text`.")
            else:
                if st.button("Translate CSV", type="primary"):
                    source_code = get_language_code(batch_source_language_name)
                    target_code = get_language_code(batch_target_language_name)

                    translated_results = []

                    progress_bar = st.progress(0)

                    for index, row in df.iterrows():
                        text = str(row["text"])

                        try:
                            translated = translate_text(
                                text,
                                source_code,
                                target_code
                            )
                        except Exception as e:
                            translated = f"Error: {e}"

                        translated_results.append(translated)
                        progress_bar.progress((index + 1) / len(df))

                    df["translated_text"] = translated_results

                    st.success("CSV translation completed!")
                    st.dataframe(df)

                    csv_data = df.to_csv(index=False).encode("utf-8")

                    st.download_button(
                        label="Download Translated CSV",
                        data=csv_data,
                        file_name="translated_output.csv",
                        mime="text/csv"
                    )

        except Exception as e:
            st.error(f"Could not read CSV file: {e}")


with tab3:
    st.subheader("Translation History")

    if len(st.session_state.history) == 0:
        st.info("No translations yet.")
    else:
        history_df = pd.DataFrame(st.session_state.history)
        st.dataframe(history_df)

        history_csv = history_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download History",
            data=history_csv,
            file_name="translation_history.csv",
            mime="text/csv"
        )

        if st.button("Clear History"):
            st.session_state.history = []
            st.rerun()


st.markdown("---")
st.caption("Built with Streamlit and deep-translator.")

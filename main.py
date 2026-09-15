import streamlit as st
from dnaformater import load_to_df
from dnagraph import graph_builder, dna, gc, nuclotide


def main():

    st.set_page_config(
        page_title="DNA Comparison Analyzer",
        page_icon="🧬",
        layout="wide"
    )

    st.title("🧬 DNA Comparison Analyzer")

    st.markdown(
        """
        Welcome! 
        Upload a FASTA file and compare DNA sequences
        using several biological analyses.
        """
    )

    try:
        uploaded_file = st.file_uploader(
            "Upload FASTA File",
            type=["fasta", "fa"]
        )
    except:
        print("File is not found")

    if uploaded_file:

        df = load_to_df(uploaded_file)

        st.success("File loaded successfully!")

        option = st.selectbox(
            "Select Analysis",
            [
                "GC Content",
                "DNA Length",
                "Nucleotide Breakdown"
            ]
        )

        col1, col2, col3 = st.columns(3)

        col1.metric("Organisms", len(df))
        col2.metric(
            "Average GC %",
            f"{df['Gc content'].str.replace('%', '').astype(float).mean():.1f}%"
        )
        col3.metric(
            "Average Length",
            int(df["Dna length"].mean())
        )

        st.divider()

        if option == "GC Content":
            st.pyplot(graph_builder(gc, df))

        elif option == "DNA Length":
            st.pyplot(graph_builder(dna, df))

        elif option == "Nucleotide Breakdown":
            st.pyplot(graph_builder(nuclotide, df))

        st.divider()

        st.dataframe(df, use_container_width=True)


if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

df = pd.read_csv(
    "data/clean_ai_research.csv"
)

total_papers = len(df)

num_categories = df["primary_category"].nunique()

num_authors = df["first_author"].nunique()

avg_authors = df["num_authors"].mean()

updated_papers = df["is_updated"].sum()

# ==========================================
# LOAD DATA
# ==========================================

top_categories = pd.read_csv(
    "tables/top_categories.csv"
)

category_counts = pd.read_csv(
    "tables/category_counts.csv"
)

theme_summary = pd.read_csv(
    "tables/theme_summary.csv"
)

cv_trigrams = pd.read_csv(
    "tables/cv_trigrams.csv"
)

lg_trigrams = pd.read_csv(
    "tables/lg_trigrams.csv"
)

cl_trigrams = pd.read_csv(
    "tables/cl_trigrams.csv"
)

word_freq = pd.read_csv(
    "tables/word_freq.csv"
)

bigram_freq = pd.read_csv(
    "tables/bigram_freq.csv"
)

trigram_freq = pd.read_csv(
    "tables/trigram_freq.csv"
)

llm_presence = pd.read_csv(
    "tables/llm_presence.csv"
)

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Research Analysis",
    layout="wide"
)

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css("styles/style.css")

# ==========================================
# HEADER
# ==========================================

logo = Image.open("assets/brand-logo-primary.jpg")

col1, col2 = st.columns(
    [1.3, 8],
    vertical_alignment="center"
)

with col1:

    st.image(
        logo,
        use_container_width=True
    )

with col2:

    st.markdown("""
<div class="hero-container">

<h1 class="hero-title">
AI Research Analysis
</h1>

<h3 class="hero-subtitle">
Understanding the AI Research Landscape
</h3>

<p class="hero-date">
September 2025 – April 2026
</p>

</div>
""", unsafe_allow_html=True)
    
st.write("")
st.write("")


# ==========================================
#  CARDS        
# ==========================================
col1,col2,col3,col4 = st.columns(4)

with col1:

    st.markdown(
f"""
<div class="kpi-card">

<div class="kpi-number">
    {len(df):,}
</div>

<div class="kpi-title">
    Papers
</div>

</div>
""",
    unsafe_allow_html=True)

with col2:

    st.markdown(
f"""
<div class="kpi-card">

<div class="kpi-number">
    {df["primary_category"].nunique()}
</div>

<div class="kpi-title">
    Categories
</div>

</div>
""", 
    unsafe_allow_html=True)

with col3:

    st.markdown(
f"""
<div class="kpi-card">
<div class="kpi-number">
    {num_authors:,}
</div>

<div class="kpi-title">
    First Authors
</div>
</div>
""",
    unsafe_allow_html=True)

with col4:

    st.markdown(
f"""
<div class="kpi-card">
<div class="kpi-number">
    8
</div>

<div class="kpi-title">
    Months
</div>
</div>
""",
    unsafe_allow_html=True)


st.write("")
st.write("")
st.write("")

# ==========================================
#  1. Overview of AI Research
# ==========================================

st.title("1. Overview of AI Research")

max_value = category_counts["paper_count"].max()

fig = px.bar(
    category_counts.head(10),
    x="paper_count",
    y="category",
    orientation="h",
    title="Top Most Researched Categories",
    text="paper_count"
)

fig.update_layout(
    template="plotly_white",
    yaxis=dict(
        autorange="reversed",
        automargin=True
    ),
    xaxis=dict(
        showticklabels=False,
        range=[0, max_value * 1.06]   # Smaller padding
    ),
    yaxis_title="",
    xaxis_title="Number of Papers",
    coloraxis_showscale=False,
    margin=dict(
        l=10,
        r=20,
        t=50,
        b=10
    )
)

fig.update_traces(
    marker_color="#B31B1B",
    textposition="outside",
    cliponaxis=False
)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={
        "displayModeBar": False,
        "scrollZoom": False,
        "staticPlot": True
    }
)

with st.expander("View all 107 categories"):
    st.dataframe(category_counts)

st.info(
    """
    **Insight**

    Computer Vision **cs.CV**, Machine Learning **cs.LG**, and Computational Linguistics **cs.CL** are the three most researched AI categories.
    """
)

st.write("")
st.write("")
st.write("")

st.subheader("Research Concentration")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(f"""
<div class="kpi-card">

<div class="kpi-number">
51.0%
</div>

<div class="kpi-title">
Top 3 Categories
<br>
of All Papers
</div>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown(f"""
<div class="kpi-card">

<div class="kpi-number">
66.4%
</div>

<div class="kpi-title">
Top 5 Categories
<br>
of All Papers
</div>

</div>
""", unsafe_allow_html=True)

with col3:

    st.markdown(f"""
<div class="kpi-card">

<div class="kpi-number">
87.3%
</div>

<div class="kpi-title">
Top 10 Categories
<br>
of All Papers
</div>

</div>
""", unsafe_allow_html=True)
    
st.write("")
    
st.info(
    """
    **Insight**

    Although the dataset spans **107 AI categories**, **the top 10 categories account for
    87.3% of all papers**, and **the Top 3 categories account for 51.0% of all papers**, highlighting a strong concentration of research activity.
    """
)

st.write("")
st.write("")
st.write("")
    
# ==========================================
# 2. RESEARCH CONTENT ANALYSIS
# ==========================================

st.header("2. Research Content Analysis")

st.write("""
Natural Language Processing (NLP) was applied to the research abstracts to uncover
the dominant topics and research directions within the three largest AI fields.
""")

tab1, tab2, tab3 = st.tabs(
    [
        "Computer Vision",
        "Machine Learning",
        "Computational Linguistics"
    ]
)

# COMPUTER VISION

with tab1:

    st.subheader("Top Trigrams in Computer Vision")

    st.dataframe(
        cv_trigrams,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        """
        **Insight**

        Computer Vision research is increasingly centered around
        **Vision-Language Models (VLMs)** and multimodal learning,
        while maintaining strong interest in image understanding,
        segmentation, and visual reasoning.
        """
    )

# MACHINE LEARNING

with tab2:

    st.subheader("Top Trigrams in Machine Learning")

    st.dataframe(
        lg_trigrams,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        """
        **Insight**

        Machine Learning research shows a strong emphasis on
        **Large Language Models**, Reinforcement Learning,
        Graph Neural Networks, and optimization techniques,
        highlighting the diversity of modern learning algorithms.
        """
    )

# COMPUTATIONAL LINGUISTICS

with tab3:

    st.subheader("Top Trigrams in Computational Linguistics")

    st.dataframe(
        cl_trigrams,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        """
        **Insight**

        Computational Linguistics is heavily dominated by
        **Large Language Models (LLMs)**, Retrieval-Augmented
        Generation (RAG), and fine-tuning strategies,
        reflecting the rapid evolution of modern language AI.
        """
    )

st.write("")
st.write("")
st.write("")

# =====================================================
# 3. Technology Trends
# =====================================================


st.header("3. Technology Trends")

st.write("""
Research abstracts were analyzed to identify the most frequently discussed AI
technologies and methodologies across the dataset. This provides a broader view
of the concepts currently shaping AI research.
""")

max_value = theme_summary["Percentage_of_Papers"].max()

fig = px.bar(
    theme_summary,
    x="Percentage_of_Papers",
    y="Theme",
    orientation="h",
    text="Percentage_of_Papers"
)

fig.update_layout(
    template="plotly_white",
    yaxis=dict(
        autorange="reversed",
        automargin=True
    ),
    xaxis=dict(
        showticklabels=False,
        range=[0, max_value * 1.08]
    ),
    xaxis_title="",
    yaxis_title="",
    margin=dict(
        l=10,
        r=20,
        t=50,
        b=10
    )
)

fig.update_traces(
    marker_color="#B31B1B",
    texttemplate="%{text:.1f}%",
    textposition="outside",
    cliponaxis=False
)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={
        "displayModeBar": False,
        "scrollZoom": False,
        "staticPlot": True
    }
)

st.info(
    """
**Insight**

**Large Language Models** are the dominant technology discussed in the dataset,
appearing in **over one-quarter of all research papers**. Fine-Tuning,
Vision-Language Models, and Retrieval-Augmented Generation also emerge as
recurring technologies, highlighting the growing influence of foundation models
across modern AI research.
"""
)

st.write("")
st.write("")
st.write("")

# =====================================================
# 4. Research Vocabulary
# =====================================================


st.header("4. Research Vocabulary")

tab1, tab2, tab3 = st.tabs(
    [
        "Words",
        "Phrases",
        "Concepts"
    ]
)

with tab1:

    st.subheader("Most Frequent Words")

    st.dataframe(
        word_freq.head(20),
        use_container_width=True,
        hide_index=True
    )

with tab2:

    st.subheader("Most Frequent Two-Word Phrases")

    st.dataframe(
        bigram_freq.head(20),
        use_container_width=True,
        hide_index=True
    )

with tab3:

    st.subheader("Most Frequent Three-Word Phrases")

    st.dataframe(
        trigram_freq.head(20),
        use_container_width=True,
        hide_index=True
    )


st.markdown(
    '<div class="spacer-lg"></div>',
    unsafe_allow_html=True
)


st.write("")
st.write("")
st.write("")

# =====================================================
# 5. LARGE LANGUAGE MODELS IN AI RESEARCH
# =====================================================

llm_presence["Category"] = [
    "Computer Vision",
    "Machine Learning",
    "Computational Linguistics"
]



st.header("5. Large Language Models in AI Research")

st.write("""
The previous section identified **Large Language Models (LLMs)** as the most
frequently discussed technology throughout the dataset. To better understand
their influence, this section examines how deeply LLMs have penetrated the
three largest AI research fields. Each chart represents the percentage of
papers within that specific category that mention Large Language Models.
""")

cols = st.columns(3)

for col, (_, row) in zip(cols, llm_presence.iterrows()):

    with col:

        fig = px.pie(
            names=["LLM", "Other Papers"],
            values=[
                row["LLM_Percentage"],
                100 - row["LLM_Percentage"]
            ],
            hole=0.65
        )

        fig.update_traces(
            textinfo="none",
            sort=False,              # Keep slice order exactly as provided
            direction="clockwise",   # Always fill in the same direction
            rotation=90,             # Start at 12 o'clock
            marker=dict(
                colors=[
                    "#B31B1B",
                    "#E6E6E6"
                ]
            )
        )

        # Percentage in the center
        fig.add_annotation(
            text=f"<b>{row['LLM_Percentage']:.1f}%</b><br><span style='font-size:20px;color:#666666;'>LLM mentioned</span>",
            showarrow=False,
            x=0.5,
            y=0.5,
            font=dict(
                size=30,
                color="#B31B1B"
            )
        )

        fig.update_layout(
            title=dict(
                text=row["Category"],
                x=0.5,
                xanchor="center",
                y=0.96,
                yanchor="top"
            ),
            showlegend=False,
            margin=dict(
                l=10,
                r=10,
                t=50,
                b=10
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={
            "displayModeBar": False,
            "scrollZoom": False,
            "staticPlot": True
            }
        )

st.info(
"""
**Insight**

These charts illustrate the proportion of papers **within each research field**
that mention **Large Language Models (LLMs)**. Computational Linguistics shows
the highest level of LLM adoption, with nearly two-thirds of its papers
referencing LLMs. Although the percentages are lower in Machine Learning and
Computer Vision, LLMs are still widely represented, indicating that they have
expanded beyond natural language processing and are becoming foundational
technologies across multiple AI disciplines.
"""
)
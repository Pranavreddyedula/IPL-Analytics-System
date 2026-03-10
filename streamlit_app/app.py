import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page settings
st.set_page_config(page_title="IPL Analytics Dashboard", layout="wide")

# Title
st.title("🏏 IPL Match Data Analysis Dashboard")
st.markdown("Analyze team performance, toss impact, venue influence and player contributions.")

# Load dataset
df = pd.read_csv("data/Cricket_data.csv")

# Sidebar filters
st.sidebar.header("Filters")

if 'season' in df.columns:
    season = st.sidebar.selectbox("Select Season", df['season'].unique())
    df = df[df['season'] == season]

# Dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Create two columns for graphs
col1, col2 = st.columns(2)

# --------------------------
# Team Wins
# --------------------------

if 'winner' in df.columns:

    with col1:
        st.subheader("Team Wins")

        wins = df['winner'].value_counts()

        fig, ax = plt.subplots()

        sns.barplot(x=wins.values, y=wins.index, ax=ax)

        ax.set_title("Total Wins by Team")

        st.pyplot(fig)

# --------------------------
# Toss Impact
# --------------------------

if 'toss_won' in df.columns and 'winner' in df.columns:

    with col2:

        st.subheader("Toss Impact")

        df['toss_match_win'] = df['toss_won'] == df['winner']

        toss = df['toss_match_win'].value_counts()

        fig2, ax2 = plt.subplots()

        toss.plot(kind="pie", autopct='%1.1f%%', ax=ax2)

        ax2.set_ylabel("")

        st.pyplot(fig2)

# Create second row
col3, col4 = st.columns(2)

# --------------------------
# Venue Analysis
# --------------------------

if 'venue_name' in df.columns:

    with col3:

        st.subheader("Top Venues")

        venue = df['venue_name'].value_counts().head(10)

        fig3, ax3 = plt.subplots()

        sns.barplot(x=venue.values, y=venue.index, ax=ax3)

        ax3.set_title("Matches by Venue")

        st.pyplot(fig3)

# --------------------------
# Player Contribution
# --------------------------

if 'pom' in df.columns:

    with col4:

        st.subheader("Top Player of Match Winners")

        top_players = df['pom'].value_counts().head(10)

        fig4, ax4 = plt.subplots()

        sns.barplot(x=top_players.values, y=top_players.index, ax=ax4)

        ax4.set_title("Player of Match Leaders")

        st.pyplot(fig4)

# --------------------------
# Score Distribution
# --------------------------

if '1st_inning_score' in df.columns:

    st.subheader("First Innings Score Distribution")

    fig5, ax5 = plt.subplots()

    sns.histplot(df['1st_inning_score'], bins=20, ax=ax5)

    ax5.set_title("Score Distribution")

    st.pyplot(fig5)

st.markdown("---")
st.markdown("📊 IPL Sports Analytics Dashboard | Built with Python & Streamlit")
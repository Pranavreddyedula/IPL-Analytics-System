
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/Cricket_data.csv")

print("Dataset Loaded")

if 'winner' in df.columns:
    team_wins = df['winner'].value_counts()

    plt.figure(figsize=(12,6))
    sns.barplot(x=team_wins.index,y=team_wins.values)
    plt.xticks(rotation=90)
    plt.title("Team Performance - Wins")
    plt.tight_layout()
    plt.show()

if 'toss_won' in df.columns and 'winner' in df.columns:
    df['toss_match_win'] = df['toss_won'] == df['winner']
    toss = df['toss_match_win'].value_counts()

    plt.figure(figsize=(6,6))
    toss.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Toss Impact on Match Outcome")
    plt.show()

if 'venue_name' in df.columns:
    venue = df['venue_name'].value_counts().head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(x=venue.values,y=venue.index)
    plt.title("Top Venues")
    plt.show()

if 'pom' in df.columns:
    top_players = df['pom'].value_counts().head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(x=top_players.values,y=top_players.index)
    plt.title("Top Player of the Match Winners")
    plt.show()

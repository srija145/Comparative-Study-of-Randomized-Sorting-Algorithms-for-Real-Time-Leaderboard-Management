import streamlit as st
import sqlite3
import pandas as pd

# Function to reshape round data
def reshape_rankings(row_data):
    records = []
    for rank in range(1, 6):
        player_id = row_data.get(f"Rank {rank} ID", None)
        score = row_data.get(f"Rank {rank} Score", None)
        name = row_data.get(f"Rank {rank} Name", None)
        if player_id and name and score:
            records.append({
                "Rank": rank,
                "Player ID": player_id,
                "Player Name": name,
                "Score": int(score)
            })
    return pd.DataFrame(records)

# Get list of available rounds
def get_rounds():
    conn = sqlite3.connect("player_rankings.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Round FROM TopPlayers")
    rounds = [row[0] for row in cursor.fetchall()]
    conn.close()
    return rounds

# Get data for a specific round
def get_round_data(round_name):
    conn = sqlite3.connect("player_rankings.db")
    df = pd.read_sql_query("SELECT * FROM TopPlayers WHERE Round = ?", conn, params=(round_name,))
    conn.close()
    return df.iloc[0].to_dict()

# Function to render the HTML table
def render_centered_html_table(df):
    html = """
    <div style='width: 80%; margin: 20px auto;'>
        <table style='border-collapse: collapse; width: 100%; text-align: center; font-size: 18px;'>
            <thead>
                <tr>
    """
    for col in df.columns:
        html += f"<th style='border: 1px solid #ddd; padding: 12px; background-color: #333;'>{col}</th>"
    html += "</tr></thead><tbody>"

    for _, row in df.iterrows():
        html += "<tr>"
        for item in row:
            html += f"<td style='border: 1px solid #ddd; padding: 12px;'>{item}</td>"
        html += "</tr>"
    html += "</tbody></table></div>"

    st.markdown(html, unsafe_allow_html=True)

# Streamlit UI layout
st.set_page_config(page_title="🏆 Player Leaderboard", layout="wide")
st.markdown("<h5 style='text-align: center;'>UMBC DATA690 - Data Structures and Algorithms (Spring 2025)</h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Project 02 (Team 01)</h5>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>🏅 Player Rankings Table</h1>", unsafe_allow_html=True)

# Style the dropdown using CSS
st.markdown("""
    <style>
        .centered-dropdown > div {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
        .stSelectbox {
            width: 300px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Dropdown container
with st.container():
    round_options = get_rounds()
    default_index = round_options.index("Total Score") if "Total Score" in round_options else 0
    st.markdown('<div class="centered-dropdown">', unsafe_allow_html=True)
    selected_round = st.selectbox("Select Round", round_options, index=default_index)
    st.markdown('</div>', unsafe_allow_html=True)

# Subheading
st.markdown(
    f"<div style='text-align: center; font-size: 22px;'>Results for: <strong>{selected_round}</strong></div>",
    unsafe_allow_html=True
)

# Get and render table
round_data = get_round_data(selected_round)
df_formatted = reshape_rankings(round_data)
render_centered_html_table(df_formatted)

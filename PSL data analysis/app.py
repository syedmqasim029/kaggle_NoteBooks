from flask import Flask, render_template, jsonify
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
from datetime import datetime

app = Flask(__name__)

# Load data
df = pd.read_csv('psl_2025_matches.csv')

# Data preprocessing
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')
df['Margin'] = pd.to_numeric(df['Margin'], errors='coerce')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/overview')
def overview():
    """Get overview statistics"""
    total_matches = len(df)
    total_teams = len(set(df['Team_1'].unique()) | set(df['Team_2'].unique()))
    venues = df['Venue'].nunique()
    
    # Win by type
    win_by_wickets = len(df[df['Won_By'] == 'Wickets'])
    win_by_runs = len(df[df['Won_By'] == 'Runs'])
    
    return jsonify({
        'total_matches': int(total_matches),
        'total_teams': int(total_teams),
        'total_venues': int(venues),
        'win_by_wickets': int(win_by_wickets),
        'win_by_runs': int(win_by_runs)
    })

@app.route('/api/team_performance')
def team_performance():
    """Get team performance data"""
    # Count wins per team
    wins = df[df['Winning_Team'] != 'No Result']['Winning_Team'].value_counts().reset_index()
    wins.columns = ['Team', 'Wins']
    
    # Count total matches per team
    team_matches = {}
    for team in df['Team_1'].unique():
        matches = len(df[(df['Team_1'] == team) | (df['Team_2'] == team)])
        team_matches[team] = matches
    
    wins['Total_Matches'] = wins['Team'].map(team_matches)
    wins['Win_Percentage'] = (wins['Wins'] / wins['Total_Matches'] * 100).round(2)
    
    # Create visualization
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=wins['Team'],
        y=wins['Wins'],
        name='Wins',
        marker_color='#00a8cc',
        text=wins['Wins'],
        textposition='auto',
    ))
    
    fig.update_layout(
        title='Team Performance - Total Wins',
        xaxis_title='Team',
        yaxis_title='Number of Wins',
        template='plotly_white',
        height=400,
        font=dict(size=12),
        showlegend=False
    )
    
    return jsonify({
        'chart': json.loads(fig.to_json()),
        'data': wins.to_dict('records')
    })

@app.route('/api/win_percentage')
def win_percentage():
    """Win percentage chart"""
    wins = df[df['Winning_Team'] != 'No Result']['Winning_Team'].value_counts().reset_index()
    wins.columns = ['Team', 'Wins']
    
    team_matches = {}
    for team in df['Team_1'].unique():
        matches = len(df[(df['Team_1'] == team) | (df['Team_2'] == team)])
        team_matches[team] = matches
    
    wins['Total_Matches'] = wins['Team'].map(team_matches)
    wins['Win_Percentage'] = (wins['Wins'] / wins['Total_Matches'] * 100).round(2)
    wins = wins.sort_values('Win_Percentage', ascending=True)
    
    fig = go.Figure(go.Bar(
        x=wins['Win_Percentage'],
        y=wins['Team'],
        orientation='h',
        marker=dict(
            color=wins['Win_Percentage'],
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="Win %")
        ),
        text=wins['Win_Percentage'].apply(lambda x: f'{x}%'),
        textposition='auto',
    ))
    
    fig.update_layout(
        title='Team Win Percentage',
        xaxis_title='Win Percentage (%)',
        yaxis_title='Team',
        template='plotly_white',
        height=400,
        font=dict(size=12)
    )
    
    return jsonify(json.loads(fig.to_json()))

@app.route('/api/toss_impact')
def toss_impact():
    """Toss impact analysis"""
    # Remove No Result matches
    df_matches = df[df['Winning_Team'] != 'No Result'].copy()
    
    # Check if toss winner won the match
    df_matches['Toss_Won_Match'] = df_matches['Toss_Winner'] == df_matches['Winning_Team']
    
    toss_wins = df_matches['Toss_Won_Match'].value_counts()
    
    fig = go.Figure(data=[go.Pie(
        labels=['Toss Winner Won', 'Toss Winner Lost'],
        values=[toss_wins.get(True, 0), toss_wins.get(False, 0)],
        hole=0.4,
        marker=dict(colors=['#00a8cc', '#ff6b6b']),
        textinfo='label+percent+value',
        textfont=dict(size=14)
    )])
    
    fig.update_layout(
        title='Toss Impact - Did Toss Winners Win the Match?',
        template='plotly_white',
        height=400,
        font=dict(size=12)
    )
    
    return jsonify(json.loads(fig.to_json()))

@app.route('/api/venue_stats')
def venue_stats():
    """Venue statistics"""
    venue_matches = df['Venue'].value_counts().reset_index()
    venue_matches.columns = ['Venue', 'Matches']
    
    fig = go.Figure(data=[go.Pie(
        labels=venue_matches['Venue'],
        values=venue_matches['Matches'],
        hole=0.3,
        textinfo='label+value',
        textfont=dict(size=11)
    )])
    
    fig.update_layout(
        title='Matches Played at Each Venue',
        template='plotly_white',
        height=400,
        font=dict(size=12)
    )
    
    return jsonify(json.loads(fig.to_json()))

@app.route('/api/win_method')
def win_method():
    """Win method analysis"""
    df_matches = df[df['Winning_Team'] != 'No Result'].copy()
    win_by = df_matches['Won_By'].value_counts().reset_index()
    win_by.columns = ['Method', 'Count']
    
    fig = go.Figure(data=[go.Bar(
        x=win_by['Method'],
        y=win_by['Count'],
        marker_color=['#4ecdc4', '#ff6b6b'],
        text=win_by['Count'],
        textposition='auto',
    )])
    
    fig.update_layout(
        title='Wins by Method (Runs vs Wickets)',
        xaxis_title='Winning Method',
        yaxis_title='Number of Wins',
        template='plotly_white',
        height=400,
        font=dict(size=12)
    )
    
    return jsonify(json.loads(fig.to_json()))

@app.route('/api/margin_distribution')
def margin_distribution():
    """Victory margin distribution"""
    df_margins = df[df['Winning_Team'] != 'No Result'].copy()
    df_margins = df_margins.dropna(subset=['Margin'])
    
    fig = go.Figure()
    
    # Separate by win type
    runs_margins = df_margins[df_margins['Won_By'] == 'Runs']['Margin']
    wickets_margins = df_margins[df_margins['Won_By'] == 'Wickets']['Margin']
    
    fig.add_trace(go.Histogram(
        x=runs_margins,
        name='Runs',
        marker_color='#00a8cc',
        opacity=0.7,
        nbinsx=15
    ))
    
    fig.add_trace(go.Histogram(
        x=wickets_margins,
        name='Wickets',
        marker_color='#ff6b6b',
        opacity=0.7,
        nbinsx=10
    ))
    
    fig.update_layout(
        title='Distribution of Victory Margins',
        xaxis_title='Margin',
        yaxis_title='Frequency',
        template='plotly_white',
        height=400,
        barmode='overlay',
        font=dict(size=12)
    )
    
    return jsonify(json.loads(fig.to_json()))

@app.route('/api/player_of_match')
def player_of_match():
    """Player of the Match analysis"""
    potm = df[df['POTM'].notna()]['POTM'].value_counts().head(10).reset_index()
    potm.columns = ['Player', 'Awards']
    
    fig = go.Figure(go.Bar(
        x=potm['Awards'],
        y=potm['Player'],
        orientation='h',
        marker=dict(
            color=potm['Awards'],
            colorscale='Blues',
            showscale=False
        ),
        text=potm['Awards'],
        textposition='auto',
    ))
    
    fig.update_layout(
        title='Top 10 Players by POTM Awards',
        xaxis_title='Number of Awards',
        yaxis_title='Player',
        template='plotly_white',
        height=500,
        font=dict(size=12)
    )
    
    return jsonify(json.loads(fig.to_json()))

@app.route('/api/toss_decision')
def toss_decision():
    """Toss decision analysis"""
    toss_decision = df['Toss_Decision'].value_counts().reset_index()
    toss_decision.columns = ['Decision', 'Count']
    
    fig = go.Figure(data=[go.Pie(
        labels=toss_decision['Decision'],
        values=toss_decision['Count'],
        hole=0.4,
        marker=dict(colors=['#4ecdc4', '#ffd93d']),
        textinfo='label+percent+value',
        textfont=dict(size=14)
    )])
    
    fig.update_layout(
        title='Toss Decision Preference (Bat vs Field)',
        template='plotly_white',
        height=400,
        font=dict(size=12)
    )
    
    return jsonify(json.loads(fig.to_json()))

@app.route('/api/match_timeline')
def match_timeline():
    """Matches over time"""
    df_timeline = df.copy()
    df_timeline['Date'] = pd.to_datetime(df_timeline['Date'])
    df_timeline = df_timeline.sort_values('Date')
    df_timeline['Match_Count'] = range(1, len(df_timeline) + 1)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df_timeline['Date'],
        y=df_timeline['Match_Count'],
        mode='lines+markers',
        line=dict(color='#00a8cc', width=2),
        marker=dict(size=6),
        fill='tozeroy',
        fillcolor='rgba(0, 168, 204, 0.2)'
    ))
    
    fig.update_layout(
        title='Tournament Timeline - Cumulative Matches',
        xaxis_title='Date',
        yaxis_title='Cumulative Match Count',
        template='plotly_white',
        height=400,
        font=dict(size=12)
    )
    
    return jsonify(json.loads(fig.to_json()))

@app.route('/api/head_to_head')
def head_to_head():
    """Head to head comparison"""
    teams = sorted(df['Team_1'].unique())
    h2h_matrix = []
    
    for team1 in teams:
        row = []
        for team2 in teams:
            if team1 == team2:
                row.append(0)
            else:
                wins = len(df[
                    ((df['Team_1'] == team1) | (df['Team_2'] == team1)) &
                    (df['Winning_Team'] == team1) &
                    ((df['Team_1'] == team2) | (df['Team_2'] == team2))
                ])
                row.append(wins)
        h2h_matrix.append(row)
    
    fig = go.Figure(data=go.Heatmap(
        z=h2h_matrix,
        x=teams,
        y=teams,
        colorscale='Blues',
        text=h2h_matrix,
        texttemplate='%{text}',
        textfont={"size": 12},
        colorbar=dict(title="Wins")
    ))
    
    fig.update_layout(
        title='Head-to-Head: Wins Matrix',
        xaxis_title='Opponent',
        yaxis_title='Team',
        template='plotly_white',
        height=500,
        font=dict(size=11)
    )
    
    return jsonify(json.loads(fig.to_json()))

@app.route('/api/recent_matches')
def recent_matches():
    """Get recent matches"""
    recent = df.tail(10).sort_values('Date', ascending=False)
    
    matches = []
    for _, row in recent.iterrows():
        matches.append({
            'date': row['Date'].strftime('%d %b %Y'),
            'team1': row['Team_1'],
            'team2': row['Team_2'],
            'winner': row['Winning_Team'],
            'venue': row['Venue'],
            'potm': row['POTM'],
            'margin': f"{int(row['Margin'])} {row['Won_By']}" if pd.notna(row['Margin']) else 'N/A'
        })
    
    return jsonify(matches)

if __name__ == '__main__':
    app.run(debug=True, port=8080)

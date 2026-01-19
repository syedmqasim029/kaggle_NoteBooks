// Load all data when page loads
document.addEventListener('DOMContentLoaded', function() {
    loadOverview();
    loadAllCharts();
    loadRecentMatches();
});

// Load overview statistics
async function loadOverview() {
    try {
        const response = await fetch('/api/overview');
        const data = await response.json();
        
        document.getElementById('totalMatches').textContent = data.total_matches;
        document.getElementById('totalTeams').textContent = data.total_teams;
        document.getElementById('totalVenues').textContent = data.total_venues;
        document.getElementById('winByWickets').textContent = data.win_by_wickets;
        document.getElementById('winByRuns').textContent = data.win_by_runs;
    } catch (error) {
        console.error('Error loading overview:', error);
    }
}

// Load all charts
async function loadAllCharts() {
    await loadTeamPerformance();
    await loadWinPercentage();
    await loadTossImpact();
    await loadVenueStats();
    await loadWinMethod();
    await loadMarginDistribution();
    await loadPlayerOfMatch();
    await loadTossDecision();
    await loadMatchTimeline();
    await loadHeadToHead();
}

// Load team performance chart
async function loadTeamPerformance() {
    try {
        const response = await fetch('/api/team_performance');
        const data = await response.json();
        Plotly.newPlot('teamPerformanceChart', data.chart.data, data.chart.layout, {
            responsive: true,
            displayModeBar: true,
            displaylogo: false
        });
    } catch (error) {
        console.error('Error loading team performance:', error);
    }
}

// Load win percentage chart
async function loadWinPercentage() {
    try {
        const response = await fetch('/api/win_percentage');
        const data = await response.json();
        Plotly.newPlot('winPercentageChart', data.data, data.layout, {
            responsive: true,
            displayModeBar: true,
            displaylogo: false
        });
    } catch (error) {
        console.error('Error loading win percentage:', error);
    }
}

// Load toss impact chart
async function loadTossImpact() {
    try {
        const response = await fetch('/api/toss_impact');
        const data = await response.json();
        Plotly.newPlot('tossImpactChart', data.data, data.layout, {
            responsive: true,
            displayModeBar: true,
            displaylogo: false
        });
    } catch (error) {
        console.error('Error loading toss impact:', error);
    }
}

// Load venue stats chart
async function loadVenueStats() {
    try {
        const response = await fetch('/api/venue_stats');
        const data = await response.json();
        Plotly.newPlot('venueStatsChart', data.data, data.layout, {
            responsive: true,
            displayModeBar: true,
            displaylogo: false
        });
    } catch (error) {
        console.error('Error loading venue stats:', error);
    }
}

// Load win method chart
async function loadWinMethod() {
    try {
        const response = await fetch('/api/win_method');
        const data = await response.json();
        Plotly.newPlot('winMethodChart', data.data, data.layout, {
            responsive: true,
            displayModeBar: true,
            displaylogo: false
        });
    } catch (error) {
        console.error('Error loading win method:', error);
    }
}

// Load margin distribution chart
async function loadMarginDistribution() {
    try {
        const response = await fetch('/api/margin_distribution');
        const data = await response.json();
        Plotly.newPlot('marginDistributionChart', data.data, data.layout, {
            responsive: true,
            displayModeBar: true,
            displaylogo: false
        });
    } catch (error) {
        console.error('Error loading margin distribution:', error);
    }
}

// Load player of match chart
async function loadPlayerOfMatch() {
    try {
        const response = await fetch('/api/player_of_match');
        const data = await response.json();
        Plotly.newPlot('playerOfMatchChart', data.data, data.layout, {
            responsive: true,
            displayModeBar: true,
            displaylogo: false
        });
    } catch (error) {
        console.error('Error loading player of match:', error);
    }
}

// Load toss decision chart
async function loadTossDecision() {
    try {
        const response = await fetch('/api/toss_decision');
        const data = await response.json();
        Plotly.newPlot('tossDecisionChart', data.data, data.layout, {
            responsive: true,
            displayModeBar: true,
            displaylogo: false
        });
    } catch (error) {
        console.error('Error loading toss decision:', error);
    }
}

// Load match timeline chart
async function loadMatchTimeline() {
    try {
        const response = await fetch('/api/match_timeline');
        const data = await response.json();
        Plotly.newPlot('matchTimelineChart', data.data, data.layout, {
            responsive: true,
            displayModeBar: true,
            displaylogo: false
        });
    } catch (error) {
        console.error('Error loading match timeline:', error);
    }
}

// Load head to head chart
async function loadHeadToHead() {
    try {
        const response = await fetch('/api/head_to_head');
        const data = await response.json();
        Plotly.newPlot('headToHeadChart', data.data, data.layout, {
            responsive: true,
            displayModeBar: true,
            displaylogo: false
        });
    } catch (error) {
        console.error('Error loading head to head:', error);
    }
}

// Load recent matches
async function loadRecentMatches() {
    try {
        const response = await fetch('/api/recent_matches');
        const matches = await response.json();
        
        const container = document.getElementById('recentMatches');
        container.innerHTML = '';
        
        matches.forEach(match => {
            const matchCard = document.createElement('div');
            matchCard.className = 'match-card';
            
            matchCard.innerHTML = `
                <div class="match-date">${match.date} • ${match.venue}</div>
                <div class="match-teams">
                    ${match.team1} <span class="match-vs">vs</span> ${match.team2}
                </div>
                <div class="match-winner">🏆 Winner: ${match.winner}</div>
                <div class="match-details">Margin: ${match.margin}</div>
                <div class="match-potm">⭐ Player of the Match: ${match.potm}</div>
            `;
            
            container.appendChild(matchCard);
        });
    } catch (error) {
        console.error('Error loading recent matches:', error);
        document.getElementById('recentMatches').innerHTML = 
            '<div class="loading">Error loading matches</div>';
    }
}

// Handle window resize for responsive charts
window.addEventListener('resize', function() {
    const chartIds = [
        'teamPerformanceChart', 'winPercentageChart', 'tossImpactChart',
        'venueStatsChart', 'winMethodChart', 'marginDistributionChart',
        'playerOfMatchChart', 'tossDecisionChart', 'matchTimelineChart',
        'headToHeadChart'
    ];
    
    chartIds.forEach(id => {
        const element = document.getElementById(id);
        if (element && element.data) {
            Plotly.Plots.resize(element);
        }
    });
});

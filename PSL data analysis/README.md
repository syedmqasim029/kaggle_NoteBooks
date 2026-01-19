# 🏏 PSL 2025 Data Analysis Dashboard

A comprehensive web-based data analysis and visualization dashboard for Pakistan Super League (PSL) 2025 matches. This project features interactive visualizations, detailed statistics, and modern UI design.

## 📊 Features

### Data Analysis
- **Tournament Overview**: Total matches, teams, venues, and win statistics
- **Team Performance**: Wins count and win percentage for each team
- **Toss Analysis**: Impact of toss on match outcomes
- **Venue Statistics**: Distribution of matches across venues
- **Victory Analysis**: Win methods (runs vs wickets) and margin distribution
- **Player Statistics**: Top Player of the Match (POTM) award winners
- **Head-to-Head**: Win matrix showing team rivalries
- **Timeline Analysis**: Tournament progression over time
- **Recent Matches**: Latest match results with details

### Visualizations
- Interactive bar charts for team performance
- Pie charts for toss impact and venue distribution
- Histograms for victory margin analysis
- Heatmaps for head-to-head comparison
- Line charts for tournament timeline
- All charts are fully interactive and responsive

### User Interface
- Modern, responsive design that works on all devices
- Beautiful gradient background and card-based layout
- Smooth animations and hover effects
- Clean, professional typography
- Mobile-friendly interface

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- Pandas (data analysis)
- Plotly (interactive visualizations)
- NumPy (numerical computing)

### Step 2: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Step 3: Access the Dashboard

Open your web browser and navigate to:
```
http://localhost:5000
```

## 📁 Project Structure

```
PSL data analysis/
│
├── app.py                      # Flask backend with API endpoints
├── psl_2025_matches.csv        # Dataset with match information
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── templates/
│   └── index.html             # Main HTML template
│
└── static/
    ├── css/
    │   └── style.css          # Styling and responsive design
    └── js/
        └── main.js            # Frontend JavaScript for charts
```

## 🔧 Technologies Used

### Backend
- **Flask**: Lightweight Python web framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualization library

### Frontend
- **HTML5**: Structure
- **CSS3**: Modern styling with gradients, animations
- **JavaScript**: Dynamic content loading
- **Plotly.js**: Client-side chart rendering
- **Google Fonts**: Poppins font family

## 📈 API Endpoints

The application provides the following REST API endpoints:

- `GET /` - Main dashboard page
- `GET /api/overview` - Tournament overview statistics
- `GET /api/team_performance` - Team wins and performance data
- `GET /api/win_percentage` - Win percentage by team
- `GET /api/toss_impact` - Toss winner vs match winner analysis
- `GET /api/venue_stats` - Matches per venue
- `GET /api/win_method` - Wins by runs vs wickets
- `GET /api/margin_distribution` - Victory margin histogram
- `GET /api/player_of_match` - Top POTM award winners
- `GET /api/toss_decision` - Bat vs field decision analysis
- `GET /api/match_timeline` - Tournament progression timeline
- `GET /api/head_to_head` - Team rivalry heatmap
- `GET /api/recent_matches` - Recent match results

## 📊 Dataset Information

The dataset (`psl_2025_matches.csv`) contains the following columns:

- **Match_ID**: Unique identifier for each match
- **Match_No**: Sequential match number
- **Date**: Match date
- **Team_1**: First team
- **Team_2**: Second team
- **Venue**: Match location
- **Toss_Winner**: Team that won the toss
- **Toss_Decision**: Bat or Field
- **Winning_Team**: Match winner
- **Won_By**: Runs or Wickets
- **Margin**: Victory margin
- **Target**: Target score (if applicable)
- **POTM**: Player of the Match
- **Notes**: Special match notes

## 🎨 Customization

### Changing Colors
Edit `static/css/style.css`:
- Gradient background: `.body` section
- Primary color: `#667eea`
- Secondary color: `#764ba2`

### Adding New Charts
1. Add API endpoint in `app.py`
2. Create chart function in `static/js/main.js`
3. Add chart container in `templates/index.html`

### Modifying Layout
- Grid layout: `.stats-grid` and `.chart-row` classes
- Card styling: `.stat-card` and `.chart-card` classes
- Responsive breakpoints: Media queries in CSS

## 🔍 Key Insights from PSL 2025

Based on the analysis:
- **Champion**: Lahore Qalandars (won the final)
- **Largest Victory**: 120 runs by Peshawar Zalmi (Match 9)
- **Highest Total**: 263/3 by Quetta Gladiators (Match 26)
- **Venues**: 5 venues across Pakistan
- **Total Matches**: 34 (including playoffs)

## 🤝 Contributing

This is a learning project demonstrating:
- Data analysis with Pandas
- Web development with Flask
- Interactive visualizations with Plotly
- Responsive UI design
- REST API development

## 📝 License

This project is created for educational purposes and data analysis practice.

## 👨‍💻 Author

Created as a practical learning project for PSL data analysis.

## 🙏 Acknowledgments

- Dataset sourced from Wikipedia (PSL 2025)
- Built with open-source technologies
- Inspired by IPL data analysis practice

---

**Happy Analyzing! 🏏📊**

For issues or questions, feel free to explore and modify the code as needed!

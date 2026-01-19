# 🚀 Quick Start Guide - PSL 2025 Dashboard

Get your PSL Data Analysis Dashboard running in 3 simple steps!

## Step 1️⃣: Install Dependencies

Open Terminal in this folder and run:

```bash
pip install -r requirements.txt
```

Wait for all packages to install (Flask, Pandas, Plotly, NumPy).

## Step 2️⃣: Start the Server

Run the application:

```bash
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

## Step 3️⃣: Open in Browser

Open your web browser and go to:

```
http://localhost:5000
```

**That's it!** 🎉

Your PSL 2025 Data Analysis Dashboard is now running!

---

## 📱 What You'll See

The dashboard includes:

✅ **Overview Stats** - Total matches, teams, venues  
✅ **Team Performance** - Wins and percentages  
✅ **Interactive Charts** - 10+ different visualizations  
✅ **Toss Analysis** - Impact on match outcomes  
✅ **Recent Matches** - Latest results  
✅ **Head-to-Head** - Team rivalries  
✅ **Player Stats** - Top POTM winners  

---

## 🛠️ Troubleshooting

### Problem: "Module not found"
**Solution**: Make sure you installed requirements:
```bash
pip install -r requirements.txt
```

### Problem: "Port already in use"
**Solution**: Change port in `app.py`:
```python
app.run(debug=True, port=5001)  # Change to 5001 or any other port
```

### Problem: "Cannot find CSV file"
**Solution**: Make sure `psl_2025_matches.csv` is in the same folder as `app.py`

---

## 🎯 Key Features

### Interactive Visualizations
- Hover over charts to see detailed data
- Zoom, pan, and download charts
- Fully responsive on mobile devices

### Real-time Data
- All statistics calculated from the dataset
- No manual updates needed
- Charts update automatically

### Modern UI
- Beautiful gradient design
- Smooth animations
- Professional layout
- Mobile-friendly

---

## 📚 Learn More

For detailed documentation, see `README.md`

For customization options, check the code:
- `app.py` - Backend logic
- `templates/index.html` - Page structure
- `static/css/style.css` - Styling
- `static/js/main.js` - Frontend logic

---

## 💡 Pro Tips

1. **Best View**: Use Chrome or Firefox for best experience
2. **Mobile**: Works great on phones and tablets too
3. **Charts**: Click and drag to zoom in on any chart
4. **Data**: Modify the CSV to analyze different seasons

---

**Enjoy exploring PSL 2025 data! 🏏📊**

Need help? Check `README.md` for detailed information.

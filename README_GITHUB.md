# ⚽ La Liga Football Data Analysis & ML Project

A comprehensive data analysis and machine learning project for La Liga football data, featuring market value prediction models and interactive visualizations.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/your-username/footaball.git
cd footaball

# Create virtual environment
python -m venv myenv
myenv\Scripts\activate  # Windows
# source myenv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the analysis
python src/model.py
python src/model_evaluation.py
```

## 📊 Features

- **Data Analysis**: Comprehensive La Liga player statistics
- **Machine Learning**: Market value prediction models
- **Visualization**: Interactive charts and maps
- **Web Scraping**: Real-time market value collection
- **Geospatial Analysis**: Club locations and stadium data

## 🎯 Model Performance

- **R² Score**: Model accuracy in predicting market values
- **MAE**: Average prediction error in euros

## 📁 Project Structure

```
footaball/
├── data/              # Data files
├── src/               # Source code
│   ├── gathering.py   # Data collection
│   ├── cleaning.py    # Data preprocessing
│   ├── analyzing.py   # Statistical analysis
│   ├── visual.py      # Data visualization
│   └── model.py       # Machine learning model
├── requirements.txt   # Python dependencies
└── README.md         # Full documentation
```

## 🔧 Technologies Used

- **Python**: pandas, numpy, scikit-learn
- **Machine Learning**: RandomForest, GradientBoosting
- **Visualization**: matplotlib, seaborn, plotly
- **Web Scraping**: requests, BeautifulSoup
- **Geocoding**: OpenCage API

## 📈 Key Insights

- Market value distribution across Spanish regions
- Performance correlation with player age and value
- Club investment patterns and squad composition
- Nationality diversity in La Liga
- Machine learning model for market value prediction


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Data sources: Transfermarkt, OpenCage Geocoding
- Football statistics and analysis
- Machine learning community

---

⭐ **Star this repository if you find it useful!**
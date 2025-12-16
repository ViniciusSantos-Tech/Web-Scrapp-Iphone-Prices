<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00FF00,100:006400&height=200&section=header&text=Scrapping%20Iphone&fontSize=45&fontColor=ffffff&animation=fadeIn" />
</p>

# 📱 Price Monitoring – iPhone 16
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.12%2B-green)
![Plotly](https://img.shields.io/badge/Plotly-5.18%2B-3F4F75)
### A real-time price monitor for the iPhone 16 that automatically collects prices from major Brazilian online stores and presents a comparative analysis through an interactive web interface.

## ✨ Features
- 🔍 Automatic Web Scraping: Collects prices from 5 online stores simultaneously
- 📊 Interactive Visualization: Dynamic charts with Plotly for price comparison
- 🏪 Monitored Stores:
- Amazon
- Zoom
- Carrefour
- Buscapé
- Livelo

- 📈 Comparative Analysis: Automatically identifies the highest and lowest prices

- 🔄 Real-Time Updates: Continuous execution for ongoing monitoring- 📱 Web Interface: Interactive dashboard with Streamlit

## Home Screen
![Initial Interface Screenshot](Views/View1.png)

## Dashboard
![Initial Interface Screenshot](Views/View2.png)


## 🛠️ Technologies Used
- Python 3.8+
- Streamlit – Web interface and dashboard
- BeautifulSoup4 – Web scraping and HTML parsing
- Requests – HTTP requests to online stores
- Pandas – Data manipulation and structuring
- Plotly – Data visualization and interactive charts


## 📦 Installation
### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step by step
1️⃣ **Clone the repository**

````
git clone https://github.com/seu-usuario/monitor-precos-iphone.git
cd monitor-precos-iphone
````

2️⃣ **Create a virtual environment (optional, but recommended)**

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

3️⃣ **Install the dependencies**

````
pip install -r requirements.txt
````
4️⃣ **Run the application**
````
streamlit run app.py
````
## 🚀 How to Use
### Basic Execution
1- Run the main script:

````
python monitor_precos.py
````

2- Access the web dashboard:
- Open your browser
- Navigate to http://localhost:8501
- View automatically updated prices


## 📊🛠️ Dashboard Features
- Price Table: View raw prices collected from each store
- Bar Chart: Visually compare prices between stores
- Value Highlighting: Automatic identification of the highest and lowest prices
- Color Scale: Visual gradient to differentiate values


## Customization
### To monitor other products:
- Replace the URLs in the code
- Adjust price selectors if necessary
- Modify store names in the dashboard


## ❗ Limitations
- Stores may change their HTML structure, breaking the scraping
- Some stores may block automated requests
- Price formats may vary between stores


## 🤝 Contributing
### Contributions are welcome! 💖
```

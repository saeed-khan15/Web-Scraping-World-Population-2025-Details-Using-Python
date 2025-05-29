# Web Scraping World Population 2025 Details Using Python

## 📌 Overview
This project focuses on scraping population data for all countries from [Worldometers](https://www.worldometers.info/world-population/population-by-country/) using Python. The goal is to extract tabular data directly from the website and save it into an Excel file for further use or analysis.

This project is both a learning exercise in web scraping and a practical example of extracting real-world data from the web.

---

## 🧰 Tools and Libraries Used

- `requests`: To make HTTP requests and fetch web page content
- `BeautifulSoup`: To parse and extract the HTML table
- `pandas`: To convert the parsed data into a structured DataFrame and export it to Excel

---

## 📂 Project Structure

```bash
web-scraping-world-population/
│
├── data/
│   └── world_population_2025.xlsx       # Output Excel file
│
├── src/
│   └── scrape_world_population.py       # Web scraping script
│
├── README.md
├── requirements.txt
```

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/web-scraping-world-population.git
cd web-scraping-world-population
```

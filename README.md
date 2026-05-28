# Climate Data Analyzer 🌡️

A Python data preprocessing tool that ingests raw climate sensor data, cleans it, converts it into proper types, engineers new features, and outputs a formatted station report — built entirely using core Python variables and data types, no external libraries.

---

## What This Project Is

Raw weather sensor data does not arrive clean. It arrives as strings — even when the values are clearly numbers. This project solves that exact problem: taking messy, untyped sensor readings and transforming them into data that is actually usable for analysis and machine learning.

This is not a toy exercise. Type casting, data validation, and feature engineering from raw sensor input are real steps in production ML pipelines at organizations like NOAA and NASA. This project does all three from scratch, manually, so the fundamentals are understood before any library handles them automatically.

---

## The Real-World Problem

Climate monitoring stations around the world collect temperature, humidity, precipitation, and wind data continuously. Before any model can run on that data, an engineer has to:

1. Validate that the reading is trustworthy
2. Cast each value to its correct data type
3. Derive new variables (unit conversions, composite features)
4. Classify and label readings for downstream use

This script does all four steps on a single station reading and outputs a formatted daily report.

---

## Project Structure

```
climate-data-analyzer/
│
├── climate_analyzer.py     # Main script — all five phases
└── README.md               # This file
```

---

## The Five Phases

### Phase 1 — Raw Data Ingestion
Simulates incoming sensor data where every value arrives as a string, exactly as a CSV or REST API would return it.

```python
raw_temp_celsius     = "34"     # string, not a number yet
raw_humidity_percent = "78"
data_quality_flag    = "1"
```

**Concepts covered:** string variables, the `type()` function, why untyped data is dangerous

---

### Phase 2 — Type Casting
Converts every raw string into its correct Python type using `int()`, `float()`, and `bool()`.

```python
temp_celsius     = int(raw_temp_celsius)       # "34" → 34
is_quality_data  = bool(int(data_quality_flag)) # "1" → 1 → True
```

**Concepts covered:** `int()`, `float()`, `bool()`, `str()`, type validation

---

### Phase 3 — Feature Engineering
Creates new variables from existing ones through unit conversion and composite calculations.

```python
temp_fahrenheit   = float((temp_celsius * 9/5) + 32)
temp_kelvin       = float(temp_celsius + 273.15)
heat_index_approx = float(temp_fahrenheit + (humidity_percent * 0.05))
precip_inches     = float(precip_mm / 25.4)
wind_mph          = float(wind_kph / 1.609)
```

**Concepts covered:** float arithmetic, `round()`, operator precedence, feature engineering

---

### Phase 4 — Classification and Labeling
Builds a danger score and categorical labels using conditional logic — the manual equivalent of a classification model.

```python
danger_score = 0
if temp_celsius > 32:
    danger_score = danger_score + 1
if humidity_percent > 70:
    danger_score = danger_score + 1
if precip_mm > 10:
    danger_score = danger_score + 1

temp_label = "EXTREME HEAT" if temp_celsius > 35 else "HIGH" if temp_celsius > 30 else "MODERATE"
```

**Concepts covered:** conditional statements, ternary expressions, accumulator pattern, string concatenation

---

### Phase 5 — Report Output
Formats all processed variables into a structured, readable station report.

```
==========================================
CLIMATE STATION DAILY REPORT
==========================================
Station ID   : WX-4471
Location     : Atlanta, Georgia
Date         : 2024-07-15
Data Valid   : True
------------------------------------------
TEMPERATURE  : 34 C / 93.2 F / 307.15 K
HUMIDITY     : 78 %  -> HUMID
WIND SPEED   : 21 kph / 13.1 mph
PRECIP       : 12 mm / 0.47 in -> MODERATE RAIN
------------------------------------------
HEAT INDEX   : 97.1 F (approx)
DANGER SCORE : 3/3
ALERT LEVEL  : HIGH
==========================================
```

**Concepts covered:** string multiplication, `print()` formatting, readable output structure

---

## Python Concepts Covered

| Concept | Where It Appears |
|---|---|
| String variables | Phase 1 — raw sensor inputs |
| Integer casting | Phase 2 — `int()` on all readings |
| Float variables | Phase 3 — conversions and calculations |
| Boolean variables | Phase 2 — data quality flag |
| `type()` function | Phases 1 and 2 |
| `int()`, `float()`, `bool()`, `str()` | Phase 2 |
| Arithmetic operators | Phase 3 |
| `round()` | Phase 3 |
| Comparison operators | Phase 4 |
| `if / else` conditionals | Phase 4 |
| Ternary expressions | Phase 4 |
| String concatenation | Phase 4 — danger score label |
| String multiplication | Phase 5 — divider lines |
| `print()` with multiple arguments | Throughout |
| Comments (`#`) | Throughout |

---

## How to Run It

**Requirements:** Python 3.8 or higher. No external libraries needed.

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/climate-data-analyzer.git

# Navigate into the folder
cd climate-data-analyzer

# Run the script
python climate_analyzer.py
```

---

## How to Customize It

Open `climate_analyzer.py` and change the raw input values at the top of Phase 1:

```python
raw_temp_celsius      = "34"   # change this
raw_humidity_percent  = "78"   # change this
raw_precip_mm         = "12"   # change this
raw_wind_kph          = "21"   # change this
data_quality_flag     = "1"    # 1 = valid reading, 0 = corrupted
```

Re-run the script. Every label, score, and conversion updates automatically.

---

## Real Data Sources

This project uses simulated data. The same preprocessing logic applies directly to real datasets:

- **NOAA GSOD** (Global Surface Summary of Day) — free daily weather observations from thousands of stations worldwide at [ncei.noaa.gov](https://www.ncei.noaa.gov)
- **NASA GISS Surface Temperature Analysis (GISTEMP)** — global surface temperature data at [data.giss.nasa.gov](https://data.giss.nasa.gov/gistemp/)
- **OpenWeatherMap API** — live weather data via REST API at [openweathermap.org](https://openweathermap.org/api)

---

## Stretch Goals (Planned)

- [ ] Store a week of readings in a list and calculate rolling averages
- [ ] Move station data into a dictionary to mirror a JSON API response
- [ ] Use a loop to process a 30-day dataset automatically
- [ ] Read real data from a NOAA GSOD CSV file
- [ ] Replace manual casting with a Pandas DataFrame

---

## Key Insight

Wrong data types do not always crash a program. Sometimes Python silently produces a wrong result and keeps running. In a pipeline processing thousands of rows, a single uncaught type error can corrupt an entire dataset before any model ever sees it.

This is why understanding type casting manually — before relying on Pandas or any other library to handle it automatically — is a foundational ML engineering skill, not a beginner exercise.

---

## Part of a Larger Learning Series

This is **Project 1** in a series of Python projects built toward ML Engineering:

| Project | Focus | Status |
|---|---|---|
| Climate Data Analyzer | Variables & Data Types | ✅ Complete |
| Blockchain Simulator | Loops & Conditionals | 🔨 In Progress |
| More coming... | Functions, File I/O, Pandas | 🔜 Planned |

---

## Author

Built while learning Python for ML Engineering. Follow along on [Medium](#Masonjtr) and [LinkedIn](#https://www.linkedin.com/in/mason-jeter-026284386/) for write-ups on each project.

---

## License

MIT License — free to use, modify, and build on.

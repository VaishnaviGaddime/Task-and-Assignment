# Blinkit Dashboard - Streamlit Application

A comprehensive dashboard built with Streamlit that visualizes sales data for BlinkIt India last Minute app, similar to the Power BI dashboard.

## Features

- **KPI Cards**: Total Sales, Number of Items, Average Sales, Average Rating
- **Interactive Charts**:
  - Outlet Establishment (Line Chart) - Sales trends over years
  - FAT CONTENT (Donut Chart) - Distribution of Low Fat vs Regular items
  - FAT by OUTLETS (Stacked Bar Chart) - Fat content breakdown by outlet tiers
  - ITEM TYPE (Horizontal Bar Chart) - Sales by item category
  - OUTLET SIZE (Donut Chart) - Sales distribution by outlet size
  - OUTLET LOCATION (Horizontal Bar Chart) - Sales by location tiers
- **Data Table**: Detailed metrics by Outlet Type
- **Interactive Filters**: Filter by Outlet Location Type, Outlet Size, and Item Type

## Setup Instructions

1. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```

2. **Install dependencies** (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   
   Option 1 - Using the run script:
   ```bash
   ./run.sh
   ```
   
   Option 2 - Manual command:
   ```bash
   streamlit run app.py
   ```

4. **Access the dashboard**:
   The app will automatically open in your browser at `http://localhost:8501`

## Project Structure

```
Vaishu/
├── venv/                 # Virtual environment
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── run.sh                # Convenience script to run the app
├── data.csv              # Dataset (auto-generated if not present)
└── README.md            # This file
```

## Notes

- If `data.csv` doesn't exist, the app will automatically generate sample data matching the dashboard metrics
- All filters in the sidebar are interactive and update all visualizations in real-time
- The dashboard is responsive and works on different screen sizes


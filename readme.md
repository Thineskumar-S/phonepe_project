# PhonePe Pulse Replica: Data Visualization 📊

PhonePe Pulse Replica project, an immersive data visualization experience that replicates the dynamic nature of the official PhonePe Pulse web application. 📈

## Project Description 🚀

In this project, I have recreated the PhonePe Pulse web app using Streamlit, offering users an interactive interface to explore data dynamically. The app closely mirrors the style and user experience of the official PhonePe Pulse. You won't be able to distinguish between the two!

## Data Collection 📂

The data for this project has been sourced from the official PhonePe GitHub repository and meticulously organized in deeply nested folders. The structure of the data repository looks like this:

```
project-root/
│
└── PhonePe-Pulse-Replica/
├── data/
│   ├── aggregated/
│   │   ├── transaction/
│   │   │   ├── country/
│   │   │   │   ├── india/
│   │   │   │   │   ├── 2018/
│   │   │   │   │   │   ├── 1.json
    │   │               |── 2.json
    ├── map 
    │   ├── transcation
    │
    └── ...
```

## ETL Process 🔄

The ETL (Extract, Transform, Load) process in this project is as follows:

- **Extraction (E):** Data is extracted from the nested folders by automating the process of locating and retrieving JSON files.

- **Transformation (T):** Data transformation occurs during the extraction process itself. The data is cleaned and organized to prepare it for analysis and visualization.

- **Loading (L):** The transformed data is loaded into an AWS RDS MySQL database.

## Dynamic Dashboard 📈

The heart of this project is the dynamic dashboard that consists of three key elements:

1. **User Options 🧐:** According to the user preferences, Users can choose years, quarters, and major categories as transactions and users.

2. **Dynamic Choropleth Chart 🗺️:** The chart dynamically updates values based on user selections, for better and clear visualtion I added this chart in maps tab.

3. **In-Depth Analysis 📊:** This section offers a detailed analysis of the data, providing insights similar to the official PhonePe Pulse web app. The values change dynamically as per user selections.

## Enhanced Visualization 📊

To make data visualization even more compelling, I've included additional visualizations to help uncover interesting insights for informed decision-making. 📌

## Challenges Faced 🤔

Throughout the project, several challenges were encountered:

1. Extracting the right data from the nested folders while deciding what to extract and what to discard was a significant challenge.

2. Data integrity issues led to missing and inconsistent values. This had addressed to ensure for accurate analysis.

3. Adjusting data types to handle numerical values, including upgrading to big int and increasing precision levels for float, was necessary to prevent data overflow.

4. Data extraction was optimized to facilitate time series analysis.

## Explore and Enjoy! 🚀

Feel free to explore the dynamic visualizations and enjoy the PhonePe Pulse experience. If you encounter any issues or have suggestions for further enhancements, please let me know. 📞

**Happy Data Exploration!** 🎉📈🌟
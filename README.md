# Netflix Data Analysis Dashboard

This project analyzes a dataset of Netflix content to provide insights about the distribution and characteristics of movies and TV shows on the platform. It includes visualizations for content types, ratings, movie durations, and most frequent countries of production.

---

## Overview

The analysis uses the `NetflixData.csv` dataset, containing information about movies and TV shows available on Netflix. Key goals are:

- Compare the number of Movies vs TV Shows.
- Visualize the distribution of content ratings.
- Analyze the duration of movies.
- Identify the top 10 countries by number of shows.

---

## Features & Visualizations

### 1. Movies vs TV Shows
- Bar chart showing the count of Movies and TV Shows.
- This helps to understand the content makeup of Netflix.

### 2. Content Ratings Distribution
- Pie chart representing the percentage share of different content ratings (e.g., PG, R, TV-MA).
- Useful for seeing how content is rated on Netflix.

### 3. Movie Duration Histogram
- Histogram showing the distribution of movie durations in minutes.
- Helps identify typical movie lengths available on Netflix.

### 4. Top 10 Countries by Number of Shows
- Horizontal bar chart showing the top 10 countries based on the number of movies/TV shows produced.
- Insight into which countries are the largest content contributors.

---

## User Interface (UI) Concept

The UI can be conceptualized as a simple web or desktop dashboard with the following layout:

- **Header:** "Netflix Content Analysis Dashboard"
- **Sidebar/Menu:** Navigation to select visualization type (Movies vs TV Shows, Ratings, Duration, Countries)
- **Main Panel:**
  - Displays the selected chart (image or interactive plot)
  - Description or brief explanation below each chart
- **Footer:** Dataset source acknowledgment and last updated date

---

## Getting Started

1. Ensure `NetflixData.csv` is in your project folder.
2. Run the provided Python script (requires `pandas` and `matplotlib`).
3. View generated plots directly or use the saved PNG files in your UI.

---

## Requirements

- Python 3.x
- pandas
- matplotlib

---

## Notes

- Data cleaning drops rows with missing critical fields.
- Movie durations are parsed from strings to integers for accurate plotting.
- The analysis focuses on the current snapshot of the dataset.

---

## Example UI Flow (Hypothetical)


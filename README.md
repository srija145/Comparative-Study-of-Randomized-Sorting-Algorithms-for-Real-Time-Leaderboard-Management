# Randomized Sorting Algorithms for Real-Time Leaderboard Management

## Project Overview

This project explores the efficiency and scalability of randomized sorting algorithms when applied to real-time leaderboard scenarios. We simulate scores for 10,000 players across 100 rounds and compare various sorting methods to determine the most effective one for updating rankings in real-time applications.


## Project Objectives

1. **Generate Synthetic Data**
   - Create a dataset of 10,000 players with scores from 100 rounds.
   - Save the dataset as `player_scores.csv`.

2. **Database Setup**
   - Use SQLite to store top 5 players for each round and based on total scores.

3. **Sorting Algorithms Implemented**
   - Randomized Radix Sort  
   - Sample Sort  
   - Randomized Heap Sort  
   - Randomized Shell Sort

4. **Performance Evaluation**
   - Measure execution time and peak memory usage.
   - Analyze which algorithm performs best in different scenarios.

5. **Visualization**
   - Plot comparative results of sorting algorithms using execution metrics.

6. **Web Application**
   - A Streamlit-based interface that:
     - Shows the top 5 players based on total scores.
     - Allows users to select a round and view top players for that round.

## Technologies Used

- **Languages & Libraries**: Python, NumPy, pandas, time, memory_profiler, matplotlib
- **Database**: SQLite
- **Visualization**: matplotlib
- **Web App**: Streamlit

## Key Results

- All algorithms were benchmarked across identical datasets.
- Visualizations clearly demonstrate the trade-offs between speed and memory usage.
- Randomized Radix and Sample Sort showed the best performance for large datasets.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/leaderboard-sorting.git
   
2. Open the Jupyter notebook Project.ipynb and run all cells to:

   * Generate data

   * Sort scores

   * Store results in database

   * Visualize performance

3. To launch the Streamlit web app:
   ```bash
   streamlit run leaderboard_app.py


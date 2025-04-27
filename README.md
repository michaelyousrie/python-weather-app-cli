# Weather Fetcher & File Sorter

A Python application that fetches the current weather data for a specified city from the OpenWeatherMap API, processes it, and saves the results in a JSON file, grouped by city. If the file already exists, the new data is appended to the existing data.

## Features

- Fetches current weather data for a specified city.
- Saves the weather data in a JSON file, grouped by city.
- Automatically creates the directory and file if they don't exist.
- Handles corrupted or empty files by starting fresh when necessary.
- Ensures non-ASCII characters like the degree symbol (°) are correctly saved.

## Requirements

- Python 3.x
- `requests` library for making API requests.

### Install Dependencies

Before running the application, make sure you have Python installed on your system. Then, install the required dependencies:

```bash
pip install requests
```
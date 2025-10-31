# Football Match Data Fetcher

Gets finished match data for Real Madrid from the 2023 La Liga season using the API-Sports football API.

## Requirements

- Python 3.x
- `requests`
- `pandas`
- `python-dotenv`

Install with:
```bash
pip install requests pandas python-dotenv
```

## Setup

Create a `.env` file in the project directory:
```
API_URL=v3.football.api-sports.io
API_KEY=your_api_key_here
```

Get your API key from [API-Sports](https://www.api-football.com/).

## What It Does

Fetches the first finished Real Madrid match from the 2023 La Liga season and prints it as formatted JSON.

## Usage
```bash
python script_name.py
```

## Configuration

Change these variables to fetch different data:
- `league_id`: 140 for La Liga (check API docs for others)
- `team_id`: 541 for Real Madrid (check API docs for others)
- `season`: Year of the season
- `status`: "FT" for finished matches

## Output

Prints detailed match information including:
- Fixture details
- Teams and scores
- Match statistics
- Venue information
- Referee details

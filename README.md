# Number Classification API

A FastAPI-based REST API that analyzes numbers and returns their mathematical properties along with interesting facts.

## Features

- Classifies numbers based on various mathematical properties
- Returns fun facts about numbers using the Numbers API
- Supports CORS for web browser access
- Input validation and error handling
- Returns responses in JSON format

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Requests

## Installation

1. Clone the repository:
```bash
git clone https://github.com/olugbedu/numbersapi-fastapi.git
cd numbersapi-fastapi
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the API

Start the server:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Documentation

### Endpoint

`GET /api/classify-number`

### Parameters

- `number` (required): Integer to analyze

### Response Format

Success (200 OK):
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3³ + 7³ + 1³ = 371"
}
```

Error (400 Bad Request):
```json
{
    "number": "invalid_input",
    "error": true
}
```

### Properties Checked

- Prime numbers
- Perfect numbers
- Armstrong numbers
- Odd/Even numbers

## Example Usage

```bash
curl http://localhost:8000/api/classify-number?number=6
```

Response:
```json
{
    "number": 6,
    "is_prime": false,
    "is_perfect": true,
    "properties": ["perfect", "even"],
    "digit_sum": 6,
    "fun_fact": "6 is the smallest perfect number"
}
```

## Error Handling

The API handles various error cases:
- Invalid input types
- Missing parameters
- Network errors when fetching fun facts

## Development

### Project Structure
```
number-classification-api/
├── main.py
├── requirements.txt
└── README.md
```

### Adding New Properties

To add a new mathematical property:
1. Create a function to check the property
2. Add the property check in the `classify_number` endpoint
3. Update the properties list in the response

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Acknowledgments

- [Numbers API](http://numbersapi.com) for providing number facts
- FastAPI framework
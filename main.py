from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perfect(n: int) -> bool:
    if n <= 1:
        return False
    sum_divisors = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
        i += 1
    return sum_divisors == n

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(abs(n))]
    num_digits = len(digits)
    return sum(d ** num_digits for d in digits) == abs(n)

def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(abs(n)))  

def get_fun_fact(n: int) -> str:
    url = f"http://numbersapi.com/{n}/math"
    response = requests.get(url)
    return response.text if response.status_code == 200 else "No fun fact available."

@app.get("/api/classify-number")
async def classify_number(number: str = Query(..., description="The number to classify")):
    try:
        number_float = float(number)
        number_int = int(number_float) if number_float.is_integer() else number_float
    except ValueError:
        raise HTTPException(status_code=400, detail={"number": number, "error": True})

    properties = []
    if isinstance(number_int, int): 
        if is_prime(number_int):
            properties.append("prime")
        if is_perfect(number_int):
            properties.append("perfect")
    if is_armstrong(number_int if isinstance(number_int, int) else int(number_float)):
        properties.append("armstrong")
    if isinstance(number_int, int) and number_int % 2 == 1:
        properties.append("odd")
    elif isinstance(number_int, int):
        properties.append("even")

    fun_fact = get_fun_fact(number_int if isinstance(number_int, int) else int(number_float))

    return {
        "number": number_int if isinstance(number_int, int) else number_float,
        "is_prime": is_prime(number_int) if isinstance(number_int, int) else False,
        "is_perfect": is_perfect(number_int) if isinstance(number_int, int) else False,
        "properties": properties,
        "digit_sum": digit_sum(number_int if isinstance(number_int, int) else int(number_float)),
        "fun_fact": fun_fact
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
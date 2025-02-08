from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
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
    digits = [int(d) for d in str(n)]
    num_digits = len(digits)
    return sum(d ** num_digits for d in digits) == n

def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(n))

def get_fun_fact(n: int) -> str:
    url = f"http://numbersapi.com/{n}/math"
    response = requests.get(url)
    return response.text if response.status_code == 200 else "No fun fact available."

@app.get("/api/classify-number")
async def classify_number(number: int = Query(..., description="The number to classify")):
    try:
        if not isinstance(number, int):
            raise HTTPException(status_code=400, detail={"number": str(number), "error": True})

        properties = []
        if is_prime(number):
            properties.append("prime")
        if is_perfect(number):
            properties.append("perfect")
        if is_armstrong(number):
            properties.append("armstrong")
        if number % 2 == 1:
            properties.append("odd")
        else:
            properties.append("even")

        fun_fact = get_fun_fact(number)

        return {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": digit_sum(number),
            "fun_fact": fun_fact
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail={"number": str(number), "error": True})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
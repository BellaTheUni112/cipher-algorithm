import requests

MASK = 0xFFFFFFFF

def mix_bits(s: int) -> int:
    s &= MASK
    s ^= (s << 13) & MASK
    s ^= (s >> 7)
    s ^= (s << 17) & MASK
    return s & MASK

def get_randomorg_numbers(count: int, minimum: int, maximum: int):
    url = (
        f"https://www.random.org/integers/"
        f"?num={count}&min={minimum}&max={maximum}"
        f"&col=1&base=10&format=plain&rnd=new"
    )
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    
    numbers = [int(line) for line in response.text.split() if line.strip().isdigit()]
    if len(numbers) != count:
        raise ValueError("Did not receive the expected number of random numbers.")
    return numbers

try:
    random_nums = get_randomorg_numbers(5, 1, 100000)

    mixed_padded = [f"{mix_bits(n) % 100_000_000:08d}" for n in random_nums]

    combined_number = "".join(mixed_padded)

    print("Random numbers:", random_nums)
    print("Mixed 40-digit number:", combined_number)

except requests.RequestException as e:
    print("Error fetching from random.org:", e)

except Exception as e:
    print("Unexpected error:", e)

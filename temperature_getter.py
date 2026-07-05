import os
import time
import json
from datetime import datetime, timedelta

OUTPUT_FILE = "tmp.json"
DURATION_SECONDS = 60 * 60  # 1 час
INTERVAL = 30  # каждые 30 секунд


def get_temp():
    # alias: tmp = vcgencmd measure_temp
    output = os.popen("tmp").read().strip()

    # expected: temp=48.2'C
    try:
        return float(output.split("=")[1].replace("'C", ""))
    except Exception:
        return None


def main():
    data = []
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=DURATION_SECONDS)

    print(f"Start: {start_time.isoformat()}")
    print(f"End:   {end_time.isoformat()}")

    while datetime.now() < end_time:
        temp = get_temp()
        now = datetime.now().isoformat()

        data.append({
            "time": now,
            "temperature": temp
        })

        print(f"{now} -> {temp}°C")

        time.sleep(INTERVAL)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print(f"\nSaved {len(data)} records to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
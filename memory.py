from datetime import datetime

LOG_FILE = "events.log"

def save_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp} - {event}\n")

    print(f"Saved: {event}")


def show_memory():
    try:
        with open(LOG_FILE, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No memories found.")
  
def last_memories(count=5):
    try:
        with open(LOG_FILE, "r") as file:
            lines = file.readlines()

        for line in lines[-count:]:
            print(line.strip())

    except FileNotFoundError:
        print("No memories found.")   
def find_memory(keyword):
    try:
        with open(LOG_FILE, "r") as file:
            lines = file.readlines()

        found = False

        for line in lines:
            if keyword.lower() in line.lower():
                print(line.strip())
                found = True

        if not found:
            print(f"No memories found for: {keyword}")

    except FileNotFoundError:
        print("No memories found.")

def last_memory_of(keyword):
    try:
        with open(LOG_FILE, "r") as file:
            lines = file.readlines()

        matches = []

        for line in lines:
            if keyword.lower() in line.lower():
                matches.append(line.strip())

        if matches:
            print(matches[-1])
        else:
            print(f"No memories found for: {keyword}")

    except FileNotFoundError:
        print("No memories found.")
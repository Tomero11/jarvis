from datetime import datetime

LOG_FILE = "events.log"


def save_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"{timestamp} - {event}\n")

    print(f"Saved: {event}")


def show_memory():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            print(file.read())

    except FileNotFoundError:
        print("No memories found.")


def last_memories(count=5):
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines[-count:]:
            print(line.strip())

    except FileNotFoundError:
        print("No memories found.")


def find_memory(keyword):
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
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

        return "No memories found."



def get_last_memories(count=5):
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()

        return "\n".join(line.strip() for line in lines[-count:])

    except FileNotFoundError:

        return "No memories found."
def search_memory(keyword):
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()

        matches = []

        for line in lines:
            if keyword.lower() in line.lower():
                matches.append(line.strip())

        return matches

    except FileNotFoundError:
        return []        
def what_i_said_today():

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()

        results = []

        for line in lines:
            if "Tomer said:" in line:
                results.append(line.strip())

        return results

    except FileNotFoundError:
        return []        

def last_user_message():

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()

        user_lines = []

        for line in lines:
            if "Tomer said:" in line:
                user_lines.append(line.strip())

        if len(user_lines) >= 2:
            return user_lines[-2]

        return "No previous messages found."

    except FileNotFoundError:

        return "No memories found."
def last_memory_of(keyword):
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()

        matches = []

        for line in lines:
            if keyword.lower() in line.lower():
                matches.append(line.strip())

        if matches:
            return matches[-1]

        return f"No memories found for: {keyword}"

    except FileNotFoundError:
        return "No memories found."
def get_name():

    result = last_memory_of("NAME:")

    if "No memories found" in result:
        return None

    return result.split("NAME:")[-1].strip()

def get_city():

    result = last_memory_of("CITY:")

    if "No memories found" in result:
        return None

    return result.split("CITY:")[-1].strip()
def get_cats():

    result = last_memory_of("CATS:")

    if "No memories found" in result:
        return None

    return result.split("CATS:")[-1].strip()
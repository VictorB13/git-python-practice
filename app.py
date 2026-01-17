import datetime

def greet(name):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"Hello my friends, {name}! The current time is {current_time}"

if __name__ == "__main__":
    user = "World"
    print(greet(user))

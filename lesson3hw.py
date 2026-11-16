print("=== My Daily Mood Advisor ===")
import datetime
now = datetime.datetime.now()
print("Hello!")
name = input("What is your Name?")
mood = input("How Are you feeling today?")
print("Time Now:",now)
if "good" in mood.lower() or "great" in mood.lower() or "very nice"in mood.lower() or "nice"in mood.lower():
  print("Hello ",name," ,I am glad to hear that.")
else:
  print("Hello ",name," ,I hope your day gets better.")
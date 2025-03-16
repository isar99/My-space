from datetime import datetime
current = datetime.now()
d = current.strftime("%I:%M:%S %p")
print(d)
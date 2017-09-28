import sys, time
mystr = "{} rows complete\r"
for i in range(0, 100):
    if i % 10 == 0:
        sys.stdout.write(mystr.format(i))
        sys.stdout.flush()
        time.sleep(1)
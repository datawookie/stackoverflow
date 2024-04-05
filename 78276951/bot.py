from datetime import datetime
import time

print("Running bot...")

with open("output.csv", "wt") as fid:
    for i in range(10):
        output = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        # Write to file.
        print(f"- Writing '{output}'.")
        fid.write(output + "\n")
        # Flush buffer so that write happens immediately.
        fid.flush()
        time.sleep(5)

print("Done!")

import matplotlib.pyplot as plt
import time as tme
import serial


com = "COM7"
ser = serial.Serial(com, 9600)
fig = plt.figure(figsize=(20, 10))
ax1 = plt.subplot(2, 1, 1)
file_name = input()
t = []
v = []
ct = 0
line, = ax1.plot(t, v)
start_time = tme.time()
Trise = []
Period = []
datastr = []
signal_prev = 0
trise_prev = 0
tfall_prev = 0
Velocity = []


def update(frame):
    st1 = tme.time()
    global ct, signal_prev, trise_prev, tfall_prev
    try:
        ct = tme.time() - start_time
        if not ser == None:
            bytesToRead = ser.inWaiting()
            line_str = ser.read(bytesToRead).decode().strip()
            if not line_str == None:
                a = line_str.split("\r\n")
                signal = float(a[0])
                print(a)
                with open(file_name, "a") as fh:
                        fh.write(" ".join(a) + "\t")
                t.append(ct)
                v.append(signal)
            ax1.set_xlim(min(t) - 1, max(t) + 1)
            ax1.set_ylim(min(v) - 1, max(v) + 1)
            line.set_data(t, v)
    except Exception as e:
        print(f"error {e}")
    return line,



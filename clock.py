import os
import time
import math
import datetime

def draw_clock():
    # ঘড়ির সংখ্যার পজিশন ম্যাপ (সঠিক জায়গায় সংখ্যা বসানোর জন্য)
    # (x, y) coordinates for numbers 1 to 12
    num_map = {
        (4, -7): "1 ", (7, -4): "2 ", (8, 0): "3 ", (7, 4): "4 ",
        (4, 7): "5 ", (0, 8): "6 ", (-4, 7): "7 ", (-7, 4): "8 ",
        (-8, 0): "9 ", (-7, -4): "10", (-4, -7): "11", (0, -8): "12"
    }

    while True:
        os.system('clear')
        print("\033[1;36m" + "━"*42)
        print("    Admin: MRK | Team: MRK Tools")
        print("━"*42 + "\033[0m")
        
        now = datetime.datetime.now()
        hr, mn, sc = now.hour % 12, now.minute, now.second
        radius = 8
        
        for y in range(-9, 10):
            line = "        " 
            x = -16
            while x <= 16:
                # সংখ্যার পজিশন চেক
                pos = (round(x/2), y)
                
                # কাঁটার এঙ্গেল
                as_ = math.radians(sc * 6 - 90)
                am_ = math.radians(mn * 6 - 90)
                ah_ = math.radians((hr * 30 + mn / 2) - 90)
                
                # কাঁটা চেকিং
                is_sec = abs(x/2 - math.cos(as_)*7) < 0.5 and abs(y - math.sin(as_)*7) < 0.5
                is_min = abs(x/2 - math.cos(am_)*6) < 0.6 and abs(y - math.sin(am_)*6) < 0.6
                is_hr = abs(x/2 - math.cos(ah_)*4) < 0.8 and abs(y - math.sin(ah_)*4) < 0.8

                if pos in num_map:
                    line += f"\033[1;32m{num_map[pos]}\033[0m"
                    x += 2 # সংখ্যা ২ অক্ষরের হলে স্পেস অ্যাডজাস্ট
                elif is_sec:
                    line += "\033[1;31m•\033[0m "
                elif is_min:
                    line += "\033[1;37m█\033[0m "
                elif is_hr:
                    line += "\033[1;33m▓\033[0m "
                else:
                    line += "  "
                x += 1
            print(line)
        
        print(f"\n\033[1;32m       Real Time: {now.strftime('%I:%M:%S %p')}\033[0m")
        print("\033[1;34m       [ Press Ctrl+C to Stop ]\033[0m")
        time.sleep(1)

try:
    draw_clock()
except KeyboardInterrupt:
    print("\n\033[1;31mClock Stopped.\033[0m")

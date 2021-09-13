# Q5.
# 1, 2, 3, 4 ~~~~ 99 까지 출력하는 코드를 작성하세요.
# 단, 2까지 출력 후, 3부터는 1초씩 쉬었다가 출력해야함.

import time
sleep = 0

for i in range(1,100):
    print(i)
    time.sleep(sleep)
    sleep += 1
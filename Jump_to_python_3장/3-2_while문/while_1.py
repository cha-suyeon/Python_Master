# while문의 기본 구조

import time
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    time.sleep(1)
    if treeHit == 10:
        print("나무 넘어갑니다.")
        

# while의 조건문은 treeHit < 10입니다.
# treeHit가 10보다 작을 동안은 while문은 print 안의 문장을 계속 출력합니다!
# treeHit가 10이 되면 "나무 넘어갑니다" 문장이 출력되며 종료됩니다. GOOD!
n = int(input())
bag = 0

# 크기가 3인 봉지에 하나씩 담아가면서 뺀 뒤 남은 설탕이 5의배수가 되면 5로 나눈 값을 합쳐서 출력함
while n >= 0:
    # 남은 설탕이 5의 배수이면 모조리 담아버리고 출력
    # break로 종료했기때문에 while-else에서 else는 출력하지 않음
    if n % 5 == 0:
        bag += n // 5
        print(bag)
        break
    # 3짜리 봉지에 옮겨담음(봉지1개추가, 설탕3kg뺴기)
    bag += 1
    n -= 3
# 3과5의 봉지로 정확하게 N킬로그램을 만들 수 없을 떄
else:
    print(1)

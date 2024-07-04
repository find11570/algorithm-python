N = 78

use20 = N//20
N %= 20
use10 = N//10
N %= 10
use5 = N//5
N %= 5
use1 = N//1
N %= 1

print(f"20을 사용한 횟수: {use20}")
print(f"10을 사용한 횟수: {use10}")
print(f"5을 사용한 횟수: {use5}")
print(f"1을 사용한 횟수: {use1}")
print(f"사용한 동전의 총 개수: {use1 + use5 + use10 + use20}")
'''
길이가 N인 수열 A1, A2, ..., AN이 주어진다. 이때, 다음 쿼리를 수행하는 프로그램을 작성하시오.

i j: Ai, Ai+1, ..., Aj에 가장 많이 등장하는 수가 몇 번 등장했는지 출력한다.

'''

'''
첫째 줄에 수열의 크기 N (1 ≤ N ≤ 100,000)이 주어진다.

둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100,000)

셋째 줄에는 쿼리의 개수 M (1 ≤ M ≤ 100,000)이 주어진다.

넷째 줄부터 M개의 줄에는 쿼리 i, j가 한 줄에 하나씩 주어진다. (1 ≤ i ≤ j ≤ n)

'''
N = int(input())
x = list(range(0,N))
x = list(map(int,input().split()))
M = int(input())
for i in range(0,M):
    i, j = map(int,input().split())
    temp_list = x[i-1:j]
    # print(list(x))
    print(temp_list)
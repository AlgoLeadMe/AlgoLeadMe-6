## ✏️ 기록   

| 차시 |    날짜    | 문제유형 | 링크 | 풀이 |
|:----:|:---------:|:----:|:-----:|:----:|
| 1차시 | 2024.01.15 |  해시  | <a href="https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3">전화번호 목록</a> | https://github.com/AlgoLeadMe/AlgoLeadMe-6/pull/1 |
| 2차시 | 2024.01.18 |  해시  | <a href="https://school.programmers.co.kr/learn/courses/30/lessons/42578">의상</a> | https://github.com/AlgoLeadMe/AlgoLeadMe-6/pull/5 |
| 3차시 | 2024.01.21 |  구현  | <a href="https://school.programmers.co.kr/learn/courses/30/lessons/258712">가장 많이 받은 선물</a> | https://github.com/AlgoLeadMe/AlgoLeadMe-6/pull/8 |
| 4차시 | 2024.01.24 |  BFS  | <a href="https://school.programmers.co.kr/learn/courses/30/lessons/250136">석유 시추</a> | https://github.com/AlgoLeadMe/AlgoLeadMe-6/pull/10 |
| 5차시 | 2024.01.27 |  이분탐색  | <a href="https://school.programmers.co.kr/learn/courses/30/lessons/43238">입국심사</a> | https://github.com/AlgoLeadMe/AlgoLeadMe-6/pull/14 |
| 6차시 | 2024.01.30 |  그리디  | <a href="https://school.programmers.co.kr/learn/courses/30/lessons/150369">택배 배달과 수거하기</a> | https://github.com/AlgoLeadMe/AlgoLeadMe-6/pull/17 |
| 7차시 | 2024.02.08 |  스택  | <a href="https://school.programmers.co.kr/learn/courses/30/lessons/12909">올바른 괄호</a> | https://github.com/AlgoLeadMe/AlgoLeadMe-6/pull/22 |
| 8차시 | 2024.02.14 |  DP  | <a href="https://www.acmicpc.net/problem/12865">평범한 배낭</a> | https://github.com/AlgoLeadMe/AlgoLeadMe-6/pull/24 |


<!-- PR은 최대한 다른 사람이 알아보기 쉽도록 자세히 써주세요. 특히 수도 코드 부분은 더더욱요...!!-->

## 🔗 문제 링크
<!-- 해결한 문제의 링크를 올려주세요. -->
[평범한 배낭](https://www.acmicpc.net/problem/12865)

## ✔️ 소요된 시간
<!-- 문제를 해결하는데 소요된 시간을 적어주세요. -->
2시간

## ✨ 수도 코드
<!-- 내가 작성한 코드를 모르는 사람이 봐도 이해할 수 있도록 글로 쉽게 풀어서 설명해주세요. -->
<!-- 알고리즘에 대한 지식이 전혀 없는 사람이 봐도 이해할 수 있도록 작성해주세요. 시각자료를 이용하면 더 좋습니다. -->

N - 4 / K - 7
|weight| value |
|:----:|:----:|
| 6 | 13 |
| 4 | 8 |
| 3 | 6 |
| 5 | 12 |

교환센세의 도움을 받아서 DP 점화식을 그렸습니다....
|index / 각 무게| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 
|:----:|:---:|:----:|:-----:|:----:|:----:|:----:|:----:|:----:|
|0| 0 | 0 | 0 | 0 | 0 | 0 | 13 | 13 |
|1| 0 | 0 | 0 | 0 | 8 | 8 | 13 | 13 |
|2| 0 | 0 | 0 | 6 | 8 | 8 | 13 | 14 |
|3| 0 | 0 | 0 | 6 | 8 | 12 | 13 | 13 |

1. weight index 반복문 돌리기(N) -> i
2. DP의 역방향으로 돌리기(k+1) -> j
3. 점화식으로 풀기
    - 총무게 - 현재 무게가 0보다 크면(무게 초과가 아니면)
        - dp[j] = dp[j]이거나 dp[j-weight[i]](현재 index) + values[i](현재 index의 value)  


우선적으로 제일 큰 7부터 돌아가는 형식으로 진행했고



## 📚 새롭게 알게된 내용
<!-- 새롭게 알게된 내용이 있다면 작성 해주시고 출처를 남겨주세요. -->

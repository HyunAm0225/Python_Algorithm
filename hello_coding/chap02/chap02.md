## 연습문제

### 가계부 앱을 개발하고 있다고 생각하자
1. 야채
2. 영화
3. SF 독서 클럽 회원 가입
#### 여러분은 돈을 어디에 썼는지 매일 앱에 기록합니다. 월말이 되면 지출을 되돌아보고 소비 금액의 합계를 계산합니다.
#### 그러니까 자료를 읽는 것보다 삽입하는 일이 훨씬 많습니다. 그럼 배열을 사용해야 할까요? 아니면 리스트를 사용해야 할까요?

- 답 : 검색보다 삽입이 많으므로 리스트를 사용해야 합니다.
- 이유 : 배열(읽기가 빠르고 삽입이 느리다), 리스트(읽기가 느리고 삽입이 빠르다)

#### 레스토랑에서 고객의 주문을 받아서 처리하는 앱을 만들고 있다고 가정하죠. 그 앱은 우선 주문 목록을 저장해야 합니다. 서비스 담당 직원은 이 리스트에 계속 주문을 추가하고,
#### 요리사는 리스트에서 주문을 꺼내어 조리를 합니다. 이런 것을 주문 큐라고 합니다. 서비스 담당 직원은 큐의 뒤에 주문을 추가하고, 요리사는 큐의 앞에서 첫 번째 주문을 꺼내어 요리합니다. 
#### 여러분은 이러한 큐를 구현하는 데 배열을 사용하겠습니까? 아니면 연결리스트를 사용하겠습니까?

- 답 : 연결리스트를 사용합니다. (요리사는 순차적으로 일을 처리하기 때문에)

#### 페이스북이 사용자 이름 목록을 가지고 있다고 합니다. 누군가가 페이스북에 로그인하려고 하면 사용자 이름 목록에서 이름을 검색해야 합니다. 만약 사용자 이름 목록에 아이디가 없다면 로그인할 수 없겠죠.
#### 사람들은 페이스북에 빈번하게 로그인합니다. 그럼 이름 목록 검색도 자주 이루어진다는겁니다. 페이스북이 이 목록을 검색하기 위해 이진 탐색을 사용한다고 가정한다면, 이진 탐색을 하기 위해 임의 접근이 가능해야 합니다. 즉, 이름 목록 중간에 있는 값도 즉시 읽을 수 있어야 합니다. 이 경우에는 목록을 구현하는데 배열을 쓸까요 리스트를 쓸까요

- 답 : 임의의 값을 조회할때는 배열이 효율적이다. 
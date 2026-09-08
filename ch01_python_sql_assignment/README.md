# AX 2회차 Chapter 1 과제

Python 기초와 SQL & 데이터베이스 기초를 한 폴더에 정리한 제출용 과제입니다.

이 과제의 목적은 단순히 정답을 출력하는 것이 아니라, **데이터를 저장하고 → 반복해서 확인하고 → 조건을 판단하고 → 결과를 저장하고 → 함수로 정리하고 → 오류를 검증하는 흐름**을 직접 이해하는 것입니다.

---

## 1. 폴더 구성

```text
ch01_python_sql_assignment/
├── README.md
├── python_assignment.py
├── members_assignment.sql
└── word_frequency_result.txt   # Python 실행 시 생성되는 단어 빈도 결과 파일
```

| 파일 | 역할 |
|---|---|
| `python_assignment.py` | Python Part 1~4와 도전 문제를 실행하는 소스 코드 |
| `members_assignment.sql` | PostgreSQL Schema/Table 생성, CRUD, 집계, 도전 문제 SQL |
| `README.md` | 코드 설명, 실행 방법, 예상 결과, 오류 검증 과정, 확인 질문 답변 |
| `word_frequency_result.txt` | Python 도전 문제에서 파일 저장 기능으로 만들어지는 결과 |

---

# 2. Python 기초 과제

## 2-1. 실행 방법

VS Code 터미널에서 저장소를 받은 뒤 다음과 같이 실행합니다.

```bash
cd ch01_python_sql_assignment
python python_assignment.py
```

Windows 환경에서 `python` 명령어가 동작하지 않는 경우 다음 명령어도 사용할 수 있습니다.

```bash
py python_assignment.py
```

실행하면 Part 1부터 Part 4, 도전 문제, 최종 검증까지 순서대로 출력됩니다.

---

## 2-2. Part 1 — 리스트와 반복문

사용한 핵심 문법은 다음과 같습니다.

```python
scores = [78, 92, 55, 64, 88, 49, 100, 73]
```

여러 학생의 점수를 `list`에 저장했습니다.

그 다음 `for` 반복문으로 점수를 하나씩 꺼냅니다.

```python
for score in scores:
```

`score`에는 반복할 때마다 리스트 안의 값이 하나씩 들어갑니다.

예를 들어 첫 번째 반복에서는 `78`, 두 번째 반복에서는 `92`, 세 번째 반복에서는 `55`가 들어갑니다.

각 점수가 60점 이상인지 `if`로 확인합니다.

```python
if score >= 60:
    result = "합격"
    pass_count = pass_count + 1
else:
    result = "불합격"
```

60점 이상이면 합격자 수를 1 증가시키고, 그렇지 않으면 불합격으로 처리합니다.

또한 80점 이상인 학생 수를 별도로 계산했습니다.

```python
if score >= 80:
    high_score_count = high_score_count + 1
```

### Part 1 예상 결과

```text
전체 학생 수: 8명
합격자 수: 6명
불합격자 수: 2명
80점 이상 학생 수: 3명
```

이 부분에서 확인할 수 있는 것은 다음과 같습니다.

- `list`에 여러 데이터를 저장할 수 있다.
- `for`로 데이터를 하나씩 꺼낼 수 있다.
- `if`로 조건에 따라 다른 처리를 할 수 있다.
- 숫자 변수를 이용하여 조건을 만족한 데이터 개수를 셀 수 있다.

---

## 2-3. Part 2 — 딕셔너리를 이용한 단어 빈도 분석

과제에 주어진 문장을 그대로 사용했습니다.

```python
sentence = """
파이썬 공부는 재미있다
파이썬 공부는 어렵지만 재미있다
데이터 분석에도 파이썬을 사용한다
파이썬 공부를 계속하면 실력이 늘어난다
"""
```

먼저 `split()`을 사용합니다.

```python
words = sentence.split()
```

`split()`은 문자열을 공백과 줄바꿈을 기준으로 나눕니다.

결과는 다음과 같은 리스트가 됩니다.

```text
['파이썬', '공부는', '재미있다', '파이썬', '공부는', ...]
```

단어 등장 횟수를 저장하기 위해 빈 딕셔너리를 만듭니다.

```python
word_counts = {}
```

여기서

- Key = 단어
- Value = 등장 횟수

입니다.

예를 들어 최종적으로 다음과 같은 형태가 됩니다.

```python
{
    '파이썬': 3,
    '공부는': 2,
    '재미있다': 2,
    '어렵지만': 1
}
```

단어를 하나씩 반복하면서 이미 등장한 단어인지 확인합니다.

```python
for word in words:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1
```

### 처음 등장한 단어

예를 들어 처음 `파이썬`을 만났을 때는 딕셔너리에 아직 `파이썬` Key가 없습니다.

따라서 다음 코드가 실행됩니다.

```python
word_counts['파이썬'] = 1
```

### 다시 등장한 단어

두 번째 `파이썬`을 만나면 이미 Key가 존재합니다.

기존 값 `1`에 `1`을 더합니다.

```python
word_counts['파이썬'] = 2
```

세 번째 등장하면 `3`이 됩니다.

### Part 2 주요 결과

```text
파이썬 : 3회
공부는 : 2회
재미있다 : 2회
어렵지만 : 1회
데이터 : 1회
분석에도 : 1회
파이썬을 : 1회
사용한다 : 1회
공부를 : 1회
계속하면 : 1회
실력이 : 1회
늘어난다 : 1회
```

2회 이상 등장한 단어는 다음과 같습니다.

```text
파이썬 : 3회
공부는 : 2회
재미있다 : 2회
```

### 주의할 점

`파이썬`과 `파이썬을`은 컴퓨터 입장에서는 서로 다른 문자열입니다.

마찬가지로 `공부는`과 `공부를`도 다른 단어로 계산됩니다.

이 과제는 자연어 형태소 분석이 아니라 `split()`을 이용한 기초 문자열 처리이므로 이 결과가 정상입니다.

---

## 2-4. Part 3 — 함수로 코드 정리

Part 2의 단어 빈도 계산 부분을 다음 함수로 만들었습니다.

```python
def count_words(sentence):
```

함수는 문자열을 입력받고 최종 딕셔너리를 `return`합니다.

```python
return word_counts
```

함수를 사용하는 코드는 다음과 같습니다.

```python
result = count_words(sentence)
```

여기서 `result`에는 함수가 반환한 단어 빈도 딕셔너리가 저장됩니다.

특정 횟수 이상 등장한 단어를 출력하는 기능도 별도의 함수로 분리했습니다.

```python
def print_words_over_count(word_counts, min_count):
```

따라서 다음과 같이 기준을 바꿔서 사용할 수 있습니다.

```python
print_words_over_count(result, 2)
print_words_over_count(result, 3)
```

함수로 만들면 같은 코드를 여러 번 복사하지 않아도 되고, 기능별로 코드를 나눌 수 있어 읽고 수정하기 쉬워집니다.

---

## 2-5. Part 4 — 오류 확인 및 예외처리

딕셔너리를 다음과 같이 조회할 수 있습니다.

```python
count = word_counts[search_word]
```

하지만 존재하지 않는 Key를 `[]`로 조회하면 `KeyError`가 발생합니다.

예를 들어 분석 결과에 `자바`라는 단어가 없는데 다음 코드를 실행하면 문제가 생길 수 있습니다.

```python
word_counts['자바']
```

그래서 다음과 같이 `try-except`로 처리했습니다.

```python
try:
    count = word_counts[search_word]
    print(f"'{search_word}'의 등장 횟수: {count}회")
except KeyError:
    print(f"'{search_word}'는 분석 결과에 없는 단어입니다.")
```

이렇게 하면 오류가 발생하더라도 프로그램 전체가 갑자기 종료되지 않고 알맞은 안내를 출력할 수 있습니다.

### 코드에서 적용한 오류 확인 순서

```text
1. 오류 메시지 확인
2. 문제가 발생한 코드 위치 확인
3. 변수 값 확인
4. 자료형 확인
5. 코드 수정
6. 다시 실행
```

### 예외처리 실행 결과

```text
[존재하는 단어 검색]
'파이썬'의 등장 횟수: 3회

[존재하지 않는 단어 검색]
'자바'는 분석 결과에 없는 단어입니다.
```

---

## 2-6. Python 도전 문제

필수 문제 외에도 다음 기능을 추가했습니다.

1. 가장 많이 등장한 단어 찾기
2. 가장 적게 등장한 단어 찾기
3. 특정 단어 검색하기
4. 특정 횟수 이상 등장한 단어 출력하기
5. 결과를 텍스트 파일로 저장하기

### 가장 많이 등장한 단어

```text
파이썬 (3회)
```

### 가장 적게 등장한 단어

1회 등장한 단어들이 모두 해당합니다.

### 특정 단어 검색

```text
'재미있다'의 등장 횟수: 2회
```

### 3회 이상 등장한 단어

```text
파이썬 : 3회
```

### 파일 저장

`save_word_counts()` 함수에서 다음 코드를 사용합니다.

```python
with open(filename, "w", encoding="utf-8") as file:
```

`encoding="utf-8"`을 지정하여 한글이 정상적으로 저장되도록 했습니다.

프로그램을 실행하면 현재 실행 폴더에 다음 파일이 만들어집니다.

```text
word_frequency_result.txt
```

---

## 2-7. Python 전체 실행 결과에서 확인할 핵심 값

```text
전체 학생 수: 8명
합격자 수: 6명
불합격자 수: 2명
80점 이상 학생 수: 3명

파이썬 : 3회
공부는 : 2회
재미있다 : 2회

'파이썬'의 등장 횟수: 3회
'자바'는 분석 결과에 없는 단어입니다.

가장 많이 등장한 단어: 파이썬 (3회)

Part 2 결과와 Part 3 결과가 같은가? True
```

마지막 `True`는 Part 2에서 직접 작성한 로직과 Part 3에서 함수로 만든 로직이 같은 결과를 만들었다는 뜻입니다.

---

# 3. Python 확인 질문 답변

## 질문 1. `for` 반복문은 이 프로그램에서 어떤 역할을 하나요?

리스트의 점수나 문장의 단어를 하나씩 꺼내서 같은 작업을 반복하는 역할을 합니다. `for`가 없으면 데이터 개수만큼 같은 코드를 직접 여러 번 작성해야 합니다.

## 질문 2. 딕셔너리의 Key와 Value에는 각각 무엇이 저장되나요?

Key에는 단어가 저장되고 Value에는 그 단어가 몇 번 등장했는지가 숫자로 저장됩니다. 예를 들어 `{'파이썬': 3}`에서 `파이썬`이 Key이고 `3`이 Value입니다.

## 질문 3. 같은 단어가 다시 등장하면 딕셔너리 값은 어떻게 달라지나요?

이미 존재하는 단어라면 기존 등장 횟수에 1을 더합니다. 예를 들어 `파이썬`의 값이 2일 때 다시 등장하면 3으로 바뀝니다.

## 질문 4. 함수를 사용하는 이유는 무엇인가요?

반복되는 코드를 하나의 기능으로 묶어서 다시 사용할 수 있기 때문입니다. 코드가 짧아지고 어떤 부분이 어떤 역할을 하는지도 구분하기 쉬워집니다.

## 질문 5. AI를 사용했다면 AI가 제안한 코드에서 직접 확인하거나 수정한 부분은 무엇인가요?

AI를 이용해 과제 구조와 코드 초안을 검토했습니다. 다만 제출 전에는 `for`, `if`, 딕셔너리의 Key/Value 변화, 함수의 `return`, 예외처리가 실제로 어떤 순서로 실행되는지 직접 확인하고, 제 환경에서 코드를 실행하여 출력 결과가 예상과 같은지 다시 검증합니다.

---

# 4. SQL & 데이터베이스 과제

## 4-1. 실행 환경

- PostgreSQL
- DBeaver

SQL 파일:

```text
members_assignment.sql
```

---

## 4-2. 실행 방법

1. PostgreSQL 서버를 실행합니다.
2. DBeaver를 실행합니다.
3. PostgreSQL 데이터베이스에 연결합니다.
4. `members_assignment.sql` 파일을 엽니다.
5. SQL을 위에서 아래 순서대로 실행합니다.
6. 각 `SELECT` 결과를 확인합니다.

파일 전체를 다시 실행할 수 있도록 다음 문장을 넣었습니다.

```sql
CREATE SCHEMA IF NOT EXISTS practice;
DROP TABLE IF EXISTS practice.members;
```

`practice` 스키마가 이미 존재해도 오류가 발생하지 않고, 기존 연습용 `members` 테이블은 삭제한 뒤 다시 생성합니다.

> 주의: `DROP TABLE`은 기존 데이터를 삭제하므로 실제 서비스 데이터에는 함부로 사용하면 안 됩니다. 이 파일에서는 반복 실행하는 과제용 테이블이기 때문에 사용했습니다.

---

## 4-3. Part 1 — Schema와 Table

스키마를 생성합니다.

```sql
CREATE SCHEMA IF NOT EXISTS practice;
```

테이블 구조는 다음과 같습니다.

| 컬럼 | 자료형 | 제약조건 | 의미 |
|---|---|---|---|
| `member_id` | `SERIAL` | `PRIMARY KEY` | 회원 고유번호 |
| `name` | `VARCHAR(50)` | `NOT NULL` | 회원 이름 |
| `email` | `VARCHAR(100)` | `UNIQUE`, `NOT NULL` | 이메일 |
| `age` | `INTEGER` | - | 나이 |
| `joined_at` | `DATE` | - | 가입일 |

### PRIMARY KEY

```sql
member_id SERIAL PRIMARY KEY
```

각 회원을 다른 회원과 구분하기 위한 고유번호입니다.

### NOT NULL

```sql
name VARCHAR(50) NOT NULL
```

반드시 값이 있어야 한다는 뜻입니다.

### UNIQUE

```sql
email VARCHAR(100) UNIQUE NOT NULL
```

같은 이메일이 두 번 저장되지 않도록 제한합니다.

---

## 4-4. Part 2 — INSERT와 SELECT

6명의 회원 데이터를 넣었습니다.

```text
김민수 / 25
이서연 / 31
박지훈 / 22
최유진 / 28
정하늘 / 35
한예린 / 24
```

과제 조건은 최소 5명이므로 조건을 만족합니다.

### 전체 조회

```sql
SELECT *
FROM practice.members;
```

`*`는 모든 컬럼을 조회한다는 뜻입니다.

### 이름과 이메일만 조회

```sql
SELECT name, email
FROM practice.members;
```

필요한 컬럼만 지정하면 전체 데이터를 모두 가져오지 않아도 됩니다.

### 25세 이상 조회

```sql
SELECT *
FROM practice.members
WHERE age >= 25;
```

`WHERE`는 어떤 행을 선택할지 조건을 정합니다.

### 특정 이름 검색

```sql
WHERE name = '최유진';
```

### 나이가 많은 순서

```sql
ORDER BY age DESC;
```

`DESC`는 큰 값에서 작은 값으로 정렬합니다.

### 가입일이 빠른 순서

```sql
ORDER BY joined_at ASC;
```

`ASC`는 작은 값에서 큰 값, 날짜의 경우 오래된 날짜에서 최근 날짜 순으로 정렬합니다.

---

## 4-5. Part 3 — UPDATE와 DELETE

### UPDATE

수정하기 전에 먼저 대상 회원을 확인합니다.

```sql
SELECT *
FROM practice.members
WHERE member_id = 1;
```

그 다음 나이를 수정합니다.

```sql
UPDATE practice.members
SET age = 30
WHERE member_id = 1;
```

수정 후 다시 `SELECT`로 확인합니다.

### DELETE

삭제하기 전에도 먼저 대상을 확인합니다.

```sql
SELECT *
FROM practice.members
WHERE member_id = 6;
```

그 다음 삭제합니다.

```sql
DELETE FROM practice.members
WHERE member_id = 6;
```

### WHERE가 중요한 이유

다음처럼 `WHERE`가 없는 UPDATE를 실행하면

```sql
UPDATE practice.members
SET age = 30;
```

모든 회원의 나이가 30으로 바뀔 수 있습니다.

다음처럼 `WHERE`가 없는 DELETE를 실행하면

```sql
DELETE FROM practice.members;
```

테이블의 모든 회원 데이터가 삭제될 수 있습니다.

그래서 실제 작업에서는 **UPDATE/DELETE 전에 같은 WHERE 조건으로 SELECT를 먼저 실행하여 대상 행을 확인하는 습관**이 중요합니다.

---

## 4-6. Part 4 — 집계 함수

UPDATE와 DELETE까지 수행한 뒤 남는 회원은 5명입니다.

김민수의 나이는 25에서 30으로 바뀌고, 한예린은 삭제됩니다.

따라서 최종 나이는 다음과 같습니다.

```text
30, 31, 22, 28, 35
```

### 전체 회원 수

```sql
SELECT COUNT(*) AS total_members
FROM practice.members;
```

예상 결과:

```text
5
```

### 평균 나이

```sql
SELECT ROUND(AVG(age), 1) AS average_age
FROM practice.members;
```

계산:

```text
(30 + 31 + 22 + 28 + 35) / 5
= 146 / 5
= 29.2
```

예상 결과:

```text
29.2
```

### 최고 나이

```text
35
```

### 최저 나이

```text
22
```

### 25세 이상 회원 수

25세 이상은 30, 31, 28, 35이므로

```text
4명
```

입니다.

---

## 4-7. SQL 도전 문제

다음 문제를 모두 추가했습니다.

### 1. 연령대별 회원 수

`CASE`를 사용하여 20대, 30대 등으로 나눕니다.

### 2. 가장 최근에 가입한 회원

```sql
ORDER BY joined_at DESC
LIMIT 1;
```

삭제된 한예린을 제외하면 가장 최근 가입자는 `정하늘`입니다.

### 3. 평균 나이보다 많은 회원

서브쿼리를 사용합니다.

```sql
WHERE age > (
    SELECT AVG(age)
    FROM practice.members
)
```

현재 평균은 29.2세이므로 30세, 31세, 35세 회원이 조회됩니다.

### 4. 이메일로 검색

```sql
WHERE email = 'yujin@example.com';
```

### 5. 조건 두 개 이상 사용

```sql
WHERE age >= 25
  AND joined_at >= '2026-08-05'
```

`AND`를 이용하면 두 조건을 모두 만족하는 회원만 조회됩니다.

---

# 5. SQL 확인 질문 답변

## 질문 1. `PRIMARY KEY`는 왜 필요한가요?

각 행을 유일하게 구분하기 위해 필요합니다. 이름이 같은 회원이 여러 명 있을 수 있지만 회원 고유번호는 서로 달라야 정확한 회원을 찾고 수정하거나 삭제할 수 있습니다.

## 질문 2. `WHERE` 없이 `UPDATE` 또는 `DELETE`를 실행하면 어떤 문제가 발생할 수 있나요?

조건이 없기 때문에 특정 회원 한 명이 아니라 테이블의 모든 행이 대상이 될 수 있습니다. UPDATE라면 모든 데이터가 수정될 수 있고 DELETE라면 모든 데이터가 삭제될 수 있습니다.

## 질문 3. `SELECT *`와 필요한 컬럼만 선택하는 SQL의 차이는 무엇인가요?

`SELECT *`는 테이블의 모든 컬럼을 조회합니다. 반면 `SELECT name, email`처럼 작성하면 필요한 컬럼만 조회합니다. 실제로 필요한 데이터만 가져오는 편이 결과를 이해하기 쉽고 불필요한 데이터 조회도 줄일 수 있습니다.

## 질문 4. `COUNT()`와 `AVG()`는 각각 어떤 값을 계산하나요?

`COUNT()`는 조건에 맞는 행의 개수를 계산하고 `AVG()`는 숫자 컬럼의 평균값을 계산합니다.

## 질문 5. Python에서 데이터를 처리하는 것과 DB에서 SQL로 데이터를 조회하는 것의 차이를 어떻게 이해했나요?

Python은 프로그램 안으로 가져온 데이터를 반복문, 조건문, 함수 등을 사용하여 직접 처리하는 데 적합합니다. SQL은 데이터베이스 안에 저장된 많은 데이터 중에서 필요한 데이터를 조건에 맞게 찾거나 집계하고 수정하는 데 사용합니다. 두 방법 모두 데이터를 다루지만 처리되는 위치와 사용하는 문법이 다릅니다.

---

# 6. 제출 전 최종 체크리스트

- [ ] `python python_assignment.py`를 직접 실행했다.
- [ ] Python 코드가 오류 없이 끝까지 실행된다.
- [ ] `파이썬 : 3회`가 출력되는지 확인했다.
- [ ] Part 4에서 존재하지 않는 단어를 검색해도 프로그램이 종료되지 않는지 확인했다.
- [ ] `word_frequency_result.txt`가 생성되는지 확인했다.
- [ ] DBeaver에서 PostgreSQL에 연결했다.
- [ ] `members_assignment.sql`을 위에서부터 직접 실행했다.
- [ ] `practice.members` 테이블이 생성되는지 확인했다.
- [ ] INSERT 후 회원 데이터가 들어가는지 확인했다.
- [ ] UPDATE 전에 SELECT로 대상을 확인했다.
- [ ] DELETE 전에 SELECT로 대상을 확인했다.
- [ ] UPDATE 후 김민수의 나이가 30으로 바뀌는지 확인했다.
- [ ] DELETE 후 회원이 5명 남는지 확인했다.
- [ ] 최종 평균 나이가 29.2인지 확인했다.
- [ ] 실행 결과가 보이도록 필요한 화면을 캡처했다.
- [ ] 제출 전에 코드 내용을 본인의 말로 설명할 수 있는지 확인했다.

---

# 7. 핵심 정리

이번 과제에서 Python은 다음 흐름으로 작성했습니다.

```text
문자열
→ split()
→ 리스트
→ for 반복
→ if 조건
→ 딕셔너리에 결과 저장
→ 함수로 정리
→ try-except로 오류 처리
→ 파일 저장
→ 결과 검증
```

SQL은 다음 흐름으로 작성했습니다.

```text
Schema 생성
→ Table 생성
→ INSERT
→ SELECT
→ WHERE
→ ORDER BY
→ UPDATE
→ DELETE
→ COUNT / AVG / MAX / MIN
→ 도전 조회
→ 최종 결과 확인
```

코드를 그대로 외우기보다는 **각 줄이 어떤 데이터를 대상으로 무엇을 하는지 설명할 수 있는 상태**로 만드는 것이 이 과제의 핵심입니다.

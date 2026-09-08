# AX 2회차 Chapter 1 — SQL & Database 기초 과제

이 폴더는 **SQL & DB 과제만 따로 제출하기 위한 폴더**입니다.

## 제출용 파일

- `AX_ch01_sql_db_assignment.sql` : Schema 생성부터 INSERT, SELECT, UPDATE, DELETE, 집계 함수, 도전 문제까지 전체 SQL
- `README.md` : 실행 방법, SQL 설명, 예상 결과, 확인 질문 답변

---

# 1. 실행 환경

과제 안내에 맞춰 다음 환경을 기준으로 작성했습니다.

- PostgreSQL
- DBeaver

SQL 파일은 위에서부터 순서대로 실행하면 전체 작업 흐름을 확인할 수 있게 정리했습니다.

---

# 2. 실행 방법

1. DBeaver를 실행합니다.
2. PostgreSQL 데이터베이스에 연결합니다.
3. `AX_ch01_sql_db_assignment.sql` 파일을 엽니다.
4. 위에서부터 순서대로 SQL을 실행합니다.
5. `SELECT` 문이 나올 때마다 결과창을 확인합니다.

전체 파일을 다시 실행하기 편하도록 다음 문장을 사용했습니다.

```sql
CREATE SCHEMA IF NOT EXISTS practice;
DROP TABLE IF EXISTS practice.members;
```

첫 문장은 `practice` Schema가 없을 때만 생성합니다.

두 번째 문장은 이전 실행에서 만들어진 `members` 테이블이 있다면 삭제하여 처음부터 다시 실습할 수 있게 합니다.

> 주의: `DROP TABLE`은 실제 데이터를 삭제할 수 있는 명령이므로 실무에서는 대상 테이블을 반드시 확인해야 합니다. 여기서는 과제용 실습 테이블을 처음부터 다시 만드는 용도로 사용했습니다.

---

# 3. Part 1 — Schema와 Table 만들기

## 3-1. Schema 생성

```sql
CREATE SCHEMA IF NOT EXISTS practice;
```

Schema는 데이터베이스 안에서 관련된 테이블을 묶어 관리하는 공간이라고 이해했습니다.

이번 과제에서는 `practice`라는 Schema 안에 `members` 테이블을 만듭니다.

## 3-2. members 테이블 생성

```sql
CREATE TABLE practice.members (
    member_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INTEGER,
    joined_at DATE
);
```

각 컬럼의 의미는 다음과 같습니다.

| 컬럼 | 자료형 | 의미 |
|---|---|---|
| `member_id` | `SERIAL` | 회원 고유번호를 자동 증가시킴 |
| `name` | `VARCHAR(50)` | 회원 이름 |
| `email` | `VARCHAR(100)` | 이메일 |
| `age` | `INTEGER` | 나이 |
| `joined_at` | `DATE` | 가입일 |

`PRIMARY KEY`는 각 행을 유일하게 구분하기 위한 기준입니다.

`NOT NULL`은 값이 반드시 있어야 한다는 의미입니다.

`UNIQUE`는 같은 이메일을 중복해서 저장할 수 없도록 제한합니다.

---

# 4. Part 2 — INSERT와 SELECT

## 4-1. 회원 데이터 입력

과제 조건은 최소 5명이며, 이 코드에서는 6명을 입력합니다.

```sql
INSERT INTO practice.members (name, email, age, joined_at)
VALUES
    ('김민수', 'minsu@example.com', 25, '2026-08-01'),
    ('이서연', 'seoyeon@example.com', 31, '2026-08-03'),
    ('박지훈', 'jihoon@example.com', 22, '2026-08-05'),
    ('최유진', 'yujin@example.com', 28, '2026-08-07'),
    ('정하늘', 'haneul@example.com', 35, '2026-08-10'),
    ('한예린', 'yerin@example.com', 24, '2026-08-12');
```

`member_id`는 `SERIAL`이므로 직접 입력하지 않아도 1부터 자동으로 만들어집니다.

## 4-2. 전체 회원 조회

```sql
SELECT *
FROM practice.members;
```

`*`는 모든 컬럼을 조회한다는 의미입니다.

## 4-3. 필요한 컬럼만 조회

```sql
SELECT name, email
FROM practice.members;
```

전체 컬럼이 필요하지 않다면 필요한 컬럼 이름만 적어 조회할 수 있습니다.

## 4-4. 25세 이상 회원

```sql
SELECT *
FROM practice.members
WHERE age >= 25;
```

`WHERE`는 조건에 맞는 행만 조회할 때 사용합니다.

## 4-5. 특정 이름 검색

```sql
SELECT *
FROM practice.members
WHERE name = '최유진';
```

## 4-6. 나이가 많은 순서

```sql
SELECT *
FROM practice.members
ORDER BY age DESC;
```

`DESC`는 큰 값에서 작은 값 순서로 정렬합니다.

## 4-7. 가입일 순서

```sql
SELECT *
FROM practice.members
ORDER BY joined_at ASC;
```

`ASC`는 작은 값에서 큰 값 순서로 정렬합니다. 날짜의 경우 오래된 날짜부터 최근 날짜 순서가 됩니다.

---

# 5. Part 3 — UPDATE와 DELETE

## 5-1. UPDATE 전 대상 확인

수정하기 전에 먼저 다음 SQL로 어떤 회원을 수정하는지 확인합니다.

```sql
SELECT *
FROM practice.members
WHERE member_id = 1;
```

그 다음 나이를 30으로 변경합니다.

```sql
UPDATE practice.members
SET age = 30
WHERE member_id = 1;
```

수정 후 같은 `SELECT`를 다시 실행해 실제 변경 여부를 확인합니다.

## 5-2. DELETE 전 대상 확인

삭제도 먼저 대상 회원을 확인합니다.

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

삭제 후 전체 데이터를 다시 조회하여 6번 회원이 사라졌는지 확인합니다.

## 왜 WHERE가 중요한가?

다음과 같이 `WHERE` 없이 실행하면 위험합니다.

```sql
UPDATE practice.members
SET age = 30;
```

이 경우 한 회원이 아니라 **모든 회원의 나이가 30으로 바뀔 수 있습니다.**

마찬가지로 다음 SQL은 모든 행을 삭제할 수 있습니다.

```sql
DELETE FROM practice.members;
```

그래서 UPDATE와 DELETE에서는 `WHERE` 조건을 특히 주의해야 합니다.

---

# 6. Part 4 — 집계 함수

DELETE 이후 최종 데이터는 5명입니다.

또한 1번 김민수의 나이는 25세에서 30세로 수정된 상태입니다.

## 전체 회원 수

```sql
SELECT COUNT(*) AS total_members
FROM practice.members;
```

예상 결과:

```text
5
```

## 평균 나이

최종 나이는 다음과 같습니다.

```text
30, 31, 22, 28, 35
```

따라서 평균은 29.2입니다.

```sql
SELECT ROUND(AVG(age), 1) AS average_age
FROM practice.members;
```

예상 결과:

```text
29.2
```

## 가장 나이가 많은 회원

```sql
SELECT MAX(age) AS oldest_age
FROM practice.members;
```

예상 결과:

```text
35
```

## 가장 나이가 어린 회원

```sql
SELECT MIN(age) AS youngest_age
FROM practice.members;
```

예상 결과:

```text
22
```

## 25세 이상 회원 수

```sql
SELECT COUNT(*) AS members_age_25_or_more
FROM practice.members
WHERE age >= 25;
```

최종 데이터에서는 30, 31, 28, 35세 회원이 해당하므로 예상 결과는 4명입니다.

---

# 7. 도전 문제

필수 문제 외에도 다음 SQL을 추가했습니다.

## 연령대별 회원 수

`CASE`로 나이를 연령대로 바꾼 후 `GROUP BY`로 묶어 회원 수를 셉니다.

## 가장 최근 가입한 회원

```sql
ORDER BY joined_at DESC
LIMIT 1;
```

가입일을 최신순으로 정렬한 뒤 첫 번째 행만 조회합니다.

## 평균 나이보다 나이가 많은 회원

```sql
WHERE age > (
    SELECT AVG(age)
    FROM practice.members
)
```

괄호 안의 SQL이 먼저 평균을 계산하고, 바깥 SQL이 그 평균보다 나이가 많은 회원만 찾습니다.

## 이메일 검색

```sql
WHERE email = 'yujin@example.com';
```

## 조건 2개 함께 사용

```sql
WHERE age >= 25
  AND joined_at >= '2026-08-05'
```

`AND`는 두 조건을 모두 만족해야 한다는 뜻입니다.

---

# 8. 확인 질문 답변

## 1) `PRIMARY KEY`는 왜 필요한가요?

각 데이터를 다른 데이터와 구별하기 위해 필요합니다. 이름이 같은 회원이 있어도 `member_id`가 다르면 서로 다른 회원임을 구분할 수 있습니다.

## 2) `WHERE` 없이 `UPDATE` 또는 `DELETE`를 실행하면 어떤 문제가 발생할 수 있나요?

조건이 없으면 특정 행만 대상으로 하지 않고 테이블의 모든 행이 수정되거나 삭제될 수 있습니다. 그래서 실행 전에 `WHERE` 조건을 확인하는 것이 중요합니다.

## 3) `SELECT *`와 필요한 컬럼만 선택하는 SQL의 차이는 무엇인가요?

`SELECT *`는 모든 컬럼을 가져옵니다. 반면 `SELECT name, email`처럼 필요한 컬럼을 지정하면 필요한 정보만 가져옵니다. 실제 데이터가 많을수록 필요한 컬럼만 선택하는 것이 결과를 확인하기 쉽고 불필요한 데이터 조회도 줄일 수 있습니다.

## 4) `COUNT()`와 `AVG()`는 각각 어떤 값을 계산하나요?

`COUNT()`는 조건에 해당하는 데이터의 개수를 계산하고, `AVG()`는 숫자 데이터의 평균을 계산합니다.

## 5) Python에서 데이터를 처리하는 것과 DB에서 SQL로 데이터를 조회하는 것의 차이를 어떻게 이해했나요?

Python에서는 프로그램으로 가져온 데이터를 반복문과 조건문 등을 이용해 직접 처리할 수 있습니다. SQL은 데이터베이스에 저장된 데이터에서 원하는 조건을 지정하여 필요한 데이터만 조회하거나 수정하는 데 사용합니다. 두 방법 모두 데이터를 처리하지만 작업하는 위치와 방식이 다르다고 이해했습니다.

---

# 9. 제출 전 체크

- [ ] PostgreSQL에 정상 연결했다.
- [ ] `practice` Schema가 생성되는 것을 확인했다.
- [ ] `members` 테이블의 컬럼을 확인했다.
- [ ] INSERT 후 회원 6명이 조회되는 것을 확인했다.
- [ ] UPDATE 후 1번 회원의 나이가 30으로 바뀌는 것을 확인했다.
- [ ] DELETE 후 회원이 5명 남는 것을 확인했다.
- [ ] 집계 결과를 직접 확인했다.
- [ ] SQL 파일을 위에서부터 다시 실행했을 때 오류가 없는지 확인했다.

제출 페이지의 **SQL&DB 과제 GitHub 링크**에는 이 `sql_db_assignment` 폴더의 GitHub 주소를 제출하면 됩니다.

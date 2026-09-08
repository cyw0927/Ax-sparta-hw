-- ============================================================
-- AX 2회차 Chapter 1 - SQL & Database 기초 과제
-- PostgreSQL + DBeaver 기준
-- ============================================================
-- 실행 방법
-- 1. DBeaver에서 PostgreSQL 연결
-- 2. 이 파일을 열고 위에서부터 순서대로 실행
-- 3. 각 SELECT 결과를 직접 확인
--
-- 전체 파일을 다시 실행하기 쉽도록
-- CREATE SCHEMA IF NOT EXISTS와 DROP TABLE IF EXISTS를 사용했습니다.
-- ============================================================


-- ------------------------------------------------------------
-- Part 1. Schema와 Table 만들기
-- ------------------------------------------------------------

-- practice 스키마가 없을 때 생성합니다.
CREATE SCHEMA IF NOT EXISTS practice;

-- 재실행할 때 기존 members 테이블이 있으면 삭제합니다.
DROP TABLE IF EXISTS practice.members;

-- 회원 정보를 저장할 members 테이블을 생성합니다.
CREATE TABLE practice.members (
    member_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INTEGER,
    joined_at DATE
);

-- 테이블 생성 확인
SELECT *
FROM practice.members;


-- ------------------------------------------------------------
-- Part 2. INSERT와 SELECT로 회원 데이터 관리하기
-- ------------------------------------------------------------

-- 최소 5명 조건을 충족하도록 회원 6명을 입력합니다.
INSERT INTO practice.members (name, email, age, joined_at)
VALUES
    ('김민수', 'minsu@example.com', 25, '2026-08-01'),
    ('이서연', 'seoyeon@example.com', 31, '2026-08-03'),
    ('박지훈', 'jihoon@example.com', 22, '2026-08-05'),
    ('최유진', 'yujin@example.com', 28, '2026-08-07'),
    ('정하늘', 'haneul@example.com', 35, '2026-08-10'),
    ('한예린', 'yerin@example.com', 24, '2026-08-12');

-- 2-1. 전체 회원 조회
SELECT *
FROM practice.members;

-- 2-2. 이름과 이메일만 조회
SELECT name, email
FROM practice.members;

-- 2-3. 25세 이상 회원 조회
SELECT *
FROM practice.members
WHERE age >= 25;

-- 2-4. 특정 이름의 회원 조회
SELECT *
FROM practice.members
WHERE name = '최유진';

-- 2-5. 나이가 많은 순서로 조회
SELECT *
FROM practice.members
ORDER BY age DESC;

-- 2-6. 가입일이 빠른 순서로 조회
SELECT *
FROM practice.members
ORDER BY joined_at ASC;


-- ------------------------------------------------------------
-- Part 3. UPDATE와 DELETE로 데이터 변경하기
-- ------------------------------------------------------------

-- UPDATE 전에 수정 대상 확인
SELECT *
FROM practice.members
WHERE member_id = 1;

-- member_id가 1인 회원의 나이를 30세로 수정
UPDATE practice.members
SET age = 30
WHERE member_id = 1;

-- UPDATE 후 결과 확인
SELECT *
FROM practice.members
WHERE member_id = 1;


-- DELETE 전에 삭제 대상 확인
SELECT *
FROM practice.members
WHERE member_id = 6;

-- member_id가 6인 회원 삭제
DELETE FROM practice.members
WHERE member_id = 6;

-- DELETE 후 전체 데이터 확인
SELECT *
FROM practice.members;


-- ------------------------------------------------------------
-- Part 4. 집계 함수를 이용한 회원 데이터 분석
-- ------------------------------------------------------------

-- 4-1. 전체 회원 수
SELECT COUNT(*) AS total_members
FROM practice.members;

-- 4-2. 회원 평균 나이
SELECT ROUND(AVG(age), 1) AS average_age
FROM practice.members;

-- 4-3. 가장 나이가 많은 회원의 나이
SELECT MAX(age) AS oldest_age
FROM practice.members;

-- 4-4. 가장 나이가 어린 회원의 나이
SELECT MIN(age) AS youngest_age
FROM practice.members;

-- 4-5. 25세 이상 회원 수
SELECT COUNT(*) AS members_age_25_or_more
FROM practice.members
WHERE age >= 25;


-- ------------------------------------------------------------
-- 도전 문제
-- ------------------------------------------------------------

-- 도전 1. 연령대별 회원 수 조회
SELECT
    CASE
        WHEN age < 20 THEN '10대 이하'
        WHEN age < 30 THEN '20대'
        WHEN age < 40 THEN '30대'
        ELSE '40대 이상'
    END AS age_group,
    COUNT(*) AS member_count
FROM practice.members
GROUP BY age_group
ORDER BY age_group;

-- 도전 2. 가장 최근에 가입한 회원 조회
SELECT *
FROM practice.members
ORDER BY joined_at DESC
LIMIT 1;

-- 도전 3. 평균 나이보다 나이가 많은 회원 조회
SELECT *
FROM practice.members
WHERE age > (
    SELECT AVG(age)
    FROM practice.members
)
ORDER BY age DESC;

-- 도전 4. 이메일 주소로 특정 회원 검색
SELECT *
FROM practice.members
WHERE email = 'yujin@example.com';

-- 도전 5. 조건 2개 이상 함께 사용
-- 25세 이상이면서 2026-08-05 이후 가입한 회원 조회
SELECT *
FROM practice.members
WHERE age >= 25
  AND joined_at >= '2026-08-05'
ORDER BY joined_at ASC;


-- ------------------------------------------------------------
-- 최종 확인
-- ------------------------------------------------------------
SELECT *
FROM practice.members
ORDER BY member_id ASC;

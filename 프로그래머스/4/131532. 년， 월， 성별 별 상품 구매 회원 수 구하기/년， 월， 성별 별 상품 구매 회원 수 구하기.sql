-- 코드를 입력하세요
SELECT DATE_FORMAT(O.SALES_DATE, '%Y') AS YEAR,
        DATE_FORMAT(O.SALES_DATE, '%m') AS MONTH,
        GENDER,
        COUNT(DISTINCT U.USER_ID) AS USERS
FROM USER_INFO U
JOIN ONLINE_SALE O
ON U.USER_ID = O.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER
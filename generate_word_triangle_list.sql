/*-----------------------------------------------------------
----------------------- RUN THIS AS -------------------------
sqlite3 < generate_word_triangle.sql > triangle_word_list.txt
-------------------------------------------------------------*/

/*create and populate word list table*/
CREATE TABLE words(word TEXT);
.import wordlist_clean.txt words

/*select words that end with a string (longer than three characters) that is also found in the word list*/
CREATE TABLE b_in_a AS 
SELECT SUBSTR(A.word,0,instr(A.word,B.word)) AS 'start', B.word AS 'ending', A.word AS 'word_A'
FROM words A, words B 
WHERE LENGTH(ending) >= 3 
AND A.word != ending 
AND A.word LIKE '%'||ending;

/*narrow down previous table to select words where both the beginnings and endings (both longer than three characters) are in the word list*/
CREATE TABLE split_words AS SELECT * FROM b_in_a INNER JOIN words ON b_in_a.start = words.word WHERE LENGTH(words.word) >=3;

/*select words that form a word triangle. Find words when the end of one is the beginning of another, then self join on the word list to see if the unused substrings also form a valid word.*/
SELECT DISTINCT C.W1||C.W2, C.W3, W.start||W.ending AS testW FROM
       (SELECT A.start AS W1, A.ending AS W2, 
       CASE 
            WHEN A.start = B.ending THEN B.start||A.start 
            WHEN A.ending = B.start THEN A.ending||B.ending 
       END AS W3, 
       CASE 
            WHEN A.start = B.ending THEN B.start||A.ending 
            WHEN A.ending = B.start THEN A.start||B.ending 
       END AS W4
       FROM split_words A, split_words B
       WHERE A.start = B.ending OR A.ending = B.start) 
AS C INNER JOIN split_words AS W ON testW = C.W4;

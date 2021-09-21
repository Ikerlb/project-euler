(ns projecteuler)

;; create lazy fibonacci seq!
;; should be evident but
;; don't evaluate it directly
(defn fibo-seq
  [p, c]
  (lazy-seq (cons p (fibo-seq c (+ p c)))))

;; take n of lazy fibo seq
(defn fibo-until
  [n]
  (take-while (fn [x] (<= x n)) (fibo-seq 0 1)))

;; filter even from fibo until
(defn sum-even-fibo-until
  [n]
  (reduce + 0 (filter even? (fibo-until n))))


(sum-even-fibo-until 4000000)

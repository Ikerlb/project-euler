;; result is in vector of nums
;; just transform to the base
;; encoding afterwards
(defn convert [n k]
  "convert n from base 10 to base k"
  (loop [n n res nil]
    (cond
      (zero? n) res
      :else (recur
              (quot n k)
              (conj res (mod n k))))))

(defn is-palindrome? [l]
  (= (reverse l) l))

(defn is-base-k-palindrome? [n k]
  (is-palindrome? (convert n k)))


(defn two-and-ten-palindromes [upto]
  (filter
    #(and (is-base-k-palindrome? % 2)
          (is-base-k-palindrome? % 10))
    (range 1 (inc upto))))

;; maybe improve this?
;; shouldn't take this long (~6s)
(time (apply + (two-and-ten-palindromes 1000000)))

(require '[clojure.string :as s])

;; returns wether word is palindromic
(defn is-palindrome?
  [n]
  (= (str n) (s/reverse (str n))))

;; log n pow function
(defn pow 
  [n k]
  (if (== k 0)
    1 
    (if (even? k)
      (let [ph (pow n (/ k  2))]
        (* ph ph))
      (let [ph (pow n (/ (dec k) 2))]
        (* ph (* ph n))))))
    
;; lil function to return all nums with k digits
(defn k-digit-nums
  [k]
  (range (pow 10 (dec k)) (pow 10 k)))

;; filter all products of k digit
;; nums that are palindromic
(defn palindromes-from-k-digit-prod
  [k]
  (filter 
    is-palindrome? 
    (let [kdn (k-digit-nums k)]
      (for [i kdn 
           j kdn] (* i j)))))

;; get the max of it all 
(apply max (palindromes-from-k-digit-prod 3))

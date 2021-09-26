(defn pow
  [n k]
  (cond
    (zero? k) 1N
    (even? k) (let [p (pow n (/ k 2))] (* p p))
    :else (let [p (pow n (/ (dec k) 2))] (* p p n))))

(defn sum-digits
  ([n] (sum-digits n 0))
  ([n s]
    (cond
      (zero? n) s
      :else (recur (quot n 10) (+ s (mod n 10))))))

;; log 1000 is arround 10 so
;; no stack overflow worries
(time (sum-digits (pow 2 1000)))


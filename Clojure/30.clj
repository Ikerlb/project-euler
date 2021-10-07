;; why is there no 5 digit number
;; that satisfies the requirements?

;; adding another digit would add 10000
;; while 9⁴ is 6561 so it is definitely
;; bounded arround k

;; can we guess what the maximum size will
;; be?

;; (10**(a - 1)) > (a*(9**k))  

;; i don't know what else to do
;; to speed this up. but well
;; 4 seconds isn't that much :p


(defn sq
  [n]
  (* n n))

(defn half
  [n]
  (int (/ n 2)))

(defn pow
  [n p]
  (loop [n n p p acc 1N]
    (cond
      (zero? p) acc
      (even? p) (recur (sq n) (half p) acc)
      :else (recur (sq n) (half p) (* acc n)))))

(defn divmod
  [n d]
  [(int (/ n d)) (mod n d)])

(defn digits
  [n]
  (loop [n n res ()]
    (cond
      (zero? n) res
      :else (let [[d m] (divmod n 10)]
              (recur d (conj res m))))))

(defn is-kth-power-digit-sum?
  [n k]
  (==
    n
    (apply + (map #(pow % k) (digits n)))))

(defn get-num-size
  [k]
  (loop [i 1]
    (if (>
         (pow 10 (dec i))
         (* i (pow 9 k)))
      i
      (recur (inc i)))))

(defn all-kth-power-digits-sums
  [k]
  (filter
    #(is-kth-power-digit-sum? % k)
    (range 2 (inc (* (get-num-size k) (pow 9 k))))))

(time
  (apply + (all-kth-power-digits-sums 5)))

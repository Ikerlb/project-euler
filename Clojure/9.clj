;; a < b < c
;; a * a + b * b = c * c
;; a + b + c = 1000

;; c = 1000 - b - a
;; a² + b² = (1000 - b - a)²

;; b = (1000(a - 500)) / (a - 1000)
(defn get-b
  [a]
  (/ (* 1000 (- a 500)) (- a 1000)))

;; 1000 - b - a 
(defn get-c
  [a b]
  (- (- 1000 b) a))

(defn sum
  [a & more]
  (reduce + a more))

(defn prod
  [a & more]
  (reduce * a more))

;; if we fix a, we can
;; calculate both b and c
;; the only naturals
;; should be the answer
(map #(apply prod %)
  (filter
    #(and (apply < (cons 0 %)) (every? int? %))
    (for [a (range 1000)]
      (let [b (get-b a)
            c (get-c b a)]
        [a b c]))))

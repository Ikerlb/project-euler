;; n * (n + 1) * (1 / 2)
(defn sum-first-n [n] (/ (* n (inc n)) 2))

;; there is a closed formula for this
;; but i don't remember it so 
;; we just brute force our way out
(defn sum-first-n-sq
  [n]
  (reduce #(+ %1 (* %2 %2)) 0 (range 1 (inc n))))

;; sq
(defn sq [n] (* n n))

;; diff of square of sums 
;; and sums of squares
;; of the first n numbers
(defn diff-sq-sms-and-sm-sqs
  [n]
  (- (sq (sum-first-n n)) (sum-first-n-sq n)))

(diff-sq-sms-and-sm-sqs 100)

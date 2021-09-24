;; kinda dissapointed
;; memoizing intermediate
;; steps with recursion
;; makes stack overflow

;; TODO: improve this
(defn collatz
  ([n] (collatz n 0))
  ([n s]
    (cond
      (== n 1) s
      (odd? n) (recur (inc (* 3 n)) (inc s))
      :else (recur (/ n 2) (inc s)))))

(def memo-collatz (memoize collatz))

;; memo barely makes a difference the first time...
(time (apply max-key memo-collatz (range 1 1000000)))

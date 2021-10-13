(require '[clojure.set :as s])

;; number to digit
(defn digits
  [n]
  (if (zero? n)
    (list) 
    (loop [n n res ()]
      (if (zero? n)
        res
        (recur (quot n 10) (conj res (mod n 10)))))))

;; convert digits back to number
(defn to-num
  [digs]
  (loop [d digs res 0]
    (if (empty? d)
      res
      (recur (rest d) (+ (* res 10) (first d))))))

;; simply remove the first
;; occurance of an element
;; in a list!
(defn remove-once
  [coll elem]
  (loop [c coll res ()]
    (cond
      (empty? c) res
      (= elem (first c)) (concat res (rest c))
      :else (recur (rest c) (conj res (first c))))))

;; just remove from the list
;; and convert back to number
;; rational numbers in clojure
;; coming in handy :p
(defn cancel-digit
  [nd dd dig]
  (/
   (to-num (remove-once nd dig))
   (let [den (to-num (remove-once dd dig))]
     (if (zero? den)
       Integer/MAX_VALUE 
       den))))

;; only worth cancelling
;; digits in both num and denom
(defn is-digit-cancellable
  [n d]
  (let [nd (digits n)
        dd (digits d)]
    (some
      #(= (cancel-digit nd dd %1) (/ n d))  
      (s/difference
        (s/intersection (set nd) (set dd))
        #{0}))))

;; less than one fractions
(defn all-digit-cancellable
  [s e]
  (for [n (range s e)
        d (range (inc n) e)
        :when (is-digit-cancellable n d)]
    (rationalize (/ n d))))

(apply * (all-digit-cancellable 10 100))

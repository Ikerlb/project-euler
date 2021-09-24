;; no stack overflow...
;; kinda confused
;; as to when *shouldn't* i 
;; use regular recursion
(def ways
  (memoize
    (fn [r c]
    (cond
      (or (< c 0) (< r 0)) 0
      (== r c 0) 1
      :else (+ (ways (dec r) c) (ways r (dec c)))))))

(time (ways 20 20))

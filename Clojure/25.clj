(defn fibo
  ([n] (fibo 0N 1N n))
  ([p c n]
   (cond
     (zero? n) p
     :else (recur c (+ c p) (dec n)))))

(def PHI
  (/ (+ (Math/sqrt 5) 1) 2))

(defn binet
  [n]
  (Math/round
    (/ (Math/pow PHI n) (Math/sqrt 5))))


(defn first-k-digit-fibo
  [k]
  (Math/round
    (/
      (+
        (* (dec k) (Math/log 10))
        (* (/ 1 2) (Math/log 5)))
      (Math/log PHI))))

(first-k-digit-fibo 1000))

;; we know (as we can see in fn binet)
;; fn = round(phi**n / sqrt(5))

;; 10**999 <= phi**n / sqrt(5) 
;; 10**999*sqrt(5) <= phi**n
;; log_phi(10**999*sqrt(5)) <= n
;; this should be enough but java doesn't
;; have a generic base log function
;; log(10**999 * sqrt(5))) / log(phi) < n
;; log(10**999) + log(sqrt(5))) / log(phi) < n
;; 999 * log(10) + log(5**(1/2)) 
;; (999 * log(10) + (1/2)log(5)) / log(phi) < n 

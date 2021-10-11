(defmacro fn-mc
  [args & body]
  `(fn ~args
     (cond
       (neg? ~'n) 0
       (zero? ~'n) 1
       (empty? ~'coins) 0
       :else (do ~@body))))

(def coins-dp
  (memoize
    (fn-mc [n coins]
      (+
        (coins-dp n (drop-last coins))
        (coins-dp (- n (last coins)) coins)))))


(coins-dp 200 [1 2 5 10 20 50 100 200])

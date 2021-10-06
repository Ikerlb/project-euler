;; afaik this can only
;; work if n is odd
(defn spiral-matrix-diags
  [n]
  (loop [n n res 0]
    (if (== n 1)
      (inc res)
      (let [nn (* n n)
            delta (dec n)
            sm (apply
                 +
                 (map
                   #(- nn (* delta %))
                   (range 4)))]
        (recur
          (- n 2)
          (+ res sm))))))

(spiral-matrix-diags 1001)


#lang racket

(provide (all-defined-out)) ;; so we can put tests in a second file

;; put your code below

(define (sequence low high stride)
  (if (> low high)
  null
  (cons low (sequence (+ low stride) high stride))))

(define (string-append-map xs suffix)
  (map (lambda (str) (string-append str suffix)) xs))

(define (list-nth-mod xs n)
  (let ([n (remainder n (length xs))])
  (cond [(< n 0) (error "list-nth-mod: negative number")]
        [(null? xs) (error "list-nth-mod: empty list")]
        [(= n 0) (car xs)]
        [#t (list-nth-mod (cdr xs) (- n 1))])))

(define (stream-for-n-steps s n)
  (if (= n 0)
  null
  (let ([pr (s)])
    (cons (car pr) (stream-for-n-steps (cdr pr) (- n 1))))))

(define funny-number-stream
  (letrec ([f (lambda (x) (cons
                         (if (= (remainder x 5) 0)
                             (- 0 x)
                             x)
                         (lambda () (f (+ x 1)))))])
    (lambda ()(f 1))))

(define dan-then-dog
   (letrec ([dan (lambda () (cons "dan.jpg" dog))]
            [dog (lambda () (cons "dog.jpg" dan))])
    (lambda ()(dan))))

(define (stream-add-zero s)
  (lambda () (let ([pr (s)])
                 (cons (cons 0 (car pr))
                      (stream-add-zero (cdr pr))))))

(define (cycle-lists xs ys)
  (letrec ([f (lambda (n) (cons
                           (cons(list-nth-mod xs n)(list-nth-mod ys n))
                           (lambda () (f (+ n 1)))))])
    (lambda ()(f 0))))

(define (vector-assoc v vec)
  (letrec ([length (vector-length vec)]
           [f (lambda (n)
                (if (equal? n length)
                    #f
                    (letrec ([nth (vector-ref vec n)])
                      (if (and (pair? nth) (equal? v (car nth)))
                          nth
                          (f (+ n 1))))))])
    (f 0)))

(define (cached-assoc xs n)
  (letrec ([vec (make-vector n #f)]
           [pos 0])
  (lambda (v)
    (letrec ([cached (vector-assoc v vec)])
      (if cached
          (begin (print "cached") cached)
          (letrec ([ans (assoc v xs)])
            (begin
              (if ans
                  (begin (vector-set! vec pos ans) (set! pos (if (< pos (- n 1)) (+ pos 1) 0)))
                  #t)
              ans)))))))                           
                       


(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))



;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  
  (define (helper index lst cur_s)
    (if (null? cur_s)
        lst
       (cons (list index (car cur_s)) (helper (+ 1 index) lst (cdr cur_s) ))
    ) 
  )
  (helper 0 nil s)
)
  ; END PROBLEM 17

;; Problem 18

(define (zip pairs)
  (list (map car pairs) (map cadr pairs))  
  )
  ; END PROBLEM 18


;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           ;(define cur_body (map let-to-lambda body ))
            ; (if (eq? (cdr cur_body) nil)
            ;     (list form params  (car (map let-to-lambda cur_body ))   )
            ;     (list form params  (map let-to-lambda cur_body )   )
            ; )
           (append (list form params ) (map let-to-lambda body ))
            
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
          ;  (define cur_body (map let-to-lambda body ))
            
          ;   (if (eq? (cdr cur_body) nil) (define final_body (car cur_body)) (define final_body cur_body)  )
            (append     (list (append  (list 'lambda (car (zip values)))  (map let-to-lambda body )   ))  
            (map let-to-lambda (cadr (zip values))) )
          
           
           
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         (map let-to-lambda expr)
         ; END PROBLEM 19
         )))

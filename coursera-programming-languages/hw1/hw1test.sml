(* Homework1 Simple Test *)
(* These are basic test cases. Passing these tests does not guarantee that your code will pass the actual homework grader *)
(* To run the test, add a new line to the top of this file: use "homeworkname.sml"; *)
(* All the tests should evaluate to true. For example, the REPL should say: val test1 = true : bool *)
use "hw1.sml";

val test1 = is_older ((1,2,3),(2,3,4)) = true
val test1_1 = is_older ((1,1,1),(1,1,1)) = false
val test1_2 = is_older ((4,2,3),(2,3,4)) = false
val test1_3 = is_older ((4,4,3),(4,4,5)) = true

val test2 = number_in_month ([(2012,2,28),(2013,12,1)],2) = 1
val test2_1 = number_in_month ([(2019,2,28),(2013,2,1),(2013,9,1)],2) = 2
val test2_2 = number_in_month ([],2) = 0

val test3 = number_in_months ([(2012,2,28),(2013,12,1),(2011,3,31),(2011,4,28)],[2,3,4]) = 3

val test4 = dates_in_month ([(2012,2,28),(2013,12,1)],2) = [(2012,2,28)]

val test5 = dates_in_months ([(2012,2,28),(2013,12,1),(2011,3,31),(2011,4,28)],[2,3,4]) = [(2012,2,28),(2011,3,31),(2011,4,28)]

val test6 = get_nth (["hi", "there", "how", "are", "you"], 2) = "there"

val test7 = date_to_string (2013, 6, 1) = "June 1, 2013"

val test8 = number_before_reaching_sum (10, [1,2,3,4,5]) = 3
val test8_1 = number_before_reaching_sum (2, [1,2,3,4,5]) = 1

val test9 = what_month 70 = 3
val test9_1 = what_month 31 = 1
val test9_2 = what_month 32 = 2
val test9_3 = what_month 60 = 3

val test10 = month_range (31, 34) = [1,2,2,2]
val test10_1 = month_range (31, 20) = []
val test10_2 = month_range (31, 31) = [1]

val test11 = oldest([(2012,2,28),(2011,3,31),(2011,4,28)]) = SOME (2011,3,31)
val test11_1 = oldest([]) = NONE

val test12_1 = in_list([1,2,3,3,2,1],3) = true
val test12_2 = in_list([1,2,3,3,2,1],5) = false
val test12_3 = in_list([1,2,3,3,2,1],1) = true
val test12_4 = remove_duplicates([]) = []
val test12_5 = remove_duplicates([1]) = [1]
val test12_6 = remove_duplicates([1,2,3,3,2,1]) = [3,2,1]
val test12_7 = number_in_months_challenge ([(2012,2,28),(2013,12,1),(2011,3,31),(2011,4,28)],[2,3,4,3,4,2]) = 3
val test12_8 = dates_in_months_challenge ([(2012,2,28),(2013,12,1),(2011,3,31),(2011,4,28)],[2,3,4,2,3,4]) = [(2012,2,28),(2011,3,31),(2011,4,28)]


val test13 = reasonable_date(1998, 9, 1) = true;
val test13_1 = reasonable_date(0, 9, 1) = false;
val test13_2 = reasonable_date(1996, 2, 29) = true;
val test13_3 = reasonable_date(1997, 2, 29) = false;
val test13_4 = reasonable_date(2000, 2, 29) = true;
val test13_5 = reasonable_date(2100, 2, 29) = false;
val test13_6 = reasonable_date(2100, 3, 31) = true;
val test13_7 = reasonable_date(2100, 4, 31) = false;
val test13_8 = reasonable_date(2100, 12, 31) = true;
val test13_9 = reasonable_date(1998, 13, 1) = false;
val test13_10 = reasonable_date(2013,0,10) = false;
val test13_11 = reasonable_date(2013,13,10) = false;
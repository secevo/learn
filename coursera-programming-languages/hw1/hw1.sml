fun is_older(date1 : int * int * int, date2 : int * int * int) =
  #1 date1 < #1 date2 orelse
  (#1 date1 = #1 date2 andalso #2 date1 < #2 date2) orelse
  (#1 date1 = #1 date2 andalso #2 date1 = #2 date2 andalso #3 date1 < #3 date2)


fun number_in_month(dates: (int * int * int) list, month : int) = 
  if null dates
  then 0
  else 
    let val suffix = number_in_month(tl dates, month)
    in  
      if #2 (hd dates) = month
      then suffix + 1
      else suffix
    end

fun number_in_months(dates: (int * int * int) list, months : int list) =
  if null months
  then 0
  else 
    number_in_month(dates, hd months) + number_in_months(dates, tl months)
      
fun dates_in_month(dates: (int * int * int) list, month : int) = 
  if null dates
  then []
  else 
    let val suffix = dates_in_month(tl dates, month)
    in
      if #2 (hd dates) = month
      then hd dates::suffix
      else suffix
    end

fun dates_in_months(dates: (int * int * int) list, months : int list) =
  if null months
  then []
  else 
    dates_in_month(dates, hd months) @ dates_in_months(dates, tl months)

fun get_nth(strings: string list, n : int) = 
  if n = 1
  then hd strings
  else get_nth(tl strings, n - 1)

fun date_to_string(date : int * int * int) = 
  let val month_names = ["January", "February", "March", "April", "May", "June", 
  "July", "August", "September", "October", "November", "December"]
  in get_nth(month_names, #2 date)^" "^Int.toString(#3 date)^", "^Int.toString(#1 date)
  end

fun number_before_reaching_sum(sum:int, numbers:int list) = 
  if hd numbers < sum
  then 1 + number_before_reaching_sum(sum - hd numbers, tl numbers)
  else 0

fun what_month(day:int) = 
  let val days_of_month = [31,28,31,30,31,30,31,31,30,31,30,31]
  in number_before_reaching_sum(day, days_of_month) + 1
  end

fun month_range(day1:int, day2:int) = 
  if day1 > day2
  then []
  else what_month(day1)::month_range(day1+1, day2)

fun oldest(dates: (int * int * int) list) = 
  if null dates
  then NONE
  else let 
  fun oldest_noempty(dates:(int * int * int) list) = 
    if null (tl dates)
    then hd dates
    else let val suffix = oldest_noempty(tl dates)
      in 
        if is_older(hd dates, suffix)
        then hd dates
        else suffix
      end
    in SOME(oldest_noempty dates)
    end

fun in_list(numbers:int list, n:int) = 
    if null numbers
    then false
    else if hd numbers = n 
      then true
      else in_list(tl numbers, n)

fun remove_duplicates(numbers:int list) = 
  if null numbers
  then []
  else 
    let val suffix = remove_duplicates(tl numbers)
    in
      if in_list(tl numbers, hd numbers)
      then suffix
      else (hd numbers)::suffix
    end

fun number_in_months_challenge(dates: (int * int * int) list, months : int list) =
  number_in_months(dates, remove_duplicates(months))

fun dates_in_months_challenge(dates: (int * int * int) list, months : int list) =
  dates_in_months(dates, remove_duplicates(months))

fun get_nth_number(numbers: int list, n : int) = 
  if n = 1
  then hd numbers
  else get_nth_number(tl numbers, n - 1)

fun is_leap_year(year:int) = 
      year mod 4 = 0 andalso year mod 100 <> 0 orelse year mod 400 = 0

fun reasonable_date(date:int * int * int) = 
  #1 date > 0 andalso 
  #2 date >= 1 andalso #2 date <= 12 andalso 
  #3 date >= 1 andalso 
    let val days_of_month = [31,28,31,30,31,30,31,31,30,31,30,31]    
      val days = get_nth_number(days_of_month, #2 date)
      val days_plus = if is_leap_year(#1 date) then days + 1 else days
    in #3 date <= days_plus
    end
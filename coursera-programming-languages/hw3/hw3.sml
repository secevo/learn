(* Coursera Programming Languages, Homework 3, Provided Code *)

exception NoAnswer

datatype pattern = Wildcard
		 | Variable of string
		 | UnitP
		 | ConstP of int
		 | TupleP of pattern list
		 | ConstructorP of string * pattern

datatype valu = Const of int
	      | Unit
	      | Tuple of valu list
	      | Constructor of string * valu

fun g f1 f2 p =
    let 
	val r = g f1 f2 
    in
	case p of
	    Wildcard          => f1 ()
	  | Variable x        => f2 x
	  | TupleP ps         => List.foldl (fn (p,i) => (r p) + i) 0 ps
	  | ConstructorP(_,p) => r p
	  | _                 => 0
    end

(**** for the challenge problem only ****)

datatype typ = Anything
	     | UnitT
	     | IntT
	     | TupleT of typ list
	     | Datatype of string

(**** you can put all your code here ****)

val only_capitals = List.filter (fn s=>Char.isUpper(String.sub(s, 0)))

val longest_string1 = foldl (fn (x, acc)=>if String.size(x) > String.size(acc) then x else acc) ""

val longest_string2 = foldl (fn (x, acc)=>if String.size(x) >= String.size(acc) then x else acc) ""

fun longest_string_helper f  = foldl (fn (x ,acc)=>if f(String.size(x), String.size(acc)) then x else acc) "" 

val longest_string3 = longest_string_helper (fn (x, y) => x > y)

val longest_string4 = longest_string_helper (fn (x, y) => x >= y)

val longest_capitalized = longest_string1 o only_capitals

val rev_string = String.implode o rev o String.explode

fun first_answer f xs = 
	case xs of
		[] => raise NoAnswer
	|	x::xs' => case f x of 
					SOME v => v
				|	NONE => first_answer f xs'

fun all_answers f xs =
	let fun all f xs acc =
		case xs of 
			[] => acc
		|	x::xs' => case f x of
						NONE => NONE
					|	SOME v => all f xs' (SOME (case acc of SOME pre => pre@v))
	in
		all f xs (SOME [])
	end
val count_wildcards = g (fn ()=>1) (fn x=>0)

val count_wild_and_variable_lengths = g (fn ()=>1) (fn x=>String.size(x))

fun count_some_var(str, p) = g (fn ()=>0) (fn x=>if x=str then 1 else 0) p

fun extract_val p = 
	case p of
	  Variable x => x::[]
	| TupleP ps         => List.foldl (fn (p,xs) => xs@(extract_val p)) [] ps
	| ConstructorP(_,p) => extract_val p
	| _                 => []

fun distinct strs =
	case strs of
		[] => true
	| str::strs' => if List.exists (fn x=>x=str) strs' then false else distinct strs'

val check_pat = distinct o extract_val

fun match(v, p) = 
	case (v, p) of
		(_, Wildcard) => SOME []
	| (v, Variable s) => SOME ((s,v)::[])
	| (Unit, UnitP) => SOME []
	| (Const i, ConstP j) => if i=j then SOME [] else NONE
	| (Tuple vs, TupleP ps) => if List.length(vs)=List.length(ps)
								then all_answers match (ListPair.zip(vs, ps))
								else NONE
	| (Constructor(s2,v), ConstructorP(s1,p)) => if s1=s2 
												then match(v, p) 
												else NONE
	| (_,_) => NONE

fun first_match v ps = 
	SOME (first_answer (fn p=> match(v, p)) ps)
	handle NoAnswer => NONE
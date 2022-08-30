let rec merge l1 l2 =
  begin
    match l1, l2 with
    | [], [] -> []
    | l, [] -> l
    | [], l -> l
    | x::xs, y::ys ->
      if x < y
      then x::(merge xs (y::ys))
      else y::(merge (x::xs) ys)
  end
exception Not_found

type 'a data = { data : 'a }
type 'a bst = Nil | Node of int * 'a data * 'a bst * 'a bst

let rec search t key = begin
  match t with
  | Nil -> raise Not_found
  | Node (k, d, l, r) ->
    if key == k
    then d
    else
      if key < k
      then search l key
      else search r key
end

let rec insert t key data = begin match t with
  | Nil -> Node (key, data, Nil, Nil)
  | Node (key', data', left, right) ->
      if key < key'
      then Node (key', data', insert left key data, right)
      else Node (key', data', left, insert right key data)
    end

let rec inorder t =
  begin
    match t with
    | Nil -> []
    | Node (k, d, l, r) ->
    inorder l @ [(k, d)] @ inorder r
  end

let test = Nil
let t1 = insert test 12 {data = "a"}
let t2 = insert t1 5 {data = "b"}
let t3 = insert t2 17 {data = "c"}
let t4 = insert t3 1 {data = "d"}
let t5 = insert t4 3 {data = "e"}
let t6 = insert t5 2 {data = "f"}
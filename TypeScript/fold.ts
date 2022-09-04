function fold_left <A, B> (f : (x : A, y : B) => A, acc : A, l : B[]) : A
{
    if (l.length == 0)
    {
        return acc;
    }
    else
    {
        let [head, ...tail] : B[] = l;
        return fold_left(f, f(acc, head), tail);
    }
}

function fold_right <A, B> (f : (x : A, y : B) => B, l: A[], acc : B) : B
{
    if (l.length == 0)
    {
        return acc;
    }
    else
    {
        let [head, ...tail] : A[] = l;
        return f(head, fold_right(f, tail, acc));
    }
}

console.log(fold_left((x, y) => x - y, 0, [1,2,3,4,5]))
console.log(fold_right((x, y) => x - y, [1,2,3,4,5], 0))
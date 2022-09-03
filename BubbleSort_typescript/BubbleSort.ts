function bubblesort<A> (l: A[]) : void
{
    for (let i = 0; i < l.length - 1; i++)
    {
        for (let j = 0; j < l.length - i - 1; j++)
        {
            if (l[j] > l[j + 1])
            {
                let temp : A = l[j];
                l[j] = l[j + 1];
                l[j + 1] = temp;
            }
        }
    }
}

let test : number[] = [1,7,3,7,0,3,5,98,2,5,2,5,743,2,35,1];
bubblesort(test);
console.log(test)
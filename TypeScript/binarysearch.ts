function binarysearch<A> (l: A[], target: A) : number
{
    let low : number = 0;
    let high: number = l.length;

    while (low <= high)
    {
        let mid : number = Math.floor(low + (high - low) / 2);
        if (l[mid] == target)
        {
            return mid;
        }
        else if (l[mid] < target)
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }

    return -1;
}

function recbinarysearch<A> (l: A[], target: A, start: number, end: number) : number
{
    if (start > end)
    {
        return -1;
    }

    let mid : number = Math.floor(start + (end - start) / 2)
    if (l[mid] == target)
    {
        return mid
    }
    else if (l[mid] < target)
    {
        return recbinarysearch(l, target, mid + 1, end)
    }
    else
    {
        return recbinarysearch(l, target, start, mid - 1)
    }
}

console.log(recbinarysearch([1,2,3,4,5,6,7], 9, 0, 7))
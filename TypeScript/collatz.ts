let memo = new Map<number, number>
memo.set(1, 0)

function collatz (n : number) : number 
{
    if (memo.has(n))
    {
        return memo.get(n)!;
    }
    else
    {
        if (n % 2 == 0)
        {
            let previousSteps : number = collatz(n / 2);
            memo.set(n, 1 + previousSteps);
            return 1 + previousSteps;
        }
        else
        {
            let previousSteps : number = collatz(3 * n + 1);
            memo.set(n, 1 + previousSteps);
            return 1 + previousSteps;
        }
    }
}

console.log(collatz(12))
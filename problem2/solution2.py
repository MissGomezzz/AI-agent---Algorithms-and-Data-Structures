# The code provided for the problem 2 by the AI agent is:

def has_love_triangle(n: int, likes: list[int]) -> bool:
    """
    Detects whether a directed 3-cycle exists.
    Time complexity: O(n)
    Space complexity: O(1) additional space (excluding input storage)
    """
    # likes is 0-indexed internally
    for i in range(n):  # O(n)
        a = likes[i]
        b = likes[a]
        c = likes[b]

        if c == i:
            return True

    return False


if __name__ == "__main__":
    n = int(input().strip())
    # Convert to 0-based indexing
    likes = [int(x) - 1 for x in input().split()]

    if has_love_triangle(n, likes):
        print("YES")
    else:
        print("NO")

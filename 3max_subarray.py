def max_sub_array(a: list[int]) -> int:
    
    sol = [0]* (len(a) + 1)
    for i in range(1, len(sol)):
        sol[i] = max(sol[i - 1] + a[i -1], a[i - 1])
        
    answer  = sol[0]
    for i in range(1, len(sol)):
        if answer < sol[i]:
            answer = sol[i]
    return answer 



if __name__ == "__main__":
    inputs = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sub_array(inputs))
    

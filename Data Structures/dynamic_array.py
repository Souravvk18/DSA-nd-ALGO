if __name__ == "__main__":
    N, Q = map(int, input().strip().split(' '))
    sequences = [[] for _ in range(N)]
    last_answer = 0
    
    for q in range(Q):
        q_type, x, y = map(int, input().strip().split(' '))
        seq_num = (x ^ last_answer) % N
        
        if q_type == 2:
            last_answer = sequences[seq_num][y % len(sequences[seq_num])]
            print(last_answer)
        else:
            sequences[seq_num].append(y)

"""
2 5
1 0 5
1 1 7
1 0 3
2 1 0
7
2 1 1
3"""
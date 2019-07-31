if __name__ == '__main__':
  H, W = map(int, input().split())
  
  A = [list(map(int, input().split())) for _ in range(H)]
  up_down = H * W * 2
  left_right = sum([abs(A[i][j] - A[i][j-1]) for i in range(H) for j in range(1, W)] +  [A[i][0] + A[i][W - 1] for i in range(H)])
  front_back = sum([abs(A[i][j] - A[i - 1][j]) for i in range(1, H) for j in range(W)] +  [A[0][j] + A[H - 1][j] for j in range(W)])

  print(up_down + left_right + front_back)


if __name__ == '__main__':
  H, W = map(int, input().split())
  
  A = [list(map(int, input().split())) for _ in range(H)]

  surface = H * W * 2
  for i in range(H + 1):
    for j in range(W + 1):
      surface += abs( (A[i][j] if j < W and i < H else 0) - (0 if i == H else A[i][j-1] if j > 0 else 0))
      surface += abs( (A[i][j] if j < W and i < H else 0) - (0 if j == W else  A[i - 1][j] if i > 0 else 0) ) 

  print(surface)

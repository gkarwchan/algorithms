def queensAttack(n, k, r_q, c_q, obs):
    stp_r = n - c_q
    stp_l = c_q - 1
    stp_u = n - r_q
    stp_d = r_q - 1
    stp_ru = min(stp_r, stp_u)
    stp_ld = min(stp_l, stp_d)
    stp_lu = min(stp_l, stp_u)
    stp_rd = min(stp_r, stp_d)
    for ob in obs:
        if ob[0] == r_q:
            if c_q > ob[1]:
                stp_l = min(stp_l, c_q - ob[1] - 1)
            else:
                stp_r = min(stp_r, ob[1] - c_q - 1)
        elif ob[1] == c_q:
            if r_q > ob[0]:
                stp_d = min(stp_d, r_q - ob[0] - 1)
            else:
                stp_u = min(stp_u, ob[0] - r_q - 1)
        elif c_q - r_q == ob[1] - ob[0]:
            if r_q < ob[0]:
                stp_ru = min(stp_ru, ob[0] - r_q - 1)
            else:
                stp_ld = min(stp_ld, r_q - ob[0] - 1)
        elif n - r_q - c_q == n - ob[0] - ob[1]:
            if r_q > ob[0]:
                stp_rd = min(stp_rd, r_q - ob[0] - 1)
            else:
                stp_lu = min(stp_lu, ob[0] - r_q - 1)
        
    return stp_r + stp_l + stp_u + stp_d + stp_ld + stp_lu + stp_rd + stp_ru


    
    

if __name__ == '__main__':
    n, k = map(int, input().split())
    r_q, c_q = map(int, input().split())
    obs = [list(map(int, input().split())) for _ in range(k)]
    result = queensAttack(n, k, r_q, c_q, obs)
    print(result)

    
    
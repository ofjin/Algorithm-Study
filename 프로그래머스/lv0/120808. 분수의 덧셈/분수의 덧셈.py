def solution(numer1, denom1, numer2, denom2):
    # 1. 분수의 합
    bottom = denom1 * denom2
    top = denom1 * numer2 + numer1 * denom2
    
    # 2. 최대공약수 구하기
    gcd_val = gcd(bottom, top)
    
    # 3. 최대공약수로 나누기 
    answer = [top / gcd_val, bottom / gcd_val]
    return answer

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
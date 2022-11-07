prime_nums=[1]
for num in range(2,250):
        is_prime = True
        for div in range(2,num):
                rest = num % div
                if(rest == 0):
                        is_prime = False
                        break
                if(is_prime):
                        prime_nums.append(num)
f = open("results.txt", "w")
for num in prime_nums:
        f.write(str(num)+" ")
f.close()
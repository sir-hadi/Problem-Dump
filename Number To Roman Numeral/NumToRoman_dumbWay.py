''' 
the dumb way kinda fail and i took a lot of time to kinda find my own way,
so i continue to find the rigth answer online
'''

kelipatan = [1, 5, 10, 50, 100, 500, 1000]
roman_num = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

num = 97

def get_kelipatan(num):
    if num >= 1000:
        return 1000
    if num < 4:
        return 1
    for i in range(len(kelipatan)-1):
        sisa = num % kelipatan[i]
        if (num > sisa) and (num >= kelipatan[i]) and (num < kelipatan[i+1]):
            print(kelipatan[i])
            if ((num/kelipatan[i+1]) <= 1) and ((kelipatan[i+1]-num) <= 10) and not(num < 4) and not(3 < num - kelipatan[i] < 4):
                return kelipatan[i+1]
            else:
                return kelipatan[i]
    return 0


def convert_romans(num):
    roman_result = ' '
    while num > 0:
        kelipatan_num = get_kelipatan(num)
        # print('kelipatan angka :', kelipatan_num)
        index = kelipatan.index(kelipatan_num)

        if( kelipatan[index]-10 <= (num) <= kelipatan[index] ):
            kurang = kelipatan_num - num
            # print('kurang :', kurang)
            kelipatan_kurang = get_kelipatan(kurang)
            # print('kelipatan_kurang :', kelipatan_kurang)

            if kelipatan_kurang == kurang:
                roman_result += roman_num[kelipatan_kurang]
            else:
                roman_result += roman_num[kelipatan_kurang]*kurang

        roman_result += roman_num[kelipatan_num]
        num -= kelipatan_num
        # print('num setelah di kurang :',num)
        
    return roman_result

print(convert_romans_test(99))

# for i in range(1,2000):
#     print(f'{i} :',convert_romans(i))
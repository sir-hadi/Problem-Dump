'''
Dimulai dari nilai terbesar dulu urutan array/listnya dan kita masukin value value yang bikin
ribet (9/4) dan dia muncul selalu begitu, dan pasti semua angka ribet ini semua jenis kombinasi
input angka pasti itu itu aja contoh:
 1789 = MDCCLXXX'IX' <=
 191 = C'XC'I <=
 3949 = MMM'CM''XL''IX' <=

jadi kalo angka angka tersebut itu kita masukin array/list, kita fokus cuma nambahin ke belakang
dari result string aja, gak usah mikir bikin satu if condition yang nambahin dari depan string result
'''

values = [1000, 900, 500, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman_num = {1: 'I', 4: 'Iv', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
             50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

def num_to_numerals(num):
    if(3999 >= num > 0):
        result = ''
        i = 0
        while num > 0:
            if(num - values[i] >= 0):
                result += roman_num[values[i]]
                num -= values[i]
            else:
                i += 1
        return result
    return 0

print(num_to_numerals(3949))

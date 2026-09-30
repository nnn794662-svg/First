Davlatlar = [ 'Angilya','ispaniya','AQSH','Argentina','Belgiya','Brazilya' ]

# print(len(Davlatlar))

# sorted(Davlatlar)

# print(Davlatlar)



Sonlar = [9,5,6,2,4]
# x = sorted(Sonlar, reverse=True)
# y =  sorted(Sonlar, reverse=False)

# print(x)

# print(Sonlar)

# Davlatlar.reverse()
# print(Davlatlar)


# Davlatlar.sort()
# print(Davlatlar)

# Davlatlar.sort(reverse=True)
# print(Davlatlar)

juft_sonlar = list(range(120, 1201, 2))
# print(juft_sonlar)

# yigindi = sum(juft_sonlar)
#
# print(f"Yig'indi: {yigindi}")



# eng_katta = max(juft_sonlar)
# eng_kichik = min(juft_sonlar)
#
#
# ayirma = eng_katta - eng_kichik
# print(f"Ular o'rtasidagi ayirma: {ayirma}")

#
# hajmi =len(juft_sonlar)
# print("Juft sonlar soni:", hajmi)


# uzunlik = len(juft_sonlar)
# orta_indeks = uzunlik // 2
#
#
# boshidan= juft_sonlar[:20]
# ortasidan= juft_sonlar[orta_indeks - 10 : orta_indeks + 10]
# oxiridan= juft_sonlar[-20:]
#
#
# print("Boshidan 20 ta:", boshidan,  "\no'rtasidan 20 ta:", ortasidan,  "\noxiridan 20 ta:" , oxiridan)


taomlar = ["osh", "somsa", "shashlik", "suyuq osh", "manti"]


nonushta = taomlar[:]


nonushta.remove("shashlik")
nonushta.remove("manti")

nonushta.append("saryog'")
nonushta.append("qaymoq")


print("Taomlar ro'yxati:", taomlar)
print("Nonushta ro'yxati:", nonushta)


nonushta = tuple(nonushta)

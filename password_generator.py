import string
import random
def parola_olusturucu (uzunluk):
    karekter_seti=string.ascii_letters+string.digits+string.punctuation

    parola="".join(random.choice(karekter_seti)for i in range(uzunluk))
    return parola
uzunluk=int(input("Lütfen parolanızda kaç karekter istediğini seçin:"))
parola= parola_oluşturucu(uzunluk)
print(f"Oluşturulan parola:{parola}")


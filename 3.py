def check_password(password):
    if len(password) < 8 or len(password) > 32:
        return "Kata sandi harus memiliki panjang antara 8 hingga 32 karakter"
    
    if password[0].isdigit():
        return "Karakter awal tidak boleh angka"
    
    if not any(char.isdigit() for char in password):
        return "Harus memiliki angka"
    
    if not any(char.islower() for char in password) or not any(char.isupper() for char in password):
        return "Harus memiliki huruf kapital dan huruf kecil"
    
    return "Kata sandi valid"


input_password = str(input("masukan password = "))
output = check_password(input_password)
print(output)

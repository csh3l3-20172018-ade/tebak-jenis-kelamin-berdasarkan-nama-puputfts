
# coding: utf-8

# In[ ]:


my_name = input('enter name : ') #input nama
my_first_name=my_name.split(' ') #memisahkan dari spasi
length=len(my_first_name[0]) #menghitung panjang kata pertama
character=list(my_first_name[0]) #membuat karakter menjadi array
i=a=u=e=t=l=b=d=o=female=male=count=0 #inisialisasi untuk menampung berapa banyak huruf iauetlbdo ada pada nama pertama dan female dan male untuk menampung total letter yg muncul 
while count < length: #mengulang sebanyak jumlah huruf pada nama pertama
    if character[count] =='i' or character[count] =='I' : #mengecek karakter pada indeks count apakah sama dengan i
        i +=1  #menambahkan 1 setiap terdapat huruf i ke variabel i
    elif character[count] =='a' or character[count] =='A' : #mengecek karakter pada indeks count apakah sama dengan a
        a+=1   #menambahkan 1 setiap terdapat huruf i ke variabel i
    elif character[count] =='u' or character[count] =='U' : #mengecek karakter pada indeks count apakah sama dengan u
        u+=1   #menambahkan 1 setiap terdapat huruf i ke variabel i
    elif character[count] =='e' or character[count] =='E' : #mengecek karakter pada indeks count apakah sama dengan e
        e+=1   #menambahkan 1 setiap terdapat huruf i ke variabel i
    elif character[count] =='t' or character[count] =='T' : #mengecek karakter pada indeks count apakah sama dengan t 
        t+=1   #menambahkan 1 setiap terdapat huruf i ke variabel i
    elif character[count] =='l' or character[count] =='L' : #mengecek karakter pada indeks count apakah sama dengan l
        l+=1   #menambahkan 1 setiap terdapat huruf i ke variabel i
    elif character[count] =='b' or character[count] =='B' : #mengecek karakter pada indeks count apakah sama dengan b
        b+=1   #menambahkan 1 setiap terdapat huruf i ke variabel i
    elif character[count] =='d' or character[count] =='D' : #mengecek karakter pada indeks count apakah sama dengan d
        d+=1   #menambahkan 1 setiap terdapat huruf i ke variabel i
    elif character[count] =='o' or character[count] =='O' : #mengecek karakter pada indeks count apakah sama dengan o
        o+=1    #menambahkan 1 setiap terdapat huruf i ke variabel i
    count += 1  #menambahkan nilai count sebanyak 1 untuk mengulang

female=i+a+u+e+t+l #menjumlahkan nilai pada iauetl sebagai penentu jenis kelamin perempuan 
male=b+d+o  #menjumlahkan nilai pada bdo sebagai penentu jenis kelamin laki laki
print('Jumlah Huruf Untuk Perempuan Terdapat ', female) #menampilkan jumlah huruf untuk perempuan yang terdapat pada nama pertama
print('Jumlah Huruf Untuk Laki Laki Terdapat ', male) #menampilkan jumlah huruf untuk laki laki yang terdapat pada nama pertama
if (female>male): #membandingkan nilai dari female dengan male jika lebih besar maka akan di cetak 'Jenis Kelamin Perempuan'
    print('Jenis Kelamin Perempuan') #cetak 'Jenis Kelamin Perempuan' jika benar female lebih besar dari male
elif (male>female): #membandingkan nilai dari male dengan female jika lebih besar maka akan di cetak 'Jenis Kelamin Laki-Laki'
    print('Jenis Kelamin Laki Laki') #cetak 'Jenis Kelamin Laki-Laki' jika benar male lebih besar dari female
else: #jika nilai female sama dengan nilai male maka akan dicetak 'Jenis Kelamin Tidak Diketahui'
    print('Jenis kelamin tidak diketahui') #cetak 'Jenis Kelamin Tidak Diketahui' jika benar nilai female dan male sama


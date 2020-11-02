## AKAN DITAMPILKAN :
        # input : 
                # Masukkan nama pokemon :
        # output :
                # Nama Pokemon :
                # HP :
                # Attack :
                # Defense : 
                # Speed :
                # Type : 
                # URL : isinya url gambar pokemon
                # Ability Name :
                #    1....
                #    2....
                #    3....
#### list pokemon
import requests
pokemon = []                                                    # in case mas kal coba run punya saya, ini emg agak lama ya mas kal, sepertinya gara-gara dia ada 893 iterasi buat input data nama pokemonnya ke dalam variabel 'pokemon' buat jadi list hehehe
for i in range(1,894):                                          # semangat mas kal nunggu nya !! hehe. kenapa 1-894 ?karena saya coba di "https://pokeapi.co/api/v2/pokemon/"cuman bisa sampai 893
        url_prev= f"https://pokeapi.co/api/v2/pokemon/{i}"      # url yang di lakukan sebanyak i, karena untuk mendapatkan nama pokemonnya
        data_prev= requests.get(url_prev)                       # untuk mendapat akses data pada url
        output_prev = data_prev.json()                          # menyimpan data_prev dalam format .json, dan disimpan dalam variabel "output_prev"
        pokemon.append(output_prev['name'])                     # diappend ke list "pokemon", sebagai nama-nama pokemon
# print(pokemon)                                                # cuman buat liat nama pokemon di dalam variabel "pokemon" ada apa aja

#### Pokemon stats
input_pokemon = input("Masukkan nama pokemon : ")               # meminta user menginput nama pokemon yang mau mereka cari stats nya sesuai output soal
while input_pokemon.lower() not in pokemon :                    # menggunakan while _ not in _ , untuk mengecek apakah inputan user ada di dalam variabel "pokemon", apabila tidak akan diproses kebawah. diaplikasikan .lower() karena semua dalam variabel "pokemon" huruf kecil 
        print(f'{input_pokemon} not found ! COBA LAGI :)')      # apabila inputan user semborno, maka akan muncul output seperti disamping, karena menggunakkan while sehingga akan dilooping sampai inputan benar
        input_pokemon = input("Masukkan nama pokemon : ")       # dan user dipaksa untuk menginput sampai inputan ada didalam variabel "pokemon"
if input_pokemon.lower() in pokemon :                           # apabila inputan user ada di dalam variabel "pokemon", maka akan dilakukan proses dibawah : 
        index = pokemon.index(input_pokemon.lower())            # mencari nilai index didalam variabek "pokemon" untuk diinput kedalam url_new
        url_new= f"https://pokeapi.co/api/v2/pokemon/{index+1}" # index + 1, karena dalam list dimulai dari 0
        data_new= requests.get(url_new)                         # untuk mengakses data di "url_new", disimpan ke dalam variabel " data_new"
        output_new = data_new.json()                            # menyimpan data_new dalam format .json, dan disimpan ke dalam variabel "output_new"
        HP = output_new['stats'][0]['base_stat']                # mengakses HP dari pokemon yang diinput
        Attack = output_new['stats'][1]['base_stat']            # mengakses Attack dari pokemon yang diinput
        Defend = output_new['stats'][2]['base_stat']            # mengakses Defend dari pokemon yang diinput
        Speed = output_new['stats'][5]['base_stat']             # mengakses Speed dari pokemon yang diinput
        Pokemon_url = output_new['sprites']['front_default']    # mengakses alamat url dari gambar pokemon yang diinput
        Type = []                                               # menggunakan list , karena ada yang memiliki lebih dari 1 type
        Ability = []                                            # ability pokemon ada yang lebih dari 1 
        T = output_new['types']                                 # mengakses type dari pokemon yang diinput
        for i in range(len(T)):                                 # dilakukan looping karena ada yang memiliki lebih dari 1 type
                Type.append(T[i]['type']['name'])               # diappend ke variabel "T"
        A = output_new['abilities']                             # mengakses ability dari pokemon yang diinput
        for i in range(len(A)):                                 # dilakukan looping karena ada yang memiliki lebih dari 1 ability
                Ability.append(A[i]['ability']['name'])         # diappend ke variabel "A"
        print("=" * 100)                                        # cuman buat pembatas 
        print(f"Nama Pokemon : {input_pokemon.capitalize()}")   # diaplikasikan .capitalize() biar indah, karena nama pokemon yang diinput akan diawali huruf kapital
        print(f"HP : {HP}")
        print(f"Attack : {Attack}")
        print(f"Defend : {Defend}")
        print(f"Speed : {Speed}")
        print(f"Type : {Type}")
        print(f"Url : {Pokemon_url}")
        print(f"Ability : {Ability}")



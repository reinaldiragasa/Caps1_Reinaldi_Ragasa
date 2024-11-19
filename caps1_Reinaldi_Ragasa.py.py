def menampilkan_data_lapangan():
    while True:
        print(''' 
        Sub Menu:
        1. Menampilkan semua data lapangan
        2. Menampilkan data dari min ke max 
        3. Menampilkan data dari max ke min 
        4. Menampilkan data minimum
        5. Menampilkan data maksimum
        6. Menampilkan data spesifik lapangan
        7. Menampilkan data berdasarkan wilayah lapangan
        8. Kembali ke main menu
        ''')
        sub_choice = input("Masukkan pilihan dari Sort Pompa: ")
        
        if sub_choice == '1':
            print("Menampilkan semua data lapangan:")
            tampilkan_semua_data_lapangan()  # Menampilkan seluruh tabel X
            return  # Langsung kembali ke main_menu
        elif sub_choice == '2':
            print('''Pilih atribut yang ingin diurutkan:
            1. Gas (scf/bbl)
            2. Water (bwpd)
            3. Oil (bpd)
            4. Temperature (F)
            5. Gas, Oil and Water Price (USD)
            6. Water Cut (%)
            7. Kembali ke menu Sort Lapangan''')
            attribute_choice = input("Masukkan angka atribut yang ingin diurutkan dari min ke max: ")

            if attribute_choice == '1':
                print("Menampilkan tabel lapangan dari kuantitas  gas terendah ke tertinggi:")
                tampilkan_tabel_lapangan_dengan_urutan_kuantitas_gas_terendah_ke_tertinggi()
            elif attribute_choice == '2':
                print("Menampilkan tabel lapangan dari kuantitas air terendah ke tertinggi:")
                tampilkan_tabel_lapangan_dengan_urutan_kuantitas_air_terendah_ke_tertinggi()
            elif attribute_choice == '3':
                print("Menampilkan tabel lapangan dari kuantitas minyak terendah ke tertinggi:")
                tampilkan_tabel_lapangan_dengan_urutan_kuantitas_minyak_terendah_ke_tertinggi()
            elif attribute_choice == '4':
                print("Menampilkan tabel lapangan dari temperatur (F) terendah ke tertinggi:")
                tampilkan_tabel_lapangan_dengan_urutan_temperatur_terendah_ke_tertinggi()
            elif attribute_choice == '5':
                print("Menampilkan tabel lapangan dari harga minyak, air dan gas terendah ke tertinggi:")
                tampilkan_tabel_lapangan_dengan_urutan_harga_gas_air_minyak_terendah_ke_tertinggi()
            elif attribute_choice == '6':
                print("Menampilkan tabel water cut terendah ke tertinggi:")
                tampilkan_tabel_lapangan_dengan_urutan_water_cut_terendah_ke_tertinggi()
            elif attribute_choice == '7':
                print("Kembali ke menu Sub Menu.")
            else:
                print("Input tidak valid.")
        elif sub_choice == '3':
            print('''Pilih atribut yang ingin diurutkan:
            1. Gas (scf/bbl)
            2. Water (bwpd)
            3. Oil (bpd)
            4. Temperature (F)
            5. Gas, Oil and Water Price (USD)
            6. Water Cut (%)
            7. Kembali ke menu Sort Pompa''')
            attribute_choice = input("Masukkan angka atribut yang ingin diurutkan dari max ke min: ")

            if attribute_choice == '1':
                print("Menampilkan tabel lapangan dari kuantitas  gas tertinggi ke terendah:")
                tampilkan_tabel_lapangan_dengan_urutan_kuantitas_gas_tertinggi_ke_terendah()
            elif attribute_choice == '2':
                print("Menampilkan tabel lapangan dari kuantitas air tertinggi ke terendah:")
                tampilkan_tabel_lapangan_dengan_urutan_kuantitas_air_tertinggi_ke_terendah()
            elif attribute_choice == '3':
                print("Menampilkan tabel lapangan dari kuantitas minyak tertinggi ke terendah:")
                tampilkan_tabel_lapangan_dengan_urutan_kuantitas_minyak_tertinggi_ke_terendah()
            elif attribute_choice == '4':
                print("Menampilkan tabel lapangan dari temperatur (F) tertinggi ke terendah:")
                tampilkan_tabel_lapangan_dengan_urutan_temperatur_tertinggi_ke_terendah()
            elif attribute_choice == '5':
                print("Menampilkan tabel lapangan dari harga minyak, air dan gas tertinggi ke terendah:")
                tampilkan_tabel_lapangan_dengan_urutan_harga_gas_air_minyak_tertinggi_ke_terendah()
            elif attribute_choice == '6':
                print("Menampilkan tabel lapangan dari water cut tertinggi ke terendah:")
                tampilkan_tabel_lapangan_dengan_urutan_water_cut_tertinggi_ke_terendah()
            elif attribute_choice == '7':
                print("Kembali ke menu Sub Menu.")
            else:
                print("Input tidak valid")
        elif sub_choice == '4':
            print('''Pilih atribut yang ingin dicari nilai minimumnya:
            1. Gas (scf/bbl)
            2. Water (bwpd)
            3. Oil (bpd)
            4. Temperature (F)
            5. Gas, Oil and Water Price (USD)
            6. Water Cut (%)
            7. Kembali ke Menu Sort Pompa''')
            attribute_choice = input("Masukkan angka atribut yang ingin dicari nilai min nya: ")
            if attribute_choice == '1':
                print("Menampilkan kuantitas gas minimal:")
                tampilkan_kuantitas_gas_minimal()
            elif attribute_choice == '2':
                print("Menampilkan kuantitas air minimal:")
                tampilkan_kuantitas_air_minimal()
            elif attribute_choice == '3':
                print("Menampilkan kuantitas minyak minimum:")
                tampilkan_kuantitas_minyak_minimal()
            elif attribute_choice == '4':
                print("Menampilkan temperatur minimum:")
                tampilkan_temperatur_minimal()
            elif attribute_choice == '5':
                print("Menampilkan harga gas, minyak dan air minimum:")
                tampilkan_harga_gas_air_minyak_minimal()
            elif attribute_choice == '6':
                print("Menampilkan water cut minimum:")
                tampilkan_water_cut_minimal()    
            elif attribute_choice == '7':
                print("Kembali ke menu Sub Menu.")
            else:
                print("Input tidak valid")

        elif sub_choice == '5':
            print('''Pilih atribut yang ingin dicari nilai maksimalnya:
            1. Gas (scf/bbl)
            2. Water (bwpd)
            3. Oil (bpd)
            4. Temperature (F)
            5. Gas, Oil and Water Price (USD)
            6. Water Cut (%)
            7. Kembali ke Sort Pompa''')
            attribute_choice = input("Masukkan angka atribut yang ingin dicari nilai max nya: ")
            if attribute_choice == '1':
                print("Menampilkan kuantitas gas maksimal:")
                tampilkan_kuantitas_gas_maksimal()
            elif attribute_choice == '2':
                print("Menampilkan kuantitas air maksimal:")
                tampilkan_kuantitas_air_maksimal()
            elif attribute_choice == '3':
                print("Menampilkan kuantitas minyak maksimal:")
                tampilkan_kuantitas_minyak_maksimal()
            elif attribute_choice == '4':
                print("Menampilkan temperatur maksimal:")
                tampilkan_temperatur_maksimal()
            elif attribute_choice == '5':
                print("Menampilkan harga gas, minyak dan air maksimal:")
                tampilkan_harga_gas_air_minyak_maksimal()
            elif attribute_choice == '6':
                print("Menampilkan water cut maksimal:")
                tampilkan_water_cut_maksimal()
            elif attribute_choice == '7':
                print("Kembali ke menu Sub Menu.")
            else:
                print("Input tidak valid")
        elif sub_choice == '6':
            # Pastikan untuk menampilkan seluruh tabel pompa terlebih dahulu
            if not list_lapangan:  # Jika data kosong
                print("Data lapangan tidak ada.")
                continue  # Kembali ke menu Sort Pompa jika data kosong

            print("=" * 156)
            print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
            print("=" * 156)

            # Menampilkan semua data pompa
            for idx, lapangan in enumerate(list_lapangan, start=1):
                print(f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    # Footer tabel
            print("=" * 156)
            
            # Menampilkan prompt untuk mencari pompa spesifik
            tampilkan_data_spesifik_lapangan()  # Panggil fungsi untuk meminta input nama pompa
        elif sub_choice == '7':
    # Menambahkan input untuk tipe pompa
            wilayah = input("Masukkan wilayah yang dicari: ")
            print(f"Menampilkan data lapangan berdasarkan wilayah: {wilayah}")
            tampilkan_data_berdasarkan_wilayah(wilayah)
        elif sub_choice == '8':
            print("Kembali ke main menu.")
            main_menu()
            break  # Langsung kembali ke main_menu
        else:
            print("Input tidak valid")

def tampilkan_semua_data_lapangan():
    if not list_lapangan:  # Mengecek apakah list_pompa kosong (semua data sudah dihapus)
        print("Data lapangan tidak ada.")
        menampilkan_data_lapangan()  # Kembali ke menu jika tidak ada data
        return  # Menghentikan eksekusi lebih lanjut

    # Header tabel
    print("=" * 156)
    print(
        f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |"
    )
    print("=" * 156)
    
    # Menampilkan data lapangan satu per satu
    for idx, lapangan in enumerate(list_lapangan, start=1):
        print(
            f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |"
        )
    
    # Footer tabel
    print("=" * 156)
    
    # Kembali ke menu utama
    menampilkan_data_lapangan()
def tampilkan_tabel_lapangan_dengan_urutan_kuantitas_gas_terendah_ke_tertinggi():
    # Salin list_pompa agar tidak merusak data asli (tabel X)
    list_lapangan_urut = list_lapangan[:]
    
    # Melakukan pengurutan berdasarkan quantity terendah ke tertinggi
    for i in range(len(list_lapangan_urut) - 1):
        for j in range(len(list_lapangan_urut) - 1 - i):
            if list_lapangan_urut[j][1] > list_lapangan_urut[j + 1][1]:
                list_lapangan_urut[j], list_lapangan_urut[j + 1] = list_lapangan_urut[j + 1], list_lapangan_urut[j]

    print("=" * 156)
    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
    print("=" * 156)
    
    # Menampilkan tabel berdasarkan urutan quantity
    for idx, lapangan in enumerate(list_lapangan_urut, start=1):
        print(f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    # Footer tabel
    print("=" * 156)
def tampilkan_tabel_lapangan_dengan_urutan_kuantitas_air_terendah_ke_tertinggi():
    # Salin list_pompa agar tidak merusak data asli (tabel X)
    list_lapangan_urut = list_lapangan[:]
    
    # Melakukan pengurutan berdasarkan harga terendah ke tertinggi
    for i in range(len(list_lapangan_urut) - 1):
        for j in range(len(list_lapangan_urut) - 1 - i):
            if list_lapangan_urut[j][2] > list_lapangan_urut[j + 1][2]:
                list_lapangan_urut[j], list_lapangan_urut[j + 1] = list_lapangan_urut[j + 1], list_lapangan_urut[j]

    print("=" * 156)
    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
    print("=" * 156)
    
    # Menampilkan tabel berdasarkan urutan harga
    for idx, lapangan in enumerate(list_lapangan_urut, start=1):
        print(f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    # Footer tabel
    print("=" * 156)
def tampilkan_tabel_lapangan_dengan_urutan_kuantitas_minyak_terendah_ke_tertinggi():
    # Salin list_pompa agar tidak merusak data asli (tabel X)
    list_lapangan_urut = list_lapangan[:]
    
    # Melakukan pengurutan berdasarkan Max Oil Lift terendah ke tertinggi
    for i in range(len(list_lapangan_urut) - 1):
        for j in range(len(list_lapangan_urut) - 1 - i):
            if list_lapangan_urut[j][3] > list_lapangan_urut[j + 1][3]:
                list_lapangan_urut[j], list_lapangan_urut[j + 1] = list_lapangan_urut[j + 1], list_lapangan_urut[j]

    print("=" * 156)
    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
    print("=" * 156)
    
    # Menampilkan tabel berdasarkan urutan Max Oil Lift
    for idx, lapangan in enumerate(list_lapangan_urut, start=1):
        print(f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    # Footer tabel
    print("=" * 156)
def tampilkan_tabel_lapangan_dengan_urutan_temperatur_terendah_ke_tertinggi():
    # Salin list_pompa agar tidak merusak data asli (tabel X)
    list_lapangan_urut = list_lapangan[:]
    
    # Melakukan pengurutan berdasarkan Min T (F) terendah ke tertinggi
    for i in range(len(list_lapangan_urut) - 1):
        for j in range(len(list_lapangan_urut) - 1 - i):
            if list_lapangan_urut[j][4] > list_lapangan_urut[j + 1][4]:
                list_lapangan_urut[j], list_lapangan_urut[j + 1] = list_lapangan_urut[j + 1], list_lapangan_urut[j]

    print("=" * 156)
    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
    print("=" * 156)
    
    # Menampilkan tabel berdasarkan urutan Min T (F)
    for idx, lapangan in enumerate(list_lapangan_urut, start=1):
        print(f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    # Footer tabel
    print("=" * 156)
def tampilkan_tabel_lapangan_dengan_urutan_harga_gas_air_minyak_terendah_ke_tertinggi():
    # Salin list_pompa agar tidak merusak data asli (tabel X)
    list_lapangan_urut = list_lapangan[:]
    
    # Melakukan pengurutan berdasarkan Max T (F) terendah ke tertinggi
    for i in range(len(list_lapangan_urut) - 1):
        for j in range(len(list_lapangan_urut) - 1 - i):
            if list_lapangan_urut[j][5] > list_lapangan_urut[j + 1][5]:
                list_lapangan_urut[j], list_lapangan_urut[j + 1] = list_lapangan_urut[j + 1], list_lapangan_urut[j]

    print("=" * 156)
    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
    print("=" * 156)
    
    # Menampilkan tabel berdasarkan urutan Max T (F)
    for idx, lapangan in enumerate(list_lapangan_urut, start=1):
        print(f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    # Footer tabel
    print("=" * 156)
def tampilkan_tabel_lapangan_dengan_urutan_water_cut_terendah_ke_tertinggi():
    # Salin list_pompa agar tidak merusak data asli (tabel X)
    list_lapangan_urut = list_lapangan[:]
    
    # Melakukan pengurutan berdasarkan lama operasi (tahun) terendah ke tertinggi
    for i in range(len(list_lapangan_urut) - 1):
        for j in range(len(list_lapangan_urut) - 1 - i):
            if list_lapangan_urut[j][7] > list_lapangan_urut[j + 1][7]:
                list_lapangan_urut[j], list_lapangan_urut[j + 1] = list_lapangan_urut[j + 1], list_lapangan_urut[j]

    print("=" * 156)
    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
    print("=" * 156)
    
    # Menampilkan tabel berdasarkan urutan lama operasi (tahun)
    for idx, lapangan in enumerate(list_lapangan_urut, start=1):
        print(f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    # Footer tabel
    print("=" * 156)
def tampilkan_tabel_lapangan_dengan_urutan_kuantitas_gas_tertinggi_ke_terendah():
    # Salin list_pompa agar tidak merusak data asli (tabel X)
    list_lapangan_urut = list_lapangan[:]
    
    # Melakukan pengurutan berdasarkan Quantity tertinggi ke terendah
    for i in range(len(list_lapangan_urut) - 1):
        for j in range(len(list_lapangan_urut) - 1 - i):
            if list_lapangan_urut[j][1] < list_lapangan_urut[j + 1][1]:  # Mengubah urutan menjadi dari tertinggi ke terendah
                list_lapangan_urut[j], list_lapangan_urut[j + 1] = list_lapangan_urut[j + 1], list_lapangan_urut[j]

    print("=" * 156)
    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
    print("=" * 156)
    
    # Menampilkan tabel berdasarkan urutan Quantity tertinggi ke terendah
    for idx, lapangan in enumerate(list_lapangan_urut, start=1):
        print(f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    # Footer tabel
    print("=" * 156)
def tampilkan_tabel_lapangan_dengan_urutan_kuantitas_air_tertinggi_ke_terendah():
    # Salin list_pompa agar tidak merusak data asli (tabel X)
    list_lapangan_urut = list_lapangan[:]
    
    # Melakukan pengurutan berdasarkan Harga (USD) tertinggi ke terendah
    for i in range(len(list_lapangan_urut) - 1):
        for j in range(len(list_lapangan_urut) - 1 - i):
            if list_lapangan_urut[j][2] < list_lapangan_urut[j + 1][2]:  # Mengubah urutan menjadi dari tertinggi ke terendah
                list_lapangan_urut[j], list_lapangan_urut[j + 1] = list_lapangan_urut[j + 1], list_lapangan_urut[j]

    print("=" * 156)
    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
    print("=" * 156)
    
    # Menampilkan tabel berdasarkan urutan Harga (USD) tertinggi ke terendah
    for idx, lapangan in enumerate(list_lapangan_urut, start=1):
        print(f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    # Footer tabel
    print("=" * 156)
def tampilkan_tabel_lapangan_dengan_urutan_kuantitas_minyak_tertinggi_ke_terendah():
    # Salin list_pompa agar tidak merusak data asli (tabel X)
    list_lapangan_urut = list_lapangan[:]
    
    # Melakukan pengurutan berdasarkan Max Oil Lift (bpd) tertinggi ke terendah
    for i in range(len(list_lapangan_urut) - 1):
        for j in range(len(list_lapangan_urut) - 1 - i):
            if list_lapangan_urut[j][3] < list_lapangan_urut[j + 1][3]:  # Mengubah urutan menjadi dari tertinggi ke terendah
                list_lapangan_urut[j], list_lapangan_urut[j + 1] = list_lapangan_urut[j + 1], list_lapangan_urut[j]

    print("=" * 156)
    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
    print("=" * 156)
    
    # Menampilkan tabel berdasarkan urutan Max Oil Lift (bpd) tertinggi ke terendah
    for idx, lapangan in enumerate(list_lapangan_urut, start=1):
        print(f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    # Footer tabel
    print("=" * 156)
def tampilkan_tabel_lapangan_dengan_urutan_temperatur_tertinggi_ke_terendah():
    # Salin list_pompa agar tidak merusak data asli (tabel X)
    list_lapangan_urut = list_lapangan[:]
    
    # Melakukan pengurutan berdasarkan Min Temperature (F) tertinggi ke terendah
    for i in range(len(list_lapangan_urut) - 1):
        for j in range(len(list_lapangan_urut) - 1 - i):
            if list_lapangan_urut[j][4] < list_lapangan_urut[j + 1][4]:  # Mengubah urutan menjadi dari tertinggi ke terendah
                list_lapangan_urut[j], list_lapangan_urut[j + 1] = list_lapangan_urut[j + 1], list_lapangan_urut[j]

    print("=" * 156)
    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
    print("=" * 156)
    
    # Menampilkan tabel berdasarkan urutan Min Temperature (F) tertinggi ke terendah
    for idx, lapangan in enumerate(list_lapangan_urut, start=1):
        print(f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    # Footer tabel
    print("=" * 156)
def tampilkan_tabel_lapangan_dengan_urutan_harga_gas_air_minyak_tertinggi_ke_terendah():
    # Salin list_pompa agar tidak merusak data asli (tabel X)
    list_lapangan_urut = list_lapangan[:]
    
    # Melakukan pengurutan berdasarkan Max Temperature (F) tertinggi ke terendah
    for i in range(len(list_lapangan_urut) - 1):
        for j in range(len(list_lapangan_urut) - 1 - i):
            if list_lapangan_urut[j][5] < list_lapangan_urut[j + 1][5]:  # Mengubah urutan menjadi dari tertinggi ke terendah
                list_lapangan_urut[j], list_lapangan_urut[j + 1] = list_lapangan_urut[j + 1], list_lapangan_urut[j]

    print("=" * 156)
    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
    print("=" * 156)
    
    # Menampilkan tabel berdasarkan urutan Max Temperature (F) tertinggi ke terendah
    for idx, lapangan in enumerate(list_lapangan_urut, start=1):
        print(f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    # Footer tabel
    print("=" * 156)
def tampilkan_tabel_lapangan_dengan_urutan_water_cut_tertinggi_ke_terendah():
    # Salin list_pompa agar tidak merusak data asli (tabel X)
    list_lapangan_urut = list_lapangan[:]
    
    # Melakukan pengurutan berdasarkan Max Temperature (F) tertinggi ke terendah
    for i in range(len(list_lapangan_urut) - 1):
        for j in range(len(list_lapangan_urut) - 1 - i):
            if list_lapangan_urut[j][7] < list_lapangan_urut[j + 1][7]:  # Mengubah urutan menjadi dari tertinggi ke terendah
                list_lapangan_urut[j], list_lapangan_urut[j + 1] = list_lapangan_urut[j + 1], list_lapangan_urut[j]

    print("=" * 156)
    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
    print("=" * 156)
    
    # Menampilkan tabel berdasarkan urutan Max Temperature (F) tertinggi ke terendah
    for idx, lapangan in enumerate(list_lapangan_urut, start=1):
        print(f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    # Footer tabel
    print("=" * 156)
# Fungsi untuk menampilkan pompa dengan quantity minimal
def tampilkan_kuantitas_gas_minimal():
    # Membuat salinan dari list_pompa yang asli
    list_lapangan_sorted = list_lapangan[:]
    
    # Mengurutkan berdasarkan quantity (dari yang terkecil ke yang terbesar)
    for i in range(len(list_lapangan_sorted) - 1):
        for j in range(len(list_lapangan_sorted) - 1 - i):
            if list_lapangan_sorted[j][1] > list_lapangan_sorted[j + 1][1]:
                list_lapangan_sorted[j], list_lapangan_sorted[j + 1] = list_lapangan_sorted[j + 1], list_lapangan_sorted[j]
    
    # Menampilkan pompa dengan quantity minimal
    gas_quantity_min = list_lapangan_sorted[0][1]
    print(f"Kuantitas gas minimum adalah {gas_quantity_min} scf/bbl.\n")
    # Menampilkan header tabel
    print("=" * 156)
    print(
        f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |"
    )
    print("=" * 156)

    # Menampilkan lapangan yang memiliki kuantitas gas minimum
    no = 1  # Untuk nomor urut di tabel


    #Menampilkan pompa dengan quantity minimal
    for lapangan in list_lapangan_sorted:
        if lapangan[1] == gas_quantity_min:
            # Menampilkan lapangan dengan kuantitas gas minimum dalam tabel
            print(
                f"| {no:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |"
            )
            no += 1

    # Menampilkan baris pembatas tabel
    print("=" * 156)
    print(f"\nKuantitas gas minimum terdapat di lapangan berikut dengan kuantitas gas sebesar {gas_quantity_min} scf/bbl:")
    for lapangan in list_lapangan_sorted:
        if lapangan[1] == gas_quantity_min:
            print(f"- {lapangan[0]} dengan kuantitas gas sebesar {lapangan[1]} scf/bbl.")

# Fungsi untuk menampilkan harga minimal
def tampilkan_kuantitas_air_minimal():
    # Membuat salinan dari list_pompa yang asli
    list_lapangan_sorted = list_lapangan[:]
    
    # Mengurutkan berdasarkan harga (dari yang terkecil ke yang terbesar)
    for i in range(len(list_lapangan_sorted) - 1):
        for j in range(len(list_lapangan_sorted) - 1 - i):
            if list_lapangan_sorted[j][2] > list_lapangan_sorted[j + 1][2]:
                list_lapangan_sorted[j], list_lapangan_sorted[j + 1] = list_lapangan_sorted[j + 1], list_lapangan_sorted[j]
    
    # Menampilkan harga minimal
    water_quantity_min = list_lapangan_sorted[0][2]  
    # Menampilkan kuantitas air minimum
    print(f"Kuantitas air minimum adalah {water_quantity_min} bwpd.\n")
    
    # Menampilkan header tabel
    print("=" * 156)
    print(
        f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |"
    )
    print("=" * 156)

    # Menampilkan lapangan yang memiliki kuantitas air minimum
    no = 1  # Untuk nomor urut di tabel
    # Mengurutkan berdasarkan max oil lift (dari yang terkecil ke yang terbesar)
    for lapangan in list_lapangan_sorted:
        if lapangan[2] == water_quantity_min:
            # Menampilkan lapangan dengan kuantitas air minimum dalam tabel
            print(
                f"| {no:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |"
            )
            no += 1

    # Menampilkan baris pembatas tabel
    print("=" * 156)
    
    # Menampilkan lapangan yang memiliki kuantitas air minimum
    print(f"\nKuantitas air minimum terdapat di lapangan berikut dengan kuantitas air sebesar {water_quantity_min} bwpd:")
    for lapangan in list_lapangan_sorted:
        if lapangan[2] == water_quantity_min:
            print(f"- {lapangan[0]} dengan kuantitas air sebesar {lapangan[2]} bwpd.")
def tampilkan_kuantitas_minyak_minimal():
    # Membuat salinan dari list_pompa yang asli
    list_lapangan_sorted = list_lapangan[:]
    
    # Mengurutkan berdasarkan min temperature (dari yang terkecil ke yang terbesar)
    for i in range(len(list_lapangan_sorted) - 1):
        for j in range(len(list_lapangan_sorted) - 1 - i):
            if list_lapangan_sorted[j][3] > list_lapangan_sorted[j + 1][3]:
                list_lapangan_sorted[j], list_lapangan_sorted[j + 1] = list_lapangan_sorted[j + 1], list_lapangan_sorted[j]
    
    # Menampilkan min temperature minimal
    oil_quantity_min = list_lapangan_sorted[0][3]  
    print(f"Kuantitas minyak minimum adalah {oil_quantity_min} bpd.\n")
        # Menampilkan header tabel
    print("=" * 156)
    print(
        f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |"
    )
    print("=" * 156)
    # Menampilkan lapangan yang memiliki kuantitas air minimum
    no = 1  # Untuk nomor urut di tabel

    # Menampilkan pompa dengan min temperature minimal
    for lapangan in list_lapangan_sorted:
        if lapangan[3] == oil_quantity_min:
            print(
                f"| {no:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |"
            )
            no += 1

    # Menampilkan baris pembatas tabel
    print("=" * 156)
    
    # Menampilkan lapangan yang memiliki kuantitas air minimum
    print(f"\nKuantitas minyak minimum terdapat di lapangan berikut dengan kuantitas minyak sebesar {oil_quantity_min} bpd:")
    for lapangan in list_lapangan_sorted:
        if lapangan[3] == oil_quantity_min:
            print(f"- {lapangan[0]} dengan kuantitas minyak sebesar {lapangan[3]} bpd.")
# Fungsi untuk menampilkan max temperature minimal
def tampilkan_temperatur_minimal():
    # Membuat salinan dari list_pompa yang asli
    list_lapangan_sorted = list_lapangan[:]
    
    # Mengurutkan berdasarkan min temperature (dari yang terkecil ke yang terbesar)
    for i in range(len(list_lapangan_sorted) - 1):
        for j in range(len(list_lapangan_sorted) - 1 - i):
            if list_lapangan_sorted[j][4] > list_lapangan_sorted[j + 1][4]:
                list_lapangan_sorted[j], list_lapangan_sorted[j + 1] = list_lapangan_sorted[j + 1], list_lapangan_sorted[j]
    
    # Menampilkan min temperature minimal
    temp_min = list_lapangan_sorted[0][4]  
    print(f"Temperatur minimum adalah {temp_min} F.")
    
    # Menampilkan header tabel
    print("=" * 156)
    print(
        f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |"
    )
    print("=" * 156)

    # Menampilkan lapangan yang memiliki kuantitas air minimum
    no = 1  # Untuk nomor urut di tabel

    # Menampilkan pompa dengan min temperature minimal
    for lapangan in list_lapangan_sorted:
        if lapangan[4] == temp_min:
            print(
                f"| {no:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |"
            )
            no += 1

    # Menampilkan baris pembatas tabel
    print("=" * 156)
    
    # Menampilkan lapangan yang memiliki kuantitas air minimum
    print(f"\nTemperatur minimum terdapat di lapangan berikut dengan temperatur sebesar {temp_min} F:")
    for lapangan in list_lapangan_sorted:
        if lapangan[4] == temp_min:
            print(f"- {lapangan[0]} dengan temperatur sebesar {lapangan[4]} F.")
def tampilkan_harga_gas_air_minyak_minimal():
    # Membuat salinan dari list_pompa yang asli
    list_lapangan_sorted = list_lapangan[:]
    
    # Mengurutkan berdasarkan min temperature (dari yang terkecil ke yang terbesar)
    for i in range(len(list_lapangan_sorted) - 1):
        for j in range(len(list_lapangan_sorted) - 1 - i):
            if list_lapangan_sorted[j][5] > list_lapangan_sorted[j + 1][5]:
                list_lapangan_sorted[j], list_lapangan_sorted[j + 1] = list_lapangan_sorted[j + 1], list_lapangan_sorted[j]
    
    # Menampilkan min temperature minimal
    harga_min = list_lapangan_sorted[0][5]  
    print(f"Harga minimum adalah {harga_min} USD.")
    
    # Menampilkan header tabel
    print("=" * 156)
    print(
        f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |"
    )
    print("=" * 156)

    # Menampilkan lapangan yang memiliki kuantitas air minimum
    no = 1  # Untuk nomor urut di tabel

    # Menampilkan pompa dengan min temperature minimal
    for lapangan in list_lapangan_sorted:
        if lapangan[5] == harga_min:
            print(
                f"| {no:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |"
            )
            no += 1

    # Menampilkan baris pembatas tabel
    print("=" * 156)
    
    # Menampilkan lapangan yang memiliki kuantitas air minimum
    print(f"\nHarga minimum terdapat di lapangan berikut dengan harga sebesar {harga_min} USD:")
    for lapangan in list_lapangan_sorted:
        if lapangan[5] == harga_min:
            print(f"- {lapangan[0]} dengan harga sebesar {lapangan[5]} USD.")
def tampilkan_water_cut_minimal():
    # Membuat salinan dari list_pompa yang asli
    list_lapangan_sorted = list_lapangan[:]
    
    # Mengurutkan berdasarkan min temperature (dari yang terkecil ke yang terbesar)
    for i in range(len(list_lapangan_sorted) - 1):
        for j in range(len(list_lapangan_sorted) - 1 - i):
            if list_lapangan_sorted[j][7] > list_lapangan_sorted[j + 1][7]:
                list_lapangan_sorted[j], list_lapangan_sorted[j + 1] = list_lapangan_sorted[j + 1], list_lapangan_sorted[j]
    
    # Menampilkan min temperature minimal
    water_cut_min = list_lapangan_sorted[0][7]  
    print(f"Water cut minimum adalah {water_cut_min}%.")
    
    # Menampilkan header tabel
    print("=" * 156)
    print(
        f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |"
    )
    print("=" * 156)

    # Menampilkan lapangan yang memiliki kuantitas air minimum
    no = 1  # Untuk nomor urut di tabel

    # Menampilkan pompa dengan min temperature minimal
    for lapangan in list_lapangan_sorted:
        if lapangan[7] == water_cut_min:
            print(
                f"| {no:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |"
            )
            no += 1

    # Menampilkan baris pembatas tabel
    print("=" * 156)
    
    # Menampilkan lapangan yang memiliki kuantitas air minimum
    print(f"\nWater cut minimum terdapat di lapangan berikut dengan water cut sebesar {water_cut_min}%:")
    for lapangan in list_lapangan_sorted:
        if lapangan[7] == water_cut_min:
            print(f"- {lapangan[0]} dengan kuantitas sebesar {lapangan[7]}%.")
# Fungsi untuk menampilkan quantity maksimal
def tampilkan_kuantitas_gas_maksimal():
    # Membuat salinan dari list_pompa yang asli
    list_lapangan_sorted = list_lapangan[:]
    
    # Mengurutkan berdasarkan min temperature (dari yang terkecil ke yang terbesar)
    for i in range(len(list_lapangan_sorted) - 1):
        for j in range(len(list_lapangan_sorted) - 1 - i):
            if list_lapangan_sorted[j][1] < list_lapangan_sorted[j + 1][1]:
                list_lapangan_sorted[j], list_lapangan_sorted[j + 1] = list_lapangan_sorted[j + 1], list_lapangan_sorted[j]
    
    # Menampilkan min temperature minimal
    gas_quantity_max = list_lapangan_sorted[0][1]  
    print(f"Kuantitas gas maksimum adalah {gas_quantity_max} bpd.\n")
        # Menampilkan header tabel
    print("=" * 156)
    print(
        f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |"
    )
    print("=" * 156)
    # Menampilkan lapangan yang memiliki kuantitas air minimum
    no = 1  # Untuk nomor urut di tabel

    #Menampilkan pompa dengan quantity minimal
    for lapangan in list_lapangan_sorted:
        if lapangan[1] == gas_quantity_max:
            # Menampilkan lapangan dengan kuantitas gas minimum dalam tabel
            print(
                f"| {no:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |"
            )
            no += 1

    # Menampilkan baris pembatas tabel
    print("=" * 156)
    print(f"\nKuantitas gas maksimum terdapat di lapangan berikut dengan kuantitas gas sebesar {gas_quantity_max} scf/bbl:")
    for lapangan in list_lapangan_sorted:
        if lapangan[1] == gas_quantity_max:
            print(f"- {lapangan[0]} dengan kuantitas gas sebesar {lapangan[1]} scf/bbl.")
# Fungsi untuk menampilkan harga maksimal
def tampilkan_kuantitas_air_maksimal():
    # Membuat salinan dari list_pompa yang asli
    list_lapangan_sorted = list_lapangan[:]
    
    # Mengurutkan berdasarkan harga (dari yang terkecil ke yang terbesar)
    for i in range(len(list_lapangan_sorted) - 1):
        for j in range(len(list_lapangan_sorted) - 1 - i):
            if list_lapangan_sorted[j][2] < list_lapangan_sorted[j + 1][2]:
                list_lapangan_sorted[j], list_lapangan_sorted[j + 1] = list_lapangan_sorted[j + 1], list_lapangan_sorted[j]
    
    # Menampilkan harga minimal
    water_quantity_max = list_lapangan_sorted[0][2]  
    # Menampilkan kuantitas air minimum
    print(f"Kuantitas air maksimum adalah {water_quantity_max} bwpd.\n")
    
    # Menampilkan header tabel
    print("=" * 156)
    print(
        f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |"
    )
    print("=" * 156)

    # Menampilkan lapangan yang memiliki kuantitas air minimum
    no = 1  # Untuk nomor urut di tabel
    # Mengurutkan berdasarkan max oil lift (dari yang terkecil ke yang terbesar)
    for lapangan in list_lapangan_sorted:
        if lapangan[2] == water_quantity_max:
            # Menampilkan lapangan dengan kuantitas air minimum dalam tabel
            print(
                f"| {no:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |"
            )
            no += 1

    # Menampilkan baris pembatas tabel
    print("=" * 156)
    
    # Menampilkan lapangan yang memiliki kuantitas air minimum
    print(f"\nKuantitas air maksimum terdapat di lapangan berikut dengan kuantitas air sebesar {water_quantity_max} bwpd:")
    for lapangan in list_lapangan_sorted:
        if lapangan[2] == water_quantity_max:
            print(f"- {lapangan[0]} dengan kuantitas air sebesar {lapangan[2]} bwpd.")
# Fungsi untuk menampilkan max oil lift maksimal
def tampilkan_kuantitas_minyak_maksimal():
   # Membuat salinan dari list_pompa yang asli
    list_lapangan_sorted = list_lapangan[:]
    
    # Mengurutkan berdasarkan min temperature (dari yang terkecil ke yang terbesar)
    for i in range(len(list_lapangan_sorted) - 1):
        for j in range(len(list_lapangan_sorted) - 1 - i):
            if list_lapangan_sorted[j][3] < list_lapangan_sorted[j + 1][3]:
                list_lapangan_sorted[j], list_lapangan_sorted[j + 1] = list_lapangan_sorted[j + 1], list_lapangan_sorted[j]
    
    # Menampilkan min temperature minimal
    oil_quantity_max = list_lapangan_sorted[0][3]  
    print(f"Kuantitas minyak maksimum adalah {oil_quantity_max} bpd.\n")
        # Menampilkan header tabel
    print("=" * 156)
    print(
        f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |"
    )
    print("=" * 156)
    # Menampilkan lapangan yang memiliki kuantitas air minimum
    no = 1  # Untuk nomor urut di tabel

    # Menampilkan pompa dengan min temperature minimal
    for lapangan in list_lapangan_sorted:
        if lapangan[3] == oil_quantity_max:
            print(
                f"| {no:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |"
            )
            no += 1

    # Menampilkan baris pembatas tabel
    print("=" * 156)
    
    # Menampilkan lapangan yang memiliki kuantitas air minimum
    print(f"\nKuantitas minyak maksimum terdapat di lapangan berikut dengan kuantitas minyak sebesar {oil_quantity_max} bpd:")
    for lapangan in list_lapangan_sorted:
        if lapangan[3] == oil_quantity_max:
            print(f"- {lapangan[0]} dengan kuantitas minyak sebesar {lapangan[3]} bpd.")
# Fungsi untuk menampilkan min temperature (T) maksimum
def tampilkan_temperatur_maksimal():
     # Membuat salinan dari list_pompa yang asli
    list_lapangan_sorted = list_lapangan[:]
    
    # Mengurutkan berdasarkan min temperature (dari yang terkecil ke yang terbesar)
    for i in range(len(list_lapangan_sorted) - 1):
        for j in range(len(list_lapangan_sorted) - 1 - i):
            if list_lapangan_sorted[j][4] < list_lapangan_sorted[j + 1][4]:
                list_lapangan_sorted[j], list_lapangan_sorted[j + 1] = list_lapangan_sorted[j + 1], list_lapangan_sorted[j]
    
    # Menampilkan min temperature minimal
    temp_max = list_lapangan_sorted[0][4]  
    print(f"Temperatur maksimum adalah {temp_max} F.")
    
    # Menampilkan header tabel
    print("=" * 156)
    print(
        f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |"
    )
    print("=" * 156)

    # Menampilkan lapangan yang memiliki kuantitas air minimum
    no = 1  # Untuk nomor urut di tabel

    # Menampilkan pompa dengan min temperature minimal
    for lapangan in list_lapangan_sorted:
        if lapangan[4] == temp_max:
            print(
                f"| {no:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |"
            )
            no += 1

    # Menampilkan baris pembatas tabel
    print("=" * 156)
    
    # Menampilkan lapangan yang memiliki kuantitas air minimum
    print(f"\nTemperatur maksimum terdapat di lapangan berikut dengan temperatur sebesar {temp_max} F:")
    for lapangan in list_lapangan_sorted:
        if lapangan[4] == temp_max:
            print(f"- {lapangan[0]} dengan temperatur sebesar {lapangan[4]} F.")
# Fungsi untuk menampilkan max temperature (T) maksimum
def tampilkan_harga_gas_air_minyak_maksimal():
    # Membuat salinan dari list_pompa yang asli
    list_lapangan_sorted = list_lapangan[:]
    
    # Mengurutkan berdasarkan min temperature (dari yang terkecil ke yang terbesar)
    for i in range(len(list_lapangan_sorted) - 1):
        for j in range(len(list_lapangan_sorted) - 1 - i):
            if list_lapangan_sorted[j][5] < list_lapangan_sorted[j + 1][5]:
                list_lapangan_sorted[j], list_lapangan_sorted[j + 1] = list_lapangan_sorted[j + 1], list_lapangan_sorted[j]
    
    # Menampilkan min temperature minimal
    harga_max = list_lapangan_sorted[0][5]  
    print(f"Harga maksimum adalah {harga_max} USD.")
    
    # Menampilkan header tabel
    print("=" * 156)
    print(
        f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |"
    )
    print("=" * 156)

    # Menampilkan lapangan yang memiliki kuantitas air minimum
    no = 1  # Untuk nomor urut di tabel

    # Menampilkan pompa dengan min temperature minimal
    for lapangan in list_lapangan_sorted:
        if lapangan[5] == harga_max:
            print(
                f"| {no:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |"
            )
            no += 1

    # Menampilkan baris pembatas tabel
    print("=" * 156)
    
    # Menampilkan lapangan yang memiliki kuantitas air minimum
    print(f"\nHarga maksimum terdapat di lapangan berikut dengan harga sebesar {harga_max} USD:")
    for lapangan in list_lapangan_sorted:
        if lapangan[5] == harga_max:
            print(f"- {lapangan[0]} dengan harga sebesar {lapangan[5]} USD.")
def tampilkan_water_cut_maksimal():
    # Membuat salinan dari list_pompa yang asli
    list_lapangan_sorted = list_lapangan[:]
    
    # Mengurutkan berdasarkan min temperature (dari yang terkecil ke yang terbesar)
    for i in range(len(list_lapangan_sorted) - 1):
        for j in range(len(list_lapangan_sorted) - 1 - i):
            if list_lapangan_sorted[j][7] < list_lapangan_sorted[j + 1][7]:
                list_lapangan_sorted[j], list_lapangan_sorted[j + 1] = list_lapangan_sorted[j + 1], list_lapangan_sorted[j]
    
    # Menampilkan min temperature minimal
    water_cut_max = list_lapangan_sorted[0][7]  
    print(f"Water cut maksimum adalah {water_cut_max}%.")
    
    # Menampilkan header tabel
    print("=" * 156)
    print(
        f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |"
    )
    print("=" * 156)

    # Menampilkan lapangan yang memiliki kuantitas air minimum
    no = 1  # Untuk nomor urut di tabel

    # Menampilkan pompa dengan min temperature minimal
    for lapangan in list_lapangan_sorted:
        if lapangan[7] == water_cut_max:
            print(
                f"| {no:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |"
            )
            no += 1

    # Menampilkan baris pembatas tabel
    print("=" * 156)
    
    # Menampilkan lapangan yang memiliki kuantitas air minimum
    print(f"\nWater cut maksimum terdapat di lapangan berikut dengan water cut sebesar {water_cut_max}%:")
    for lapangan in list_lapangan_sorted:
        if lapangan[7] == water_cut_max:
            print(f"- {lapangan[0]} dengan water cut sebesar {lapangan[7]}%.")
        
def tampilkan_data_spesifik_lapangan():
    # Meminta pengguna untuk memasukkan nama pompa
    print("Masukkan nama lapangan yang ingin ditampilkan:")
    
    try:  # Kode yang berpotensi menyebabkan error
        # Menerima input nama pompa yang diinginkan pengguna
        selected_name = input().strip()  # Mengambil input nama pompa dan menghapus spasi ekstra
        
        # Flag untuk menandai apakah pompa ditemukan
        found = False
        for lapangan in list_lapangan:
            if selected_name.lower() in lapangan[0].lower():  # Membandingkan nama pompa (case insensitive)
                if not found:  # Menampilkan header tabel hanya sekali jika data ditemukan
                    print("=" * 156)
                    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
                    print("=" * 156)
                found = True
                # Menampilkan data pompa yang ditemukan dengan format yang rapi
                print(f"| {list_lapangan.index(lapangan) + 1:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
        
        # Jika tidak ada data yang ditemukan
        if not found:
            print("Pompa yang dicari tidak ditemukan!")
            # Panggil menu Sort Pompa lagi setelah data tidak ditemukan
            menampilkan_data_lapangan()
        else:
            print("=" * 156)  # Menampilkan garis bawah tabel setelah data ditampilkan
            # Setelah menampilkan data, kembali ke menu Sort Pompa
            menampilkan_data_lapangan()  # Kembali ke menu Sort Pompa setelah menampilkan data

    except ValueError:  # Menangani error yang terjadi di dalam try
        print("Input tidak valid!")  # Menangani jika terjadi kesalahan input
        # Panggil menu Sort Pompa setelah error input
        menampilkan_data_lapangan()
# Fungsi menampilkan data berdasarkan tipe pompa
def tampilkan_data_berdasarkan_wilayah(wilayah):
    # Mencari pompa dengan tipe yang sesuai
    ditemukan = False
    for i, lapangan in enumerate(list_lapangan):
        if lapangan[6].lower() == wilayah.lower():  # Case-insensitive pencocokan tipe
            if not ditemukan:
                # Hanya tampilkan header tabel sekali, saat pertama kali ditemukan pompa dengan tipe yang sesuai
                print("=" * 156)
                print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
                print("=" * 156)
                ditemukan = True
            
            # Menampilkan data pompa sesuai tipe yang dicari
            print(f"| {i+1:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    if not ditemukan:
        # Jika tidak ada pompa ditemukan, tampilkan pesan ini
        print(f"Tidak ada lapangan di wilayah '{wilayah}'.")
    else:
        print("="*156)
def menambah_lapangan():
    while True:
        print('''
        1. Menambah Lapangan
        2. Kembali ke Main Menu
        ''')
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            # Tampilkan data pompa dalam format tabel X sebelum menambah pompa
            print("\nData Lapangan Sebelum Penambahan:")
            menampilkan_daftar_lapangan()

            nama_lapangan = input('Masukkan Nama Lapangan: ')

            # Cek jika nama pompa sudah ada dalam list
            for lapangan in list_lapangan:
                if lapangan[0].lower() == nama_lapangan.lower():
                    print("Error: Data ini telah ada!\n")
                    break
            else:  # Jika nama pompa tidak ditemukan dalam list
                # Validasi untuk Quantity
                while True:
                    try:
                        gas_quantity = int(input('Masukkan kuantitas gas: '))
                        break
                    except ValueError:
                        print("Data tidak valid! Harap masukkan angka.")

                # Validasi untuk Harga
                while True:
                    try:
                        water_quantity = int(input('Masukkan kuantitas air: '))
                        break
                    except ValueError:
                        print("Data tidak valid! Harap masukkan angka.")

                # Validasi untuk Max Oil Lift
                while True:
                    try:
                        oil_quantity = int(input('Masukkan kuantitas minyak: '))
                        break
                    except ValueError:
                        print("Data tidak valid! Harap masukkan angka.")

                # Validasi untuk Min Temperature
                while True:
                    try:
                        temp = int(input('Masukkan temperatur: '))
                        break
                    except ValueError:
                        print("Data tidak valid! Harap masukkan angka.")

                # Validasi untuk Max Temperature
                while True:
                    try:
                        harga_gas_air_minyak = int(input('Masukkan harga gas, air dan minyak: '))
                        break
                    except ValueError:
                        print("Data tidak valid! Harap masukkan angka.")

                wilayah = input('Masukkan wilayah lapangan: ')
                while True:
                    try:
                        water_cut = int(input('Masukkan water cut: '))
                        break
                    except ValueError:
                        print("Data tidak valid! Harap masukkan angka.")

                # Konfirmasi data yang akan disimpan
                print("\nData yang akan disimpan:")
                print(f"Field name: {nama_lapangan}")
                print(f"Gas (scf/bbl): {gas_quantity}")
                print(f"Water (bwpd): {water_quantity}")
                print(f"Oil (bpd): {oil_quantity}")
                print(f"Temperature (F): {temp}")
                print(f"Gas, water and oil price: {harga_gas_air_minyak}")
                print(f"Region: {wilayah}")
                print(f"Water Cut (%): {water_cut}")

                simpan = input("Apakah Anda ingin menyimpan data ini? (y/n): ").lower()
                if simpan == 'y':
                    list_lapangan.append([nama_lapangan, gas_quantity, water_quantity, oil_quantity, temp, harga_gas_air_minyak, wilayah, water_cut])
                    print(f'\nLapangan {nama_lapangan} berhasil ditambahkan dan disimpan!')
                    
                    # Tampilkan data pompa dalam format tabel X setelah penambahan
                    print("\nData Lapangan Setelah Penambahan:")
                    menampilkan_daftar_lapangan()
                elif simpan == 'n':
                    print('Data tidak disimpan. Kembali ke menu utama.\n')
                else:
                    print("Input tidak valid! Kembali ke menu utama.\n")
        elif pilihan == '2':
            print("Kembali ke main menu...\n")
            break
        else:
            print("Pilihan tidak valid. Harap pilih 1 atau 2.\n")

def menampilkan_daftar_lapangan():
    print("\nDaftar Pompa:")
    print("=" * 156)
    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
    print("=" * 156)
    for idx, lapangan in enumerate(list_lapangan, start=1):
        print(f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    # Footer tabel
    print("=" * 156)
def menghapus_lapangan():
    while True:
        # Menampilkan sub-menu untuk pilihan penghapusan
        print(''' 
            Menu Penghapusan Lapangan:
            1. Menghapus Lapangan
            2. Kembali ke Main Menu
        ''')
        pilihan = input("Masukkan pilihan Anda (1/2): ")
        if pilihan == '1':
            # Menampilkan tabel pompa sebelum penghapusan
            print("=" * 156)
            print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
            print("=" * 156)
    
    # Menampilkan tabel berdasarkan urutan quantity
            for idx, lapangan in enumerate(list_lapangan, start=1):
                print(f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    # Footer tabel
            print("=" * 156)

            nama_lapangan = input("Masukkan nama lapangan yang ingin dihapus: ")
            # Mencari pompa berdasarkan nama
            found = False
            for i, lapangan in enumerate(list_lapangan):
                if lapangan[0].lower() == nama_lapangan.lower():
                    found = True
                    # Tampilkan konfirmasi penghapusan
                    print("\nLapangan yang ingin Anda hapus adalah:")
                    print("=" * 156)
                    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
                    print("=" * 156)
                    print(f"| {i+1:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
                    print("=" * 156)
                    validasi = input("Hapus data? (y/n): ").lower()
                    if validasi == 'y':
                        print(f"Lapangan {lapangan[0]} berhasil dihapus.")
                        del list_lapangan[i]  # Hapus data pompa
                    elif validasi == 'n':
                        print("Data batal dihapus.")
                    else:
                        print("Input tidak valid! Masukkan 'y' atau 'n'.")
                    break  # Keluar dari pencarian pompa

            if not found:
                print("Data tidak ditemukan. Anda akan kembali ke menu penghapusan.")
                continue  # Kembali ke menu penghapusan
            else:
                # Setelah penghapusan atau batal, kembali ke menu penghapusan
                continue
        elif pilihan == '2':
            return  # Kembali ke main menu
        else:
            print("Input tidak valid! Masukkan angka 1 atau 2.")
def update_lapangan():
    while True:
        print("\n1. Mengupdate Lapangan per Kolom")
        print("2. Mengupdate Semua Kolom Lapangan")
        print("3. Kembali ke Main Menu")
        pilihan_awal = input("Masukkan pilihan (1/2/3): ")

        if pilihan_awal == '1':
            # Menampilkan daftar lapangan tanpa fungsi tambahan
            print("\nDaftar Lapangan:")
            print("=" * 156)
            print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
            print("=" * 156)
            for idx, lapangan in enumerate(list_lapangan, start=1):
                print(f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    # Footer tabel
            print("=" * 156)

            nama_lapangan = input("Masukkan nama lapangan yang mau diupdate: ")

            # Mencari lapangan berdasarkan nama
            lapangan_ditemukan = False
            for i, lapangan in enumerate(list_lapangan):
                if lapangan[0].lower() == nama_lapangan.lower():  # Pencocokan nama (case-insensitive)
                    lapangan_ditemukan = True
                    nomor_lapangan = i

                    # Tampilkan data lapangan yang dipilih
                    print("\nLapangan yang Dipilih:")
                    print("\nLapangan yang ingin Anda hapus adalah:")
                    print("=" * 156)
                    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water CUt (%)':<15} |")
                    print("=" * 156)
                    print(f"| {i+1:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
                    print("=" * 156)
                    break
            
            if not lapangan_ditemukan:
                print("Error: Nama lapangan tidak ditemukan.")
                continue

            # Konfirmasi untuk lanjut update
            validasi = input("Lanjutkan update? (y/n): ").lower()
            while validasi not in ['y', 'n']:
                print("Input tidak valid! Harap masukkan 'y' atau 'n'.")
                validasi = input("Lanjutkan update? (y/n): ").lower()

            if validasi == 'n':
                print("Kembali ke menu update.")
                continue  # Kembali ke menu update tanpa perubahan

            # Simpan salinan data lama untuk rollback jika diperlukan
            data_awal = list_lapangan[nomor_lapangan][:]

            while True:
                print("\nPilih kolom yang ingin diupdate:")
                print("1. Gas (scf/bbl)")
                print("2. Water (bwpd)")
                print("3. Oil (bpd)")
                print("4. Temperatur (F)")
                print("5. Gas, water and oil price (USD)")
                print("6. Region")
                print("7. Water Cut (%)")
                
                try:
                    pilihan = int(input("Masukkan nomor pilihan (1-7): "))
                except ValueError:
                    print("Data tidak valid! Harap masukkan angka antara 1 hingga 7.")
                    continue

                # Memasukkan nilai baru ke kolom yang dipilih
                if pilihan == 1:
                    while True:
                        try:
                            gas_quantity = int(input('Masukkan kuantitas gas baru: '))
                            list_lapangan[nomor_lapangan][1] = gas_quantity
                            break
                        except ValueError:
                            print("Data tidak valid! Harap masukkan angka untuk kuantitas gas.")
                
                elif pilihan == 2:
                    while True:
                        try:
                            water_quantity = int(input('Masukkan kuantitas air baru: '))
                            list_lapangan[nomor_lapangan][2] = water_quantity
                            break
                        except ValueError:
                            print("Data tidak valid! Harap masukkan angka untuk kuantitas air.")
                
                elif pilihan == 3:
                    while True:
                        try:
                            oil_quantity = int(input('Masukkan kuantitas minyak baru: '))
                            list_lapangan[nomor_lapangan][3] = oil_quantity
                            break
                        except ValueError:
                            print("Data tidak valid! Harap masukkan angka untuk kuantitas minyak.")
                
                elif pilihan == 4:
                    while True:
                        try:
                            temp = int(input('Masukkan temperatur baru: '))
                            list_lapangan[nomor_lapangan][4] = temp
                            break
                        except ValueError:
                            print("Data tidak valid! Harap masukkan angka untuk temperature.")
                
                elif pilihan == 5:
                    while True:
                        try:
                            harga_gas_air_minyak = int(input('Masukkan harga gas, air dan minyak baru: '))
                            list_lapangan[nomor_lapangan][5] = harga_gas_air_minyak
                            break
                        except ValueError:
                            print("Data tidak valid! Harap masukkan angka untuk harga gas, air dan minyak.")
                
                elif pilihan == 6:
                    wilayah = input('Masukkan wilayah baru: ')
                    list_lapangan[nomor_lapangan][6] = wilayah
                elif pilihan == 7:
                    while True:
                        try:
                            water_cut = int(input('Masukkan water cut baru: '))
                            list_lapangan[nomor_lapangan][7] = water_cut
                            break
                        except ValueError:
                            print("Data tidak valid! Harap masukkan angka untuk water cut.")
                else:
                    print("Pilihan tidak valid! Silakan pilih antara 1 hingga 7.")
                    continue

                # Konfirmasi untuk update data
                update_validasi = input("Update data? (y/n): ").lower()
                while update_validasi not in ['y', 'n']:
                    print("Input tidak valid! Harap masukkan 'y' atau 'n'.")
                    update_validasi = input("Update data? (y/n): ").lower()

                if update_validasi == 'y':
                    print("Data berhasil diupdate dan disimpan.")
                    break
                elif update_validasi == 'n':
                    # Rollback ke data awal
                    list_lapangan[nomor_lapangan] = data_awal
                    print("Perubahan dibatalkan. Data dikembalikan ke kondisi semula.")
                    break

            # Tampilkan data lapangan setelah diupdate
            print("\nData Lapangan Setelah Update:")
            print("\nLapangan yang ingin Anda hapus adalah:")
            print("=" * 156)
            print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
            print("=" * 156)
            print(f"| {i+1:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
            print("=" * 156)

        elif pilihan_awal == '2':
    # Menampilkan daftar lapangan
            print("=" * 156)
            print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
            print("=" * 156)
            for idx, lapangan in enumerate(list_lapangan, start=1):
                print(f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    # Footer tabel
            print("=" * 156)

            nama_lapangan = input("Masukkan nama lapangan yang mau diupdate: ")

    # Mencari lapangan berdasarkan nama
            lapangan_ditemukan = False
            for i, lapangan in enumerate(list_lapangan):
                if lapangan[0].lower() == nama_lapangan.lower():  # Pencocokan nama (case-insensitive)
                    lapangan_ditemukan = True
                    nomor_lapangan = i

            # Tampilkan data lapangan yang dipilih
                    print("\nLapangan yang Dipilih:")
                    print("=" * 156)
                    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
                    print("=" * 156)
                    print(f"| {i+1:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
                    print("=" * 156)

            # Konfirmasi sebelum melanjutkan update
                    lanjutkan = input("Lanjutkan update (y/n): ").lower()
                    if lanjutkan == 'n':
                # Kembali ke menu
                        print("\n1. Mengupdate Lapangan per Kolom")
                        print("2. Mengupdate Semua Kolom Lapangan")
                        print("3. Kembali ke Main Menu")
                        break
                    elif lanjutkan != 'y':
                        print("Pilihan tidak valid. Kembali ke menu.")
                        break

            # Masukkan data baru untuk kolom yang diizinkan
                    print("\nMasukkan data baru untuk kolom gas, water, oil, temperature, price, region dan water cut:")
                    while True:
                        try:
                            gas_quantity = int(input('Gas (scf/bbl): '))
                            break
                        except ValueError:
                            print("Harap masukkan angka untuk data numerik!")
                    while True:
                        try:    
                            water_quantity = int(input('Water (bwpd): '))
                            break
                        except ValueError:
                            print("Harap masukkan angka untuk data numerik!")
                    while True:
                        try:   
                            oil_quantity = int(input('Oil (bpd): '))
                            break
                        except ValueError:
                             print("Harap masukkan angka untuk data numerik!")
                    while True:
                        try:
                            temp = int(input('Temperatur (F): '))
                            break
                        except ValueError:
                            print("Harap masukkan angka untuk data numerik!")
                         
                    while True:
                        try:
                            harga_gas_air_minyak = int(input('Harga gas, air, minyak (USD): '))
                            break
                        except ValueError:
                            print("Harap masukkan angka untuk data numerik!")
                    region_baru = input("Region Baru: ")  # Input Region Baru diminta lebih dulu
                    while True:
                        try:       
                            water_cut = int(input('Water Cut (%) (y): '))  # Input Lama Operasi diminta setelah Region Baru
                            break
                        except ValueError:
                            print("Harap masukkan angka untuk data numerik!")
                        

                    # Konfirmasi penyimpanan data
                    simpan_data = input("Update data (y/n): ").lower()
                    if simpan_data == 'n':
                        print("\n1. Mengupdate Lapangan per Kolom")
                        print("2. Mengupdate Semua Kolom Lapangan")
                        print("3. Kembali ke Main Menu")
                        break
                    elif simpan_data != 'y':
                        print("Pilihan tidak valid. Data tidak disimpan.")
                        break


            # Simpan data baru (kecuali nama lapangan)
                    list_lapangan[nomor_lapangan][1] = gas_quantity
                    list_lapangan[nomor_lapangan][2] = water_quantity
                    list_lapangan[nomor_lapangan][3] = oil_quantity
                    list_lapangan[nomor_lapangan][4] = temp
                    list_lapangan[nomor_lapangan][5] = harga_gas_air_minyak
                    list_lapangan[nomor_lapangan][6] = region_baru
                    list_lapangan[nomor_lapangan][7] = water_cut

                    print("\nData berhasil diupdate!")
                    print("\nData Lapangan Setelah Update:")
                    print("=" * 156)
                    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
                    print("=" * 156)
                    print(f"| {i+1:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
                    print("=" * 156)
                    break

            if not lapangan_ditemukan:
                print(f"Lapangan dengan nama '{nama_lapangan}' tidak ditemukan.")


        elif pilihan_awal == '3':
            print("Kembali ke main menu.")
            break

        else:
            print("Pilihan tidak valid! Harap pilih antara 1, 2, atau 3.")

def menampilkan_daftar_lapangan():
    print("\nDaftar Lapangan:")
    print("=" * 156)
    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
    print("=" * 156)
    for idx, lapangan in enumerate(list_lapangan, start=1):
        print(f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
    # Footer tabel
    print("=" * 156)
def analisa_lapangan():
    list_lapangan = [
        ['Aqua Field', 400, 150, 6000, 100, 456684, 'Jawa', 2.4],
        ['Pascal Field', 100, 1100, 28000, 350, 2105948, 'Jawa', 3.8],
        ['Ferros Field', 400, 8200, 2000, 35, 135928, 'Jawa', 80],
        ['Newton Field', 1200, 3500, 10000, 240, 777920, 'Sumatera', 26],
        ['Landak Field', 1000, 3000, 2000, 160, 149820, 'Sumatera', 60],
        ['Ruby Field', 900, 600, 5000, 280, 386895, 'Sumatera', 11],
        ['Emerald Field', 430, 4600, 440, 60, 24350, 'Kalimantan', 91],
        ['Chromosom Field', 1400, 3000, 23000, 190, 1812702, 'Kalimantan', 11],
        ['Genus Field', 1450, 5000, 3000, 55, 227658, 'Kalimantan', 62.5],
        ['Metallica Field', 900, 1500, 1900, 220, 144476, 'Sulawesi', 44],
        ['Phalanx Field', 200, 1000, 5000, 140, 375910, 'Sulawesi', 17],
        ['Weadow Field', 450, 1400, 500, 300, 35354, 'Sulawesi', 74],
    ]
    
    harga_pompa = {
        'ESP': 500000,  # Harga untuk pompa ESP
        'PCP': 350000,  # Harga untuk pompa PCP
        'SRP': 200000,   # Harga untuk pompa SRP
    }

    while True:
        print('Pilih jenis analisa lapangan:')
        pilihanAnalisa = input('''
                                1. Analisa Lapangan Pemboran
                                2. Daftar Pompa Pemboran
                                3. Kembali ke Menu Utama
                                Masukkan angka Menu yang ingin dijalankan: 
        ''')
    
        if pilihanAnalisa == '1':
            print("=" * 156)
            print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
            print("=" * 156)
    
            # Menampilkan data dari tabel lapangan
            for i, lapangan in enumerate(list_lapangan, start=1):
                print(f"| {i:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
    
            print("=" * 156)
            
            # Meminta input nama lapangan
            lapangan_name = input('Masukkan nama lapangan yang ingin dianalisa: ')
            
            # Mencari lapangan yang sesuai dengan input
            lapangan_ditemukan = False
            lapangan_terpilih = None
            for i, lapangan in enumerate(list_lapangan):
                if lapangan_name.lower() == lapangan[0].lower():
                    lapangan_ditemukan = True
                    lapangan_terpilih = lapangan
                    print("=" * 156)
                    print(f"| {'No':<3} | {'Field Name':<15} | {'Gas (scf/bbl)':<14} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} | {'Gas, Water and Oil Price (USD)':<30} | {'Region':<10} | {'Water Cut (%)':<15} |")
                    print("=" * 156)
                    print(f"| {i+1:<3} | {lapangan[0]:<15} | {lapangan[1]:<14} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} | {lapangan[5]:<30} | {lapangan[6]:<10} | {lapangan[7]:<15} |")
                    print("=" * 156)
                    break
            
            if not lapangan_ditemukan:
                print(f"Lapangan dengan nama {lapangan_name} tidak ditemukan.")
                continue
            
            # Menambahkan pilihan tipe pompa setelah melanjutkan analisa
            print("\nMasukkan tipe pompa yang mau digunakan untuk pemboran migas:")
            print("1. ESP (Electric Submersible Pump)")
            print("2. PCP (Progressing Cavity Pump)")
            print("3. SRP (Sucker Rod Pump)")

            tipe_pompa = input("Masukkan tipe pompa yang dipilih: ")

            # Menentukan harga pompa berdasarkan pilihan
            if tipe_pompa == '1':  # ESP
                harga_pompa_terpilih = harga_pompa['ESP']
                print(f"\nAnda memilih pompa ESP (Electric Submersible Pump).")
            elif tipe_pompa == '2':  # PCP
                harga_pompa_terpilih = harga_pompa['PCP']
                print(f"\nAnda memilih pompa PCP (Progressing Cavity Pump).")
            elif tipe_pompa == '3':  # SRP
                harga_pompa_terpilih = harga_pompa['SRP']
                print(f"\nAnda memilih pompa SRP (Sucker Rod Pump).")
            else:
                print("Pilihan pompa tidak valid. Silakan coba lagi.")
                continue
            
            # Analisa kapabilitas pompa berdasarkan lapangan yang dipilih
            print("\n** Analisa Kapabilitas Pompa Berdasarkan Lapangan **")
            gas = lapangan_terpilih[1]
            water = lapangan_terpilih[2]
            oil = lapangan_terpilih[3]
            temperature = lapangan_terpilih[4]

            # Validasi kapabilitas pompa berdasarkan tipe yang dipilih
            kondisi = True
            
            if tipe_pompa == '1':  # ESP
                print("\nKapabilitas untuk Pompa ESP (Electric Submersible Pump):\n\nAllowable gas: 1500 scf/bbl\nWater lift capacity: 1000 bwpd - 50000 bwpd\nOil lift capacity: 200 bpd - 30000 bpd\nTemperature range: 50 F - 350 F\n")
                if gas >= 1500:
                    print("Allowable gas di lapangan ini diluar kapabilitas pompa ESP, akan terjadi gas lock.")
                    kondisi = False
                else:
                    print("Gas sesuai dengan kapasitas pompa ESP.")
                
                if water < 1000 or water > 50000:
                    print("Water di lapangan ini diluar kapabilitas pompa ESP.")
                    kondisi = False
                else:
                    print("Water sesuai dengan kapasitas pompa ESP.")
                
                if oil < 200 or oil > 30000:
                    print("Oil di lapangan ini diluar kapabilitas pompa ESP.")
                    kondisi = False
                else:
                    print("Oil sesuai dengan kapasitas pompa ESP.")
                
                if temperature < 50 or temperature > 350:
                    print("Temperatur di lapangan ini diluar kapabilitas pompa ESP.")
                    kondisi = False
                else:
                    print("Temperatur sesuai dengan kapasitas pompa ESP.")
            
            elif tipe_pompa == '2':  # PCP
                print("\nKapabilitas untuk Pompa PCP (Progressive Cavity Pump):\n\nAllowable gas: 500 scf/bbl\nWater lift capacity: 50 bwpd - 10000 bwpd\nOil lift capacity: 10 bpd - 8000 bpd\nTemperature range: 32 F - 300 F\n")
                if gas >= 500:
                    print("Allowable gas di lapangan ini diluar kapabilitas pompa PCP.")
                    kondisi = False
                else:
                    print("Gas sesuai dengan kapasitas pompa PCP.")
                
                if water <= 50 or water >= 10000:
                    print("Water di lapangan ini diluar kapabilitas pompa PCP.")
                    kondisi = False
                else:
                    print("Water sesuai dengan kapasitas pompa PCP.")
                
                if oil <= 10 or oil >= 8000:
                    print("Oil di lapangan ini diluar kapabilitas pompa PCP.")
                    kondisi = False
                else:
                    print("Oil sesuai dengan kapasitas pompa PCP.")
                
                if temperature <= 32 or temperature >= 300:
                    print("Temperatur di lapangan ini diluar kapabilitas pompa PCP.")
                    kondisi = False
                else:
                    print("Temperatur sesuai dengan kapasitas pompa PCP.")
            
            elif tipe_pompa == '3':  # SRP
                print("\nKapabilitas untuk Pompa PCP (Progressive Cavity Pump):\n\nAllowable gas: 1000 scf/bbl\nWater lift capacity: 50 bwpd - 3000 bwpd\nOil lift capacity: 10 bpd - 2000 bpd\nTemperature range: 32 F - 250 F\n")
                if gas >= 1000:
                    print("Allowable gas di lapangan ini diluar kapabilitas pompa SRP.")
                    kondisi = False
                else:
                    print("Gas sesuai dengan kapasitas pompa SRP.")
                
                if water <= 50 or water >= 3000:
                    print("Water di lapangan ini diluar kapabilitas pompa SRP.")
                    kondisi = False
                else:
                    print("Water sesuai dengan kapasitas pompa SRP.")
                
                if oil <= 10 or oil >= 2000:
                    print("Oil di lapangan ini diluar kapabilitas pompa SRP.")
                    kondisi = False
                else:
                    print("Oil sesuai dengan kapasitas pompa SRP.")
                
                if temperature <= 32 or temperature >= 250:
                    print("Temperatur di lapangan ini diluar kapabilitas pompa SRP.")
                    kondisi = False
                else:
                    print("Temperatur sesuai dengan kapasitas pompa SRP.")
            
            # Menampilkan hasil setelah analisa
            if kondisi:
                print("\nPompa dapat digunakan untuk lapangan ini.")
                print(f"\nHarga Pompa yang Anda pilih: {harga_pompa_terpilih} USD\nBiaya operasi pemboran adalah: 123500000 USD sehingga total keseluruhan biaya pemboran adalah {round(harga_pompa_terpilih+123500000)}\nProfit dari gas sebesar {oil} bpd x {gas} scf/bbl x 0.00291: {round(oil*gas*0.00291)} USD\nProfit dari minyak sebesar {oil} x 75: {round(oil*75)} USD\nBiaya air yang harus dibuang sebesar {water} x 2: {round(water*2)} USD\nPenghasilan dari pemboran sebesar profit dari gas {round(oil*gas*0.00291)} USD + profit dari minyak sebesar {round(oil*75)} USD - biaya pembuangan air sebesar {round(water*2)} USD sehingga profit proyek ini sebesar {round((((oil*75)+(oil*gas*0.00291)-(water*2))*365*5))}\nProfit dari proyek ini sebesar biaya pemboran {round(123500000+harga_pompa_terpilih)} USD - penghasilan dari proses pemboran {round((((oil*75)+(oil*gas*0.00291)-(water*2))*365*5))} USD")
                keuntungan = round((((oil*75)+(oil*gas*0.00291)-(water*2))*365*5)-(123500000+harga_pompa_terpilih)) # Keuntungan dihitung dari harga pompa + gas (scf/bbl)
                if keuntungan >= 0:
                    print(f"Karena Anda memilih lapangan {lapangan_terpilih[0]} dan setelah beroperasi selama 5 tahun di {lapangan_terpilih[0]}, Anda untung USD {keuntungan}.")
                else:
                    print(f"Karena Anda memilih lapangan {lapangan_terpilih[0]} dan setelah beroperasi selama 5 tahun di {lapangan_terpilih[0]},5 Anda rugi USD {abs(keuntungan)}.")
                
            else:
                print("Pompa ini tidak dapat digunakan untuk lapangan ini. Silahkan pilih pompa lain.")
        
        elif pilihanAnalisa == '2':
            daftar_pompa_pemboran()
            return
        elif pilihanAnalisa == '3':
            break  # Kembali ke menu utama
        else:
            print('Invalid Input !!!')

def daftar_pompa_pemboran():
    list_pompa_pemboran = [['ESP', 1500, '1000-50000', '200-30000', '50-350'], ['PCP', 500, '50-10000', '10-8000', '32-300'], 
    ['SRP', 1000, '50-3000', '10-2000', '32-250']]
    # Header tabel
    print("=" * 108)
    print(
        f"| {'No':<3} | {'Pump Type':<15} | {'Allowable Gas (scf/bbl)':<30} | {'Water (bwpd)':<14} | {'Oil (bpd)':<12} | {'Temperatur (F)':<15} |"
    )
    print("=" * 108)
    
    # Menampilkan data lapangan satu per satu
    for idx, lapangan in enumerate(list_pompa_pemboran, start=1):
        print(
            f"| {idx:<3} | {lapangan[0]:<15} | {lapangan[1]:<30} | {lapangan[2]:<14} | {lapangan[3]:<12} | {lapangan[4]:<15} |"
        )
    
    # Footer tabel
    print("=" * 108)
    analisa_lapangan()
def main_menu():
    while True:
        pilihanMenu = input(''' 
                            Selamat Datang di Tempat Analisa Pemboran
                            List Menu:
                            1. Menampilkan Data Lapangan
                            2. Menambah Lapangan
                            3. Menghapus Lapangan
                            4. Mengupdate Lapangan
                            5. Analisa Lapangan
                            6. Exit Program
                            Masukkan angka Menu yang ingin dijalankan: 
        ''')

        if pilihanMenu == '1': 
            menampilkan_data_lapangan()
        elif pilihanMenu == '2': 
            menambah_lapangan()     
        elif pilihanMenu == '3': 
            menghapus_lapangan()
        elif pilihanMenu == '4':
            update_lapangan()
        elif pilihanMenu == '5': 
            analisa_lapangan()
        elif pilihanMenu == '6':
            print('Keluar dari Program !!!') 
            break
        else:
            print('Invalid Input !!!')
list_lapangan = [
    ['Aqua Field', 400, 150, 6000, 100, 456684, 'Jawa', 2.4],['Pascal Field', 100, 1100, 28000, 350, 2105948, 'Jawa', 3.8],
    ['Ferros Field', 400, 8200, 2000, 35, 135928, 'Jawa', 80],['Newton Field', 1200, 3500, 10000, 240, 777920, 'Sumatera', 26],
    ['Landak Field', 1000, 3000, 2000, 160, 149820, 'Sumatera', 60],['Ruby Field', 900, 600, 5000, 280, 386895,  'Sumatera', 11],
    ['Emerald Field', 430, 4600, 440, 60, 24350, 'Kalimantan', 91],['Chromosom Field', 1400, 3000, 23000, 190, 1812702, 'Kalimantan',11],
    ['Genus Field', 1450, 5000, 3000, 55, 227658, 'Kalimantan', 62.5],['Metallica Field', 900, 1500, 1900, 220, 144476, 'Sulawesi', 44],
    ['Phalanx Field', 200, 1000, 5000, 140, 375910, 'Sulawesi', 17], ['Weadow Field', 450, 1400, 500, 300, 35354, 'Sulawesi', 74],
    ]
main_menu()
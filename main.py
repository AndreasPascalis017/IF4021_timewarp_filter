# Kita import library yang digunakan
import cv2 

def capture_video(): #fungsi utama untuk mengaplikasikan filter
    # digunakan untuk membuka kamera (webcam)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Tidak bisa membuka camera. Coba lagi")
        return

    # pengaturan time warp 
    threshold = 2  # Jumlah iterasi pixel persatuan waktu. makin tinggi maka garis distorsi akan semakin cepat.
    is_upside_down = False  # fungsi ini digunakan untuk membalik pixel vertikal

    # Kita baca frame pertama
    ret, initial_frame = cap.read()
    if not ret:
        print("Error: Frame tidak dapat dibaca.")
        cap.release()
        return # di cek keberhasilannya semisal gagal maka pesan di atas akan keluar.

    warped_frame = initial_frame.copy() # salinan dari frame yang berhasil disimpan
    temp_frame = initial_frame.copy() # kemudian disimpan sementara di sini.
    current_row = 0 # indeks awal

    print(f"Frame dimensions: {initial_frame.shape}")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Gagal membaca frame dari kamera.")
            break

        frame = cv2.flip(frame, int(not is_upside_down))

        # fungsi ini digunakan untuk menggabungkan bagian frame yang baru dan lama kedalam efek timewarp
        temp_frame[current_row:current_row + threshold] = frame[current_row:current_row + threshold]
        warped_frame[:current_row] = temp_frame[:current_row]
        warped_frame[current_row:] = frame[current_row:]

        # fungsi untuk membuat garis hijau peanda distorsi
        cv2.line(warped_frame, (0, current_row), (warped_frame.shape[1], current_row), (0, 255, 0), thickness=2)

        current_row += threshold

        # tampilkan video
        cv2.imshow('Timewarp Filter', warped_frame)

        # memberhentikan proses semisal tombol esc ditekan (27 adalah ASCII untuk esc)
        if cv2.waitKey(33) == 27 or current_row >= frame.shape[0]:
            break

    # kita simpan dalam bentuk file gambar
    output_filename = 'timewarp_output.png'
    cv2.imwrite(output_filename, warped_frame)
    print(f"Timewarp filter berhasil disimpan sebagai '{output_filename}'.")

    cap.release()
    cv2.destroyAllWindows()

# Jalankan filter
if __name__ == "__main__":
    capture_video()

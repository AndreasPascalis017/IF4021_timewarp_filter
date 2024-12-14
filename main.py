import cv2      ## Import library yang akan digunakan.
## cv2 digunakan untuk pengolahan gambar dan video dalam proyek.

cap = cv2.VideoCapture(0) ## fungsi untuk membuka kamera default (webcam).

threshold = 1  ## mengambil 1 piksel yang akan digunakan sebagai iteras (masih akan dicoba lebih lanjut niali yang sesuai)
ret, temp = cap.read()  ## setelah membaca 1 piksel disimpan sementara di temp.
lasth = 0  ## variabel untuk melacak baris yang sedang diproses (semua nama variabel masih berupa nama acak mungkin ada yang diubah ada yang tidak).
newing = temp.copy()
upsidedown = False

print(temp.shape)
while True:
    ret, img = cap.read()  ## setelah membaca frame disimpan dalam img.
    img = cv2.flip(img, int(not upsidedown))
    if (type(img) == type(None)):
        break
    temp[lasth:lasth + threshold] = img[lasth:lasth +threshold]

    newing[0: lasth] = temp[0: lasth]
    newing[lasth:-1] = img[lasth:-1]
    cv2.line(newing, (0, lasth), (640, lasth),
             (0, 255, 0), thickness=2)  ## untuk membuat garis penanda distorsi (hijau)
    lasth += threshold
    cv2.imshow('video', newing)  ## menampilkan video dalam window.
    if cv2.waitKey(33) == 27:
        break
    if lasth >= img.shape[1]:
        break

cv2.imwrite('image.png', newing)  ## file disimpan dengan nama image.png
cv2.destroyAllWindows()  

## update terakhir tgl 14-12-2024
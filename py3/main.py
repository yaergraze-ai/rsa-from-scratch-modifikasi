import time
import textwrap
from rsa import RSA

BOX_WIDTH = 80

def print_tabel(label, value):
    prefix = f"{label:<15}: "
    text = str(value)

    batas_teks = BOX_WIDTH - len(prefix)

    lines = textwrap.wrap(
        text,
        width=batas_teks,
        break_long_words=True,
        break_on_hyphens=False
    )

    if not lines:
        print(prefix)
        return

    print(prefix + lines[0])

    for line in lines[1:]:
        print(" " * len(prefix) + line)


def ubah_ke_teks(data):
    if isinstance(data, bytes):
        return data.decode("utf-8", errors="replace")
    return str(data)


def jalankan_eksperimen(size, message):
    print("=" * BOX_WIDTH)

    try:
        panjang_pesan = len(message)

        start = time.perf_counter()
        alice = RSA(size=size)
        bob = RSA(size=size)
        end = time.perf_counter()
        waktu_generate_key = end - start

        start = time.perf_counter()
        ciphertext = alice.encrypt(message, bob.public_key)
        end = time.perf_counter()
        waktu_encrypt = end - start

        start = time.perf_counter()
        decrypted = bob.decrypt(ciphertext)
        end = time.perf_counter()
        waktu_decrypt = end - start

        signature = alice.sign("Alice Signature")
        verified = bob.verify(signature, alice.public_key)

        hasil_decrypt = ubah_ke_teks(decrypted)
        hasil_signature = ubah_ke_teks(verified)

        status = "Berhasil" if hasil_decrypt == message else "Gagal"

        print_tabel("RSA Size", f"{size} bit")
        print_tabel("Pesan asli", message)
        print_tabel("Panjang", f"{panjang_pesan} karakter")
        print_tabel("Ciphertext", ciphertext.text)
        print_tabel("Hasil decrypt", hasil_decrypt)
        print_tabel("Signature valid", hasil_signature)
        print_tabel("Status", status)

        print("-" * BOX_WIDTH)
        print_tabel("Generate key", f"{waktu_generate_key:.6f} detik")
        print_tabel("Encrypt", f"{waktu_encrypt:.6f} detik")
        print_tabel("Decrypt", f"{waktu_decrypt:.6f} detik")

    except Exception as error:
        print_tabel("RSA Size", f"{size} bit")
        print_tabel("Pesan asli", message)
        print_tabel("Status", "Error")
        print_tabel("Keterangan", error)

    print("=" * BOX_WIDTH)
    print()


def main():
    experiments = [
        (64, "Kana coba RSA"),
        (128, "Fatiha coba RSA"),
        (256, "Arya coba RSA!"),
        (512, "Kana Fatiha Arya belajar RSA!"),
    ]

    for size, message in experiments:
        jalankan_eksperimen(size, message)


if __name__ == "__main__":
    main()
import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Konfigurasi logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Fungsi untuk mengambil data dari API dummy
def fetch_dummy_data(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    return None

# Fungsi untuk menangani perintah /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Halo! Saya adalah OSINT Bot milik @Xalxxx ( MR./Xalxxx†♣. Kirimkan ID pengguna (contoh: 1-10), dan saya akan mencari data dummy untuk Anda!")

# Fungsi untuk menangani pesan teks
def handle_message(update: Update, context: CallbackContext):
    user_input = update.message.text.strip()
    
    if user_input.isdigit():
        user_id = int(user_input)
        data = fetch_dummy_data(user_id)
        
        if data:
            response = (
                f"Data ditemukan:\n"
                f"Nama: {data['name']}\n"
                f"Username: {data['username']}\n"
                f"Email: {data['email']}\n"
                f"Alamat: {data['address']['street']}, {data['address']['city']}\n"
                f"Perusahaan: {data['company']['name']}\n"
            )
            update.message.reply_text(response)
        else:
            update.message.reply_text("Data tidak ditemukan untuk ID tersebut.")
    else:
        update.message.reply_text("Harap masukkan ID pengguna yang valid (angka).")

# Fungsi utama
def main():
    # Masukkan token bot Anda di sini
    TOKEN = "8332677116:AAFI92708Ijc7tilnJQJPs51RP5o455KZVQ"
    updater = Updater(TOKEN)

    # Dispatcher untuk menangani perintah dan pesan
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Jalankan bot
    updater.start_polling()
    updater.idle()

# Menjalankan bot
if __name__ == "__main__":
    main()
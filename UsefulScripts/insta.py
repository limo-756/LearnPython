import requests

if __name__ == '__main__':
    # Set up the Instagram API endpoint and parameters
    # endpoint = "https://api.instagram.com/v1/users/sonalsharma54/followed-by"
    # endpoint = "https://api.instagram.com/v1/users/sonalsharma54/followers"
    endpoint = "https://www.instagram.com/api/v1/friendships/7862863552/followers/?count=12&max_id=12&search_surface=follow_list_page"
    user_id = "sonalsharma54"
    access_token = "{access_token}"
    params = {
        "access_token": "pjq0FkoKtPqcLOI5gn4pxpyNFLLOyAIF",
        "X-CSRFToken": "pjq0FkoKtPqcLOI5gn4pxpyNFLLOyAIF",
        "X-IG-App-ID": "936619743392459",
        "X-ASBD-ID": "198387",
        "X-IG-WWW-Claim": "hmac.AR37JJW6Uq2Iwhrq7Cv2gAIwxIdWTF2ATnkNkT7WH7wwIGsW",
        "Cookie" : 'ig_did=2E642345-5F6F-4C2D-B84D-5852BE325288; datr=2WUPZB1-S-UVwNAtQm9kYrM9; csrftoken=pjq0FkoKtPqcLOI5gn4pxpyNFLLOyAIF; mid=ZA9l3gAEAAF3Q_IMq8DvMfZHDiWk; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; dpr=2; fbsr_124024574287414=_T0-Sx91GJ_rgmrY6iS6dSu0z_fTcwazfdmKztz3PuA.eyJ1c2VyX2lkIjoiMTAwMDA5Njc0ODY0NjAxIiwiY29kZSI6IkFRQXFXSGdOYWc5UldKdmZiOFBEZFVNSGhjMWJlWFVFSl93SnQ2dDZ0Uk90OFJFQWhPckxXWU9JbFl2eFUzeVRkQUlZa0NsYUMxb3NuVVkybGI5QnRBMVVTZkd5d0ljTGxuSndwUEtOWEFHRmE0N2h5MFhtR2lBMmczeTBtaW1CUnlRanBBVmpPRlAyWk5SeGMxQUc2ZVdjcVhLSjlkbzdTVW13cF9aNmM1VU5Lc1UyNmZUM3EwYUw0dHRDOW9sVHk1X2ROaDZCT3VFR18xNEE4M3htWGZrV2VCRHd2VTdub2tjNVhEN0ltM0lwQWtnWllrNmhhZDZVS1d5OEFNT0NjZFNWY1dTbmFxZmN6NGtlN0lOOWtoZDBFSjNSVjVuekdCYmFvY2FlMW53VXRmSzk4X184TmJ3bkNZeVh3SXhmeF93Z3lLMGpqUnVFMFpvQWVVT2tMTzBLIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUlTRHp0Z0V2WU1LRDlPd3RIZFZTdkdHQjI4c3pIdU5zWFR3d1dZUHpENVRucG1aQkUzZnhvYVpDUlF6VXJ4RWFIajdLQWJOU3FoRHNlbFloUFY1Mmx1eFNENmw0RktJSmR1SlBXdWQwMmk2Q29FUjVOb1gzVFpDaXBMTU1aQXdIYmNXWkNTaUY0eEphelpDNjI1eWtsNGV5ODEyek1DSFNTZzNJZkJYSUJYM2huYmQ3U3VqNFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2ODE1NjIwODd9; rur="EAG\0549263074971\0541713098155:01f75e1ba5a32a7c343783bce7c46080685f55ee4bce92d72b3da3ba35f3ac43f821dc3c"; ds_user_id=9263074971; sessionid=9263074971%3AKrr0dUhC0Obsbp%3A22%3AAYdIXTk0XiHpX6V2nDt_CjCX0046RbRXKbAl1EUdIQ; shbid="3114\0549263074971\0541712982604:01f78a232f613732fed3c71fefc2bd3fad5276f3ab3504a5467b9510e040e7ca703e0953"; shbts="1681446604\0549263074971\0541712982604:01f79ffe3ba87eb2a0a851a5abd4466ebd477dfbe3ef2d77a53635a7326fe6e4faafe72e"'
    }

    print("Making API call to insta")
    # Make the API request to fetch the user's followers
    response = requests.get(endpoint, params=params)

    print(response)
    print(response.__dict__)
    print(response.text)
    print(response.json()["status"])
    print(response.json()["users"])

    # Print the list of followers
    followers = response.json()["data"]
    for follower in followers:
        print(follower["username"])

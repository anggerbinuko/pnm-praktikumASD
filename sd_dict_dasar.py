dictMhs = {"name": "Bintang", "age":19, "gender":"male", "active": True}

print("dictMhs = ",dictMhs)
print("Nama = ",dictMhs["name"])
print("Usia = ",dictMhs["age"])
dictMhs["age"] = "sembilan belas"
print("Usia diubah = ",dictMhs["age"])
del dictMhs["age"]
print("Status aktif = ",dictMhs["active"])
print("dictMhs = ",dictMhs)


dictGithub = {
    "login": "anggerbinuko",
    "id": 3633301,
    "node_id": "MDQ6VXNlcjM2MzMzMDE=",
    "avatar_url": "https://avatars.githubusercontent.com/u/3633301?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/anggerbinuko",
    "html_url": "https://github.com/anggerbinuko",
    "followers_url": "https://api.github.com/users/anggerbinuko/followers",
    "following_url": "https://api.github.com/users/anggerbinuko/following{/other_user}",
    "gists_url": "https://api.github.com/users/anggerbinuko/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/anggerbinuko/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/anggerbinuko/subscriptions",
    "organizations_url": "https://api.github.com/users/anggerbinuko/orgs",
    "repos_url": "https://api.github.com/users/anggerbinuko/repos",
    "events_url": "https://api.github.com/users/anggerbinuko/events{/privacy}",
    "received_events_url": "https://api.github.com/users/anggerbinuko/received_events",
    "type": "User",
    "site_admin": False,
    "name": "Angger Binuko Paksi",
    "company": "Politeknik Negeri Madiun",
    "blog": "http://www.binuko.com",
    "location": None,
    "email": None,
    "hireable": None,
    "bio": None,
    "twitter_username": None,
    "public_repos": 12,
    "public_gists": 0,
    "followers": 1,
    "following": 0,
    "created_at": "2013-02-19T04:53:40Z",
    "updated_at": "2022-10-03T07:36:08Z"
}

print(f'Nama {dictGithub["name"]}, bekerja di {dictGithub["company"]}')

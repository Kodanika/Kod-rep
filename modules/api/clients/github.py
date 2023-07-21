import requests

class GitHub:

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            'https://api.github.com/search/repositories',
            params={"q": name})
        body = r.json()

        return body

    def get_emojis(self):
        r = requests.get('https://api.github.com/emojis')
        body = r.json()

        return body
       
    def get_commit(self, commit_name):
        r = requests.get(
            'https://api.github.com/search/commits',
             params={"q": commit_name})                
        body = r.json()

        return body

    def get_list_commit(self, owner, repo ):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')
        status_code = r.status_code

        return status_code

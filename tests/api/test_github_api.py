import pytest

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] =='defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 42

@pytest.mark.api
def test_repo_connot_be_found(github_api):
    r = github_api.search_repo('sergii_butenko_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

@pytest.mark.api
def test_check_emojis(github_api):
    r = github_api.get_emojis()   
    assert r['ant'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f41c.png?v8'

@pytest.mark.api
def test_commit_can_be_found(github_api):
    r = github_api.get_commit('Kodanika')
    assert r['total_count'] == 1
    assert 'Kodanika' in r['items'][0]['url']

@pytest.mark.api
def test_commit_cannot_be_found(github_api):
    r = github_api.get_commit('Kod-anika')
    assert r['total_count'] == 0

@pytest.mark.api
def test_list_commit_can_be_found(github_api):
    r = github_api.get_list_commit('Kodanika', 'Kod-rep')
    assert r == 200

@pytest.mark.api
def test_list_commit_cannot_be_found(github_api):
    r = github_api.get_list_commit('KodenkoAnna', 'Kod-rep')
    assert r == 404


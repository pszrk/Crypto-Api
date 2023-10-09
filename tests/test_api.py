import requests
base_url = 'http://localhost:5000/api/stats'

def test_get_stats():
    data = {"name": "bitcoin"}

    response = requests.post(f"{base_url}", json=data)

    data = response.json()
    assert 'name' in data
    assert 'price' in data
    assert 'ath' in data
    assert 'ath_date' in data
    assert 'around_in_21' in data    
    assert 'low_after_ath' in data
    assert 'low_after_ath_date' in data
    assert 'decline_from_ath' in data
    assert 'ath_was_in_2021' in data
    assert 'gain_to_ath' in data
    assert 'tracked_from' in data

    assert data['price'] > 0

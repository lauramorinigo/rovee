def test_create_user(client):
    # Action: Send POST request to create a user
    user_payload = {'name': 'Astronaut Mark', 'role': 'Botanist'}
    response = client.post('/users', json=user_payload)
    
    # Assert: Check for 201 Created status and correct ID
    assert response.status_code == 201
    assert 'id' in response.json
    assert response.json['name'] == 'Astronaut Mark'

def test_get_user_by_id_returns_data(client):
    # Setup: Create a user first so we have something to fetch
    new_user = {'name': 'Commander Lewis', 'role': 'Geologist'}
    post_response = client.post('/users', json=new_user)
    user_id = post_response.json['id']
    
    # Action: Send GET request to retrieve the specific user
    get_response = client.get(f'/users/{user_id}')
    
    # Assert: Check for 200 OK and matching data
    assert get_response.status_code == 200
    assert get_response.json['id'] == user_id
    assert get_response.json['name'] == 'Commander Lewis'

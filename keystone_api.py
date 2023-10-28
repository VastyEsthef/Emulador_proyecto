import json, requests

# KEYSTONE API
def password_authentication_with_scoped_authorization(auth_endpoint, user_domain_name, username, password, project_domain_id, project_name):
    url = auth_endpoint + '/auth/tokens'

    data = \
        {
            "auth": {
                "identity": {
                    "methods": [
                        "password"
                    ],
                    "password": {
                        "user": {
                            "name": username,
                            "domain": {
                                "name": user_domain_name
                            },
                            "password": password
                        }
                    }
                },
                "scope": {
                    "project": {
                        "domain": {
                            "id": project_domain_id
                        },
                        "name": project_name
                    }
                }
            }
        }
        
    r = requests.post(url=url, data=json.dumps(data))
    # status_code success = 201
    return r

def token_authentication_with_scoped_authorization(auth_endpoint, token, project_domain_id, project_name):
    url = auth_endpoint + '/auth/tokens'

    data = \
        {
            "auth": {
                "identity": {
                    "methods": [
                        "token"
                    ],
                    "token": {
                        "id": token
                    }
                },
                "scope": {
                    "project": {
                        "domain": {
                            "id": project_domain_id
                        },
                        "name": project_name
                    }
                }
            }
        }

    r = requests.post(url=url, data=json.dumps(data))
    # status_code success = 201
    return r


def create_project(auth_endpoint, token, domain_id, project_name, project_description):
        
    url = auth_endpoint + '/projects'
    headers = {'Content-type': 'application/json', 'X-Auth-Token': token}

    data = \
        {
            "project": {
                "name": project_name,
                "description": project_description,
                "domain_id": domain_id
            }
        }

    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    # status_code success = 201
    return r

